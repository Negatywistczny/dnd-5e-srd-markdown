#!/usr/bin/env python3
"""Scrape all D&D 2024 subclass pages from dnd2024.wikidot.com."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from html import unescape
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

BASE_URL = "http://dnd2024.wikidot.com"
CLASSES = [
    "artificer",
    "barbarian",
    "bard",
    "cleric",
    "druid",
    "fighter",
    "monk",
    "paladin",
    "ranger",
    "rogue",
    "sorcerer",
    "warlock",
    "wizard",
]
SKIP_SLUGS = {
    "main",
    "spell-list",
    "metamagic",
    "eldritch-invocation",
}
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "dnd2024-wikidot"
REQUEST_DELAY = 0.5


def fetch_html(path: str, retries: int = 3) -> str:
    url = f"{BASE_URL}/{path}"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "dnd2024-subclass-scraper/1.0"},
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(1 + attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def discover_subclass_slugs(class_name: str) -> list[str]:
    html = fetch_html(f"{class_name}:main")
    pattern = re.compile(rf'href="/{re.escape(class_name)}:([^"]+)"')
    slugs: list[str] = []
    for slug in pattern.findall(html):
        if slug in SKIP_SLUGS:
            continue
        if slug not in slugs:
            slugs.append(slug)
    return slugs


def slug_to_title(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.replace("-", " ").split())


def inline_to_markdown(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        return unescape(str(node))

    name = node.name or ""
    children = "".join(inline_to_markdown(child) for child in node.children)

    if name in {"strong", "b"}:
        return f"**{children.strip()}**"
    if name in {"em", "i"}:
        return f"*{children.strip()}*"
    if name == "br":
        return "\n"
    if name == "a":
        href = node.get("href", "")
        text = children.strip() or href
        if href.startswith("/"):
            href = f"{BASE_URL}{href}"
        return f"[{text}]({href})"
    if name == "code":
        return f"`{children}`"
    if name == "span":
        return children
    if name == "sup":
        return f"^{children}^"
    if name == "sub":
        return f"~{children}~"

    return children


def block_to_markdown(node: Tag | NavigableString, depth: int = 0) -> str:
    if isinstance(node, NavigableString):
        text = unescape(str(node))
        return text if text.strip() else ""

    name = node.name or ""
    if name == "p":
        return inline_to_markdown(node).strip() + "\n\n"
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        title = inline_to_markdown(node).strip()
        return f"{'#' * level} {title}\n\n"
    if name == "ul":
        lines = []
        for child in node.find_all("li", recursive=False):
            item = inline_to_markdown(child).strip()
            lines.append(f"- {item}")
        return "\n".join(lines) + "\n\n"
    if name == "ol":
        lines = []
        for index, child in enumerate(node.find_all("li", recursive=False), start=1):
            item = inline_to_markdown(child).strip()
            lines.append(f"{index}. {item}")
        return "\n".join(lines) + "\n\n"
    if name == "table":
        return table_to_markdown(node)
    if name == "blockquote":
        body = "".join(block_to_markdown(child, depth + 1) for child in node.children).strip()
        return "\n".join(f"> {line}" for line in body.splitlines()) + "\n\n"
    if name == "div":
        return "".join(block_to_markdown(child, depth + 1) for child in node.children)

    return inline_to_markdown(node)


def table_to_markdown(table: Tag) -> str:
    rows = table.find_all("tr")
    if not rows:
        return ""

    parsed_rows: list[list[str]] = []
    for row in rows:
        cells = row.find_all(["th", "td"])
        parsed_rows.append([inline_to_markdown(cell).strip().replace("\n", " ") for cell in cells])

    if not parsed_rows:
        return ""

    header = parsed_rows[0]
    body = parsed_rows[1:] if len(parsed_rows) > 1 else []
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in body:
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(padded[: len(header)]) + " |")
    return "\n".join(lines) + "\n\n"


def extract_page_content(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True).replace(" - D&D 5e (2024)", "") if title_tag else ""

    content = soup.find("div", id="page-content")
    if content is None:
        raise ValueError("Missing #page-content")

    markdown = "".join(block_to_markdown(child) for child in content.children).strip()
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return title, markdown


def scrape_subclass(class_name: str, slug: str) -> dict:
    path = f"{class_name}:{slug}"
    html = fetch_html(path)
    title, markdown = extract_page_content(html)
    source_match = re.search(r"^Source:\s*(.+)$", markdown, flags=re.MULTILINE)
    source = source_match.group(1).strip() if source_match else None
    return {
        "class": class_name,
        "slug": slug,
        "title": title or slug_to_title(slug),
        "url": f"{BASE_URL}/{path}",
        "source": source,
        "markdown": markdown,
    }


def write_outputs(subclasses: list[dict]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    subclasses_dir = OUTPUT_DIR / "subclasses"
    subclasses_dir.mkdir(parents=True, exist_ok=True)

    index: dict[str, list[dict]] = {}
    for item in subclasses:
        class_name = item["class"]
        index.setdefault(class_name, []).append(
            {
                "slug": item["slug"],
                "title": item["title"],
                "url": item["url"],
                "source": item["source"],
            }
        )

        file_name = f"{class_name}-{item['slug']}.md"
        body = (
            f"# {item['title']}\n\n"
            f"**Class:** {class_name}\n"
            f"**Source URL:** {item['url']}\n"
        )
        if item["source"]:
            body += f"**Source:** {item['source']}\n"
        body += f"\n---\n\n{item['markdown']}\n"
        (subclasses_dir / file_name).write_text(body, encoding="utf-8")

    combined_lines = ["# D&D 2024 Subclasses (dnd2024.wikidot.com)\n"]
    for class_name in CLASSES:
        entries = index.get(class_name, [])
        if not entries:
            continue
        combined_lines.append(f"\n## {class_name.capitalize()}\n")
        for entry in entries:
            combined_lines.append(f"\n### {entry['title']}\n")
            combined_lines.append(f"URL: {entry['url']}\n")
            subclass = next(s for s in subclasses if s["slug"] == entry["slug"] and s["class"] == class_name)
            combined_lines.append(subclass["markdown"])
            combined_lines.append("\n---\n")

    (OUTPUT_DIR / "subclasses.md").write_text("".join(combined_lines), encoding="utf-8")
    (OUTPUT_DIR / "subclasses.json").write_text(
        json.dumps({"classes": index, "subclasses": subclasses}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    subclasses: list[dict] = []
    failures: list[str] = []

    for class_name in CLASSES:
        print(f"Discovering {class_name} subclasses...")
        slugs = discover_subclass_slugs(class_name)
        time.sleep(REQUEST_DELAY)
        print(f"  found {len(slugs)}: {', '.join(slugs)}")

        for slug in slugs:
            path = f"{class_name}:{slug}"
            print(f"  scraping {path}...")
            try:
                subclasses.append(scrape_subclass(class_name, slug))
            except Exception as exc:  # noqa: BLE001 - collect and continue
                failures.append(f"{path}: {exc}")
                print(f"    ERROR: {exc}")
            time.sleep(REQUEST_DELAY)

    write_outputs(subclasses)
    print(f"\nSaved {len(subclasses)} subclasses to {OUTPUT_DIR}")
    if failures:
        print(f"Failures ({len(failures)}):")
        for failure in failures:
            print(f"  - {failure}")


if __name__ == "__main__":
    main()
