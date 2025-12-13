#!/usr/bin/env python3
"""
Generate index.html from 3d_nodes.csv with media galleries and ComfyUI-style node rendering.
Clones repos to extract full node definitions (inputs/outputs).
"""
import ast
import csv
import glob
import re
import json
import os
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

OUTPUT_FILE = "../index.html"

def find_input_file():
    """Find the latest ai_3d_nodes CSV file."""
    files = glob.glob("ai_3d_nodes*.csv")
    if not files:
        # Fallback to old name
        if Path("3d_nodes.csv").exists():
            return "3d_nodes.csv"
        raise FileNotFoundError("No ai_3d_nodes*.csv or 3d_nodes.csv found")
    return sorted(files)[-1]  # Latest by date suffix

CLONE_DIR = "/tmp/comfyui_nodes"
MAX_WORKERS_CLONE = 5
MAX_WORKERS_MEDIA = 20

# Category display names and order
CATEGORIES = {
    "image-to-3d": "Image-to-3D",
    "text-to-3d": "Text-to-3D",
    "multi-view": "Multi-View Generation",
    "mesh-processing": "Mesh Processing",
    "texturing": "Texturing",
    "gaussian-splatting": "Gaussian Splatting",
    "rigging-animation": "Rigging & Animation",
    "depth-normal": "Depth & Normal",
    "visualization": "Visualization",
    "cad": "CAD",
    "human-body": "Human Body",
    "other-3d": "Other 3D"
}

# Media file extensions
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
VIDEO_EXTS = {'.mp4', '.webm', '.mov', '.avi'}
MEDIA_EXTS = IMAGE_EXTS | VIDEO_EXTS

# =============================================================================
# Node Definition Extraction (clone repos, parse Python)
# =============================================================================

def extract_github_info(github_url):
    """Extract owner/repo from GitHub URL."""
    match = re.search(r"github\.com/([^/]+)/([^/\s]+)", github_url)
    if match:
        return match.group(1), match.group(2).replace(".git", "")
    return None, None

def clone_repo(github_url, dest_dir):
    """Clone a repo to destination directory."""
    try:
        result = subprocess.run(
            ["git", "clone", "--quiet", github_url, dest_dir],
            capture_output=True,
            timeout=120
        )
        return result.returncode == 0
    except Exception:
        return False

def find_python_files(repo_dir):
    """Find all Python files in repo."""
    return list(Path(repo_dir).rglob("*.py"))

def parse_class_attribute(node, attr_name):
    """Extract a class attribute value from AST."""
    for item in node.body:
        if isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name) and target.id == attr_name:
                    return item.value
        elif isinstance(item, ast.AnnAssign):
            if isinstance(item.target, ast.Name) and item.target.id == attr_name:
                return item.value
    return None

def ast_to_value(node):
    """Convert AST node to Python value (simplified)."""
    if node is None:
        return None
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Tuple):
        return tuple(ast_to_value(el) for el in node.elts)
    if isinstance(node, ast.List):
        return [ast_to_value(el) for el in node.elts]
    if isinstance(node, ast.Dict):
        result = {}
        for k, v in zip(node.keys, node.values):
            key = ast_to_value(k)
            if key:
                result[key] = ast_to_value(v)
        return result
    return None

def extract_input_types(class_node):
    """Extract INPUT_TYPES from a class."""
    inputs = {"required": {}, "optional": {}}

    for item in class_node.body:
        # Check for INPUT_TYPES as classmethod
        if isinstance(item, ast.FunctionDef) and item.name == "INPUT_TYPES":
            for stmt in ast.walk(item):
                if isinstance(stmt, ast.Return) and stmt.value:
                    val = ast_to_value(stmt.value)
                    if isinstance(val, dict):
                        for key in ["required", "optional"]:
                            if key in val and isinstance(val[key], dict):
                                for name, spec in val[key].items():
                                    if isinstance(spec, tuple) and len(spec) > 0:
                                        inputs[key][name] = spec[0]
                                    else:
                                        inputs[key][name] = str(spec)
                    return inputs

        # Check for INPUT_TYPES as class attribute
        if isinstance(item, ast.Assign):
            for target in item.targets:
                if isinstance(target, ast.Name) and target.id == "INPUT_TYPES":
                    val = ast_to_value(item.value)
                    if isinstance(val, dict):
                        for key in ["required", "optional"]:
                            if key in val and isinstance(val[key], dict):
                                for name, spec in val[key].items():
                                    if isinstance(spec, tuple) and len(spec) > 0:
                                        inputs[key][name] = spec[0]
                                    else:
                                        inputs[key][name] = str(spec)
                    return inputs

    return inputs

def extract_node_class(class_node):
    """Extract node definition from a class AST node."""
    node_def = {
        "inputs": {"required": {}, "optional": {}},
        "outputs": [],
        "output_names": [],
        "category": ""
    }

    node_def["inputs"] = extract_input_types(class_node)

    return_types = parse_class_attribute(class_node, "RETURN_TYPES")
    if return_types:
        val = ast_to_value(return_types)
        if isinstance(val, (tuple, list)):
            node_def["outputs"] = [str(t) for t in val]

    return_names = parse_class_attribute(class_node, "RETURN_NAMES")
    if return_names:
        val = ast_to_value(return_names)
        if isinstance(val, (tuple, list)):
            node_def["output_names"] = [str(n) for n in val]

    category = parse_class_attribute(class_node, "CATEGORY")
    if category:
        val = ast_to_value(category)
        if val:
            node_def["category"] = str(val)

    return node_def

def find_node_mappings(repo_dir):
    """Find NODE_CLASS_MAPPINGS in repo and extract node definitions."""
    nodes = {}
    class_defs = {}

    # First pass: collect all class definitions
    for py_file in find_python_files(repo_dir):
        try:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_defs[node.name] = node
        except Exception:
            continue

    # Second pass: find NODE_CLASS_MAPPINGS
    for py_file in find_python_files(repo_dir):
        try:
            content = py_file.read_text(encoding='utf-8', errors='ignore')
            if "NODE_CLASS_MAPPINGS" not in content:
                continue

            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == "NODE_CLASS_MAPPINGS":
                            if isinstance(node.value, ast.Dict):
                                for k, v in zip(node.value.keys, node.value.values):
                                    node_name = ast_to_value(k)
                                    if node_name:
                                        class_name = None
                                        if isinstance(v, ast.Name):
                                            class_name = v.id
                                        elif isinstance(v, ast.Attribute):
                                            class_name = v.attr

                                        if class_name and class_name in class_defs:
                                            node_def = extract_node_class(class_defs[class_name])
                                            nodes[node_name] = node_def
                                        else:
                                            nodes[node_name] = {
                                                "inputs": {"required": {}, "optional": {}},
                                                "outputs": [],
                                                "output_names": [],
                                                "category": ""
                                            }
        except Exception:
            continue

    return nodes

def extract_repo_nodes(row):
    """Clone a repo and extract node definitions."""
    github_url = row["github_url"]
    owner, repo = extract_github_info(github_url)

    if not owner or not repo:
        return github_url, {}

    repo_dir = os.path.join(CLONE_DIR, f"{owner}_{repo}")

    try:
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)

        if not clone_repo(github_url, repo_dir):
            return github_url, {}

        nodes = find_node_mappings(repo_dir)
        return github_url, nodes

    except Exception:
        return github_url, {}

    finally:
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir, ignore_errors=True)

# =============================================================================
# Media Fetching
# =============================================================================

def fetch_readme(owner, repo):
    """Fetch README via raw.githubusercontent.com"""
    for branch in ["main", "master"]:
        for fname in ["README.md", "readme.md", "Readme.md"]:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{fname}"
            try:
                with urlopen(url, timeout=10) as resp:
                    return resp.read().decode("utf-8", errors="replace"), branch
            except:
                continue
    return "", "main"

def extract_media_from_readme(readme_content, owner, repo, branch):
    """Extract media URLs from README content."""
    media = []

    img_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    for match in re.finditer(img_pattern, readme_content):
        url = match.group(1).strip()
        media.append(normalize_url(url, owner, repo, branch))

    html_img_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    for match in re.finditer(html_img_pattern, readme_content, re.IGNORECASE):
        url = match.group(1).strip()
        media.append(normalize_url(url, owner, repo, branch))

    video_pattern = r'<video[^>]+src=["\']([^"\']+)["\']|<source[^>]+src=["\']([^"\']+)["\']'
    for match in re.finditer(video_pattern, readme_content, re.IGNORECASE):
        url = (match.group(1) or match.group(2)).strip()
        media.append(normalize_url(url, owner, repo, branch))

    return [url for url in media if url and is_media_url(url)]

def normalize_url(url, owner, repo, branch):
    """Convert relative URLs to absolute GitHub raw URLs."""
    if not url:
        return ""
    if url.startswith(('http://', 'https://')):
        return url
    url = url.lstrip('./')
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{url}"

def is_media_url(url):
    """Check if URL points to a media file."""
    url_lower = url.lower().split('?')[0]
    return any(url_lower.endswith(ext) for ext in MEDIA_EXTS)

def fetch_repo_media(owner, repo, branch):
    """Fetch list of media files from repo via GitHub API."""
    media = []
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        req = Request(url, headers={"User-Agent": "ComfyUI-3D-Index"})
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())

        for item in data.get("tree", []):
            if item["type"] == "blob":
                path = item["path"].lower()
                if any(path.endswith(ext) for ext in MEDIA_EXTS):
                    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{item['path']}"
                    media.append(raw_url)
    except Exception:
        pass

    return media

def fetch_repo_updated_at(owner, repo):
    """Fetch last updated date from GitHub API."""
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        req = Request(url, headers={"User-Agent": "ComfyUI-3D-Index"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data.get("pushed_at", "")  # ISO format: 2024-01-15T10:30:00Z
    except Exception:
        return ""

def fetch_node_media(node):
    """Fetch all media for a node."""
    github_url = node["github_url"]
    owner, repo = extract_github_info(github_url)

    if not owner or not repo:
        return [], ""

    readme, branch = fetch_readme(owner, repo)
    readme_media = extract_media_from_readme(readme, owner, repo, branch)
    repo_media = fetch_repo_media(owner, repo, branch)
    updated_at = fetch_repo_updated_at(owner, repo)

    readme_set = set(readme_media)
    all_media = readme_media + [m for m in repo_media if m not in readme_set]

    return all_media[:12], updated_at

# =============================================================================
# HTML Generation
# =============================================================================

def format_stars(stars):
    """Format star count (e.g., 3500 -> 3.5k)"""
    try:
        n = int(stars)
        if n >= 1000:
            return f"{n/1000:.1f}k".replace(".0k", "k")
        return str(n)
    except:
        return stars

def get_data_tag(model_author):
    """Get filter tag from model author"""
    author_lower = model_author.lower() if model_author else ""
    if "tencent" in author_lower:
        return "tencent"
    if "microsoft" in author_lower:
        return "microsoft"
    if "meta" in author_lower:
        return "meta"
    if "vast" in author_lower:
        return "vast-ai"
    if "stability" in author_lower:
        return "stability"
    return "community"

def generate_media_gallery(media_urls):
    """Generate HTML for media gallery."""
    if not media_urls:
        return ""

    items = []
    for url in media_urls[:6]:
        url_lower = url.lower()
        if any(url_lower.endswith(ext) for ext in VIDEO_EXTS):
            items.append(f'<video src="{url}" muted loop playsinline class="gallery-item" onclick="this.paused ? this.play() : this.pause()"></video>')
        else:
            items.append(f'<img src="{url}" alt="Preview" class="gallery-item" loading="lazy" onerror="this.style.display=\'none\'">')

    if not items:
        return ""

    return f'''<div class="media-gallery">{"".join(items)}</div>'''

def generate_card(node, media_urls, node_defs, updated_at):
    """Generate HTML for a single card"""
    github_url = node["github_url"]
    # Use repo name from URL instead of package title
    _, repo_name = extract_github_info(github_url)
    name = repo_name or node["name"]
    stars_raw = node["stars"]
    stars = format_stars(stars_raw)
    node_author = node["node_author"]
    model_author = node["model_author"] or "Community"
    description = node["description"]
    category = node["category"]
    data_tag = get_data_tag(model_author)

    # Get node definitions for this package
    package_nodes = node_defs.get(github_url, {})
    node_names = list(package_nodes.keys())

    # Nodes list HTML
    nodes_html = ""
    if node_names:
        nodes_html = f'''<div class="nodes-list"><span class="nodes-label">Nodes ({len(node_names)}):</span> {", ".join(node_names[:5])}{" ..." if len(node_names) > 5 else ""}</div>'''

    # Generate media gallery
    gallery_html = generate_media_gallery(media_urls)
    fallback_style = "" if media_urls else 'style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 120px;"'

    # Data attribute for node definitions (for client-side rendering)
    node_data = json.dumps(package_nodes) if package_nodes else "{}"

    # Format updated date for display
    updated_display = ""
    if updated_at:
        updated_display = updated_at[:10]  # Just the date part

    return f'''
                    <div class="card" data-tags="{data_tag}" data-nodes='{node_data}' data-stars="{stars_raw}" data-updated="{updated_at}" data-category="{category}">
                        <div class="card-media" {fallback_style}>
                            {gallery_html if media_urls else ""}
                        </div>
                        <div class="card-content">
                            <div class="card-header">
                                <div class="card-title">{name}</div>
                                <div class="card-stars"><i class="fas fa-star"></i> {stars}</div>
                            </div>
                            <div class="card-authors">
                                <span class="node-author">{node_author}</span> · <span class="model-author">{model_author}</span>
                            </div>
                            <div class="card-tags">
                                <span class="tag tag-io">{category}</span>
                            </div>
                            <div class="card-description">{description}</div>
                            {nodes_html}
                            <div class="card-links">
                                <a href="{github_url}" target="_blank">GitHub</a>
                                <a href="#" class="show-nodes" onclick="showNodeDefs(this.closest('.card')); return false;">View Nodes</a>
                            </div>
                        </div>
                    </div>'''

def generate_html(all_nodes_with_media, node_defs):
    """Generate complete HTML page with client-side node rendering."""

    # Collect all unique categories
    categories_in_use = set()
    for node, media, updated in all_nodes_with_media:
        categories_in_use.add(node.get("category", "other-3d"))

    # Generate filter buttons
    filter_buttons = '<button class="filter-btn active" onclick="filterCards(\'all\')">All</button>\n'
    for cat_id, cat_name in CATEGORIES.items():
        if cat_id in categories_in_use:
            filter_buttons += f'                        <button class="filter-btn" onclick="filterCards(\'{cat_id}\')">{cat_name}</button>\n'

    # Generate all cards in one grid (sorted by stars)
    sorted_nodes = sorted(all_nodes_with_media, key=lambda x: int(x[0]["stars"]) if x[0]["stars"].isdigit() else 0, reverse=True)
    all_cards = "\n".join(generate_card(node, media, node_defs, updated) for node, media, updated in sorted_nodes)

    return f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome ComfyUI 3D</title>
    <meta name="description" content="A curated index of ComfyUI 3D nodes for mesh generation, texturing, Gaussian splatting, rigging, and more.">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1520px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}

        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}

        .section {{
            margin: 40px 0;
            width: 100%;
        }}

        .section-title {{
            font-size: 24px;
            margin-bottom: 20px;
            padding-left: 20px;
            border-left: 4px solid #3498db;
        }}

        .cards-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 20px;
            padding: 20px;
            width: 100%;
        }}

        .card {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
        }}

        .card:hover {{
            transform: scale(1.02);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }}

        .card-media {{
            width: 100%;
            min-height: 120px;
            background: #f0f0f0;
            overflow: hidden;
        }}

        .media-gallery {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2px;
            width: 100%;
        }}

        .gallery-item {{
            width: 100%;
            height: 80px;
            object-fit: cover;
            cursor: pointer;
            transition: opacity 0.2s;
        }}

        .gallery-item:hover {{
            opacity: 0.8;
        }}

        .gallery-item:first-child {{
            grid-column: span 2;
            grid-row: span 2;
            height: 162px;
        }}

        .card-content {{
            padding: 15px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 5px;
        }}

        .card-title {{
            font-size: 1.05em;
            font-weight: bold;
            flex: 1;
        }}

        .card-stars {{
            display: flex;
            align-items: center;
            gap: 3px;
            font-size: 0.85em;
            color: #666;
            background: #f0f0f0;
            padding: 2px 8px;
            border-radius: 10px;
        }}

        .card-stars i {{
            color: #f0ad4e;
        }}

        .card-authors {{
            font-size: 0.8em;
            color: #666;
            margin-bottom: 8px;
        }}

        .card-authors .node-author {{
            color: #0366d6;
        }}

        .card-authors .model-author {{
            color: #888;
        }}

        .card-description {{
            font-size: 0.85em;
            color: #555;
            margin-bottom: 10px;
            flex-grow: 1;
            line-height: 1.4;
        }}

        .nodes-list {{
            font-size: 0.75em;
            color: #666;
            background: #f8f8f8;
            padding: 6px 10px;
            border-radius: 4px;
            margin-bottom: 10px;
            font-family: monospace;
        }}

        .nodes-label {{
            font-weight: bold;
            color: #333;
        }}

        .card-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-bottom: 10px;
        }}

        .tag {{
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 10px;
            font-weight: 500;
        }}

        .tag-io {{ background: #e3f2fd; color: #1565c0; }}

        .card-links {{
            margin-top: auto;
            display: flex;
            gap: 15px;
        }}

        .card-links a {{
            color: #0366d6;
            text-decoration: none;
            font-size: 0.85em;
        }}

        .card-links a:hover {{
            text-decoration: underline;
        }}

        nav {{
            background: white;
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}

        nav .nav-links {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            align-items: center;
        }}

        nav a {{
            color: #333;
            text-decoration: none;
            font-size: 14px;
        }}

        nav a:hover {{
            color: #3498db;
        }}

        .sort-controls {{
            display: flex;
            gap: 8px;
            margin-left: auto;
            align-items: center;
        }}

        .sort-controls label {{
            font-size: 13px;
            color: #666;
        }}

        .sort-btn {{
            padding: 5px 12px;
            border: 1px solid #ddd;
            background: white;
            border-radius: 4px;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .sort-btn:hover {{
            border-color: #3498db;
            color: #3498db;
        }}

        .sort-btn.active {{
            background: #3498db;
            color: white;
            border-color: #3498db;
        }}

        .filter-controls {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .filter-btn {{
            padding: 6px 14px;
            border: 1px solid #ddd;
            background: white;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .filter-btn:hover {{
            border-color: #3498db;
            color: #3498db;
        }}

        .filter-btn.active {{
            background: #3498db;
            color: white;
            border-color: #3498db;
        }}

        /* Modal for node viewer */
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 1000;
            overflow-y: auto;
        }}

        .modal.active {{
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding: 40px 20px;
        }}

        .modal-content {{
            background: #1a1a2e;
            border-radius: 12px;
            padding: 20px;
            max-width: 1200px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
        }}

        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            color: white;
        }}

        .modal-close {{
            background: none;
            border: none;
            color: white;
            font-size: 24px;
            cursor: pointer;
        }}

        .nodes-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 15px;
        }}

        /* ComfyUI-style node rendering */
        .comfy-node {{
            background: #2d2d44;
            border-radius: 8px;
            overflow: hidden;
            font-size: 12px;
        }}

        .comfy-node-header {{
            background: #3d5a80;
            color: white;
            padding: 8px 12px;
            font-weight: bold;
            font-size: 13px;
        }}

        .comfy-node-body {{
            padding: 10px;
        }}

        .comfy-node-row {{
            display: flex;
            align-items: center;
            margin: 4px 0;
        }}

        .comfy-socket {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 8px;
            flex-shrink: 0;
        }}

        .comfy-socket.output {{
            margin-right: 0;
            margin-left: 8px;
        }}

        .comfy-socket-IMAGE {{ background: #64b5f6; }}
        .comfy-socket-MASK {{ background: #fff176; }}
        .comfy-socket-LATENT {{ background: #ff79c6; }}
        .comfy-socket-MODEL {{ background: #b39ddb; }}
        .comfy-socket-CLIP {{ background: #ffb74d; }}
        .comfy-socket-VAE {{ background: #ef5350; }}
        .comfy-socket-CONDITIONING {{ background: #ffa726; }}
        .comfy-socket-FLOAT {{ background: #81c784; }}
        .comfy-socket-INT {{ background: #4db6ac; }}
        .comfy-socket-STRING {{ background: #90a4ae; }}
        .comfy-socket-MESH {{ background: #ce93d8; }}
        .comfy-socket-default {{ background: #78909c; }}

        .comfy-input-name {{
            color: #a0a0a0;
        }}

        .comfy-output-name {{
            color: #a0a0a0;
            text-align: right;
            flex-grow: 1;
        }}

        .comfy-type {{
            color: #606060;
            font-size: 10px;
            margin-left: 5px;
        }}

        .comfy-section-label {{
            color: #707070;
            font-size: 10px;
            margin: 8px 0 4px 0;
            text-transform: uppercase;
        }}

        .comfy-outputs {{
            border-top: 1px solid #404060;
            margin-top: 8px;
            padding-top: 8px;
        }}
    </style>
</head>

<body>
    <div class="header">
        <h1>Awesome ComfyUI 3D</h1>
        <p>A curated index of ComfyUI nodes for 3D generation, processing, and visualization.</p>
        <p><a href="https://github.com/PozzettiAndrea/ComfyUI-3D_nodes_index">GitHub</a></p>
    </div>

    <main>
        <nav>
            <div class="nav-links">
                <div class="filter-controls">
                    {filter_buttons}
                </div>
                <div class="sort-controls">
                    <label>Sort by:</label>
                    <button class="sort-btn active" onclick="sortCards('stars')">Stars</button>
                    <button class="sort-btn" onclick="sortCards('updated')">Last Updated</button>
                </div>
            </div>
        </nav>

        <div class="content">
            <div class="cards-container">
{all_cards}
            </div>
        </div>
    </main>

    <!-- Node viewer modal -->
    <div id="nodeModal" class="modal" onclick="if(event.target===this) closeModal()">
        <div class="modal-content">
            <div class="modal-header">
                <h2 id="modalTitle">Nodes</h2>
                <button class="modal-close" onclick="closeModal()">&times;</button>
            </div>
            <div id="nodesGrid" class="nodes-grid"></div>
        </div>
    </div>

    <script>
        // Socket color mapping
        const socketColors = {{
            'IMAGE': 'comfy-socket-IMAGE',
            'MASK': 'comfy-socket-MASK',
            'LATENT': 'comfy-socket-LATENT',
            'MODEL': 'comfy-socket-MODEL',
            'CLIP': 'comfy-socket-CLIP',
            'VAE': 'comfy-socket-VAE',
            'CONDITIONING': 'comfy-socket-CONDITIONING',
            'FLOAT': 'comfy-socket-FLOAT',
            'INT': 'comfy-socket-INT',
            'STRING': 'comfy-socket-STRING',
            'MESH': 'comfy-socket-MESH'
        }};

        function getSocketClass(type) {{
            return socketColors[type] || 'comfy-socket-default';
        }}

        function renderNode(name, def) {{
            let inputsHtml = '';

            // Required inputs
            if (def.inputs && def.inputs.required) {{
                const required = Object.entries(def.inputs.required);
                if (required.length > 0) {{
                    inputsHtml += '<div class="comfy-section-label">Required</div>';
                    for (const [inputName, inputType] of required) {{
                        const socketClass = getSocketClass(inputType);
                        inputsHtml += `
                            <div class="comfy-node-row">
                                <div class="comfy-socket ${{socketClass}}"></div>
                                <span class="comfy-input-name">${{inputName}}</span>
                                <span class="comfy-type">${{inputType}}</span>
                            </div>
                        `;
                    }}
                }}
            }}

            // Optional inputs
            if (def.inputs && def.inputs.optional) {{
                const optional = Object.entries(def.inputs.optional);
                if (optional.length > 0) {{
                    inputsHtml += '<div class="comfy-section-label">Optional</div>';
                    for (const [inputName, inputType] of optional) {{
                        const socketClass = getSocketClass(inputType);
                        inputsHtml += `
                            <div class="comfy-node-row">
                                <div class="comfy-socket ${{socketClass}}"></div>
                                <span class="comfy-input-name">${{inputName}}</span>
                                <span class="comfy-type">${{inputType}}</span>
                            </div>
                        `;
                    }}
                }}
            }}

            // Outputs
            let outputsHtml = '';
            if (def.outputs && def.outputs.length > 0) {{
                outputsHtml = '<div class="comfy-outputs">';
                for (let i = 0; i < def.outputs.length; i++) {{
                    const outputType = def.outputs[i];
                    const outputName = def.output_names && def.output_names[i] ? def.output_names[i] : outputType;
                    const socketClass = getSocketClass(outputType);
                    outputsHtml += `
                        <div class="comfy-node-row">
                            <span class="comfy-output-name">${{outputName}}</span>
                            <span class="comfy-type">${{outputType}}</span>
                            <div class="comfy-socket output ${{socketClass}}"></div>
                        </div>
                    `;
                }}
                outputsHtml += '</div>';
            }}

            return `
                <div class="comfy-node">
                    <div class="comfy-node-header">${{name}}</div>
                    <div class="comfy-node-body">
                        ${{inputsHtml}}
                        ${{outputsHtml}}
                    </div>
                </div>
            `;
        }}

        function showNodeDefs(card) {{
            const nodeData = JSON.parse(card.dataset.nodes || '{{}}');
            const title = card.querySelector('.card-title').textContent;

            document.getElementById('modalTitle').textContent = title + ' - Nodes';

            const grid = document.getElementById('nodesGrid');
            grid.innerHTML = '';

            const nodes = Object.entries(nodeData);
            if (nodes.length === 0) {{
                grid.innerHTML = '<p style="color: #888;">No node definitions found. The package may use dynamic registration.</p>';
            }} else {{
                for (const [name, def] of nodes) {{
                    grid.innerHTML += renderNode(name, def);
                }}
            }}

            document.getElementById('nodeModal').classList.add('active');
        }}

        function closeModal() {{
            document.getElementById('nodeModal').classList.remove('active');
        }}

        // Close on escape
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeModal();
        }});

        // Sorting functionality
        function sortCards(sortBy) {{
            // Update button states
            document.querySelectorAll('.sort-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            // Sort cards
            document.querySelectorAll('.cards-container').forEach(container => {{
                const cards = Array.from(container.querySelectorAll('.card'));

                cards.sort((a, b) => {{
                    if (sortBy === 'stars') {{
                        const starsA = parseInt(a.dataset.stars) || 0;
                        const starsB = parseInt(b.dataset.stars) || 0;
                        return starsB - starsA; // Descending
                    }} else if (sortBy === 'updated') {{
                        const dateA = a.dataset.updated || '';
                        const dateB = b.dataset.updated || '';
                        return dateB.localeCompare(dateA); // Descending (newest first)
                    }}
                    return 0;
                }});

                // Re-append in sorted order
                cards.forEach(card => container.appendChild(card));
            }});
        }}

        // Category filtering
        function filterCards(category) {{
            // Update button states
            document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            // Show/hide cards based on category
            document.querySelectorAll('.card').forEach(card => {{
                if (category === 'all' || card.dataset.category === category) {{
                    card.style.display = '';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
'''

def main():
    os.makedirs(CLONE_DIR, exist_ok=True)

    # Find and read CSV
    input_file = find_input_file()
    print(f"Reading {input_file}...")
    nodes_by_category = defaultdict(list)

    with open(input_file, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row.get("category", "other-3d")
            if category not in CATEGORIES:
                category = "other-3d"
            nodes_by_category[category].append(row)

    total = sum(len(nodes) for nodes in nodes_by_category.values())
    print(f"Found {total} packages in {len(nodes_by_category)} categories")

    # Sort by stars
    for category in nodes_by_category:
        nodes_by_category[category].sort(
            key=lambda n: int(n["stars"]) if n["stars"].isdigit() else 0,
            reverse=True
        )

    all_nodes = []
    for cat_nodes in nodes_by_category.values():
        all_nodes.extend(cat_nodes)

    # Step 1: Clone repos and extract node definitions
    print("\nStep 1: Extracting node definitions (cloning repos)...")
    node_defs = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS_CLONE) as executor:
        futures = {executor.submit(extract_repo_nodes, row): row for row in all_nodes}

        with tqdm(total=len(all_nodes), desc="Cloning & parsing", unit="repo") as pbar:
            for future in as_completed(futures):
                github_url, nodes = future.result()
                node_defs[github_url] = nodes
                pbar.set_postfix(nodes=sum(len(n) for n in node_defs.values()))
                pbar.update(1)

    total_nodes = sum(len(n) for n in node_defs.values())
    print(f"Extracted {total_nodes} node definitions")

    # Step 2: Fetch media and updated dates
    print("\nStep 2: Fetching media and dates from GitHub repos...")
    media_by_url = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS_MEDIA) as executor:
        futures = {executor.submit(fetch_node_media, node): node["github_url"] for node in all_nodes}

        with tqdm(total=len(all_nodes), desc="Fetching media", unit="repo") as pbar:
            for future in as_completed(futures):
                github_url = futures[future]
                try:
                    media, updated_at = future.result()
                    media_by_url[github_url] = (media, updated_at)
                except Exception:
                    media_by_url[github_url] = ([], "")
                pbar.update(1)

    # Build final structure (flat list)
    all_nodes_with_media = []
    for node in all_nodes:
        media, updated_at = media_by_url.get(node["github_url"], ([], ""))
        all_nodes_with_media.append((node, media, updated_at))

    # Generate HTML
    print("\nGenerating HTML...")
    html = generate_html(all_nodes_with_media, node_defs)

    Path(OUTPUT_FILE).write_text(html)
    print(f"Generated {OUTPUT_FILE}")

    # Cleanup
    shutil.rmtree(CLONE_DIR, ignore_errors=True)
    print("Done!")

if __name__ == "__main__":
    main()
