"""Shared utilities for scraping dnd2024.wikidot.com."""

from __future__ import annotations

import re
import time
import urllib.error
import urllib.request
from html import unescape
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

from clean_wikidot_artifacts import clean_wikidot_artifacts

BASE_URL = "http://dnd2024.wikidot.com"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent.parent / "dnd2024-wikidot"
REQUEST_DELAY = 0.5
USER_AGENT = "dnd2024-wiki-scraper/1.0"


def fetch_html(path: str, retries: int = 3) -> str:
    url = f"{BASE_URL}/{path}" if not path.startswith("http") else path
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(1 + attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def page_url(path: str) -> str:
    return f"{BASE_URL}/{path}"


def slug_to_title(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.replace("-", " ").split())


def discover_slugs(prefix: str, index_slug: str = "all", skip: set[str] | None = None) -> list[str]:
    skip = skip or set()
    html = fetch_html(f"{prefix}:{index_slug}")
    pattern = re.compile(rf'href="/{re.escape(prefix)}:([^"#]+)"')
    slugs: list[str] = []
    for slug in pattern.findall(html):
        if slug in skip:
            continue
        if slug not in slugs:
            slugs.append(slug)
    return slugs


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
        lines = [f"- {inline_to_markdown(child).strip()}" for child in node.find_all("li", recursive=False)]
        return "\n".join(lines) + "\n\n"
    if name == "ol":
        lines = [
            f"{index}. {inline_to_markdown(child).strip()}"
            for index, child in enumerate(node.find_all("li", recursive=False), start=1)
        ]
        return "\n".join(lines) + "\n\n"
    if name == "table":
        return table_to_markdown(node)
    if name == "blockquote":
        body = "".join(block_to_markdown(child, depth + 1) for child in node.children).strip()
        return "\n".join(f"> {line}" for line in body.splitlines()) + "\n\n"
    if name == "div":
        return "".join(block_to_markdown(child, depth + 1) for child in node.children)
    if name == "hr":
        return "---\n\n"

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

    if content.find(id="404-message"):
        raise ValueError("Page not found (404)")

    markdown = "".join(block_to_markdown(child) for child in content.children).strip()
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return title, clean_wikidot_artifacts(markdown).strip()


def extract_source(markdown: str) -> str | None:
    source_match = re.search(r"^Source:\s*(.+)$", markdown, flags=re.MULTILINE)
    return source_match.group(1).strip() if source_match else None


def scrape_page(path: str, section: str, slug: str, extra: dict | None = None) -> dict:
    html = fetch_html(path)
    title, markdown = extract_page_content(html)
    item = {
        "section": section,
        "slug": slug,
        "path": path,
        "title": title or slug_to_title(slug),
        "url": page_url(path),
        "source": extract_source(markdown),
        "markdown": markdown,
    }
    if extra:
        item.update(extra)
    return item


def write_page_markdown(output_dir: Path, section: str, slug: str, item: dict, metadata_lines: list[str]) -> Path:
    section_dir = output_dir / section
    section_dir.mkdir(parents=True, exist_ok=True)
    file_path = section_dir / f"{slug}.md"
    body = f"# {item['title']}\n\n" + "\n".join(metadata_lines) + f"\n\n---\n\n{item['markdown']}\n"
    file_path.write_text(body, encoding="utf-8")
    return file_path


def throttle() -> None:
    time.sleep(REQUEST_DELAY)
