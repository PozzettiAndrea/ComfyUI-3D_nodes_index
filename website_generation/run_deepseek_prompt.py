#!/usr/bin/env python3
"""
Filter ComfyUI nodes for 3D relevance using DeepSeek via OpenRouter.
Outputs AI-generated analysis to ai_3d_nodes.csv
"""
import csv
import json
import getpass
import glob
import os
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import urlopen, Request
from pathlib import Path
from tqdm import tqdm

# all_comfyui_nodes_*.csv stores whole READMEs in one field, which routinely exceeds
# csv's default 128 KB field cap and aborts the read with "field larger than field limit".
csv.field_size_limit(1 << 30)

DATE_TAG = datetime.now().strftime("%Y-%m-%d")
OUTPUT_3D = f"ai_3d_nodes_{DATE_TAG}.csv"
OUTPUT_NON_3D = f"ai_non_3d_nodes_{DATE_TAG}.csv"  # Also serves as skip list
PROMPT_FILE = "deepseek_prompt.txt"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-chat"
MAX_WORKERS = 30

def find_latest_input_file():
    """Find the most recent all_comfyui_nodes_*.csv file."""
    files = glob.glob("all_comfyui_nodes_*.csv")
    if not files:
        # Fallback to old name
        if Path("all_comfyui_nodes.csv").exists():
            return "all_comfyui_nodes.csv"
        raise FileNotFoundError("No all_comfyui_nodes*.csv found")
    return sorted(files)[-1]  # Latest by date suffix

def load_prompt():
    """Load system prompt from file."""
    return Path(PROMPT_FILE).read_text()

def load_skip_list():
    """Load repos to skip from all ai_non_3d_nodes*.csv files"""
    skip = set()
    # Scan all non-3D CSVs (across all dates)
    for path in glob.glob("ai_non_3d_nodes*.csv"):
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    skip.add(row["github_url"].lower())
        except Exception:
            continue
    return skip

def classify_node(api_key, system_prompt, row):
    """Classify a single node using DeepSeek."""
    name, github_url, stars, author, desc, readme = row

    # Truncate readme to save tokens
    readme_short = readme[:3000] if readme else ""

    user_msg = f"Package: {name}\nURL: {github_url}\nAuthor: {author}\nDescription: {desc}\n\nREADME:\n{readme_short}"

    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_msg}
        ],
        "max_tokens": 300,
        "temperature": 0
    }).encode()

    req = Request(OPENROUTER_URL, data=payload, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/ComfyUI-3D_nodes_index",
        "X-Title": "ComfyUI 3D Node Filter"
    })

    try:
        with urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
            content = result["choices"][0]["message"]["content"]
            # Try to parse JSON, handle if model wraps in markdown
            content = content.strip()
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            return json.loads(content)
    except Exception as e:
        return {"relevant": False, "confidence": "low", "category": "", "model_author": "", "description": "", "nodes_list": "", "_debug": str(e)[:200]}

def main():
    api_key = os.environ.get("OPENROUTER_API_KEY") or getpass.getpass("OpenRouter API key: ")
    system_prompt = load_prompt()
    skip_list = load_skip_list()

    # Find and read input CSV
    input_file = find_latest_input_file()
    print(f"Reading {input_file}...")
    all_rows = []
    with open(input_file, encoding="utf-8") as f:
        reader = csv.reader(line.replace("\x00", "") for line in f)
        header = next(reader)
        for row in reader:
            all_rows.append(row)

    print(f"Found {len(all_rows)} total nodes")

    # Filter out already-skipped repos
    rows = []
    for row in all_rows:
        github_url = row[1].lower()
        if github_url not in skip_list:
            rows.append(row)

    skipped = len(all_rows) - len(rows)
    if skipped:
        print(f"Skipping {skipped} repos already classified (in ai_non_3d_nodes*.csv)")

    # Top N by stars: env var TOP_N, or interactive prompt if stdin is a TTY, else all
    top_n = os.environ.get("TOP_N", "").strip()
    if not top_n and sys.stdin.isatty():
        top_n = input("Top N nodes by stars (blank for all): ").strip()
    if top_n:
        top_n = int(top_n)
        # Sort by stars (column 2) descending
        rows.sort(key=lambda r: int(r[2]) if r[2].isdigit() else 0, reverse=True)
        rows = rows[:top_n]
        print(f"Selected top {top_n} nodes by stars")

    print(f"Classifying {len(rows)} nodes with {MAX_WORKERS} workers...")

    results_3d = []
    results_non_3d = []
    errors = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(classify_node, api_key, system_prompt, row): row for row in rows}

        with tqdm(total=len(rows), desc="Classifying", unit="node") as pbar:
            for future in as_completed(futures):
                row = futures[future]
                result = future.result()

                if "_debug" in result:
                    errors.append((row[0], result["_debug"]))
                elif result.get("relevant"):
                    results_3d.append((row, result))
                else:
                    results_non_3d.append((row, result))

                pbar.set_postfix(found=len(results_3d), errs=len(errors))
                pbar.update(1)

    if errors:
        print(f"\n{len(errors)} errors occurred. First 3:")
        for name, err in errors[:3]:
            print(f"  - {name}: {err}")

    # CSV header for both files
    header = ["name", "github_url", "stars", "node_author", "model_author", "description", "nodes_list", "category", "confidence"]

    def write_results(filename, results):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row, result in results:
                writer.writerow([
                    row[0],  # name
                    row[1],  # github_url
                    row[2],  # stars
                    row[3],  # node_author
                    result.get("model_author", ""),
                    result.get("description", ""),
                    result.get("nodes_list", ""),
                    result.get("category", ""),
                    result.get("confidence", "")
                ])

    # Write 3D nodes
    print(f"\nWriting {len(results_3d)} 3D nodes to {OUTPUT_3D}...")
    write_results(OUTPUT_3D, results_3d)

    # Write non-3D nodes (append to existing)
    existing_non_3d = []
    if Path(OUTPUT_NON_3D).exists():
        with open(OUTPUT_NON_3D, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            existing_non_3d = list(reader)

    print(f"Writing {len(results_non_3d)} new non-3D nodes to {OUTPUT_NON_3D}...")
    with open(OUTPUT_NON_3D, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        # Write existing
        for row in existing_non_3d:
            writer.writerow(row)
        # Write new
        for row, result in results_non_3d:
            writer.writerow([
                row[0], row[1], row[2], row[3],
                result.get("model_author", ""),
                result.get("description", ""),
                result.get("nodes_list", ""),
                result.get("category", ""),
                result.get("confidence", "")
            ])

    print(f"\nDone! Found {len(results_3d)} 3D-relevant nodes.")
    print(f"Review {OUTPUT_3D}, then run generate_index.py — it merges every ai_3d_nodes*.csv automatically.")

if __name__ == "__main__":
    main()
