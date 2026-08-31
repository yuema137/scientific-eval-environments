#!/usr/bin/env python3
"""Sort every axis-page Related Works index by First appeared, newest first."""

import argparse
import os
import sys


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "update_agent"))

from related_works import sort_all  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = sort_all(ROOT, check=args.check)
    if changed:
        print("\n".join(changed))
        if args.check:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
