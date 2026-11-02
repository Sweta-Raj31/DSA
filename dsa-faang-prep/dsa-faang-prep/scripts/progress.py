#!/usr/bin/env python3
"""Reads PROBLEMS.md, counts ticked checkboxes per section, and rewrites the
dashboard in README.md between the PROGRESS markers.

Usage:  python3 scripts/progress.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "PROBLEMS.md"
README = ROOT / "README.md"
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"


def bar(done, total, width=20):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def main():
    sections = []  # [title, done, total, core_done, core_total]
    for line in PROBLEMS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## \d+\. (.+)$", line)
        if m:
            sections.append([m.group(1), 0, 0, 0, 0])
            continue
        m = re.match(r"^- \[( |x|X)\] (⭐ )?\[", line)
        if m and sections:
            done = m.group(1).lower() == "x"
            core = m.group(2) is not None
            s = sections[-1]
            s[2] += 1
            s[1] += done
            if core:
                s[4] += 1
                s[3] += done

    td = sum(s[1] for s in sections)
    tt = sum(s[2] for s in sections)
    cd = sum(s[3] for s in sections)
    ct = sum(s[4] for s in sections)

    rows = [
        f"**Overall: {td}/{tt} solved** ({100*td//max(tt,1)}%)  |  **Core: {cd}/{ct}** ({100*cd//max(ct,1)}%)",
        "",
        f"`{bar(cd, ct)}` core progress",
        "",
        "| Pattern | Solved | Core | Progress |",
        "|---|---|---|---|",
    ]
    for t, d, tot, cdn, ctt in sections:
        rows.append(f"| {t} | {d}/{tot} | {cdn}/{ctt} | `{bar(d, tot, 10)}` |")
    block = "\n".join(rows)

    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new = f"{START}\n{block}\n{END}"
    if pattern.search(text):
        text = pattern.sub(lambda _: new, text)
    else:
        text += "\n" + new + "\n"
    README.write_text(text, encoding="utf-8")
    print(f"Updated README: {td}/{tt} solved, core {cd}/{ct}")


if __name__ == "__main__":
    main()
