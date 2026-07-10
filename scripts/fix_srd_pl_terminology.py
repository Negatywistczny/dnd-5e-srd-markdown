#!/usr/bin/env python3
"""Fix PL terminology per docs/terminologia-tlumaczenie.md in srd-5.2.1/pl and dnd2024-wikidot-pl."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from metric_units import apply_metric_units
MG_RE = re.compile(r"\bMG\b")
PZ_RE = re.compile(r"\bPŻ\b")

# Order matters: longer / more specific patterns first.
REPLACEMENTS: list[tuple[str, str]] = [
    # Sorcerer class name
    ("Czarnoksiężnicy", "Zaklinacze"),
    ("Czarnoksiężnik", "Zaklinacz"),
    ("czarnoksiężnika", "zaklinacza"),
    ("czarnoksiężnikiem", "zaklinaczem"),
    ("czarnoksiężników", "zaklinaczy"),
    ("czarnoksiężnik", "zaklinacz"),
    ("czarnoksięstwa", "zaklinania"),
    ("Jako zaklinacza zyskujesz", "Jako zaklinacz zyskujesz"),
    # Proficiency bonus
    ("Premia od Biegłości", "Premia z biegłości"),
    ("premia od biegłości", "premia z biegłości"),
    ("Premii do biegłości", "Premii z biegłości"),
    ("premii do biegłości", "premii z biegłości"),
    ("Premie do biegłości", "Premie z biegłości"),
    ("premie do biegłości", "premie z biegłości"),
    ("Premia do biegłości", "Premia z biegłości"),
    ("premia do biegłości", "premia z biegłości"),
    ("premię do biegłości", "premię z biegłości"),
    ("twojej premii do biegłości", "twojej premii z biegłości"),
    ("twoją premię do biegłości", "twoją premię z biegłości"),
    ("PdB | Premia do biegłości", "PdB | Premia z biegłości"),
    ("premia do biegłości równa twojej premii do biegłości", "premia z biegłości równa twojej premii z biegłości"),
    ("premia do biegłości równa twojej premii z biegłości", "premia z biegłości równa twojej premii z biegłości"),
    # Spellcasting focus
    ("_Skupienie rzucania czarów._", "_Magiczny fokus._"),
    ("**Skupienie rzucania czarów.**", "**Magiczny fokus.**"),
    ("jako skupienia rzucania czarów do czarów", "jako magicznego fokusu do rzucania czarów"),
    ("Skupienie rzucające zaklęcia", "Magiczny fokus"),
    ("Skupienia Rzucania Czarów", "magicznych fokusów"),
    ("Skupień Rzucania Czarów", "magicznych fokusów"),
    ("Skupienie rzucania czarów", "Magiczny fokus"),
    ("skupienia rzucania czarów", "magicznego fokusu"),
    ("skupienie rzucania czarów", "magiczny fokus"),
    ("_Fokus rzucania czarów._", "_Magiczny fokus._"),
    ("fokusu rzucania czarów", "magicznego fokusu"),
    ("Fokusu rzucania czarów", "Magicznego fokusu"),
    ("skupienia arkanicznego", "magicznego fokusu"),
    ("fokusu arkanicznego", "magicznego fokusu"),
    ("druidzkiego fokusa", "druidycznego fetysza"),
    # Skills
    ("Persuazja", "Perswazja"),
    # Immunity
    ("Damage Niewrażliwość", "Niepodatność na obrażenia"),
    ("Elemental Niewrażliwość", "Niepodatność żywiołowa"),
    ("Niewrażliwość", "Niepodatność"),
    ("niewrażliwość", "niepodatność"),
    # Expertise
    ("Ekspertyzę", "Znawstwo"),
    ("Ekspertyza", "Znawstwo"),
    ("ekspertyzę", "znawstwo"),
    ("ekspertyza", "znawstwo"),
    # Hide action
    ("#### Ukrycie [Akcja]", "#### Ukrycie się [Akcja]"),
    ("akcji Ukryj", "akcji Ukrycia się"),
    ("Dzięki akcji Ukryj", "Dzięki akcji Ukrycia się"),
    # Cover (rules-glossary)
    (
        "Połowa osłony (premia +2 do rzutów obronnych na KP i Zręczność), Osłona Trzy czwarte (premia +5 do rzutów obronnych na KP i Zręczność) oraz Całkowita osłona",
        "osłona połowiczna (premia +2 do KP i rzutów obronnych na Zręczność), osłona w trzech czwartych (premia +5 do KP i rzutów obronnych na Zręczność) oraz osłona całkowita",
    ),
    ("akcję Ukrycie,", "akcję Ukrycia się,"),
    ("akcję Ukrycie.", "akcję Ukrycia się."),
    ("<td>Ukrycie</td>", "<td>Ukrycie się</td>"),
    ("Twoja Premia Biegłości", "Twoja premia z biegłości"),
    ("zdobywasz ją w jednej umiejętności", "zdobywasz je w jednej umiejętności"),
    ("Ekspertyzy w tym samym", "Znawstwa w tym samym"),
    # Class features (proj.)
    ("Drugie tchnienie", "Drugi oddech"),
    ("Przypływ działania", "Przypływ sił"),
    ("Dziką postać", "Dzika postać"),
    ("Dzikiej postaci", "Dzikiej postaci"),
    # Blindsight mistranslation
    ("Ślepy wzrok", "Ślepowidzenie"),
    ("ślepozmysł", "ślepowidzenie"),
    ("Ślepozmysł", "Ślepowidzenie"),
    # Tremorsense
    ("Wyczulanie", "Wyczucie drgań"),
    ("Wyczuwanie drgań", "Wyczucie drgań"),
    # Cover / obscured (PG + proj.)
    ("„Okładka”", "„Osłona”"),
    ("Całkowitą Osłonę", "osłonę całkowitą"),
    ("za Trzy Czwartą Osłoną lub Całkowitą Osłoną", "za osłoną w trzech czwartych albo za osłoną całkowitą"),
    ("będąc Mocno Zasłoniętym lub za osłoną w trzech czwartych", "w silnie przesłoniętym obszarze lub za osłoną w trzech czwartych"),
    ("Obszar Ciemności jest Mocno Zasłonięty.", "Obszar ciemności jest silnie przesłonięty."),
    ("#### Pozbawiony widoczności", "#### Silnie przesłonięty"),
    ("#### Ograniczona widoczność", "#### Lekko przesłonięty"),
    ("#### Obszary z ograniczoną widocznością", "#### Obszary przesłonięte"),
    ("**Mocno zasłonięty obszar**", "**Silnie przesłonięty obszar**"),
    ("w mocno zasłoniętym obszarze", "w silnie przesłoniętym obszarze"),
    ("mocno zasłonięty", "silnie przesłonięty"),
    ("silnie zasłonięty", "silnie przesłonięty"),
    ("Silnie zasłonięty", "Silnie przesłonięty"),
    ("Mistrz Gry", "Mistrz Podziemi"),
    ("lekko zasłonięty", "lekko przesłonięty"),
    ("„Mocno zasłonięte”", "„Silnie przesłonięty”"),
    (
        "W obszarze o **Ograniczonej widoczności**, takim jak słabe światło, miejscowa mgła lub umiarkowane zarośla, istoty mają Utrudnienie do testów Mądrości (Percepcja), które opierają się na wzroku.",
        "W **lekko przesłoniętym** obszarze, takim jak przy słabym świetle, miejscowej mgle lub umiarkowanych zaroślach, istoty mają Utrudnienie do testów Mądrości (Percepcja), które opierają się na wzroku.",
    ),
    # Dim light
    ("**Przyciemnione światło.**", "**Słabe światło.**"),
    ("Przyciemnione światło,", "Słabe światło,"),
    ("przyciemnionego światła", "słabego światła"),
    ("przyciemnionym świetle", "słabym świetle"),
    ("przyciemnione", "słabe"),
    ("Przyciemnionego światła", "Słabego światła"),
    ("przy przyciemnionym świetle", "przy słabym świetle"),
    # Magic action
    ("#### Magia [Akcja]", "#### Akcja magiczna"),
    ("akcję Magii", "Akcję magiczną"),
    ("akcji Magii", "akcji magicznej"),
    ("akcja Magii", "Akcja magiczna"),
    ("Akcję Magii", "Akcję magiczną"),
    ("aktywacji Magii", "aktywacji Akcji magicznej"),
    ("z wyjątkiem akcji Magii", "z wyjątkiem Akcji magicznej"),
    # Warlock invocations (not Eldritch Blast feature names)
    ("Nieziemskie inwokacje", "Mistyczne inwokacje"),
    ("nieziemskich inwokacji", "mistycznych inwokacji"),
    ("Mistyczne Inwokacje", "Mistyczne inwokacje"),
    ("### Opcje nieziemskich inwokacji", "### Opcje mistycznych inwokacji"),
    ("### Poziom 1: Nieziemskie inwokacje", "### Poziom 1: Mistyczne inwokacje"),
    # Passive Perception (rules prose; stat blocks keep „Pasywna Percepcja”)
    ("#### Pasywna percepcja", "#### Pasywna Mądrość (Percepcja)"),
    ("„Pasywna percepcja”", "„Pasywna Mądrość (Percepcja)”"),
    ("Percepcja Pasywna to", "Pasywna Mądrość (Percepcja) to"),
    (
        "Pasywna Percepcja stworzenia wynosi 10 plus premia do testu Mądrości (Percepcji) stworzenia.",
        "Pasywna Mądrość (Percepcja) stworzenia wynosi 10 plus modyfikator z Mądrości stworzenia, z zastosowaniem premii z biegłości i innych premii oraz kar.",
    ),
    ("ma Percepcję Pasywną 14", "ma pasywną Mądrość (Percepcja) o wartości 14"),
    ("jego percepcja pasywna", "jego pasywna Mądrość (Percepcja)"),
    ("_Pasywna percepcja._", "_Pasywna Mądrość (Percepcja)._"),
    ("twojej pasywnej percepcji", "twojej pasywnej Mądrości (Percepcja)"),
    ("Pasywna Mądrość (Percepcja) to wynik odzwierciedlający", "Pasywna Mądrość (Percepcja) to wartość odzwierciedlająca"),
    ("aby określić pasywną percepcję:", "aby określić pasywną Mądrość (Percepcja):"),
    (
        "Pasywna percepcja = 10 + modyfikator testu Mądrości (Percepcja)",
        "Pasywna Mądrość (Percepcja) = 10 + modyfikator z Mądrości + premia z biegłości (jeśli masz biegłość w Percepcji)",
    ),
    ("masz pasywną percepcję 14", "masz pasywną Mądrość (Percepcja) o wartości 14"),
    ("wynik pasywnej percepcji potwora", "pasywną Mądrość (Percepcja) potwora"),
    ("Pasywna percepcja i specjalne zmysły", "Pasywna Mądrość (Percepcja) i specjalne zmysły"),
    # Cleanup after focus replacements
    (
        "Możesz używać magicznego fokusu jako magicznego fokusu do rzucania czarów",
        "Możesz używać magicznego fokusu do rzucania czarów",
    ),
    # Crawkowanie (literówka)
    ("„Crawkowanie”", "„Czołganie się”"),
    # PW (zamiast PŻ)
    ("<td>PŻ</td>", "<td>PW</td>"),
    ("<th>PŻ</th>", "<th>PW</th>"),
    ("<th>Odzyskane PŻ</th>", "<th>Odzyskane PW</th>"),
    ("**PŻ**", "**PW**"),
    (" maksimum PŻ ", " maksimum PW "),
    (" jego PŻ ", " jego PW "),
    (" jej PŻ ", " jej PW "),
    (" twoje PŻ", " twoje PW"),
    (" odzyskujesz PŻ", " odzyskujesz PW"),
    (" otrzymuje 15 PŻ", " odzyskuje 15 PW"),
    ("mniej niż 100 PŻ", "mniej niż 100 PW"),
    ("połowie maksimum PW przyzywającego", "połowie maksimum PW przyzywającego"),
    # Fokusy (PG)
    ("Skupienie arkaniczne", "Magiczny fokus"),
    ("skupienia arkanicznego", "magicznego fokusu"),
    ("Skupienie arkaniczne (kryształ lub różdżka)", "Magiczny fokus (kryształ lub różdżka)"),
    ("Druidzki Focus", "Druidyczny fetysz"),
    ("Druidzki fetysz", "Druidyczny fetysz"),
    ("Symbol wiary", "Święty symbol"),
    ("Symbol wiary (relikwiarz)", "Święty symbol (relikwiarz)"),
    # Metadane tła / klasy (EN → PL)
    ("**Tool Proficiencies**:", "**Biegłości w narzędziach:**"),
    ("**Tool Proficiencies:**", "**Biegłości w narzędziach:**"),
    ("**Skill Proficiencies**:", "**Biegłości w umiejętnościach:**"),
    ("**Skill Proficiencies:**", "**Biegłości w umiejętnościach:**"),
    ("**Atut:** Choose one", "**Atut:** Wybierz jeden"),
    # Cantrip Upgrade (pozostałości EN)
    (
        "**Cantrip Upgrade.** The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), i 17 (4d6).",
        "**Ulepszenie sztuczki.** Obrażenia zwiększają się o 1k6, gdy osiągniesz 5. poziom (2k6), 11. poziom (3k6) i 17. poziom (4k6).",
    ),
    (
        "**Cantrip Upgrade.** The damage increases by one die when you reach levels 5 (2d8 lub 2d12), 11 (3d8 lub 3d12), i 17 (4d8 lub 4d12).",
        "**Ulepszenie sztuczki.** Obrażenia zwiększają się o jedną kość, gdy osiągniesz 5. poziom (2k8 albo 2k12), 11. poziom (3k8 albo 3k12) i 17. poziom (4k8 albo 4k12).",
    ),
    # Akcja Wykorzystaj (2024)
    ("Utilize action", "akcję Wykorzystaj"),
    ("the Utilize action", "akcję Wykorzystaj"),
    ("take the Utilize action", "wykonać akcję Wykorzystaj"),
    ("**Utilize.**", "**Wykorzystaj.**"),
    ("**Utilize:**", "**Wykorzystaj:**"),
    # Błędna odmiana typów obrażeń
    ("obrażenia od psychiczne", "obrażenia psychiczne"),
    ("obrażenia od nekrotyczne", "obrażenia nekrotyczne"),
    ("obrażenia od przeszywające", "obrażenia kłute"),
    ("obrażenia od świetliste", "obrażenia od światłości"),
    ("obrażenia od obuchowe", "obrażenia obuchowe"),
    ("obrażenia od cięte", "obrażenia cięte"),
    # Święty symbol (odmiana)
    ("symbolem wiary", "świętym symbolem"),
]

DAMAGE_TYPE_REPLACEMENTS: list[tuple[str, str]] = [
    ("<td>Przeszywające</td>", "<td>Kłute</td>"),
    ("<td>Tnące</td>", "<td>Cięte</td>"),
    ("<td>Grzmot</td>", "<td>Dźwięk</td>"),
    ("<td>Promienne</td>", "<td>Światło</td>"),
    ("<td>Błyskawica</td>", "<td>Elektryczność</td>"),
    ("<td>Trucizna</td>", "<td>Trucizny</td>"),
    ("<td>Zimno</td>", "<td>Zimna</td>"),
]

TARGETS = {
    "srd": REPO / "srd-5.2.1" / "pl",
    "wikidot": REPO / "dnd2024-wikidot-pl",
}


def apply_replacements(text: str, *, glossary: bool = False) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text = MG_RE.sub("MP", text)
    text = PZ_RE.sub("PW", text)
    if glossary:
        for old, new in DAMAGE_TYPE_REPLACEMENTS:
            text = text.replace(old, new)
    return text


def fix_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    glossary = path.name == "rules-glossary.md"
    text = apply_replacements(text, glossary=glossary)
    text = apply_metric_units(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def fix_tree(root: Path) -> int:
    changed = 0
    if not root.is_dir():
        return 0
    for path in sorted(root.rglob("*")):
        if path.suffix in {".md", ".json"} and path.is_file():
            changed += fix_file(path)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        nargs="?",
        choices=["all", "srd", "wikidot"],
        default="all",
        help="Which tree to fix (default: all)",
    )
    args = parser.parse_args()

    roots = list(TARGETS.values()) if args.target == "all" else [TARGETS[args.target]]
    total = 0
    for root in roots:
        n = fix_tree(root)
        total += n
        print(f"Updated {n} files under {root}")
    print(f"Total: {total} files")


if __name__ == "__main__":
    main()
