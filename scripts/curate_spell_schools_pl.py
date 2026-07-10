#!/usr/bin/env python3
"""Generate curated PL spell school index files from EN sources."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "dnd2024-wikidot" / "spells"
PL_DIR = ROOT / "dnd2024-wikidot-pl" / "spells"

SCHOOL_TITLES = {
    "abjuration-school": "Czary odpychania",
    "conjuration-school": "Czary przywoływania",
    "divination-school": "Czary wieszczenia",
    "enchantment-school": "Czary uroków",
    "evocation-school": "Czary wywoływania",
    "illusion-school": "Czary iluzji",
    "necromancy-school": "Czary nekromancji",
    "transmutation-school": "Czary przemian",
}

SCHOOL_PL = {
    "Abjuration": "odpychania",
    "Conjuration": "przywoływania",
    "Divination": "wieszczenia",
    "Enchantment": "uroków",
    "Evocation": "wywoływania",
    "Illusion": "iluzji",
    "Necromancy": "nekromancji",
    "Transmutation": "przemian",
}

CLASS_PL = {
    "Artificer": "wynalazca",
    "Bard": "bard",
    "Cleric": "kleryk",
    "Druid": "druid",
    "Paladin": "paladyn",
    "Ranger": "łowca",
    "Sorcerer": "zaklinacz",
    "Warlock": "czarownik",
    "Wizard": "mag",
}

LEVEL_TABS = [
    ("Cantrip", "Sztuczka"),
    ("1st Level", "1. krąg"),
    ("2nd Level", "2. krąg"),
    ("3rd Level", "3. krąg"),
    ("4th Level", "4. krąg"),
    ("5th Level", "5. krąg"),
    ("6th Level", "6. krąg"),
    ("7th Level", "7. krąg"),
    ("8th Level", "8. krąg"),
    ("9th Level", "9. krąg"),
]

ROW_RE = re.compile(
    r"^\| \[([^\]]+)\]\(([^)]+)\) \| \*([^*]+)\* \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$"
)
SLUG_RE = re.compile(r"spell:([a-z0-9-]+)")
STAT_RE = re.compile(r"^\*\*(Zasięg|Czas trwania):\*\* (.+)$")
FEET_RE = re.compile(r"(\d+(?:\.\d+)?)-foot\b", re.I)
FEET_WORD_RE = re.compile(r"(\d+(?:\.\d+)?) feet\b", re.I)


def load_pl_spell_names() -> dict[str, str]:
    names: dict[str, str] = {}
    for path in PL_DIR.glob("*.md"):
        if path.name.endswith("-school.md"):
            continue
        first = path.read_text(encoding="utf-8").splitlines()[0]
        if first.startswith("# "):
            names[path.stem] = first[2:].strip()
    return names


def load_pl_spell_stats() -> dict[str, dict[str, str]]:
    stats: dict[str, dict[str, str]] = {}
    for path in PL_DIR.glob("*.md"):
        if path.name.endswith("-school.md"):
            continue
        data: dict[str, str] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            match = STAT_RE.match(line)
            if match:
                data[match.group(1)] = match.group(2).strip()
        if data:
            stats[path.stem] = data
    return stats


def feet_to_meters(value: str) -> str:
    num = float(value)
    meters = num * 0.3
    if meters == int(meters):
        return str(int(meters))
    return f"{meters:.1f}".rstrip("0").rstrip(".")


def translate_range(text: str) -> str:
    text = text.strip()
    if any(
        token in text
        for token in ("metr", "Ty", "Dotyk", "linia", "walec", "emanacja", "sfera", "sześcian")
    ):
        return text
    mapping = {
        "Self": "Ty",
        "Touch": "Dotyk",
    }
    if text in mapping:
        return mapping[text]

    def repl_feet(match: re.Match[str]) -> str:
        return f"{feet_to_meters(match.group(1))}-metrowy"

    def repl_feet_word(match: re.Match[str]) -> str:
        m = feet_to_meters(match.group(1))
        return f"{m} metrów" if float(match.group(1)) != 1 else "1 metr"

    out = FEET_RE.sub(repl_feet, text)
    out = FEET_WORD_RE.sub(repl_feet_word, out)
    out = out.replace("-foot-", "-metrowy-")
    out = out.replace("Line", "linia")
    out = out.replace("Cylinder", "walec")
    out = out.replace("Sphere", "sfera")
    out = out.replace("Cube", "sześcian")
    out = out.replace("Emanation", "emanacja")
    out = out.replace("wide", "szerokości")
    out = out.replace("radius", "promień")
    out = out.replace("high", "wysokości")
    out = out.replace("long", "długości")
    return out


def translate_casting_time(text: str) -> str:
    text = text.strip()
    text = text.replace(" or ", " lub ")
    text = text.replace("*^R^*", "rytuał")
    replacements = [
        ("Bonus Action", "Akcja dodatkowa"),
        ("Reaction", "Reakcja"),
        ("Action", "Akcja"),
        ("10 minutes", "10 minut"),
        ("1 minute", "1 minuta"),
        ("1 hour", "1 godzina"),
        ("24 hours", "24 godziny"),
    ]
    for en, pl in replacements:
        text = text.replace(en, pl)
    return text


def translate_duration(text: str) -> str:
    text = text.strip()
    if any(token in text for token in ("Natychmiastowy", "Koncentracja", "godzin", "minut", "rozproszenia", "runda", "dzień", "dni")):
        return text
    if text == "Instantaneous":
        return "Natychmiastowy"
    if text == "Until dispelled":
        return "Do rozproszenia"
    if text == "1 round":
        return "1 runda"
    if text == "1 day":
        return "1 dzień"
    if text == "10 days":
        return "10 dni"

    text = text.replace("Until dispelled or triggered", "Do rozproszenia lub wyzwolenia")
    text = re.sub(r"\*\^C\^\*, up to 1 minute", "Koncentracja, do 1 minuty", text)
    text = re.sub(r"\*\^C\^\*, up to 10 minutes", "Koncentracja, do 10 minut", text)
    text = re.sub(r"\*\^C\^\*, up to 1 hour", "Koncentracja, do 1 godziny", text)
    text = re.sub(r"\*\^C\^\* up to 1 hour", "Koncentracja, do 1 godziny", text)
    text = text.replace("8 hours", "8 godzin")
    text = text.replace("1 hour", "1 godzina")
    text = text.replace("24 hours", "24 godziny")
    text = text.replace("10 minutes", "10 minut")
    text = text.replace("1 minute", "1 minuta")
    return text


def translate_classes(text: str) -> str:
    parts = [p.strip() for p in text.split(",")]
    return ", ".join(CLASS_PL.get(p, p.lower()) for p in parts)


def slug_from_link(link: str) -> str:
    match = SLUG_RE.search(link)
    if match:
        return match.group(1)
    return Path(link).stem


def process_file(school_file: str, pl_names: dict[str, str], pl_stats: dict[str, dict[str, str]]) -> str:
    en_path = EN_DIR / school_file
    content = en_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    slug = school_file.replace(".md", "")
    title = SCHOOL_TITLES[slug]
    url = f"http://dnd2024.wikidot.com/spell:{slug}"

    out: list[str] = [
        f"# {title}",
        "",
        f"**URL źródła:** {url}",
        "",
        "---",
        "",
    ]

    table_header = (
        "| Nazwa | Szkoła | Listy klas | Czas rzucania | Zasięg | Komponenty | Czas trwania |"
    )
    table_sep = "| --- | --- | --- | --- | --- | --- | --- |"

    for line in lines:
        if line.startswith("| Name |"):
            if out and out[-1] != table_sep:
                out.extend([table_header, table_sep])
            continue
        if line.startswith("| --- |"):
            continue

        match = ROW_RE.match(line)
        if not match:
            continue

        _en_name, link, school, classes, casting, range_, components, duration = match.groups()
        spell_slug = slug_from_link(link)
        pl_name = pl_names.get(spell_slug, _en_name)
        school_pl = SCHOOL_PL.get(school, school.lower())
        spell_stats = pl_stats.get(spell_slug, {})

        out.append(
            "| "
            + " | ".join(
                [
                    f"[{pl_name}]({spell_slug}.md)",
                    f"*{school_pl}*",
                    translate_classes(classes),
                    translate_casting_time(casting),
                    translate_range(spell_stats.get("Zasięg", range_)),
                    components.strip(),
                    translate_duration(spell_stats.get("Czas trwania", duration)),
                ]
            )
            + " |"
        )

    out.append("")
    return "\n".join(out)


def main() -> None:
    pl_names = load_pl_spell_names()
    pl_stats = load_pl_spell_stats()
    for school_file in sorted(SCHOOL_TITLES):
        filename = f"{school_file}.md"
        pl_content = process_file(filename, pl_names, pl_stats)
        out_path = PL_DIR / filename
        out_path.write_text(pl_content, encoding="utf-8")
        print(f"Wrote {out_path.name}")


if __name__ == "__main__":
    main()
