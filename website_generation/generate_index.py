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
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

OUTPUT_FILE = "../index.html"

def load_all_3d_nodes():
    """Load and merge every ai_3d_nodes*.csv into one deduped list of rows.

    Fetch is incremental, so each dated CSV holds only the repos newly found that run.
    The full catalog is the union of all of them. We dedupe by github_url with
    newest-file-wins (later date suffix overrides earlier), so re-classified repos keep
    their most recent category/description.
    """
    files = sorted(glob.glob("ai_3d_nodes*.csv"))  # ascending by date suffix
    if not files:
        if Path("3d_nodes.csv").exists():
            files = ["3d_nodes.csv"]
        else:
            raise FileNotFoundError("No ai_3d_nodes*.csv or 3d_nodes.csv found")

    by_url = {}  # github_url(lower) -> row; later files overwrite earlier
    for path in files:
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                url = (row.get("github_url") or "").strip()
                if url:
                    row["category"] = normalize_category(row.get("category"))
                    by_url[url.lower()] = row
    print(f"Merged {len(files)} CSV(s) -> {len(by_url)} unique 3D packages")
    return list(by_url.values())

def normalize_category(value):
    """Coerce a classifier category to one of CATEGORIES.

    The model occasionally hedges and returns several categories in one field
    ("visualization,mesh-processing" or "text-to-3d|image-to-3d"). A package lives in
    exactly one bucket here, and the value is now also a URL slug, so take the first
    recognised category rather than dropping the package into Other 3D.
    """
    raw = (value or "").strip()
    if raw in CATEGORIES:
        return raw
    for part in re.split(r"[,|/;]+", raw):
        part = part.strip().lower()
        if part in CATEGORIES:
            return part
    return "other-3d"

CLONE_DIR = "/tmp/comfyui_nodes"
MAX_WORKERS_CLONE = 5
MAX_WORKERS_MEDIA = 20

# This stage makes ~2 GitHub API calls per package. Anonymous access is capped at
# 60 requests/hour, which silently returns empty media and dates for most of the
# catalog. A token raises the cap to 5000/hour. Falls back to the gh CLI's token.
def _candidate_tokens():
    for env in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(env)
        if value and value.strip():
            yield env, value.strip()
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0 and result.stdout.strip():
            yield "gh auth token", result.stdout.strip()
    except Exception:
        pass

def _github_token():
    """Return the first token that actually authenticates, else "" for anonymous.

    An expired token is worse than none: GitHub answers 401 to every request, where
    anonymous access would still have served 60 requests/hour. Verify once up front
    rather than silently producing an index with no dates or media.
    """
    for source, token in _candidate_tokens():
        try:
            req = Request("https://api.github.com/rate_limit",
                          headers={"User-Agent": "ComfyUI-3D-Index", "Authorization": f"Bearer {token}"})
            with urlopen(req, timeout=15) as resp:
                limit = json.loads(resp.read())["rate"]["limit"]
            print(f"GitHub auth: using {source} ({limit} requests/hour)")
            return token
        except HTTPError as e:
            if e.code == 401:
                print(f"GitHub auth: {source} is invalid/expired — ignoring it")
                continue
            print(f"GitHub auth: {source} check failed ({e.code}) — ignoring it")
        except Exception as e:
            print(f"GitHub auth: {source} check failed ({e}) — ignoring it")
    print("GitHub auth: anonymous (60 requests/hour) — dates and media will be "
          "incomplete for a catalog this size. Set GITHUB_TOKEN or run: gh auth login")
    return ""

GITHUB_TOKEN = _github_token()

def github_headers():
    headers = {"User-Agent": "ComfyUI-3D-Index"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

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

    # Standalone GitHub asset URLs (rendered as inline media by GitHub)
    asset_pattern = r'https://github\.com/(?:user-attachments/assets/[a-f0-9-]+|[^/]+/[^/]+/assets/\d+/[a-f0-9-]+)'
    for match in re.finditer(asset_pattern, readme_content):
        url = match.group(0).strip()
        if url not in media:  # Avoid duplicates
            media.append(url)

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

# Probing an extensionless URL costs a network round trip. Card generation is
# single-threaded, so without this cache the whole catalog is probed serially and
# dominates the runtime of the final stage. warm_media_type_cache() fills it in parallel.
_MEDIA_TYPE_CACHE = {}

def warm_media_type_cache(media_by_url):
    """Resolve every media type up front, in parallel, so generate_card() never blocks."""
    urls = {url for media, _, _ in media_by_url.values() for url in media}
    todo = [u for u in urls if u not in _MEDIA_TYPE_CACHE]
    if not todo:
        return
    with ThreadPoolExecutor(max_workers=MAX_WORKERS_MEDIA) as executor:
        futures = {executor.submit(detect_media_type, url): url for url in todo}
        with tqdm(total=len(todo), desc="Resolving media types", unit="url") as pbar:
            for future in as_completed(futures):
                try:
                    _MEDIA_TYPE_CACHE[futures[future]] = future.result()
                except Exception:
                    _MEDIA_TYPE_CACHE[futures[future]] = 'image'
                pbar.update(1)

def detect_media_type(url):
    """Detect if URL is video or image via HEAD request. Returns 'video', 'image', or None."""
    if url in _MEDIA_TYPE_CACHE:
        return _MEDIA_TYPE_CACHE[url]
    # If URL has extension, use that
    url_lower = url.lower().split('?')[0]
    if any(url_lower.endswith(ext) for ext in VIDEO_EXTS):
        return 'video'
    if any(url_lower.endswith(ext) for ext in IMAGE_EXTS):
        return 'image'

    # For extensionless URLs (like GitHub user-attachments), check Content-Type via GET request
    # Note: GitHub blocks HEAD requests with 403, so we must use GET and close immediately
    if 'user-attachments/assets/' in url or re.search(r'/assets/\d+/', url):
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            with urlopen(req, timeout=10) as resp:
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
        req = Request(url, headers=github_headers())
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

def fetch_repo_meta(owner, repo):
    """Fetch live repo state from GitHub.

    One call yields the push date, the current star count and whether the repo still
    exists. Stars in the CSVs are frozen at classification time (the pipeline never
    re-classifies an indexed repo), so this is what keeps them honest.

    state is 'ok' | 'archived' | 'moved' | 'gone' | 'unknown'. Only 'gone' is a
    definitive 404/410; 'unknown' means the request failed and the caller must not
    treat it as evidence of anything.
    """
    meta = {"updated_at": "", "stars": None, "state": "unknown", "full_name": ""}
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        req = Request(url, headers=github_headers())
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        meta["updated_at"] = data.get("pushed_at", "")  # ISO: 2024-01-15T10:30:00Z
        meta["stars"] = data.get("stargazers_count")
        meta["full_name"] = data.get("full_name", "")
        if data.get("archived"):
            meta["state"] = "archived"
        elif meta["full_name"].lower() != f"{owner}/{repo}".lower():
            meta["state"] = "moved"
        else:
            meta["state"] = "ok"
    except HTTPError as e:
        if e.code in (404, 410):
            meta["state"] = "gone"
    except Exception:
        pass
    return meta

def fetch_node_media(node):
    """Fetch all media for a node."""
    github_url = node["github_url"]
    owner, repo = extract_github_info(github_url)

    if not owner or not repo:
        return [], {"updated_at": "", "stars": None, "state": "unknown", "full_name": ""}, ""

    readme, branch = fetch_readme(owner, repo)
    readme_media = extract_media_from_readme(readme, owner, repo, branch)
    repo_media = fetch_repo_media(owner, repo, branch)
    meta = fetch_repo_meta(owner, repo)

    readme_set = set(readme_media)
    all_media = readme_media + [m for m in repo_media if m not in readme_set]

    # Clean readme for search: strip markdown, limit size
    readme_text = clean_readme_for_search(readme)

    return all_media[:12], meta, readme_text

def clean_readme_for_search(readme):
    """Clean README content for search indexing."""
    if not readme:
        return ""
    # Remove markdown links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', readme)
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]+`', '', text)
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Limit to 5000 chars to keep HTML size reasonable
    return text[:5000]

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

def slugify(value):
    """Lowercase URL slug for a package, used as its /node/<slug> route."""
    slug = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return slug or "package"

def build_slug_map(all_nodes):
    """Map github_url -> unique URL slug. Two repos can share a name across owners,
    so collisions fall back to <owner>-<repo>, then a numeric suffix."""
    slugs = {}
    used = set()
    for node in all_nodes:
        github_url = node["github_url"]
        owner, repo_name = extract_github_info(github_url)
        base = slugify(repo_name or node["name"])
        candidate = base
        if candidate in used and owner:
            candidate = slugify(f"{owner}-{repo_name}")
        n = 2
        while candidate in used:
            candidate = f"{base}-{n}"
            n += 1
        used.add(candidate)
        slugs[github_url] = candidate
    return slugs

def generate_card(node, media_urls, node_defs, updated_at, readme="", slug=""):
    """Generate HTML for a single card"""
    github_url = node["github_url"]
    # Use repo name from URL instead of package title
    _, repo_name = extract_github_info(github_url)
    name = repo_name or node["name"]
    slug = slug or slugify(name)
    stars_raw = node["stars"]
    stars = format_stars(stars_raw)
    node_author = node["node_author"]
    model_author = node["model_author"] or "Community"
    description = node["description"]
    category = node["category"]
    data_tag = get_data_tag(model_author)
    # Escape readme for HTML attribute
    readme_escaped = readme.replace('"', '&quot;').replace("'", '&#39;').replace('<', '&lt;').replace('>', '&gt;') if readme else ""

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

    # Data attributes for client-side rendering.
    # These JSON blobs sit inside single-quoted HTML attributes and are read back via
    # card.dataset.* + JSON.parse, so escape HTML-significant chars (esp. apostrophes,
    # which appear in stringified combo widgets like "['sRGB', 'Linear']" and would
    # otherwise terminate the attribute early). The browser decodes them before JSON.parse.
    def esc_attr(s):
        return s.replace('&', '&amp;').replace("'", '&#39;').replace('<', '&lt;').replace('>', '&gt;')

    node_data = esc_attr(json.dumps(package_nodes) if package_nodes else "{}")
    # Store media as list of {url, type} objects for proper JS rendering
    media_with_types = [{"url": url, "type": media_types.get(url, "image")} for url in media_urls] if media_urls else []
    media_data = esc_attr(json.dumps(media_with_types))

    # Last-updated badge. Colour-coded by age so a dead package is obvious at a glance
    # without reading the date.
    updated_display = updated_at[:10] if updated_at else ""
    freshness = "unknown"
    if updated_display:
        try:
            age = (datetime.now(timezone.utc) - datetime.strptime(updated_display, "%Y-%m-%d").replace(tzinfo=timezone.utc)).days
            freshness = "fresh" if age <= 90 else "recent" if age <= 365 else "stale"
        except ValueError:
            pass
    updated_html = (
        f'<div class="card-updated {freshness}" title="Last pushed {updated_display}">'
        f'<i class="far fa-clock"></i> {updated_display}</div>'
        if updated_display else
        '<div class="card-updated unknown" title="No push date available">'
        '<i class="far fa-clock"></i> unknown</div>'
    )

    return f'''
                    <div class="card" data-slug="{slug}" data-name="{name}" data-tags="{data_tag}" data-nodes='{node_data}' data-media='{media_data}' data-stars="{stars_raw}" data-updated="{updated_at}" data-category="{category}" data-github="{github_url}" data-description="{description}" data-author="{node_author}" data-model-author="{model_author}" data-readme="{readme_escaped}" onclick="openDetail(this)">
                        <div class="card-media" {fallback_style}>
                            {gallery_html if media_urls else ""}
                        </div>
                        <div class="card-content">
                            <div class="card-header">
                                <div class="card-title">{name}</div>
                                <div class="card-badges">
                                    <div class="card-stars"><i class="fas fa-star"></i> {stars}</div>
                                    {updated_html}
                                </div>
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
    for node, media, updated, readme in all_nodes_with_media:
        categories_in_use.add(node.get("category", "other-3d"))

    # Package count per category, shown on the filter buttons so the size of each
    # category is visible before clicking into it. The count element is updated live
    # by applyFilters() as the search narrows, so these are just the initial values.
    counts = Counter(node.get("category", "other-3d") for node, _, _, _ in all_nodes_with_media)

    # Generate filter buttons. data-category is the URL slug the router reads/writes,
    # so the button set doubles as the list of valid category routes. data-label keeps
    # the clean name available for page titles, free of the count.
    filter_buttons = (
        f'<button class="filter-btn active" data-category="all" data-label="All" '
        f'onclick="filterCards(this)">All <span class="filter-count">'
        f'{len(all_nodes_with_media)}</span></button>\n'
    )
    for cat_id, cat_name in CATEGORIES.items():
        if cat_id in categories_in_use:
            filter_buttons += (
                f'                    <button class="filter-btn" data-category="{cat_id}" '
                f'data-label="{cat_name}" onclick="filterCards(this)">{cat_name} '
                f'<span class="filter-count">{counts[cat_id]}</span></button>\n'
            )

    # Generate all cards in one grid (sorted by stars)
    sorted_nodes = sorted(all_nodes_with_media, key=lambda x: int(x[0]["stars"]) if x[0]["stars"].isdigit() else 0, reverse=True)
    slug_map = build_slug_map([node for node, _, _, _ in sorted_nodes])
    all_cards = "\n".join(
        generate_card(node, media, node_defs, updated, readme, slug_map.get(node["github_url"], ""))
        for node, media, updated, readme in sorted_nodes
    )

    # Replace placeholders
    html = template.replace("<!-- FILTER_BUTTONS -->", filter_buttons)
    html = html.replace("<!-- CARDS -->", all_cards)

    return html

def main():
    os.makedirs(CLONE_DIR, exist_ok=True)

    # Load and merge all 3D CSVs (incremental fetch means each file is partial)
    nodes_by_category = defaultdict(list)
    for row in load_all_3d_nodes():
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
                empty = ([], {"updated_at": "", "stars": None, "state": "unknown", "full_name": ""}, "")
                try:
                    media_by_url[github_url] = future.result()
                except Exception:
                    media_by_url[github_url] = empty
                pbar.update(1)

    # Refresh stars from the live repo data and drop packages whose repo is gone.
    # Only a definitive 404/410 counts as gone: a failed request must never delete
    # a package from the index.
    empty_meta = {"updated_at": "", "stars": None, "state": "unknown", "full_name": ""}
    gone, moved, archived, restarred = [], [], [], []
    live_nodes = []
    for node in all_nodes:
        media, meta, readme = media_by_url.get(node["github_url"], ([], empty_meta, ""))
        if meta["state"] == "gone":
            gone.append(node)
            continue
        if meta["state"] == "moved":
            moved.append((node, meta["full_name"]))
        elif meta["state"] == "archived":
            archived.append(node)
        if meta["stars"] is not None:
            was = node["stars"]
            if str(meta["stars"]) != str(was):
                restarred.append((node, was, meta["stars"]))
            node["stars"] = str(meta["stars"])
        live_nodes.append(node)

    # Collapse entries that resolve to the same repo. When a repo is renamed or merged
    # into another, GitHub keeps redirecting the old URL, so both the old and the new
    # name sit in the CSVs and the catalog shows one project as two cards. Keep the
    # entry whose URL matches the repo's current full_name.
    by_repo = defaultdict(list)
    for node in live_nodes:
        meta = media_by_url.get(node["github_url"], ([], empty_meta, ""))[1]
        key = (meta["full_name"] or node["github_url"]).lower()
        by_repo[key].append(node)

    deduped, dupes = [], []
    for key, nodes in by_repo.items():
        if len(nodes) == 1:
            deduped.append(nodes[0])
            continue
        # Prefer the entry already using the repo's canonical name.
        def canonical_name(node):
            owner, repo = extract_github_info(node["github_url"])
            return f"{owner}/{repo}".lower() if owner and repo else ""

        canonical = next((n for n in nodes if canonical_name(n) == key), nodes[0])
        deduped.append(canonical)
        dupes.extend((n, canonical) for n in nodes if n is not canonical)

    # Identity, not equality: two rows can compare equal as dicts.
    keep_ids = {id(n) for n in deduped}
    live_nodes = [n for n in live_nodes if id(n) in keep_ids]

    print(f"\nLive check: {len(live_nodes)} kept, {len(gone)} hidden (repo gone), "
          f"{len(dupes)} hidden (duplicate of a renamed repo), "
          f"{len(archived)} archived, {len(restarred)} star counts refreshed")
    for node in gone:
        print(f"  gone:      {node['name'][:38]:40} {node['github_url']}")
    for node, canonical in dupes:
        print(f"  duplicate: {node['github_url']}  ==  {canonical['github_url']}")

    # Build final structure (flat list)
    all_nodes_with_media = []
    for node in live_nodes:
        media, meta, readme = media_by_url.get(node["github_url"], ([], empty_meta, ""))
        all_nodes_with_media.append((node, media, meta["updated_at"], readme))

    warm_media_type_cache(media_by_url)

    # Generate HTML
    print("\nGenerating HTML...")
    html = generate_html(all_nodes_with_media, node_defs)

    Path(OUTPUT_FILE).write_text(html)
    print(f"Generated {OUTPUT_FILE}")

    # Router paths (/gaussian-splatting, /node/<slug>) 404 on GitHub Pages without
    # this shim, which bounces them back to index.html with the path preserved.
    shutil.copyfile(Path(__file__).parent / "404.html", Path(OUTPUT_FILE).parent / "404.html")
    print(f"Copied 404.html routing shim to {Path(OUTPUT_FILE).parent / '404.html'}")

    # Cleanup
    shutil.rmtree(CLONE_DIR, ignore_errors=True)
    print("Done!")

if __name__ == "__main__":
    main()
