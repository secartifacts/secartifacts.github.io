#!/usr/bin/env python3
"""
Generate _data/artifinder_nonevaluated.yaml, _data/artifinder_authorlinks.yaml,
and _data/artifinder_names.yaml.

artifinder_nonevaluated.yaml: non-evaluated papers with discovered artifacts,
  cross-checked against _conferences to exclude formally evaluated ones.

artifinder_authorlinks.yaml: for papers that went through evaluation, collect where
  ArtiFinder found a different artifact URL in the paper than the one in results.md.

artifinder_names.yaml: display names for the conference identifiers used above.
"""

import os
import re
from typing import Any

import yaml

ARTIFINDER_DATA_DIR = "_artifinder/data"
EVAL_RESULTS_DIR = "_conferences"
ARTIFACTS_OUT = "_data/artifinder_nonevaluated.yaml"
LINKS_OUT = "_data/artifinder_authorlinks.yaml"
NAMES_OUT = "_data/artifinder_names.yaml"

# _conferences directory prefix to _artifinder/data directory name
CONF_PREFIX_MAP = {
    "acsac": "acsac",
    "ndss": "ndss",
    "usenixsec": "usenix",
    "sp": "sp",
}

# _artifinder/data directory name to display name
CONF_DISPLAY_NAMES = {
    "acsac": "ACSAC",
    "ccs": "ACM CCS",
    "ndss": "NDSS",
    "sp": "IEEE S&P",
    "usenix": "USENIX Security",
}


def compare_titles(title_a: str, title_b: str) -> bool:
    def normalize(title: str) -> str:
        title = re.sub(r"\s*\[artifacts?\]", "", title, flags=re.IGNORECASE)
        return re.sub(r"\s+", " ", title).strip().rstrip(".").lower()

    return normalize(title_a) == normalize(title_b)


def normalize_url(url: str) -> str:
    """
    Strips whitespace and trailing slash. Adds an http:// scheme if none is
    present, but never rewrites an existing scheme.
    For comparing two URLs regardless of scheme, use compare_urls.
    """
    if not url:
        return ""
    url = url.strip().rstrip("/")
    if not re.match(r"^https?://", url, re.IGNORECASE):
        url = f"http://{url}"
    return url


def compare_urls(url_a: str, url_b: str) -> bool:
    def normalize(url: str) -> str:
        url = url.strip().rstrip("/")
        return re.sub(r"^https?://", "", url, flags=re.IGNORECASE).lower()

    return normalize(url_a) == normalize(url_b)


def read_front_matter(path: str) -> dict[str, Any]:
    with open(path) as f:
        content = f.read().replace("\t", "  ")
    parts = content.split("---")
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def get_eval_url(artifact: dict[str, Any]) -> str:
    url = artifact.get("artifact_url")
    if isinstance(url, list):
        url = url[0] if url else None
    return normalize_url(str(url)) if url else ""

def conf_id_for_prefix(prefix: str) -> str | None:
    return CONF_PREFIX_MAP.get(prefix)


# {(conf, year): (eval_dir_name, [(title, eval_url), ...])}
EvaluatedPapers = dict[tuple[str, str], tuple[str, list[tuple[str, str]]]]


def load_evaluated_papers() -> EvaluatedPapers:
    """
    Read titles and artifact URLs from _conferences/*/results.md, i.e. papers
    that went through formal artifact evaluation.
    """
    result: EvaluatedPapers = {}
    for entry in os.listdir(EVAL_RESULTS_DIR):
        m = re.match(r"^([a-z]+)(\d{4})$", entry)
        if not m:
            continue
        conf_id = conf_id_for_prefix(m.group(1))
        if conf_id is None:
            continue
        results_path = os.path.join(EVAL_RESULTS_DIR, entry, "results.md")
        if not os.path.exists(results_path):
            continue
        fm = read_front_matter(results_path)
        titles = [(a["title"], get_eval_url(a)) for a in fm.get("artifacts", [])]
        if titles:
            result[(conf_id, m.group(2))] = (entry, titles)
    return result


def generate_artifact_data(evaluated_papers: EvaluatedPapers) -> None:
    """
    Walk each conference-year's ArtiFinder papers once, splitting them into:
    - non-evaluated papers with a discovered artifact (artifinder_nonevaluated.yaml)
    - evaluated papers where ArtiFinder found a different artifact URL than the
      one submitted for evaluation, keyed by _conferences directory name
      (artifinder_authorlinks.yaml)
    """
    conferences = sorted(os.listdir(ARTIFINDER_DATA_DIR))
    artifacts_result = {}
    links_result = {}
    total_kept = 0
    total_excluded = 0
    total_links = 0

    for conf in conferences:
        conf_dir = os.path.join(ARTIFINDER_DATA_DIR, conf)
        if not os.path.isdir(conf_dir):
            continue

        years = sorted(
            (f[:-5] for f in os.listdir(conf_dir) if f.endswith(".yaml")),
            reverse=True,
        )

        year_to_artifacts = {}
        for year in years:
            path = os.path.join(conf_dir, f"{year}.yaml")
            with open(path) as fh:
                papers = yaml.safe_load(fh) or []

            # Evaluated titles for this conference-year, empty if it never went
            # through formal evaluation (or has no matching _conferences entry).
            dir_name, evaluated = evaluated_papers.get((conf, year), (None, []))

            noneval_artifacts = []
            mismatched_urls = {}
            for p in papers:
                # Does this ArtiFinder paper correspond to a formally evaluated one?
                match = next(
                    (t for t in evaluated if compare_titles(p["title"], t[0])), None
                )
                has_artifact = bool(p.get("discovered_artifact"))

                if match is not None:
                    # Evaluated paper: only relevant if ArtiFinder found a URL that
                    # differs from the one submitted for evaluation.
                    if has_artifact:
                        raw_title, eval_url = match
                        af_url = normalize_url(p["discovered_artifact"])
                        if af_url and not compare_urls(af_url, eval_url):
                            mismatched_urls[raw_title] = {
                                "url": af_url,
                                "validated": bool(p.get("validated")),
                            }
                            total_links += 1
                        total_excluded += 1
                    # Skip the rest for evaluated papers.
                    continue

                if not has_artifact:
                    continue

                # Save non-evaluated papers with a discovered artifact.
                noneval_artifacts.append({
                    "title": p["title"],
                    "page_link": p.get("page_link"),
                    "artifact": normalize_url(p["discovered_artifact"]),
                    "validated": bool(p.get("validated")),
                })

            total_kept += len(noneval_artifacts)
            if noneval_artifacts:
                year_to_artifacts[year] = noneval_artifacts
            if dir_name and mismatched_urls:
                links_result[dir_name] = mismatched_urls

        if year_to_artifacts:
            artifacts_result[conf] = year_to_artifacts

    os.makedirs(os.path.dirname(ARTIFACTS_OUT), exist_ok=True)
    with open(ARTIFACTS_OUT, "w") as fh:
        yaml.dump(artifacts_result, fh, allow_unicode=True, sort_keys=False)
    print(f"artifinder_nonevaluated.yaml: excluded {total_excluded}, kept {total_kept}")

    with open(LINKS_OUT, "w") as fh:
        yaml.dump(links_result, fh, allow_unicode=True, sort_keys=False)
    print(f"artifinder_authorlinks.yaml: {total_links} alternative links across {len(links_result)} conf-years")


def generate_names() -> None:
    with open(NAMES_OUT, "w") as fh:
        yaml.dump(CONF_DISPLAY_NAMES, fh, allow_unicode=True, sort_keys=False)

    print(f"artifinder_names.yaml: {len(CONF_DISPLAY_NAMES)} conference names")


if __name__ == "__main__":
    evaluated_papers = load_evaluated_papers()
    print(f"Loaded evaluated titles for {len(evaluated_papers)} conference-years")

    generate_artifact_data(evaluated_papers)
    generate_names()
