#!/usr/bin/env python3
"""Build the self-contained SciEval static site from Markdown ground truth."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

try:
    from scripts.export_explorer_data import ROOT, build_dataset, write_dataset, write_documents
except ModuleNotFoundError:  # Direct execution: python3 scripts/build_explorer_site.py
    from export_explorer_data import ROOT, build_dataset, write_dataset, write_documents


STATIC_FILES = ("index.html", "app.js", "styles.css")


def source_commit_date(source_sha: str) -> str:
    """Committer date (ISO 8601) of ``source_sha``, or "unknown".

    The snapshot date is taken from the source commit rather than the wall
    clock, so rebuilding the same commit yields byte-identical output.
    """
    if not source_sha or source_sha == "unknown":
        return "unknown"
    try:
        result = subprocess.run(
            ["git", "show", "-s", "--format=%cI", source_sha],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def build_site(output_dir: Path, source_sha: str = "unknown", source_date: str | None = None) -> None:
    source_dir = ROOT / "site"
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in STATIC_FILES:
        shutil.copy2(source_dir / name, output_dir / name)

    assets_output = output_dir / "assets"
    if assets_output.exists():
        shutil.rmtree(assets_output)
    shutil.copytree(source_dir / "assets", assets_output)

    data = build_dataset(ROOT)
    write_dataset(data, output_dir / "data" / "index.json")
    write_documents(output_dir, ROOT)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")
    (output_dir / "manifest.json").write_text(
        json.dumps(
            {
                "source_repository": "yuema137/scientific-eval-environments",
                "source_sha": source_sha,
                "source_committed_at": source_date or source_commit_date(source_sha),
                "latest_first_appeared": data["stats"]["first_appeared_latest"],
                "latest_monthly_report": data["monthly_reports"][0]["month"] if data["monthly_reports"] else None,
                "ground_truth": "repository Markdown",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--source-sha", default="unknown")
    parser.add_argument(
        "--source-date",
        default=None,
        help="Snapshot date to record; defaults to the committer date of --source-sha.",
    )
    args = parser.parse_args()
    build_site(args.output.resolve(), args.source_sha, args.source_date)


if __name__ == "__main__":
    main()
