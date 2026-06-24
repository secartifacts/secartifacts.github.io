#!/usr/bin/env python3
"""Generate _data/artifinder_artifacts.yaml and _data/artifinder_links.yaml.

artifinder_artifacts.yaml: non-evaluated papers with discovered artifacts,
  cross-checked against _conferences to exclude formally evaluated ones.

artifinder_links.yaml: for papers that went through evaluation, cases where
  ArtiFinder found a different artifact URL than the one in results.md.
"""

import os
import re
import yaml

DATA_DIR = "_artifinder/data"
CONFERENCES_DIR = "_conferences"
ARTIFACTS_OUT = "_data/artifinder_artifacts.yaml"
LINKS_OUT = "_data/artifinder_links.yaml"

# Maps _conferences directory prefix → _artifinder/data directory name
CONF_PREFIX_MAP = {
    "ndss": "ndss",
    "usenixsec": "usenix",
    "sp": "sp",
}


def normalize_title(title):
    title = re.sub(r"\s*\[artifacts?\]", "", title, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", title).strip().rstrip(".").lower()


def normalize_url(url):
    if not url:
        return ""
    url = url.strip().rstrip("/")
    url = re.sub(r"^http://", "https://", url)
    return url


def read_front_matter(path):
    with open(path) as f:
        content = f.read().replace("\t", "  ")
    parts = content.split("---")
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def get_eval_url(artifact):
    url = artifact.get("artifact_url")
    if isinstance(url, list):
        url = url[0] if url else None
    return normalize_url(url or "")


def load_conference_data():
    """Return {dir_name: {norm_title: (raw_title, eval_url)}} for all matching conf-years."""
    result = {}
    for entry in os.listdir(CONFERENCES_DIR):
        m = re.match(r"^([a-z]+)(\d{4})$", entry)
        if not m or m.group(1) not in CONF_PREFIX_MAP:
            continue
        results_path = os.path.join(CONFERENCES_DIR, entry, "results.md")
        if not os.path.exists(results_path):
            continue
        fm = read_front_matter(results_path)
        by_norm = {}
        for a in fm.get("artifacts", []):
            by_norm[normalize_title(a["title"])] = (a["title"], get_eval_url(a))
        if by_norm:
            result[entry] = (CONF_PREFIX_MAP[m.group(1)], m.group(2), by_norm)
    return result


conf_data = load_conference_data()

# Build evaluated-title lookup for artifact filtering: {(conf, year): set_of_norm_titles}
evaluated_lookup = {
    (conf, year): set(by_norm.keys())
    for _, (conf, year, by_norm) in conf_data.items()
}
print(f"Loaded evaluated titles for {len(evaluated_lookup)} conference-years")

# ── Generate artifinder_artifacts.yaml ────────────────────────────────────────

conferences = sorted(os.listdir(DATA_DIR))
artifacts_result = {}
total_kept = 0
total_excluded = 0

for conf in conferences:
    conf_dir = os.path.join(DATA_DIR, conf)
    if not os.path.isdir(conf_dir):
        continue

    years = sorted(
        (f[:-5] for f in os.listdir(conf_dir) if f.endswith(".yaml")),
        reverse=True,
    )

    conf_data_out = {}
    for year in years:
        path = os.path.join(conf_dir, f"{year}.yaml")
        with open(path) as fh:
            papers = yaml.safe_load(fh) or []

        evaluated = evaluated_lookup.get((conf, year), set())

        artifacts = []
        for p in papers:
            if not p.get("discovered_artifact"):
                continue
            if normalize_title(p["title"]) in evaluated:
                total_excluded += 1
                continue
            artifacts.append({
                "title": p["title"],
                "page_link": p.get("page_link"),
                "artifact": p["discovered_artifact"],
            })

        total_kept += len(artifacts)
        if artifacts:
            conf_data_out[year] = artifacts

    if conf_data_out:
        artifacts_result[conf] = conf_data_out

os.makedirs(os.path.dirname(ARTIFACTS_OUT), exist_ok=True)
with open(ARTIFACTS_OUT, "w") as fh:
    yaml.dump(artifacts_result, fh, allow_unicode=True, sort_keys=False)

print(f"artifinder_artifacts.yaml — excluded: {total_excluded}, kept: {total_kept}")

# ── Generate artifinder_links.yaml ────────────────────────────────────────────
# For evaluated papers where ArtiFinder found a different artifact URL.
# Keyed by _conferences directory name → raw results.md title → AF url.

links_result = {}
total_links = 0

for dir_name, (conf, year, by_norm) in sorted(conf_data.items()):
    af_path = os.path.join(DATA_DIR, conf, f"{year}.yaml")
    if not os.path.exists(af_path):
        continue

    with open(af_path) as fh:
        af_papers = yaml.safe_load(fh) or []

    af_by_norm = {
        normalize_title(p["title"]): normalize_url(p.get("discovered_artifact") or "")
        for p in af_papers
    }

    dir_links = {}
    for norm_title, (raw_title, eval_url) in by_norm.items():
        af_url = af_by_norm.get(norm_title, "")
        if af_url and af_url != eval_url:
            dir_links[raw_title] = af_url
            total_links += 1

    if dir_links:
        links_result[dir_name] = dir_links

with open(LINKS_OUT, "w") as fh:
    yaml.dump(links_result, fh, allow_unicode=True, sort_keys=False)

print(f"artifinder_links.yaml — {total_links} alternative links across {len(links_result)} conf-years")
