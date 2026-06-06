#!/usr/bin/env python3
"""
Fetch all ComfyUI nodes from ComfyUI-Manager AND Comfy Registry, merge and dedupe.
"""
import csv
import glob
import json
import re
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

DATE_TAG = datetime.now().strftime("%Y-%m-%d")
OUTPUT_FILE = f"all_comfyui_nodes_{DATE_TAG}.csv"
MANAGER_URL = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json"
STATS_URL = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/github-stats.json"
REGISTRY_URL = "https://api.comfy.org/nodes"
MAX_WORKERS = 50

def load_classified_urls():
    """Return lowercased github_urls already classified (3D or non-3D) in prior runs.

    Incremental fetch: any repo present in an ai_3d_nodes*.csv or ai_non_3d_nodes*.csv
    has already had its README fetched and classified, so we skip re-downloading it.
    """
    classified = set()
    for path in glob.glob("ai_3d_nodes*.csv") + glob.glob("ai_non_3d_nodes*.csv"):
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = (row.get("github_url") or "").strip().lower()
                    if url:
                        classified.add(url)
        except Exception:
            continue
    return classified

def fetch_manager_nodes():
    """Fetch nodes from ComfyUI-Manager custom-node-list.json."""
    print("Fetching from ComfyUI-Manager...")
    req = Request(MANAGER_URL)
    with urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    nodes = data.get("custom_nodes", [])
    print(f"  Found {len(nodes)} nodes")
    return nodes

def fetch_registry_nodes():
    """Fetch all nodes from Comfy Registry API."""
    print("Fetching from Comfy Registry...")
    nodes = []
    page = 1
    while True:
        url = f"{REGISTRY_URL}?limit=100&page={page}"
        req = Request(url, headers={"User-Agent": "ComfyUI-3D-Index"})
        try:
            with urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            nodes.extend(data.get("nodes", []))
            total_pages = data.get("totalPages", 1)
            if page >= total_pages:
                break
            page += 1
            if page % 10 == 0:
                print(f"  Page {page}/{total_pages}...")
        except Exception as e:
            print(f"  Error on page {page}: {e}")
            break
    print(f"  Found {len(nodes)} nodes")
    return nodes

def fetch_github_stats():
    """Fetch star counts from github-stats.json."""
    print("Fetching GitHub stats...")
    req = Request(STATS_URL)
    with urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def extract_github_info(node):
    """Extract GitHub owner/repo from node data."""
    repo_url = node.get("reference", "") or node.get("repository", "") or ""
    match = re.search(r"github\.com/([^/]+)/([^/\s]+)", repo_url)
    if match:
        return match.group(1), match.group(2).replace(".git", "")
    return None, None

def fetch_readme(owner, repo):
    """Fetch README via raw.githubusercontent.com"""
    for branch in ["main", "master"]:
        for fname in ["README.md", "readme.md", "Readme.md"]:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{fname}"
            try:
                with urlopen(url, timeout=10) as resp:
                    return resp.read().decode("utf-8", errors="replace")
            except:
                continue
    return ""

def process_node(args):
    """Process a single node - fetch its README."""
    idx, node, owner, repo, stars = args
    readme = fetch_readme(owner, repo)
    name = node.get("title") or node.get("name") or repo
    desc = node.get("description", "")[:500]
    github_url = f"https://github.com/{owner}/{repo}"
    return (idx, [name, github_url, stars, owner, desc, readme])

def extract_github_info_from_url(url):
    """Extract owner/repo from a GitHub URL."""
    if not url:
        return None, None
    match = re.search(r"github\.com/([^/]+)/([^/\s]+)", url)
    if match:
        return match.group(1), match.group(2).replace(".git", "").rstrip("/")
    return None, None

def main():
    # Fetch from both sources
    manager_nodes = fetch_manager_nodes()
    registry_nodes = fetch_registry_nodes()
    stats = fetch_github_stats()

    # Merge and deduplicate by GitHub repo URL
    seen_repos = {}  # key -> (node_dict, owner, repo, stars)

    # Process ComfyUI-Manager nodes first (priority source)
    for node in manager_nodes:
        owner, repo = extract_github_info(node)
        if owner and repo:
            key = f"{owner}/{repo}".lower()
            github_url = f"https://github.com/{owner}/{repo}"
            stars = stats.get(github_url, {}).get("stars", 0)
            if key not in seen_repos:
                seen_repos[key] = (node, owner, repo, stars)

    manager_count = len(seen_repos)
    print(f"After ComfyUI-Manager: {manager_count} unique repos")

    # Add Registry nodes (fill in missing)
    registry_added = 0
    for node in registry_nodes:
        repo_url = node.get("repository", "")
        owner, repo = extract_github_info_from_url(repo_url)
        if owner and repo:
            key = f"{owner}/{repo}".lower()
            if key not in seen_repos:
                # Convert registry format to our format
                node_dict = {
                    "title": node.get("name", ""),
                    "description": node.get("description", ""),
                    "reference": repo_url
                }
                stars = node.get("github_stars", 0)
                seen_repos[key] = (node_dict, owner, repo, stars)
                registry_added += 1

    print(f"Added {registry_added} new repos from Registry")

    unique_nodes = list(seen_repos.values())
    print(f"Total unique GitHub repos: {len(unique_nodes)}")

    # Incremental: skip repos already classified (3D or non-3D) in prior runs.
    classified = load_classified_urls()
    if classified:
        before = len(unique_nodes)
        unique_nodes = [
            (node, owner, repo, stars)
            for (node, owner, repo, stars) in unique_nodes
            if f"https://github.com/{owner}/{repo}".lower() not in classified
        ]
        print(f"Skipping {before - len(unique_nodes)} already-classified repos; "
              f"fetching {len(unique_nodes)} new ones")

    total = len(unique_nodes)

    # Prepare work items
    work_items = [(i, node, owner, repo, stars) for i, (node, owner, repo, stars) in enumerate(unique_nodes)]

    # Process in parallel
    results = [None] * total

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_node, item): item[0] for item in work_items}

        with tqdm(total=total, desc="Fetching READMEs", unit="repo") as pbar:
            for future in as_completed(futures):
                idx, row = future.result()
                results[idx] = row
                pbar.update(1)

    # Write CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "github_url", "stars", "author", "description", "readme"])
        for row in results:
            if row:
                writer.writerow(row)

    print(f"\nDone! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
