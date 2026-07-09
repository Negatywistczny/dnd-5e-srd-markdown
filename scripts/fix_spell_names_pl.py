#!/usr/bin/env python3
"""Fix Polish spell names in srd-5.2.1/pl/ to match docs/czary-tlumaczenie.md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF_PATH = ROOT / "docs" / "czary-tlumaczenie.md"
PL_DIR = ROOT / "srd-5.2.1" / "pl"
EN_SPELLS = ROOT / "srd-5.2.1" / "en" / "spells.md"
PL_SPELLS = ROOT / "srd-5.2.1" / "pl" / "spells.md"

SKIP_HEADERS = {"Actions", "Traits", "Bonus Actions", "Animated Object"}

RENAME_MAP = {
    "acid arrow": "melf's acid arrow",
    "arcane hand": "bigby's hand",
    "arcane sword": "mordenkainen's sword",
    "black tentacles": "evard's black tentacles",
    "arcanist's magic aura": "nystul's magic aura",
    "faithful hound": "mordenkainen's faithful hound",
    "floating disk": "tenser's floating disk",
    "freezing sphere": "otiluke's freezing sphere",
    "resilient sphere": "otiluke's resilient sphere",
    "hideous laughter": "tasha's hideous laughter",
    "hunter's mark": "hunter's mark",
    "instant summons": "drawmij's instant summons",
    "irresistible dance": "otto's irresistible dance",
    "magnificent mansion": "mordenkainen's magnificent mansion",
    "private sanctum": "mordenkainen's private sanctum",
    "secret chest": "leomund's secret chest",
    "telepathic bond": "rary's telepathic bond",
    "tiny hut": "leomund's tiny hut",
}

# 5.2.1-only spells without an entry in czary-tlumaczenie.md
NEW_SPELL_PL = {
    "animate objects": "Animowanie obiektów",
    "befuddlement": "Zamroczenie",
    "charm monster": "Zauroczenie potwora",
    "divine smite": "Boskie ugodzenie",
    "dragon's breath": "Oddech smoka",
    "elementalism": "Żywiołomagia",
    "ice knife": "Lodowy nóż",
    "mind spike": "Kolce umysłu",
    "shining smite": "Lśniące ugodzenie",
    "sorcerous burst": "Czarodziejski wybuch",
    "starry wisp": "Gwiezdna iskra",
    "summon dragon": "Przywołanie smoka",
    "vitriolic sphere": "Kwasowa sfera",
}

EXTRA_REPLACEMENTS = {
    "Magiczne Oko": "Magiczne oko",
    "Magiczny Pocisk": "Magiczny pocisk",
    "Magicznego Pocisku": "Magicznego pocisku",
    "Wskrzeszenie umarłych": "Wskrzeszenie",
    "Wskrzeszanie Umarłych": "Wskrzeszenie",
    "Rozproszenie Magii": "Rozproszenie magii",
    "Pola Antymagicznego": "Pola antymagii",
}


def norm(s: str) -> str:
    s = s.lower()
    for ch in "'\u2019\u2018\u02bc\u0060\u00b4\u2032":
        s = s.replace(ch, "'")
    return s.replace("ĳ", "ij").replace("Ĳ", "ij")


def load_reference() -> dict[str, str]:
    ref: dict[str, str] = {}
    for line in REF_PATH.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\| (.+?) \| (.+?) \|", line)
        if match and match.group(1) not in ("Angielska nazwa", "---"):
            en, pl = match.group(1).strip(), match.group(2).strip()
            ref[norm(en)] = pl
    return ref


def expected_pl(en_name: str, ref: dict[str, str]) -> str | None:
    key = norm(en_name)
    if key in ref:
        return ref[key]
    if key in RENAME_MAP:
        renamed = RENAME_MAP[key]
        if renamed and norm(renamed) in ref:
            return ref[norm(renamed)]
    if key in NEW_SPELL_PL:
        return NEW_SPELL_PL[key]
    return None


def extract_headers(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    marker = "## Opisy czarów" if "Opisy czarów" in text else "## Spell Descriptions"
    section = text.split(marker, 1)[1]
    return [
        match.group(1).strip()
        for line in section.splitlines()
        if (match := re.match(r"^#### (.+)$", line))
    ]


def build_mappings(ref: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    en_headers = extract_headers(EN_SPELLS)
    pl_headers = extract_headers(PL_SPELLS)

    en_to_pl: dict[str, str] = {}
    pl_to_pl: dict[str, str] = {}

    for en, pl in zip(en_headers, pl_headers):
        if en in SKIP_HEADERS:
            continue
        correct = expected_pl(en, ref)
        if not correct:
            continue
        en_to_pl[en] = correct
        if norm(pl) != norm(correct):
            pl_to_pl[pl] = correct

    pl_to_pl.update(EXTRA_REPLACEMENTS)
    return en_to_pl, pl_to_pl


def fix_spell_headers(ref: dict[str, str]) -> int:
    text = PL_SPELLS.read_text(encoding="utf-8")
    marker = "## Opisy czarów"
    before, section = text.split(marker, 1)
    lines = section.splitlines()

    en_headers = extract_headers(EN_SPELLS)
    pl_headers = extract_headers(PL_SPELLS)
    header_map = dict(zip(pl_headers, en_headers))

    changes = 0
    new_lines: list[str] = []
    for line in lines:
        match = re.match(r"^(#### )(.+)$", line)
        if match:
            current = match.group(2).strip()
            en = header_map.get(current)
            if en and en not in SKIP_HEADERS:
                correct = expected_pl(en, ref)
                if correct and current != correct:
                    line = f"{match.group(1)}{correct}"
                    changes += 1
        new_lines.append(line)

    PL_SPELLS.write_text(before + marker + "\n".join(new_lines), encoding="utf-8")
    return changes


def apply_replacements(en_to_pl: dict[str, str], pl_to_pl: dict[str, str]) -> dict[str, int]:
    replacements: list[tuple[str, str]] = []

    for wrong, right in pl_to_pl.items():
        replacements.append((f"_{wrong}_", f"_{right}_"))
        replacements.append((f"**{wrong}**", f"**{right}**"))
        replacements.append((f"<td>{wrong}</td>", f"<td>{right}</td>"))

    for en, pl in en_to_pl.items():
        replacements.append((f"_{en}_", f"_{pl}_"))
        replacements.append((f"**{en}**", f"**{pl}**"))

    replacements.sort(key=lambda item: len(item[0]), reverse=True)

    stats: dict[str, int] = {}
    for path in sorted(PL_DIR.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated = original
        file_changes = 0
        for old, new in replacements:
            if old in updated:
                count = updated.count(old)
                updated = updated.replace(old, new)
                file_changes += count
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            stats[path.name] = file_changes
    return stats


def main() -> None:
    ref = load_reference()
    en_to_pl, pl_to_pl = build_mappings(ref)
    header_changes = fix_spell_headers(ref)
    file_stats = apply_replacements(en_to_pl, pl_to_pl)

    print(f"Spell headers fixed: {header_changes}")
    print(f"PL name corrections mapped: {len(pl_to_pl)}")
    print(f"EN->PL mappings: {len(en_to_pl)}")
    for name, count in sorted(file_stats.items()):
        print(f"  {name}: {count} replacements")


if __name__ == "__main__":
    main()
