#!/usr/bin/env python3
"""
Fetch all ComfyUI nodes from ComfyUI-Manager and their READMEs into a CSV.
"""
import csv
import json
import re
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

OUTPUT_FILE = "all_comfyui_nodes.csv"
MANAGER_URL = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/custom-node-list.json"
MAX_WORKERS = 50  # Can go higher since it's just HTTP

def fetch_manager_nodes():
    """Fetch nodes from ComfyUI-Manager custom-node-list.json."""
    print("Fetching from ComfyUI-Manager...")
    req = Request(MANAGER_URL)
    with urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    nodes = data.get("custom_nodes", [])
    print(f"Found {len(nodes)} nodes")
    return nodes

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
    idx, node, owner, repo = args
    readme = fetch_readme(owner, repo)
    name = node.get("title") or node.get("name") or repo
    desc = node.get("description", "")[:500]
    github_url = f"https://github.com/{owner}/{repo}"
    return (idx, [name, github_url, owner, desc, readme])

def main():
    nodes = fetch_manager_nodes()

    # Deduplicate by GitHub repo
    seen_repos = set()
    unique_nodes = []

    for node in nodes:
        owner, repo = extract_github_info(node)
        if owner and repo:
            key = f"{owner}/{repo}".lower()
            if key not in seen_repos:
                seen_repos.add(key)
                unique_nodes.append((node, owner, repo))

    total = len(unique_nodes)
    print(f"Unique GitHub repos: {total}")
    print(f"Fetching READMEs with {MAX_WORKERS} parallel workers...")

    # Prepare work items
    work_items = [(i, node, owner, repo) for i, (node, owner, repo) in enumerate(unique_nodes)]

    # Process in parallel
    results = [None] * total
    completed = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_node, item): item[0] for item in work_items}

        for future in as_completed(futures):
            idx, row = future.result()
            results[idx] = row
            completed += 1
            if completed % 100 == 0 or completed == total:
                print(f"Progress: {completed}/{total}")

    # Write CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "github_url", "author", "description", "readme"])
        for row in results:
            if row:
                writer.writerow(row)

    print(f"\nDone! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
