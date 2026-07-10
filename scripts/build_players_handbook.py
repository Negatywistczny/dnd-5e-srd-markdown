#!/usr/bin/env python3
"""Compile Player's Handbook markdown from SRD and wikidot sources."""

from __future__ import annotations

import argparse
import json
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRD = {"en": ROOT / "srd-5.2.1" / "en", "pl": ROOT / "srd-5.2.1" / "pl"}
WIKI = {"en": ROOT / "dnd2024-wikidot", "pl": ROOT / "dnd2024-wikidot-pl"}

PHB_SOURCE_MARKERS = {
    "en": "Source: Player's Handbook",
    "pl": ("Źródło: Podręcznik Gracza", "Source: Player's Handbook"),
}

CHAPTER_TITLES = {
    "en": {
        1: "Ch. 1: Playing the Game",
        2: "Ch. 2: Creating a Character",
        3: "Ch. 3: Character Classes",
        4: "Ch. 4: Character Origins",
        5: "Ch. 5: Feats",
        6: "Ch. 6: Equipment",
        7: "Ch. 7: Spells",
    },
    "pl": {
        1: "Rozdz. 1: Zasady gry",
        2: "Rozdz. 2: Tworzenie postaci",
        3: "Rozdz. 3: Klasy postaci",
        4: "Rozdz. 4: Pochodzenie postaci",
        5: "Rozdz. 5: Atuty",
        6: "Rozdz. 6: Wyposażenie",
        7: "Rozdz. 7: Czary",
    },
}

BOOK_TITLES = {"en": "Player's Handbook", "pl": "Podręcznik Gracza"}

TOC_TITLES = {"en": "Contents", "pl": "Spis treści"}

CLASSES_EN = [
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

# Alphabetical by Polish display name (Barbarzyńca, Bard, Czarownik, …).
CLASSES_PL = [
    "barbarian",
    "bard",
    "warlock",
    "druid",
    "cleric",
    "rogue",
    "ranger",
    "wizard",
    "monk",
    "paladin",
    "fighter",
    "sorcerer",
]

CLASS_SPELL_LISTS = {
    "bard": ("Bard Spell List", "Lista czarów barda"),
    "cleric": ("Cleric Spell List", "Lista czarów kleryka"),
    "druid": ("Druid Spell List", "Lista czarów druida"),
    "paladin": ("Paladin Spell List", "Lista czarów paladyna"),
    "ranger": ("Ranger Spell List", "Lista czarów łowcy"),
    "sorcerer": ("Sorcerer Spell List", "Lista czarów zaklinacza"),
    "warlock": ("Warlock Spell List", "Lista czarów czarownika"),
    "wizard": ("Wizard Spell List", "Lista czarów maga"),
}

CLASS_OPTIONS = {
    "sorcerer": "sorcerer-metamagic.md",
    "warlock": "warlock-eldritch-invocation.md",
}

SUBCLASSES: dict[str, list[str]] = {
    "barbarian": [
        "barbarian-path-of-the-berserker",
        "barbarian-path-of-the-wild-heart",
        "barbarian-path-of-the-world-tree",
        "barbarian-path-of-the-zealot",
    ],
    "bard": [
        "bard-college-of-dance",
        "bard-college-of-glamour",
        "bard-college-of-lore",
        "bard-college-of-valor",
    ],
    "cleric": [
        "cleric-life-domain",
        "cleric-light-domain",
        "cleric-trickery-domain",
        "cleric-war-domain",
    ],
    "druid": [
        "druid-circle-of-the-land",
        "druid-circle-of-the-moon",
        "druid-circle-of-the-sea",
        "druid-circle-of-the-stars",
    ],
    "fighter": [
        "fighter-battle-master",
        "fighter-champion",
        "fighter-eldritch-knight",
        "fighter-psi-warrior",
    ],
    "monk": [
        "monk-warrior-of-mercy",
        "monk-warrior-of-shadow",
        "monk-warrior-of-the-elements",
        "monk-warrior-of-the-open-hand",
    ],
    "paladin": [
        "paladin-oath-of-devotion",
        "paladin-oath-of-glory",
        "paladin-oath-of-the-ancients",
        "paladin-oath-of-vengeance",
    ],
    "ranger": [
        "ranger-beast-master",
        "ranger-fey-wanderer",
        "ranger-gloom-stalker",
        "ranger-hunter",
    ],
    "rogue": [
        "rogue-arcane-trickster",
        "rogue-assassin",
        "rogue-soulknife",
        "rogue-thief",
    ],
    "sorcerer": [
        "sorcerer-aberrant-sorcery",
        "sorcerer-clockwork-sorcery",
        "sorcerer-draconic-sorcery",
        "sorcerer-wild-magic-sorcery",
    ],
    "warlock": [
        "warlock-archfey-patron",
        "warlock-celestial-patron",
        "warlock-fiend-patron",
        "warlock-great-old-one-patron",
    ],
    "wizard": [
        "wizard-abjurer",
        "wizard-diviner",
        "wizard-evoker",
        "wizard-illusionist",
    ],
}

BACKGROUNDS = [
    "acolyte",
    "artisan",
    "charlatan",
    "criminal",
    "entertainer",
    "farmer",
    "guard",
    "guide",
    "hermit",
    "merchant",
    "noble",
    "sage",
    "sailor",
    "scribe",
    "soldier",
    "wayfarer",
]

SPECIES = [
    "aasimar",
    "dragonborn",
    "dwarf",
    "elf",
    "gnome",
    "goliath",
    "halfling",
    "human",
    "orc",
    "tiefling",
]

ORIGIN_FEATS = {"alert", "magic-initiate", "savage-attacker", "skilled"}

CONDITIONS_EN = [
    "Blinded",
    "Charmed",
    "Deafened",
    "Exhaustion",
    "Frightened",
    "Grappled",
    "Incapacitated",
    "Invisible",
    "Paralyzed",
    "Petrified",
    "Poisoned",
    "Prone",
    "Restrained",
    "Stunned",
    "Unconscious",
]

CONDITIONS_PL = [
    "Oślepiony",
    "Zauroczony",
    "Ogłuchony",
    "Wyczerpanie",
    "Przerażony",
    "Pochwycony",
    "Obezwładniony",
    "Niewidzialny",
    "Sparaliżowany",
    "Skamieniały",
    "Zatruty",
    "Powalony",
    "Unieruchomiony",
    "Ogłuszony",
    "Nieprzytomny",
]

SERVICES_SECTIONS_EN = [
    "Lifestyle Expenses",
    "Food, Drink, and Lodging",
    "Hirelings",
    "Spellcasting",
]

SERVICES_SECTIONS_PL = [
    "Koszty utrzymania",
    "Jedzenie, napoje i nocleg",
    "Najemnicy",
    "Usługi rzucania czarów",
]

WIKIDOT_BASE = "http://dnd2024.wikidot.com/"

SPECIAL_PATH_TITLES: dict[str, dict[str, str]] = {
    "class:multiclassing": {"en": "Multiclassing", "pl": "Wieloklasowość"},
    "feat:all": {"en": "Feat Descriptions", "pl": "Opisy atutów"},
    "equipment:tool": {"en": "Tools", "pl": "Narzędzia"},
    "equipment:weapon": {"en": "Weapons", "pl": "Bronie"},
}

FRAGMENT_TITLES: dict[str, dict[str, str]] = {
    "mastery-properties": {
        "en": "Mastery Properties",
        "pl": "Właściwości mistrzostwa",
    },
    "properties": {"en": "Properties", "pl": "Właściwości"},
}

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

FIGHTING_STYLE_FEATS = {
    "archery",
    "blind-fighting",
    "defense",
    "dueling",
    "great-weapon-fighting",
    "interception",
    "protection",
    "thrown-weapon-fighting",
    "two-weapon-fighting",
    "unarmed-fighting",
}

FEAT_CATEGORY_TITLES = {
    "en": {
        "origin": "Origin Feats",
        "general": "General Feats",
        "fighting": "Fighting Style Feats",
        "epic": "Epic Boon Feats",
    },
    "pl": {
        "origin": "Atuty pochodzenia",
        "general": "Atuty ogólne",
        "fighting": "Atuty stylu walki",
        "epic": "Atuty boskich łask",
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def is_phb_content(text: str, lang: str) -> bool:
    marker = PHB_SOURCE_MARKERS[lang]
    if isinstance(marker, tuple):
        return any(m in text for m in marker)
    return marker in text


def bump_headings(text: str, amount: int) -> str:
    if amount == 0:
        return text

    def repl(match: re.Match[str]) -> str:
        hashes = match.group(1)
        new_level = len(hashes) + amount
        if new_level > 6:
            new_level = 6
        return "#" * new_level + match.group(2)

    return re.sub(r"^(#{1,6})(\s+.+)$", repl, text, flags=re.MULTILINE)


def first_heading_title(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def strip_wikidot_metadata(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    if i < len(lines) and lines[i].startswith("# "):
        i += 1
    while i < len(lines) and (
        lines[i].startswith("**")
        or lines[i].strip() == ""
        or lines[i].strip() == "---"
        or lines[i].startswith("Źródło:")
        or lines[i].startswith("Source:")
    ):
        if lines[i].strip() == "---":
            i += 1
            break
        i += 1
    while i < len(lines) and (
        lines[i].startswith("Źródło:")
        or lines[i].startswith("Source:")
        or lines[i].strip() == ""
    ):
        i += 1
    out.extend(lines[i:])
    return "\n".join(out).strip()


def extract_section(text: str, heading: str, level: int = 2) -> str:
    prefix = "#" * level + " "
    pattern = re.compile(
        rf"^{re.escape(prefix)}{re.escape(heading)}\s*$",
        flags=re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        raise KeyError(f"Section not found: {prefix}{heading}")

    start = match.end()
    next_heading = re.compile(rf"^#{{1,{level}}}\s+", flags=re.MULTILINE)
    end = len(text)
    for candidate in next_heading.finditer(text, start):
        if candidate.start() > start:
            end = candidate.start()
            break
    return text[start:end].strip()


def drop_top_heading(text: str) -> str:
    return re.sub(r"^#\s+.+\n+", "", text, count=1, flags=re.MULTILINE).strip()


def join_blocks(blocks: list[str]) -> str:
    return "\n\n".join(block.strip() for block in blocks if block.strip())


def extract_conditions(lang: str) -> str:
    glossary = read_text(SRD[lang] / "rules-glossary.md")
    entries: list[str] = []
    tag = "Condition" if lang == "en" else "Stan"
    pattern = re.compile(
        rf"^#### ([^\[\n]+) \[{tag}\]\s*\n\n(.*?)(?=\n#### |\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    by_title = {m.group(1).strip(): m.group(2).strip() for m in pattern.finditer(glossary)}
    order = CONDITIONS_EN if lang == "en" else CONDITIONS_PL
    for title in order:
        body = by_title.get(title, "")
        if body:
            entries.append(f"#### {title}\n\n{body}")
    return join_blocks(entries)


def build_chapter_1(lang: str) -> str:
    playing = read_text(SRD[lang] / "playing-the-game.md")
    body = drop_top_heading(playing)
    conditions_title = "Conditions" if lang == "en" else "Stany"
    return join_blocks(
        [
            f"## {CHAPTER_TITLES[lang][1]}",
            bump_headings(body, 1),
            f"### {conditions_title}",
            extract_conditions(lang),
        ]
    )


def build_chapter_2(lang: str) -> str:
    creation = read_text(SRD[lang] / "character-creation.md")
    body = drop_top_heading(creation)
    return join_blocks([f"## {CHAPTER_TITLES[lang][2]}", bump_headings(body, 1)])


def load_wikidot_body(lang: str, rel_path: str, heading_shift: int) -> str:
    text = read_text(WIKI[lang] / rel_path)
    body = strip_wikidot_metadata(text)
    return bump_headings(body, heading_shift)


def build_chapter_3(lang: str) -> str:
    classes = CLASSES_EN if lang == "en" else CLASSES_PL
    blocks = [f"## {CHAPTER_TITLES[lang][3]}"]

    for slug in classes:
        class_path = f"classes/{slug}.md"
        class_body = load_wikidot_body(lang, class_path, heading_shift=3)
        class_title = first_heading_title(read_text(WIKI[lang] / class_path))
        blocks.append(f"### {class_title}\n\n{class_body}")

        if slug in CLASS_SPELL_LISTS:
            _, list_title_pl = CLASS_SPELL_LISTS[slug]
            list_title = CLASS_SPELL_LISTS[slug][0] if lang == "en" else list_title_pl
            list_body = load_wikidot_body(lang, f"spell-lists/{slug}.md", heading_shift=3)
            blocks.append(f"#### {list_title}\n\n{list_body}")

        if slug in CLASS_OPTIONS:
            options_body = load_wikidot_body(lang, f"class-options/{CLASS_OPTIONS[slug]}", heading_shift=3)
            options_title = first_heading_title(
                read_text(WIKI[lang] / "class-options" / CLASS_OPTIONS[slug])
            )
            blocks.append(f"#### {options_title}\n\n{options_body}")

        for sub_slug in SUBCLASSES[slug]:
            sub_path = f"subclasses/{sub_slug}.md"
            sub_title = first_heading_title(read_text(WIKI[lang] / sub_path))
            sub_body = load_wikidot_body(lang, sub_path, heading_shift=2)
            blocks.append(f"#### {sub_title}\n\n{sub_body}")

    return join_blocks(blocks)


def build_chapter_4(lang: str) -> str:
    origins = read_text(SRD[lang] / "character-origins.md")
    if lang == "en":
        parts_bg = extract_section(origins, "Parts of a Background", level=3)
        parts_sp = extract_section(origins, "Parts of a Species", level=3)
        origin_heading = "Origin Components"
        bg_heading = "Background Descriptions"
        sp_heading = "Species Descriptions"
    else:
        parts_bg = extract_section(origins, "Elementy pochodzenia", level=3)
        parts_sp = extract_section(origins, "Elementy gatunku", level=3)
        origin_heading = "Elementy pochodzenia"
        bg_heading = "Opisy pochodzeń"
        sp_heading = "Opisy gatunków"

    bg_items: list[tuple[str, str]] = []
    for slug in BACKGROUNDS:
        path = WIKI[lang] / "backgrounds" / f"{slug}.md"
        title = first_heading_title(read_text(path))
        body = bump_headings(strip_wikidot_metadata(read_text(path)), 2)
        bg_items.append((title, body))
    bg_items.sort(key=lambda item: item[0].casefold())

    sp_items: list[tuple[str, str]] = []
    for slug in SPECIES:
        path = WIKI[lang] / "species" / f"{slug}.md"
        title = first_heading_title(read_text(path))
        body = bump_headings(strip_wikidot_metadata(read_text(path)), 3)
        sp_items.append((title, body))
    sp_items.sort(key=lambda item: item[0].casefold())

    blocks = [
        f"## {CHAPTER_TITLES[lang][4]}",
        f"### {origin_heading}",
        f"#### {'Parts of a Background' if lang == 'en' else 'Elementy pochodzenia'}\n\n{parts_bg}",
        f"#### {'Parts of a Species' if lang == 'en' else 'Elementy gatunku'}\n\n{parts_sp}",
        f"### {bg_heading}",
    ]
    blocks.extend(f"#### {title}\n\n{body}" for title, body in bg_items)
    blocks.append(f"### {sp_heading}")
    blocks.extend(f"#### {title}\n\n{body}" for title, body in sp_items)
    return join_blocks(blocks)


def categorize_feat(slug: str, text: str) -> str:
    if slug in ORIGIN_FEATS:
        return "origin"
    if (
        slug in FIGHTING_STYLE_FEATS
        or "Fighting Style Feature" in text
        or "Fighting Style Feat" in text
        or "Atut stylu walki" in text
    ):
        return "fighting"
    if slug.startswith("boon-of-") or "Level 19+" in text or "Epic Boon" in text:
        return "epic"
    return "general"


def build_chapter_5(lang: str) -> str:
    feats_intro = read_text(SRD[lang] / "feats.md")
    if lang == "en":
        intro = extract_section(feats_intro, "Feat Descriptions", level=2)
        intro = extract_section(f"## Feat Descriptions\n\n{intro}", "Parts of a Feat", level=3)
        descriptions_heading = "Feat Descriptions"
        parts_heading = "Parts of a Feat"
    else:
        intro = extract_section(feats_intro, "Opisy atutów", level=2)
        intro = extract_section(
            f"## Opisy atutów\n\n{intro}",
            "Elementy opisu atutu",
            level=3,
        )
        descriptions_heading = "Opisy atutów"
        parts_heading = "Elementy opisu atutu"

    categorized: dict[str, list[tuple[str, str]]] = {
        "origin": [],
        "general": [],
        "fighting": [],
        "epic": [],
    }
    for path in sorted((WIKI[lang] / "feats").glob("*.md")):
        text = read_text(path)
        if not is_phb_content(text, lang):
            continue
        category = categorize_feat(path.stem, text)
        title = first_heading_title(text)
        body = strip_wikidot_metadata(text)
        categorized[category].append((title, body))

    blocks = [
        f"## {CHAPTER_TITLES[lang][5]}",
        f"### {descriptions_heading}",
        f"#### {parts_heading}\n\n{intro}",
    ]
    for category in ("origin", "general", "fighting", "epic"):
        items = sorted(categorized[category], key=lambda item: item[0].casefold())
        if not items:
            continue
        blocks.append(f"### {FEAT_CATEGORY_TITLES[lang][category]}")
        blocks.extend(f"#### {title}\n\n{body}" for title, body in items)
    return join_blocks(blocks)


def wrap_services_section(lang: str, equipment: str) -> str:
    service_titles = SERVICES_SECTIONS_EN if lang == "en" else SERVICES_SECTIONS_PL
    services_label = "Services" if lang == "en" else "Usługi"
    extracted: list[str] = []
    for title in service_titles:
        try:
            extracted.append(
                f"#### {title}\n\n{extract_section(equipment, title, level=3)}"
            )
        except KeyError:
            continue
    if not extracted:
        return equipment

    for title in service_titles:
        equipment = re.sub(
            rf"^### {re.escape(title)}\s*\n.*?(?=^### |\Z)",
            "",
            equipment,
            count=1,
            flags=re.MULTILINE | re.DOTALL,
        )

    services_block = join_blocks([f"### {services_label}"] + extracted)
    magic_items = "Magic Items" if lang == "en" else "Magiczne przedmioty"
    marker = f"### {magic_items}"
    if marker in equipment:
        head, tail = equipment.split(marker, 1)
        return join_blocks([head.strip(), services_block, f"{marker}{tail}"])
    return join_blocks([equipment.strip(), services_block])


def build_chapter_6(lang: str) -> str:
    equipment = read_text(SRD[lang] / "equipment.md")
    body = drop_top_heading(equipment)
    body = bump_headings(body, 1)
    body = wrap_services_section(lang, body)
    crafting_title = (
        "Crafting Equipment"
        if lang == "en"
        else "Tworzenie wyposażenia"
    )
    body = re.sub(
        r"^### Crafting Nonmagical Items$",
        f"### {crafting_title}",
        body,
        flags=re.MULTILINE,
    )
    body = re.sub(
        r"^### Tworzenie przedmiotów niemagicznych$",
        f"### {crafting_title}",
        body,
        flags=re.MULTILINE,
    )
    return join_blocks([f"## {CHAPTER_TITLES[lang][6]}", body])


def build_chapter_7(lang: str) -> str:
    spells = read_text(SRD[lang] / "spells.md")
    if lang == "en":
        rules = spells.split("## Spell Descriptions", 1)[0].strip()
        rules = drop_top_heading(rules)
        descriptions_heading = "Spell Descriptions"
    else:
        rules = spells.split("## Opisy czarów", 1)[0].strip()
        rules = drop_top_heading(rules)
        descriptions_heading = "Opisy czarów"

    spell_items: list[tuple[str, str]] = []
    for path in sorted((WIKI[lang] / "spells").glob("*.md")):
        text = read_text(path)
        if not is_phb_content(text, lang):
            continue
        title = first_heading_title(text)
        body = strip_wikidot_metadata(text)
        spell_items.append((title, body))
    spell_items.sort(key=lambda item: item[0].casefold())

    blocks = [
        f"## {CHAPTER_TITLES[lang][7]}",
        bump_headings(rules, 1),
        f"### {descriptions_heading}",
    ]
    blocks.extend(f"#### {title}\n\n{body}" for title, body in spell_items)
    return join_blocks(blocks)


def github_slug(text: str) -> str:
    text = re.sub(r"\[\]\(\)", "", text).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def normalize_heading_title(text: str) -> str:
    text = re.sub(r"\[\]\(\)", "", text).strip()
    return re.sub(r"\s*\([^)]*\)\s*$", "", text).strip()


@lru_cache(maxsize=2)
def load_manifest_path_titles() -> dict[str, str]:
    manifest = json.loads(read_text(WIKI["en"] / "manifest.json"))
    titles: dict[str, str] = {}
    for items in manifest.get("sections", {}).values():
        for item in items:
            titles[item["path"]] = item["title"]
            titles[item["url"].replace(WIKIDOT_BASE, "")] = item["title"]
    return titles


def resolve_file_title(lang: str, section: str, slug: str) -> str | None:
    path = WIKI[lang] / section / f"{slug}.md"
    if path.exists():
        return normalize_heading_title(first_heading_title(read_text(path)))
    return None


def resolve_link_target_title(target: str, lang: str) -> str | None:
    target = target.strip()
    if not target or target.startswith("#"):
        return None

    fragment = ""
    if "#" in target:
        target, fragment = target.split("#", 1)

    if target.startswith(WIKIDOT_BASE):
        target = target[len(WIKIDOT_BASE) :]

    if target.startswith("../"):
        target = target[3:]
    if target.startswith("./"):
        target = target[2:]
    if target.endswith(".md"):
        target = target[:-3]

    if fragment and fragment in FRAGMENT_TITLES:
        return FRAGMENT_TITLES[fragment][lang]

    if "/" in target:
        section, slug = target.split("/", 1)
        title = resolve_file_title(lang, section, slug)
        if title:
            return title

    if target in SPECIAL_PATH_TITLES:
        return SPECIAL_PATH_TITLES[target][lang]

    manifest_titles = load_manifest_path_titles()
    if target in manifest_titles:
        title = manifest_titles[target]
        if lang == "pl":
            if ":" in target:
                section, slug = target.split(":", 1)
                section_map = {
                    "spell": "spells",
                    "feat": "feats",
                    "background": "backgrounds",
                }
                mapped = section_map.get(section)
                if mapped:
                    localized = resolve_file_title(lang, mapped, slug)
                    if localized:
                        return localized
            elif target.endswith(":spell-list"):
                class_slug = target.split(":", 1)[0]
                localized = resolve_file_title(lang, "spell-lists", class_slug)
                if localized:
                    return localized
        return title

    if ":" in target:
        section, slug = target.split(":", 1)
        section_dirs = {
            "spell": "spells",
            "feat": "feats",
            "background": "backgrounds",
            "barbarian": "subclasses",
            "bard": "subclasses",
            "cleric": "subclasses",
            "druid": "subclasses",
            "fighter": "subclasses",
            "monk": "subclasses",
            "paladin": "subclasses",
            "ranger": "subclasses",
            "rogue": "subclasses",
            "sorcerer": "subclasses",
            "warlock": "subclasses",
            "wizard": "subclasses",
        }
        if section in section_dirs:
            file_slug = f"{section}-{slug}"
            title = resolve_file_title(lang, section_dirs[section], file_slug)
            if title:
                return title
        if section in CLASSES_EN and slug == "spell-list":
            titles = CLASS_SPELL_LISTS.get(section)
            if titles:
                return titles[1] if lang == "pl" else titles[0]

    return None


def build_heading_index(text: str) -> dict[str, str]:
    counts: dict[str, int] = {}
    index: dict[str, str] = {}

    def register(key: str, slug: str) -> None:
        key = key.strip()
        if not key:
            return
        index[key.casefold()] = slug
        index[github_slug(key)] = slug

    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not match:
            continue
        raw = normalize_heading_title(match.group(2))
        base = github_slug(raw)
        duplicate = counts.get(base, 0)
        slug = base if duplicate == 0 else f"{base}-{duplicate}"
        counts[base] = duplicate + 1

        register(raw, slug)
        level_match = re.match(r"^Level \d+:\s*(.+)$", raw, flags=re.IGNORECASE)
        if level_match:
            register(level_match.group(1), slug)

    return index


def lookup_anchor(title: str | None, fragment: str | None, index: dict[str, str]) -> str | None:
    candidates: list[str] = []
    if fragment:
        candidates.append(fragment.replace("-", " "))
        candidates.append(fragment)
    if title:
        candidates.append(title)

    for candidate in candidates:
        for key in (candidate, github_slug(candidate)):
            slug = index.get(key.casefold()) or index.get(key)
            if slug:
                return f"#{slug}"

    if fragment:
        slug = index.get(fragment.casefold()) or index.get(fragment)
        if slug:
            return f"#{slug}"

    return None


def localize_links(text: str, lang: str) -> str:
    text = re.sub(r"\[\]\(\)", "", text)
    index = build_heading_index(text)

    def replace_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()

        if target.startswith("javascript:"):
            return label

        if target.startswith(("http://", "https://")) and not target.startswith(WIKIDOT_BASE):
            return label

        fragment = ""
        raw_target = target
        if target.startswith("#"):
            fragment = target[1:]
            resolved = lookup_anchor(label, fragment, index)
            return f"[{label}]({resolved})" if resolved else label

        if "#" in target:
            raw_target, fragment = target.split("#", 1)

        normalized_target = raw_target
        if normalized_target.startswith("../"):
            normalized_target = normalized_target[3:]
        if normalized_target.startswith("./"):
            normalized_target = normalized_target[2:]
        if normalized_target.endswith(".md"):
            normalized_target = normalized_target[:-3]

        title = resolve_link_target_title(raw_target, lang)
        if (
            fragment == "mastery-properties"
            or (
                not fragment
                and normalized_target in ("equipment/weapon", "equipment:weapon")
                and re.search(r"mastery|mistrz", label, re.I)
            )
        ):
            fragment = "mastery-properties"
            title = FRAGMENT_TITLES["mastery-properties"][lang]

        resolved = lookup_anchor(title or label, fragment or None, index)
        if resolved:
            return f"[{label}]({resolved})"
        return label

    return MARKDOWN_LINK_RE.sub(replace_link, text)


def generate_table_of_contents(text: str, lang: str) -> str:
    toc_title = TOC_TITLES[lang]
    lines = [f"## {toc_title}", ""]
    skip_titles = {toc_title.casefold(), BOOK_TITLES[lang].casefold()}
    open_levels: list[int] = []
    slug_counts: dict[str, int] = {}

    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not match:
            continue

        level = len(match.group(1))
        if level == 1:
            continue
        title = normalize_heading_title(match.group(2))
        if title.casefold() in skip_titles:
            continue

        while open_levels and open_levels[-1] >= level:
            open_levels.pop()

        base = github_slug(title)
        duplicate = slug_counts.get(base, 0)
        slug = base if duplicate == 0 else f"{base}-{duplicate}"
        slug_counts[base] = duplicate + 1

        if level == 2:
            lines.append(f"- [{title}](#{slug})")
        elif level == 3 and open_levels in ([2], [2, 3]):
            lines.append(f"  - [{title}](#{slug})")

        open_levels.append(level)

    return "\n".join(lines)


def build_book(lang: str) -> str:
    chapters = [
        build_chapter_1(lang),
        build_chapter_2(lang),
        build_chapter_3(lang),
        build_chapter_4(lang),
        build_chapter_5(lang),
        build_chapter_6(lang),
        build_chapter_7(lang),
    ]
    body = localize_links(join_blocks(chapters), lang)
    toc = generate_table_of_contents(body, lang)
    return join_blocks([f"# {BOOK_TITLES[lang]}", toc, body])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lang",
        choices=("en", "pl", "both"),
        default="both",
        help="Which handbook version to build (default: both).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "compiled",
        help="Output directory (default: compiled/).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    langs = ("en", "pl") if args.lang == "both" else (args.lang,)
    for lang in langs:
        output = args.output_dir / f"players-handbook-{lang}.md"
        write_text(output, build_book(lang))
        lines = output.read_text(encoding="utf-8").count("\n") + 1
        size_kb = output.stat().st_size // 1024
        print(f"Wrote {output} ({lines:,} lines, {size_kb:,} KB)")


if __name__ == "__main__":
    main()
