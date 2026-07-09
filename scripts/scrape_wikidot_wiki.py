#!/usr/bin/env python3
"""Scrape all D&D 2024 wiki content from dnd2024.wikidot.com."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from wikidot_common import (
    DEFAULT_OUTPUT_DIR,
    discover_slugs,
    scrape_page,
    throttle,
    write_page_markdown,
)

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

CLASS_SPELL_LISTS = [
    "artificer",
    "bard",
    "cleric",
    "druid",
    "paladin",
    "ranger",
    "sorcerer",
    "warlock",
    "wizard",
]

SUBCLASS_SKIP = {"main", "spell-list", "metamagic", "eldritch-invocation"}

BACKGROUND_SKIP = {"all"}
SPECIES_SKIP = {"all"}
FEAT_SKIP = {"all"}
SPELL_SKIP: set[str] = set()
MAGIC_ITEM_SKIP = {"all", "type", "sources"}
EQUIPMENT_SKIP = {"all"}
UA_SKIP = {"all"}

MAGIC_ITEM_CATEGORIES = [
    "crafting",
    "consumable",
    "armor",
    "potion",
    "ring",
    "rod",
    "staff",
    "scroll",
    "wand",
    "weapon",
    "wondrous-item",
]

EQUIPMENT_CATEGORIES = [
    "crafting",
    "adventuring-gear",
    "armor",
    "weapon",
    "mounts-and-vehicles",
    "trinket",
    "currency",
    "poison",
    "tool",
]

MISC_PAGES = [
    "bastions",
    "circle-magic",
    "class:multiclassing",
]

CLASS_OPTION_PAGES = [
    "sorcerer:metamagic",
    "warlock:eldritch-invocation",
]

SECTION_NAMES = [
    "backgrounds",
    "species",
    "classes",
    "subclasses",
    "class-options",
    "spell-lists",
    "feats",
    "equipment",
    "magic-items",
    "magic-item-categories",
    "spells",
    "misc",
    "ua",
]


def scrape_indexed(section: str, prefix: str, slugs: list[str], metadata_fn) -> tuple[list[dict], list[str]]:
    pages: list[dict] = []
    failures: list[str] = []
    for slug in slugs:
        path = f"{prefix}:{slug}"
        print(f"  scraping {path}...")
        try:
            item = scrape_page(path, section, slug)
            pages.append(item)
            write_page_markdown(
                DEFAULT_OUTPUT_DIR,
                section,
                slug,
                item,
                metadata_fn(item),
            )
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{path}: {exc}")
            print(f"    ERROR: {exc}")
        throttle()
    return pages, failures


def scrape_paths(section: str, paths: list[str], metadata_fn) -> tuple[list[dict], list[str]]:
    pages: list[dict] = []
    failures: list[str] = []
    for path in paths:
        slug = path.replace(":", "-")
        print(f"  scraping {path}...")
        try:
            item = scrape_page(path, section, slug)
            pages.append(item)
            write_page_markdown(
                DEFAULT_OUTPUT_DIR,
                section,
                slug,
                item,
                metadata_fn(item),
            )
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{path}: {exc}")
            print(f"    ERROR: {exc}")
        throttle()
    return pages, failures


def scrape_section(section: str) -> tuple[list[dict], list[str]]:
    print(f"\n=== {section} ===")
    pages: list[dict] = []
    failures: list[str] = []

    if section == "backgrounds":
        slugs = discover_slugs("background", skip=BACKGROUND_SKIP)
        throttle()
        print(f"  found {len(slugs)} backgrounds")
        section_pages, section_failures = scrape_indexed(
            section,
            "background",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "species":
        slugs = discover_slugs("species", skip=SPECIES_SKIP)
        throttle()
        print(f"  found {len(slugs)} species")
        section_pages, section_failures = scrape_indexed(
            section,
            "species",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "classes":
        print(f"  found {len(CLASSES)} classes")
        for class_name in CLASSES:
            path = f"{class_name}:main"
            slug = class_name
            print(f"  scraping {path}...")
            try:
                item = scrape_page(path, section, slug, {"class": class_name})
                pages.append(item)
                write_page_markdown(
                    DEFAULT_OUTPUT_DIR,
                    section,
                    slug,
                    item,
                    [f"**Class:** {class_name}", f"**Source URL:** {item['url']}"],
                )
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{path}: {exc}")
                print(f"    ERROR: {exc}")
            throttle()

    elif section == "subclasses":
        for class_name in CLASSES:
            slugs = discover_slugs(class_name, index_slug="main", skip=SUBCLASS_SKIP)
            throttle()
            print(f"  {class_name}: found {len(slugs)} subclasses")
            for slug in slugs:
                path = f"{class_name}:{slug}"
                print(f"  scraping {path}...")
                try:
                    item = scrape_page(path, section, f"{class_name}-{slug}", {"class": class_name})
                    pages.append(item)
                    metadata = [
                        f"**Class:** {class_name}",
                        f"**Source URL:** {item['url']}",
                    ]
                    if item["source"]:
                        metadata.append(f"**Source:** {item['source']}")
                    write_page_markdown(DEFAULT_OUTPUT_DIR, section, f"{class_name}-{slug}", item, metadata)
                except Exception as exc:  # noqa: BLE001
                    failures.append(f"{path}: {exc}")
                    print(f"    ERROR: {exc}")
                throttle()

    elif section == "class-options":
        print(f"  found {len(CLASS_OPTION_PAGES)} class option pages")
        section_pages, section_failures = scrape_paths(
            section,
            CLASS_OPTION_PAGES,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "spell-lists":
        paths = [f"{class_name}:spell-list" for class_name in CLASS_SPELL_LISTS]
        print(f"  found {len(paths)} spell lists")
        for class_name in CLASS_SPELL_LISTS:
            path = f"{class_name}:spell-list"
            slug = class_name
            print(f"  scraping {path}...")
            try:
                item = scrape_page(path, section, slug, {"class": class_name})
                pages.append(item)
                write_page_markdown(
                    DEFAULT_OUTPUT_DIR,
                    section,
                    slug,
                    item,
                    [f"**Class:** {class_name}", f"**Source URL:** {item['url']}"],
                )
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{path}: {exc}")
                print(f"    ERROR: {exc}")
            throttle()

    elif section == "feats":
        slugs = discover_slugs("feat", skip=FEAT_SKIP)
        throttle()
        print(f"  found {len(slugs)} feats")
        section_pages, section_failures = scrape_indexed(
            section,
            "feat",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "equipment":
        print(f"  found {len(EQUIPMENT_CATEGORIES)} equipment categories")
        section_pages, section_failures = scrape_indexed(
            section,
            "equipment",
            EQUIPMENT_CATEGORIES,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "magic-items":
        slugs = discover_slugs("magic-item", skip=MAGIC_ITEM_SKIP)
        throttle()
        print(f"  found {len(slugs)} magic items")
        section_pages, section_failures = scrape_indexed(
            section,
            "magic-item",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "magic-item-categories":
        print(f"  found {len(MAGIC_ITEM_CATEGORIES)} magic item categories")
        section_pages, section_failures = scrape_indexed(
            section,
            "magic-item",
            MAGIC_ITEM_CATEGORIES,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "spells":
        slugs = discover_slugs("spell", skip=SPELL_SKIP)
        throttle()
        print(f"  found {len(slugs)} spells")
        section_pages, section_failures = scrape_indexed(
            section,
            "spell",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "misc":
        print(f"  found {len(MISC_PAGES)} misc pages")
        section_pages, section_failures = scrape_paths(
            section,
            MISC_PAGES,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    elif section == "ua":
        slugs = discover_slugs("ua", skip=UA_SKIP)
        throttle()
        print(f"  found {len(slugs)} UA pages")
        section_pages, section_failures = scrape_indexed(
            section,
            "ua",
            slugs,
            lambda item: [f"**Source URL:** {item['url']}"],
        )
        pages.extend(section_pages)
        failures.extend(section_failures)

    else:
        raise ValueError(f"Unknown section: {section}")

    print(f"  saved {len(pages)} pages")
    return pages, failures


def write_manifest(all_pages: dict[str, list[dict]], all_failures: list[str]) -> None:
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source": "http://dnd2024.wikidot.com/",
        "sections": {
            section: [
                {
                    "slug": page["slug"],
                    "title": page["title"],
                    "path": page["path"],
                    "url": page["url"],
                    "source": page.get("source"),
                }
                for page in pages
            ]
            for section, pages in all_pages.items()
        },
        "counts": {section: len(pages) for section, pages in all_pages.items()},
        "total": sum(len(pages) for pages in all_pages.values()),
        "failures": all_failures,
    }
    (DEFAULT_OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape dnd2024.wikidot.com content")
    parser.add_argument(
        "--section",
        action="append",
        choices=SECTION_NAMES,
        help="Scrape only selected section(s); can be repeated",
    )
    parser.add_argument("--list-sections", action="store_true", help="List available sections")
    args = parser.parse_args()

    if args.list_sections:
        for name in SECTION_NAMES:
            print(name)
        return

    sections = args.section or SECTION_NAMES
    all_pages: dict[str, list[dict]] = {}
    all_failures: list[str] = []

    for section in sections:
        pages, failures = scrape_section(section)
        all_pages[section] = pages
        all_failures.extend(failures)

    write_manifest(all_pages, all_failures)

    total = sum(len(pages) for pages in all_pages.values())
    print(f"\nDone. Saved {total} pages to {DEFAULT_OUTPUT_DIR}")
    for section, pages in all_pages.items():
        print(f"  {section}: {len(pages)}")
    if all_failures:
        print(f"\nFailures ({len(all_failures)}):")
        for failure in all_failures[:20]:
            print(f"  - {failure}")
        if len(all_failures) > 20:
            print(f"  ... and {len(all_failures) - 20} more")


if __name__ == "__main__":
    main()
