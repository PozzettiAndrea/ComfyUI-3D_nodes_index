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
    """Convert relative URLs and GitHub blob URLs to raw URLs."""
    if not url:
        return ""

    # Convert GitHub blob URLs to raw URLs
    # https://github.com/owner/repo/blob/branch/path -> https://raw.githubusercontent.com/owner/repo/branch/path
    blob_match = re.match(r'https?://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)', url)
    if blob_match:
        return f"https://raw.githubusercontent.com/{blob_match.group(1)}/{blob_match.group(2)}/{blob_match.group(3)}/{blob_match.group(4)}"

    if url.startswith(('http://', 'https://')):
        return url
    url = url.lstrip('./')
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{url}"

def is_media_url(url):
    """Check if URL points to a media file."""
    url_lower = url.lower().split('?')[0]
    # Check file extensions
    if any(url_lower.endswith(ext) for ext in MEDIA_EXTS):
        return True
    # GitHub user-attachments (no extension, but can be images or videos)
    if 'github.com/user-attachments/assets/' in url_lower:
        return True
    # GitHub repo assets (format: github.com/{owner}/{repo}/assets/{user_id}/{uuid})
    if re.search(r'github\.com/[^/]+/[^/]+/assets/\d+/', url_lower):
        return True
    return False

def detect_media_type(url):
    """Detect if URL is video or image via HEAD request. Returns 'video', 'image', or None."""
    # If URL has extension, use that
    url_lower = url.lower().split('?')[0]
    if any(url_lower.endswith(ext) for ext in VIDEO_EXTS):
        return 'video'
    if any(url_lower.endswith(ext) for ext in IMAGE_EXTS):
        return 'image'

    # For extensionless URLs (like GitHub user-attachments), check Content-Type
    if 'user-attachments/assets/' in url or re.search(r'/assets/\d+/', url):
        try:
            req = Request(url, method='HEAD', headers={"User-Agent": "ComfyUI-3D-Index"})
            with urlopen(req, timeout=5) as resp:
                content_type = resp.headers.get('Content-Type', '').lower()
                if 'video' in content_type:
                    return 'video'
                if 'image' in content_type:
                    return 'image'
        except Exception:
            pass
    return 'image'  # Default to image

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

def generate_media_gallery(media_urls, media_types=None):
    """Generate HTML for media gallery."""
    if not media_urls:
        return ""

    media_types = media_types or {}
    items = []
    for url in media_urls[:6]:
        media_type = media_types.get(url, detect_media_type(url))
        if media_type == 'video':
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

    # Detect media types for extensionless URLs
    media_types = {url: detect_media_type(url) for url in media_urls} if media_urls else {}

    # Generate media gallery
    gallery_html = generate_media_gallery(media_urls, media_types)
    fallback_style = "" if media_urls else 'style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 120px;"'

    # Data attributes for client-side rendering
    node_data = json.dumps(package_nodes) if package_nodes else "{}"
    # Store media as list of {url, type} objects for proper JS rendering
    media_with_types = [{"url": url, "type": media_types.get(url, "image")} for url in media_urls] if media_urls else []
    media_data = json.dumps(media_with_types)

    # Format updated date for display
    updated_display = ""
    if updated_at:
        updated_display = updated_at[:10]  # Just the date part

    return f'''
                    <div class="card" data-tags="{data_tag}" data-nodes='{node_data}' data-media='{media_data}' data-stars="{stars_raw}" data-updated="{updated_at}" data-category="{category}" data-github="{github_url}" data-description="{description}" data-author="{node_author}" data-model-author="{model_author}" onclick="openDetail(this)">
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
                        </div>
                    </div>'''

TEMPLATE_FILE = Path(__file__).parent / "template.html"

def generate_html(all_nodes_with_media, node_defs):
    """Generate complete HTML page using template."""

    # Load template
    template = TEMPLATE_FILE.read_text()

    # Collect all unique categories
    categories_in_use = set()
    for node, media, updated in all_nodes_with_media:
        categories_in_use.add(node.get("category", "other-3d"))

    # Generate filter buttons
    filter_buttons = '<button class="filter-btn active" onclick="filterCards(\'all\')">All</button>\n'
    for cat_id, cat_name in CATEGORIES.items():
        if cat_id in categories_in_use:
            filter_buttons += f'                    <button class="filter-btn" onclick="filterCards(\'{cat_id}\')">{cat_name}</button>\n'

    # Generate all cards in one grid (sorted by stars)
    sorted_nodes = sorted(all_nodes_with_media, key=lambda x: int(x[0]["stars"]) if x[0]["stars"].isdigit() else 0, reverse=True)
    all_cards = "\n".join(generate_card(node, media, node_defs, updated) for node, media, updated in sorted_nodes)

    # Replace placeholders
    html = template.replace("<!-- FILTER_BUTTONS -->", filter_buttons)
    html = html.replace("<!-- CARDS -->", all_cards)

    return html

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
