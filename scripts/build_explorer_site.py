#!/usr/bin/env python3
"""Build the self-contained SciEval static site from Markdown ground truth."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

try:
    from scripts.export_explorer_data import ROOT, build_dataset, write_dataset, write_documents
except ModuleNotFoundError:  # Direct execution: python3 scripts/build_explorer_site.py
    from export_explorer_data import ROOT, build_dataset, write_dataset, write_documents


STATIC_FILES = ("index.html", "app.js", "styles.css")


def build_site(output_dir: Path, source_sha: str = "unknown") -> None:
    source_dir = ROOT / "site"
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in STATIC_FILES:
        shutil.copy2(source_dir / name, output_dir / name)

    assets_output = output_dir / "assets"
    if assets_output.exists():
        shutil.rmtree(assets_output)
    shutil.copytree(source_dir / "assets", assets_output)

    write_dataset(build_dataset(ROOT), output_dir / "data" / "index.json")
    write_documents(output_dir, ROOT)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")
    (output_dir / "manifest.json").write_text(
        json.dumps(
            {
                "source_repository": "yuema137/scientific-eval-environments",
                "source_sha": source_sha,
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
    args = parser.parse_args()
    build_site(args.output.resolve(), args.source_sha)


if __name__ == "__main__":
    main()
