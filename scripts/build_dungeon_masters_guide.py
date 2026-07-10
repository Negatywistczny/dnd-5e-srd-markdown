#!/usr/bin/env python3
"""Compile a best-effort Dungeon Master's Guide from SRD and wikidot sources."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_players_handbook import (  # noqa: E402
    ROOT as PH_ROOT,
    SRD,
    WIKI,
    bump_headings,
    drop_top_heading,
    extract_section,
    first_heading_title,
    generate_table_of_contents,
    join_blocks,
    localize_links,
    read_text,
    strip_wikidot_metadata,
    write_text,
)

assert ROOT == PH_ROOT

DMG_SOURCE_MARKERS = {
    "en": "Source: Dungeon Master's Guide",
    "pl": ("Źródło: Podręcznik Mistrza Gry", "Source: Dungeon Master's Guide"),
}

BOOK_TITLES = {
    "en": "Dungeon Master's Guide",
    "pl": "Podręcznik Mistrza Gry",
}

COMPILATION_NOTES = {
    "en": (
        "> **Compiled edition.** This book merges SRD 5.2.1 and "
        "dnd2024.wikidot content tagged *Dungeon Master's Guide*. "
        "It follows the 2024 DMG chapter outline where sources exist. "
        "**Not included** (no scrape in this repository): ch. 1 *The Basics*, "
        "ch. 4 *Creating Adventures*, ch. 5 *Creating Campaigns*, "
        "*Greyhawk*, ch. 6 *Cosmology*, and DMG-only sections such as "
        "*Treasure Themes*, gemstone/art-object/random magic item tables, "
        "*Chases*, *Doors*, *Dungeons*, *Settlements*, and similar narrative "
        "DMG chapters. Appendix A is the full SRD *Rules Glossary*; "
        "Appendix B covers stat block rules without creature lists."
    ),
    "pl": (
        "> **Wydanie skompilowane.** Ten tom łączy SRD 5.2.1 oraz treści "
        "z dnd2024.wikidot oznaczone *Podręcznik Mistrza Gry*. "
        "Struktura odpowiada PMG 2024 tam, gdzie mamy źródła. "
        "**Pominięto** (brak scrapu w repozytorium): rozdz. 1 *Podstawy*, "
        "rozdz. 4 *Tworzenie przygód*, rozdz. 5 *Tworzenie kampanii*, "
        "*Greyhawk*, rozdz. 6 *Kosmologia* oraz sekcje PMG bez odpowiednika "
        "w SRD/wikidot (tematy skarbów, tabele klejnotów i dzieł sztuki, "
        "losowe przedmioty magiczne, pościgi, drzwi, lochy, osiedla itd.). "
        "Dodatek A to pełny *Słownik reguł* SRD; dodatek B — zasady bloków "
        "statystyk bez listy potworów."
    ),
}

CHAPTER_TITLES = {
    "en": {
        2: "Ch. 2: Running the Game",
        3: "Ch. 3: DM's Toolbox",
        7: "Ch. 7: Treasure",
        8: "Ch. 8: Bastions",
        "appendix_a": "Appendix A: Rules Glossary",
        "appendix_b": "Appendix B: Stat Blocks",
    },
    "pl": {
        2: "Rozdz. 2: Prowadzenie gry",
        3: "Rozdz. 3: Narzędzia MG",
        7: "Rozdz. 7: Skarb",
        8: "Rozdz. 8: Bastiony",
        "appendix_a": "Dodatek A: Słownik reguł",
        "appendix_b": "Dodatek B: Bloki statystyk",
    },
}

SECTION_ALIASES = {
    "en": {
        "d20_tests": "D20 Tests",
        "proficiency": "Proficiency",
        "social": "Social Interaction",
        "exploration": "Exploration",
        "combat": "Combat",
        "damage": "Damage and Healing",
        "travel": "Travel Pace",
        "level_advancement": "Level Advancement",
        "coins": "Coins",
        "magic_items_az": "Magic Items A–Z",
    },
    "pl": {
        "d20_tests": "Testy k20",
        "proficiency": "Biegłość",
        "social": "Interakcje społeczne",
        "exploration": "Eksploracja",
        "combat": "Walka",
        "damage": "Obrażenia i leczenie",
        "travel": "Tempo podróży",
        "level_advancement": "Awans poziomów",
        "coins": "Monety",
        "magic_items_az": "Przedmioty magiczne A–Z",
    },
}

TOOLBOX_SECTIONS = {
    "en": [
        "Creating a Background",
        "Curses and Magical Contagions",
        "Environmental Effects",
        "Fear and Mental Stress",
        "Traps",
        "Combat Encounters",
        "Troubleshooting",
    ],
    "pl": [
        "Tworzenie pochodzenia",
        "Klątwy i magiczne zarazy",
        "Efekty środowiskowe",
        "Strach i obciążenie psychiczne",
        "Pułapki",
        "Spotkania bojowe",
        "Rozwiązywanie problemów",
    ],
}


def is_dmg_wikidot_content(text: str, lang: str) -> bool:
    marker = DMG_SOURCE_MARKERS[lang]
    if isinstance(marker, tuple):
        return any(m in text for m in marker)
    return marker in text


def load_wikidot_body(lang: str, rel_path: str, heading_shift: int) -> str:
    text = read_text(WIKI[lang] / rel_path)
    body = strip_wikidot_metadata(text)
    return bump_headings(body, heading_shift)


def split_magic_items_rules(lang: str) -> tuple[str, str]:
    text = read_text(SRD[lang] / "magic-items.md")
    az_heading = SECTION_ALIASES[lang]["magic_items_az"]
    if f"## {az_heading}" not in text:
        raise KeyError(f"Magic items A–Z section not found: {az_heading}")
    rules, _ = text.split(f"## {az_heading}", 1)
    return drop_top_heading(rules).strip(), az_heading


def extract_named_section(text: str, heading: str, level: int = 2) -> str:
    return extract_section(text, heading, level=level).strip()


def build_chapter_2(lang: str) -> str:
    aliases = SECTION_ALIASES[lang]
    playing = read_text(SRD[lang] / "playing-the-game.md")
    toolbox = read_text(SRD[lang] / "gameplay-toolbox.md")
    creation = read_text(SRD[lang] / "character-creation.md")

    resolving_title = "Resolving Outcomes" if lang == "en" else "Rozstrzyganie wyników"
    resolving_blocks = [
        f"#### {aliases['d20_tests']}\n\n{extract_named_section(playing, aliases['d20_tests'])}",
        f"#### {aliases['proficiency']}\n\n{extract_named_section(playing, aliases['proficiency'])}",
    ]

    social_title = (
        "Running Social Interaction"
        if lang == "en"
        else "Prowadzenie interakcji społecznych"
    )
    explore_title = (
        "Running Exploration" if lang == "en" else "Prowadzenie eksploracji"
    )
    combat_title = "Running Combat" if lang == "en" else "Prowadzenie walki"
    advancement_title = (
        "Character Advancement" if lang == "en" else "Awans postaci"
    )
    travel_label = "Travel" if lang == "en" else "Podróż"

    blocks = [
        f"## {CHAPTER_TITLES[lang][2]}",
        f"### {resolving_title}",
        *resolving_blocks,
        f"### {social_title}",
        bump_headings(extract_named_section(playing, aliases["social"]), 1),
        f"### {explore_title}",
        bump_headings(extract_named_section(playing, aliases["exploration"]), 1),
        f"#### {travel_label}",
        bump_headings(extract_named_section(toolbox, aliases["travel"]), 1),
        f"### {combat_title}",
        bump_headings(extract_named_section(playing, aliases["combat"]), 1),
        bump_headings(extract_named_section(playing, aliases["damage"]), 1),
        f"### {advancement_title}",
        bump_headings(
            extract_named_section(creation, aliases["level_advancement"]),
            1,
        ),
    ]
    return join_blocks(blocks)


def build_chapter_3(lang: str) -> str:
    toolbox = read_text(SRD[lang] / "gameplay-toolbox.md")
    poison_title = "Poison" if lang == "en" else "Trucizny"
    blocks = [f"## {CHAPTER_TITLES[lang][3]}"]

    for section in TOOLBOX_SECTIONS[lang]:
        blocks.append(
            f"### {section}\n\n{bump_headings(extract_named_section(toolbox, section), 1)}"
        )

    poison_path = WIKI[lang] / "equipment" / "poison.md"
    if poison_path.is_file():
        poison_body = load_wikidot_body(lang, "equipment/poison.md", heading_shift=2)
        blocks.append(f"### {poison_title}\n\n{poison_body}")
    else:
        blocks.append(
            f"### {poison_title}\n\n"
            f"{bump_headings(extract_named_section(toolbox, poison_title), 1)}"
        )

    return join_blocks(blocks)


def build_chapter_7(lang: str) -> str:
    equipment = read_text(SRD[lang] / "equipment.md")
    rules, az_heading = split_magic_items_rules(lang)
    blocks = [
        f"## {CHAPTER_TITLES[lang][7]}",
        f"### {SECTION_ALIASES[lang]['coins']}",
        bump_headings(extract_named_section(equipment, SECTION_ALIASES[lang]["coins"]), 1),
        bump_headings(rules, 1),
    ]

    crafting_path = WIKI[lang] / "magic-items" / "crafting.md"
    if crafting_path.is_file():
        special_title = (
            "Magic Item Special Features"
            if lang == "en"
            else "Specjalne cechy przedmiotów magicznych"
        )
        crafting_text = read_text(crafting_path)
        marker = (
            "# Magic Item Special Features"
            if lang == "en"
            else "# Szczególne cechy przedmiotów magicznych"
        )
        if marker not in crafting_text:
            marker = "# Magic Item Special Features"
        if marker in crafting_text:
            special_body = crafting_text.split(marker, 1)[1].strip()
            special_body = bump_headings(special_body, 3)
            blocks.append(f"### {special_title}\n\n{special_body}")

    items: list[tuple[str, str]] = []
    for path in sorted((WIKI[lang] / "magic-items").glob("*.md")):
        if path.name == "crafting.md":
            continue
        text = read_text(path)
        if not is_dmg_wikidot_content(text, lang):
            continue
        title = first_heading_title(text)
        body = strip_wikidot_metadata(text)
        items.append((title, body))
    items.sort(key=lambda item: item[0].casefold())

    blocks.append(f"### {az_heading}")
    blocks.extend(f"#### {title}\n\n{body}" for title, body in items)
    return join_blocks(blocks)


def build_chapter_8(lang: str) -> str:
    bastions = load_wikidot_body(lang, "misc/bastions.md", heading_shift=2)
    return join_blocks([f"## {CHAPTER_TITLES[lang][8]}", bastions])


def build_appendix_a(lang: str) -> str:
    glossary = drop_top_heading(read_text(SRD[lang] / "rules-glossary.md"))
    return join_blocks(
        [
            f"## {CHAPTER_TITLES[lang]['appendix_a']}",
            bump_headings(glossary, 1),
        ]
    )


def build_appendix_b(lang: str) -> str:
    monsters = drop_top_heading(read_text(SRD[lang] / "monsters.md"))
    return join_blocks(
        [
            f"## {CHAPTER_TITLES[lang]['appendix_b']}",
            bump_headings(monsters, 1),
        ]
    )


def build_book(lang: str) -> str:
    chapters = [
        build_chapter_2(lang),
        build_chapter_3(lang),
        build_chapter_7(lang),
        build_chapter_8(lang),
        build_appendix_a(lang),
        build_appendix_b(lang),
    ]
    body = localize_links(join_blocks(chapters), lang)
    toc = generate_table_of_contents(body, lang)
    return join_blocks(
        [
            f"# {BOOK_TITLES[lang]}",
            COMPILATION_NOTES[lang],
            toc,
            body,
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lang",
        choices=("en", "pl", "both"),
        default="both",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "compiled",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    langs = ("en", "pl") if args.lang == "both" else (args.lang,)
    for lang in langs:
        output = args.output_dir / f"dungeon-masters-guide-{lang}.md"
        write_text(output, build_book(lang))
        lines = output.read_text(encoding="utf-8").count("\n") + 1
        size_kb = output.stat().st_size // 1024
        print(f"Wrote {output} ({lines:,} lines, {size_kb:,} KB)")


if __name__ == "__main__":
    main()
