#!/usr/bin/env python3
"""Scaffold a solution file from templates/solution.cpp.

Usage:
  python3 scripts/new.py <leetcode-number> <slug> <folder>
Example:
  python3 scripts/new.py 1 two-sum arrays-hashing
  -> solutions/arrays-hashing/0001-two-sum.cpp
"""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    num, slug, folder = sys.argv[1], sys.argv[2], sys.argv[3]
    target_dir = ROOT / "solutions" / folder
    if not target_dir.exists():
        print(f"Folder solutions/{folder} does not exist. Options:")
        print("  " + ", ".join(sorted(p.name for p in (ROOT / 'solutions').iterdir() if p.is_dir())))
        sys.exit(1)
    target = target_dir / f"{int(num):04d}-{slug}.cpp"
    if target.exists():
        print(f"Already exists: {target}")
        sys.exit(1)
    tpl = (ROOT / "templates" / "solution.cpp").read_text(encoding="utf-8")
    tpl = (tpl.replace("{{NUM}}", num)
              .replace("{{SLUG}}", slug)
              .replace("{{DATE}}", date.today().isoformat()))
    target.write_text(tpl, encoding="utf-8")
    print(f"Created {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
