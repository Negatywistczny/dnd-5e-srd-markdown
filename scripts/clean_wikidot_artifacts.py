#!/usr/bin/env python3
"""Remove useless Wikidot UI artifacts from scraped markdown."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# Wikidot tab labels (spell level, rarity, etc.) — not real navigation in static md.
_TAB_LABEL = (
    r"Sztuczka|Cantrip|\?\?\?|"
    r"\d+(?:st|nd|rd|th)\s+Level|\d+\.\s*krąg|"
    r"Pospolity|Niezwykły|Rzadki|Bardzo\s+rzadki|Legendarny|Artefakt|"
    r"Common|Uncommon|Rare|Very\s+Rare|Legendary|Artifact"
)
TAB_LINE_RE = re.compile(
    rf"^- \[\*(?:{_TAB_LABEL})\*\]\(javascript:;\)\s*$",
    re.IGNORECASE,
)

OZONE_BLOCK_RE = re.compile(
    r"//<!\[CDATA\[\s*\nOZONE\.dom\.onDomReady\(function\(\)\{.*?\n//\]\]>\s*",
    re.DOTALL,
)

FOLD_UNFOLD_RE = re.compile(r"\[Fold\]\(javascript:;\)\[Unfold\]\(javascript:;\)")

# Whole-line Wikidot TOC blobs (#toc0 anchors don't exist in repo markdown).
WIKIDOT_TOC_LINE_RE = re.compile(
    r"^\[Fold\]\(javascript:;\)\[Unfold\]\(javascript:;\).*#toc\d+.*$",
    re.MULTILINE,
)

JS_LINK_RE = re.compile(r"\[([^\]]+)\]\(javascript:;\)")

# Empty tab links left after javascript:; cleanup (e.g. "### Arcane Study []()").
EMPTY_LINK_RE = re.compile(r" *\[\]\(\)")


def clean_wikidot_artifacts(text: str) -> str:
    text = OZONE_BLOCK_RE.sub("", text)
    text = WIKIDOT_TOC_LINE_RE.sub("", text)
    text = FOLD_UNFOLD_RE.sub("", text)
    text = EMPTY_LINK_RE.sub("", text)

    lines: list[str] = []
    for line in text.splitlines():
        if TAB_LINE_RE.match(line):
            continue
        if JS_LINK_RE.search(line):
            line = JS_LINK_RE.sub(r"\1", line)
            # List item that was only a fake link: "- *Name*" -> "- Name"
            m = re.match(r"^(- )\*(.+)\*$", line)
            if m:
                line = f"{m.group(1)}{m.group(2)}"
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def clean_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    cleaned = clean_wikidot_artifacts(original)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


def clean_tree(root: Path) -> int:
    changed = 0
    if not root.is_dir():
        return 0
    for path in sorted(root.rglob("*.md")):
        if clean_file(path):
            changed += 1
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        nargs="?",
        choices=["all", "en", "pl"],
        default="all",
    )
    args = parser.parse_args()

    roots = {
        "en": REPO / "dnd2024-wikidot",
        "pl": REPO / "dnd2024-wikidot-pl",
    }
    selected = list(roots.values()) if args.target == "all" else [roots[args.target]]
    total = 0
    for root in selected:
        n = clean_tree(root)
        total += n
        print(f"Cleaned {n} files under {root}")
    print(f"Total: {total} files")


if __name__ == "__main__":
    main()
