#!/usr/bin/env python3
"""Generate Polish dnd2024-wikidot-pl from English dnd2024-wikidot.

Uses terminology and translations from:
- DND-TLUMACZENIE (Foundry compendium)
- srd-5.2.1/pl/
- docs/czary-tlumaczenie.md
- sources/5e-SRD_v1.0.md terminology conventions
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from metric_units import feet_to_meters
from clean_wikidot_artifacts import clean_wikidot_artifacts

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "dnd2024-wikidot"
OUTPUT_DIR = REPO_ROOT / "dnd2024-wikidot-pl"
TLUMACZENIE = Path("/Users/kacper/Documents/GitHub/DND-TLUMACZENIE/lang-pl-dnd5")
COMPENDIUM_DIR = TLUMACZENIE / "lang/pl/compendium"
SRD_PL = REPO_ROOT / "srd-5.2.1/pl"
SRD_V1 = REPO_ROOT / "sources/5e-SRD_v1.0.md"

from wikidot_translate_data import (
    BACKGROUND_NAMES_EXTRA,
    BACKGROUND_NARRATIVES_EXTRA,
    CLASS_INTROS_ALL,
    EXTRA_PHRASES,
    FEAT_BODIES_EXTRA,
)

WIKIDOT_BASE = "http://dnd2024.wikidot.com/"

# --- Curated PHB 2024 background narratives (Polish) ---
BACKGROUND_NARRATIVES: dict[str, str] = {
    "acolyte": (
        "Poświęciłeś się służbie w świątyni — w mieście albo w ukrytym gaju świętym. "
        "Odprawiałeś tam obrzędy na cześć bóstwa lub panteonu. Służyłeś pod kierunkiem kapłana "
        "i studiowałeś religię. Dzięki jego nauczaniu i własnej pobożności nauczyłeś się też "
        "kanalizować odrobinę boskiej mocy w służbie miejscu kultu i ludziom, którzy się tam modlili."
    ),
    "artisan": (
        "Zacząłeś od mycia podłóg i szorowania lad w warsztacie rzemieślnika za kilka miedziaków "
        "dziennie, gdy tylko byłeś w stanie unieść wiadro. Gdy dorósłeś na ucznia, nauczyłeś się "
        "tworzyć podstawowe wyroby i przekonywać wymagających klientów. Twój fach dał ci też "
        "wyczucie detalu."
    ),
    "charlatan": (
        "Gdy skończyłeś tyle lat, by zamówić piwo, w każdej karczmie w promieniu dziesięciu mil "
        "od miejsca urodzenia miałeś swój ulubiony stołek. Wędrując od zajazdu do zajazdu, "
        "nauczyłeś się żerować na nieszczęśnikach szukających pocieszającej kłamstewka — "
        "może pozorowanej mikstury albo sfałszowanych aktów rodowych."
    ),
    "criminal": (
        "Ledwo wiązałeś koniec z końcem w ciemnych zaułkach, obcinając sakiewki albo włamując się "
        "do sklepów. Być może należałeś do małego gangu podobnie myślących złoczyńców, którzy "
        "na siebie uważali. A może byłeś samotnym wilkiem, broniącym się przed miejscową gildią "
        "złodziei i groźniejszymi przestępcami."
    ),
    "entertainer": (
        "Młodość spędziłeś, podążając za wędrownymi jarmarkami i karnawałami, wykonując dziwne "
        "zlecenia dla muzyków i akrobatów w zamian za lekcje. Być może nauczyłeś się chodzić po "
        "linie, grać na lutni w charakterystycznym stylu albo recytować poezję z nienaganną dykcją. "
        "Do dziś rozkwitasz pod brawami i tęsknisz za sceną."
    ),
    "farmer": (
        "Wychowałeś się blisko ziemi. Lata opieki nad zwierzętami i uprawy nagrodziły cię cierpliwością "
        "i dobrym zdrowiem. Masz głębokie uznanie dla obfitości natury i zdrowy respekt przed jej gniewem."
    ),
    "guard": (
        "Stopy bolą na wspomnienie niezliczonych godzin na posterunku w wieży. Wyszkolono cię, "
        "by jednym okiem patrzeć za mur — na maruderów wyłaniających się z pobliskiego lasu — "
        "a drugim wewnątrz, szukając kieszonkowców i awanturników."
    ),
    "guide": (
        "Dorastałeś na łonie natury, daleko od osiedli. Domem było każde miejsce, gdzie rozłożyłeś "
        "śpiwór. W dziczy są cuda — dziwne potwory, dziewicze lasy i strumienie, porośnięte ruinami "
        "wspaniałych sal, którymi kiedyś stąpały olbrzymy — i nauczyłeś się radzić sobie sam, "
        "gdy je odkrywałeś. Od czasu do czasu prowadziłeś przyjaznych kapłanów natury, którzy "
        "nauczyli cię podstaw kanalizowania magii dziczy."
    ),
    "hermit": (
        "Wczesne lata spędziłeś w odosobnieniu w chatce lub klasztorze daleko poza obrzeżami "
        "najbliższej osady. Towarzyszyły ci wtedy tylko leśne stworzenia i ci, którzy odwiedzali "
        "cię, by przynieść wieści ze świata i zapasy. Samotność pozwoliła ci spędzić wiele godzin "
        "nad tajemnicami stworzenia."
    ),
    "merchant": (
        "Byłeś uczniem kupca, mistrza karawany albo sklepikarza i poznałeś podstawy handlu. "
        "Dużo podróżowałeś i zarabiałeś na kupnie i sprzedaży surowców potrzebnych rzemieślnikom "
        "albo gotowych wyrobów od nich. Może przewoziłeś towary (statkiem, wozem albo karawaną) "
        "albo kupowałeś od wędrownych handlarzy i sprzedawałeś w własnym sklepie."
    ),
    "noble": (
        "Wychowałeś się w zamku, wśród bogactwa, władzy i przywilejów. Rodzina drobnej arystokracji "
        "zadbała o pierwszorzędne wykształcenie — część doceniałeś, część gardziłeś. Czas spędzony "
        "na dworze, zwłaszcza obserwując rodzinę w sprawach państwowych, nauczył cię wiele o przywództwie."
    ),
    "sage": (
        "Formacyjne lata spędziłeś, podróżując między dworami a klasztorami i wykonując różne "
        "zlecenia w zamian za dostęp do bibliotek. Wiele długich wieczorów poświęciłeś na książki "
        "i zwoje, poznając wiedzę o multiwersum — nawet podstawy magii — i twój umysł wciąż pragnie więcej."
    ),
    "sailor": (
        "Żyłeś jako żeglarz — wiatr w plecy, pokład kołyszący się pod stopami. Siedziałeś na stołkach "
        "w niezliczonych portach, stawiałeś czoła potężnym sztormom i wymieniałeś się opowieściami "
        "z istotami żyjącymi pod falami."
    ),
    "scribe": (
        "Formacyjne lata spędziłeś w skryptorium, klasztorze strzegącym wiedzy albo urzędzie państwowym, "
        "gdzie nauczyłeś się pisać czytelnie i tworzyć starannie opracowane teksty. Być może spisywałeś "
        "dokumenty urzędowe albo kopiowałeś tomy literatury. Możesz mieć talent do poezji, narracji "
        "albo prac naukowych. Przede wszystkim masz skrupulatną dbałość o szczegóły, dzięki której "
        "nie wprowadzasz błędów do kopiowanych i tworzonych dokumentów."
    ),
    "soldier": (
        "Szkolenie do wojny rozpocząłeś, gdy tylko osiągnąłeś pełnoletność, i niewiele pamiętasz "
        "z życia sprzed brania w ręce oręża. Bitwa płynie w twojej krwi. Czasem łapiesz się na tym, "
        "że mimowolnie wykonujesz podstawowe ćwiczenia bojowe. W końcu wykorzystałeś to szkolenie "
        "na polu bitwy, chroniąc krainę prowadząc wojnę."
    ),
    "wayfarer": (
        "Dorastałeś na ulicach wśród podobnie nieszczęśliwych odrzuconych — część z nich przyjaciółmi, "
        "część rywalami. Spałeś, gdzie się dało, i wykonywałeś dorywcze roboty za jedzenie. Czasem, "
        "gdy głód stawał się nie do zniesienia, uciekałeś się do kradzieży. Mimo to nigdy nie straciłeś "
        "dumy i nigdy nie porzuciłeś nadziei. Los jeszcze z tobą nie skończył."
    ),
}

BACKGROUND_NAMES: dict[str, str] = {
    "acolyte": "Akolita",
    "artisan": "Rzemieślnik",
    "charlatan": "Szarlatan",
    "criminal": "Przestępca",
    "entertainer": "Artysta",
    "farmer": "Rolnik",
    "guard": "Strażnik",
    "guide": "Przewodnik",
    "hermit": "Pustelnik",
    "merchant": "Kupiec",
    "noble": "Szlachcic",
    "sage": "Mędrzec",
    "sailor": "Marynarz",
    "scribe": "Skryba",
    "soldier": "Żołnierz",
    "wayfarer": "Wędrowiec",
    "aberrant-heir": "Dziedzic aberracji",
    "archaeologist": "Archeolog",
    "house-agent": "Agent rodu",
    "house-cannith-heir": "Dziedzic rodu Cannith",
    "house-deneith-heir": "Dziedzic rodu Deneith",
    "house-ghallanda-heir": "Dziedzic rodu Ghallanda",
    "house-jorasco-heir": "Dziedzic rodu Jorasco",
    "house-kundarak-heir": "Dziedzic rodu Kundarak",
    "house-lyrandar-heir": "Dziedzic rodu Lyrandar",
    "house-medani-heir": "Dziedzic rodu Medani",
    "house-orien-heir": "Dziedzic rodu Orien",
    "house-phiarlan-heir": "Dziedzic rodu Phiarlan",
    "house-sivis-heir": "Dziedzic rodu Sivis",
    "house-tharashk-heir": "Dziedzic rodu Tharashk",
    "house-thuranni-heir": "Dziedzic rodu Thuranni",
    "house-vadalis-heir": "Dziedzic rodu Vadalis",
    "inheritance": "Dziedzictwo",
    "initiate": "Inicjowany",
    "inquisitive": "Inkwizytor",
    "knight-of-the-crown": "Rycerz Korony",
    "knight-of-the-rose": "Rycerz Róży",
    "knight-of-the-sword": "Rycerz Miecza",
    "lorwyn-expert": "Ekspert Lorwyn",
    "mulhorandi-tomb-raider": "Łupieżca grobowców Mulhorandu",
    "phlan-refugee": "Uchodźca z Phlan",
    "planar-philosopher": "Filozof planarny",
    "ruined": "Zrujnowany",
    "shipwright": "Stoczniowiec",
    "student-of-the-sword": "Uczeń miecza",
    "volstrucker-agent": "Agent Volstrucker",
    "wildspacer": "Dziki kosmos",
    "witchlight-hand": "Służący Witchlight",
    "witherbloom-student": "Student Witherbloom",
}

CLASS_INTROS: dict[str, str] = {
    "barbarian": (
        "Barbarzyńcy to potężni wojownicy napędzani prymitywnymi siłami multiwersum, które manifestują się jako Szał. "
        "To coś więcej niż emocja — i nie ograniczone do gniewu — ten Szał jest ucieleśnieniem dzikości drapieżnika, "
        "wściekłości burzy i wzburzenia morza.\n\n"
        "Niektórzy barbarzyńcy uosabiają swój Szał jako dzikiego ducha lub czczonego przodka. Inni widzą w nim związek "
        "z bólem i cierpieniem świata, bezosobowy węzeł dzikiej magii albo wyraz najgłębszej jaźni. Dla każdego barbarzyńcy "
        "Szał to moc napędzająca nie tylko sprawność bojową, lecz także nadnaturalne refleksy i wyostrzone zmysły.\n\n"
        "Barbarzyńcy często pełnią rolę obrońców i przywódców swych społeczności. Rzucają się na niebezpieczeństwo, "
        "by ci pod ich ochroną nie musieli tego robić. Ich odwaga wobec zagrożenia czyni ich idealnymi poszukiwaczami przygód."
    ),
}

FEAT_BODIES: dict[str, str] = {
    "crafter": """Zyskujesz następujące korzyści.

**Biegłość w narzędziach.** Zyskujesz biegłość w trzech różnych narzędziach rzemieślniczych według własnego wyboru z tabeli Szybkie wytwarzanie.

**Zniżka.** Za każdym razem, gdy kupujesz niemagiczny przedmiot, otrzymujesz na niego 20% zniżki.

**Szybkie wytwarzanie.** Po zakończeniu długiego odpoczynku możesz wytworzyć jeden element ekwipunku z tabeli Szybkie wytwarzanie, o ile masz narzędzia rzemieślnicze powiązane z tym przedmiotem i biegłość w nich. Przedmiot trwa do momentu zakończenia kolejnego długiego odpoczynku, kiedy ulega rozpadowi.

#### Szybkie wytwarzanie

| Narzędzia rzemieślnicze | Wytworzony ekwipunek |
| --- | --- |
| Narzędzia cieśli | Drabina, Pochodnia |
| Narzędzia kaletnika | Futerał, Sakiewka |
| Narzędzia kamieniarza | Blok i krętka |
| Narzędzia garncarza | Dzban, Lampa |
| Narzędzia kowala | Kulki łożyskowe, Wiadro, Kolczatki, Hak wspinaczkowy, Żelazny garnek |
| Narzędzia majsterkowicza | Dzwonek, Łopata, Krzesiwo |
| Narzędzia tkacza | Kosz, Lina, Sieć, Namiot |
| Narzędzia rzeźbiarza | Maczuga, Wielka maczuga, Kij""",
}

BACKGROUND_NARRATIVES.update(BACKGROUND_NARRATIVES_EXTRA)
BACKGROUND_NAMES.update(BACKGROUND_NAMES_EXTRA)
CLASS_INTROS.update(CLASS_INTROS_ALL)
FEAT_BODIES.update(FEAT_BODIES_EXTRA)

CLASS_NAMES: dict[str, str] = {
    "artificer": "Wynalazca",
    "barbarian": "Barbarzyńca",
    "bard": "Bard",
    "cleric": "Kleryk",
    "druid": "Druid",
    "fighter": "Wojownik",
    "monk": "Mnich",
    "paladin": "Paladyn",
    "ranger": "Łowca",
    "rogue": "Łotr",
    "sorcerer": "Zaklinacz",
    "warlock": "Czarownik",
    "wizard": "Mag",
    "psion": "Psionik",
}

ABILITIES: dict[str, str] = {
    "Strength": "Siła",
    "Dexterity": "Zręczność",
    "Constitution": "Kondycja",
    "Intelligence": "Inteligencja",
    "Wisdom": "Mądrość",
    "Charisma": "Charyzma",
}

SKILLS: dict[str, str] = {
    "Acrobatics": "Akrobatyka",
    "Animal Handling": "Opieka nad zwierzętami",
    "Arcana": "Wiedza tajemna",
    "Athletics": "Atletyka",
    "Deception": "Oszustwo",
    "History": "Historia",
    "Insight": "Intuicja",
    "Investigation": "Śledztwo",
    "Intimidation": "Zastraszanie",
    "Medicine": "Medycyna",
    "Nature": "Przyroda",
    "Perception": "Percepcja",
    "Performance": "Występy",
    "Persuasion": "Perswazja",
    "Religion": "Religia",
    "Sleight of Hand": "Zwinne dłonie",
    "Stealth": "Skradanie się",
    "Survival": "Sztuka przetrwania",
}

CONDITIONS: dict[str, str] = {
    "Blinded": "oślepiony",
    "Charmed": "zauroczony",
    "Deafened": "ogłuszony",
    "Exhaustion": "wyczerpanie",
    "Frightened": "przerażony",
    "Grappled": "pochwycony",
    "Incapacitated": "obezwładniony",
    "Invisible": "niewidzialny",
    "Paralyzed": "sparaliżowany",
    "Petrified": "skamieniały",
    "Poisoned": "zatruty",
    "Prone": "powalony",
    "Restrained": "skrępowany",
    "Stunned": "ogłuszony",
    "Unconscious": "nieprzytomny",
}

DAMAGE_TYPES: dict[str, str] = {
    "Acid": "kwasu",
    "Bludgeoning": "obuchowe",
    "Cold": "zimna",
    "Fire": "ognia",
    "Force": "mocy",
    "Lightning": "elektryczności",
    "Necrotic": "nekrotyczne",
    "Piercing": "przeszywające",
    "Poison": "trucizny",
    "Psychic": "psychiczne",
    "Radiant": "świetliste",
    "Slashing": "sieczne",
    "Thunder": "grzmiące",
}

SCHOOLS: dict[str, str] = {
    "Abjuration": "Odrzucania",
    "Conjuration": "Przywoływania",
    "Divination": "Wieszczenia",
    "Enchantment": "Uroku",
    "Evocation": "Wywoływania",
    "Illusion": "Iluzji",
    "Necromancy": "Nekromancji",
    "Transmutation": "Transmutacji",
}

SOURCE_LABELS: dict[str, str] = {
    "Player's Handbook": "Podręcznik Gracza",
    "Dungeon Master's Guide": "Podręcznik Mistrza Gry",
    "Monster Manual": "Podręcznik Potworów",
    "Eberron - Forge of the Artificer": "Eberron — Kuźnia Wynalazcy",
    "Ravenloft - The Horrors Within": "Ravenloft — Horrory wewnątrz",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_compendium_names() -> dict[str, str]:
    names: dict[str, str] = {}
    if not COMPENDIUM_DIR.exists():
        return names
    for path in sorted(COMPENDIUM_DIR.glob("*.json")):
        data = load_json(path)
        entries = data.get("entries", {})
        for en_key, entry in entries.items():
            if isinstance(entry, dict) and entry.get("name"):
                names[en_key] = entry["name"]
                # slug variants
                slug = slugify(en_key)
                names[slug] = entry["name"]
    names.update(BACKGROUND_NAMES)
    names.update(CLASS_NAMES)
    return names


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_spell_name_map(names: dict[str, str]) -> dict[str, str]:
    mapping: dict[str, str] = dict(names)
    czary = REPO_ROOT / "docs/czary-tlumaczenie.md"
    if czary.exists():
        for line in czary.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\| (.+?) \| (.+?) \|", line)
            if m and m.group(1) != "Angielska nazwa":
                mapping[m.group(1).strip()] = m.group(2).strip()
    spells24 = COMPENDIUM_DIR / "dnd5e.spells24.json"
    if spells24.exists():
        for en, entry in load_json(spells24).get("entries", {}).items():
            if entry.get("name"):
                mapping[en] = entry["name"]
    return mapping


def parse_markdown_sections(text: str, header_prefix: str) -> dict[str, str]:
    """Parse #### or ### sections keyed by title."""
    sections: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    pattern = re.compile(rf"^{re.escape(header_prefix)} (.+)$")
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def parse_pl_spells() -> dict[str, str]:
  text = (SRD_PL / "spells.md").read_text(encoding="utf-8")
  return parse_markdown_sections(text, "####")


def parse_pl_magic_items() -> dict[str, str]:
  text = (SRD_PL / "magic-items.md").read_text(encoding="utf-8")
  return parse_markdown_sections(text, "####")


def parse_pl_feats() -> dict[str, str]:
  text = (SRD_PL / "feats.md").read_text(encoding="utf-8")
  return parse_markdown_sections(text, "####")


def parse_pl_classes() -> dict[str, str]:
  text = (SRD_PL / "classes.md").read_text(encoding="utf-8")
  sections: dict[str, str] = {}
  current: str | None = None
  buf: list[str] = []
  for line in text.splitlines():
    if line.startswith("## "):
      if current:
        sections[current] = "\n".join(buf).strip()
      current = line[3:].strip()
      buf = []
    elif current is not None:
      buf.append(line)
  if current:
    sections[current] = "\n".join(buf).strip()
  return sections


def parse_pl_origins() -> dict[str, str]:
  text = (SRD_PL / "character-origins.md").read_text(encoding="utf-8")
  return parse_markdown_sections(text, "####")


def build_path_map(manifest: dict) -> dict[str, tuple[str, str]]:
  """wikidot path -> (section_dir, slug)"""
  path_map: dict[str, tuple[str, str]] = {}
  for section, items in manifest.get("sections", {}).items():
    for item in items:
      path_map[item["path"]] = (section, item["slug"])
      path_map[item["url"]] = (section, item["slug"])
      path_map[f"{WIKIDOT_BASE}{item['path']}"] = (section, item["slug"])
  return path_map


def relative_link(from_section: str, from_slug: str, to_section: str, to_slug: str) -> str:
  if from_section == to_section:
    return f"{to_slug}.md"
  return f"../{to_section}/{to_slug}.md"


def rewrite_links(text: str, from_section: str, from_slug: str, path_map: dict, names: dict[str, str]) -> str:
  def repl_wikidot(m: re.Match) -> str:
    label = m.group(1)
    url = m.group(2)
    path = url.replace(WIKIDOT_BASE, "")
    if path not in path_map:
      return m.group(0)
    to_section, to_slug = path_map[path]
    rel = relative_link(from_section, from_slug, to_section, to_slug)
    return f"[{label}]({rel})"

  text = re.sub(r"\[([^\]]+)\]\(" + re.escape(WIKIDOT_BASE) + r"([^)]+)\)", repl_wikidot, text)

  def repl_anchor(m: re.Match) -> str:
    label = m.group(1)
    anchor = m.group(2)
    return f"[{translate_phrase(label, names)}](#{anchor})"

  text = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", repl_anchor, text)
  return text


def apply_replacement(text: str, old: str, new: str) -> str:
  if not old:
    return text
  if " " in old:
    return text.replace(old, new)
  # Short tokens often appear inside plurals (Pouches, Bottles).
  if len(old) <= 6:
    return re.sub(rf"(?<![A-Za-zÀ-ž]){re.escape(old)}(?![A-Za-zÀ-ž])", new, text)
  return text.replace(old, new)


def build_phrase_replacements(names: dict[str, str]) -> list[tuple[str, str]]:
  phrases: list[tuple[str, str]] = [
    ("**Source URL:**", "**URL źródła:**"),
    ("Source:", "Źródło:"),
    ("**Class:**", "**Klasa:**"),
    ("**Ability Scores:**", "**Wartości cech:**"),
    ("**Feat:**", "**Atut:**"),
    ("**Skill Proficiencies:**", "**Biegłości w umiejętnościach:**"),
    ("**Tool Proficiency:**", "**Biegłość w narzędziach:**"),
    ("**Equipment:**", "**Wyposażenie:**"),
    ("Choose A or B:", "Wybierz A lub B:"),
    ("Choose one kind of", "Wybierz jeden rodzaj"),
    ("Casting Time:", "Czas rzucania:"),
    ("Range:", "Zasięg:"),
    ("Components:", "Komponenty:"),
    ("Duration:", "Czas trwania:"),
    ("Action", "Akcja"),
    ("Bonus Action", "Akcja dodatkowa"),
    ("Reaction", "Reakcja"),
    ("Instantaneous", "Natychmiastowy"),
    ("Long Rest", "Długi odpoczynek"),
    ("Short Rest", "Krótki odpoczynek"),
    ("Proficiency Bonus", "Premia z biegłości"),
    ("Hit Point Die", "Kość wytrzymałości"),
    ("Hit Points", "Punkty wytrzymałości"),
    ("Saving Throw", "Rzut obronny"),
    ("saving throw", "rzut obronny"),
    ("Ability Score Improvement", "Zwiększenie wartości cechy"),
    ("Weapon Mastery", "Mistrzostwo broni"),
    ("Primary Ability", "Cecha podstawowa"),
    ("Armor Training", "Wyszkolenie w pancerzach"),
    ("Starting Equipment", "Wyposażenie startowe"),
    ("Skill Proficiencies", "Biegłości w umiejętnościach"),
    ("Weapon Proficiencies", "Biegłości w broniach"),
    ("Saving Throw Proficiencies", "Biegłości w rzutach obronnych"),
    ("Tool Proficiency", "Biegłość w narzędziach"),
    ("You gain the following benefits.", "Zyskujesz następujące korzyści."),
    ("Using a Higher-Level Spell Slot.", "Użycie komórki czaru wyższego kręgu."),
    ("Level ", "Poziom "),
    ("Unarmed Strike", "Uderzenie bez broni"),
    ("Critical Hit", "Trafienie krytyczne"),
    ("Immunity", "Niewrażliwość"),
    ("the Charmed", "stan zauroczony"),
    ("the Frightened", "stan przerażony"),
    ("Charmed", "zauroczony"),
    ("Frightened", "przerażony"),
    ("GP", "sz"),
    ("Rage Damage", "Obrażenia z szału"),
    ("Rages", "Szały"),
    ("Rage", "Szał"),
    ("Martial weapons", "broń bojowa"),
    ("Martial weapon", "broń bojowa"),
    ("Simple weapons", "broń prosta"),
    ("Shields", "Tarcze"),
    ("Sphere", "sfera"),
    ("Emanation", "emanacja"),
    ("Cone", "stożek"),
    ("Cube", "sześcian"),
    ("Cylinder", "walec"),
    ("Line", "linia"),
  ]
  for en, pl in ABILITIES.items():
    phrases.append((en, pl))
  for en, pl in SKILLS.items():
    phrases.append((en, pl))
  for en, pl in CONDITIONS.items():
    phrases.append((f"the {en} condition", f"stan {pl}"))
    phrases.append((f"{en} condition", f"stan {pl}"))
    phrases.append((en, pl))
  for en, pl in DAMAGE_TYPES.items():
    phrases.append((f"{en} damage", f"obrażenia od {pl}"))
    phrases.append((f"{en} Damage", f"Obrażenia od {pl}"))
  for en, pl in SCHOOLS.items():
    phrases.append((en, pl))
  for en, pl in SOURCE_LABELS.items():
    phrases.append((en, pl))
  phrases.extend(EXTRA_PHRASES)
  phrases.append((" and ", " i "))
  phrases.append((" or ", " lub "))
  phrases.append(("Calligrapher's Supplies", "Przybory kaligraficzne"))
  phrases.append(("Calligrapher's Supplies", "Przybory kaligraficzne"))
  phrases.append(("Artisan's Tools", "Narzędzia rzemieślnicze"))
  phrases.append(("Holy Symbol", "Święty symbol"))
  phrases.append(("Traveler's Clothes", "Ubranie podróżne"))
  phrases.append(("Traveler’s Clothes", "Ubranie podróżne"))
  phrases.append(("Book (prayers)", "Księga (modlitwy)"))
  phrases.append(("Parchment (10 sheets)", "Pergamin (10 arkuszy)"))
  phrases.append(("Robe", "Szata"))
  phrases.append(("Robes", "Szaty"))
  # compendium multi-word names only (avoid breaking English words)
  for en, pl in sorted(names.items(), key=lambda x: len(x[0]), reverse=True):
    if " " in en and len(en) > 4:
      phrases.append((en, pl))
  # dedupe preserving longest
  seen: set[str] = set()
  unique: list[tuple[str, str]] = []
  for old, new in sorted(phrases, key=lambda x: len(x[0]), reverse=True):
    if old not in seen:
      seen.add(old)
      unique.append((old, new))
  return unique


def translate_phrase(text: str, names: dict[str, str]) -> str:
  text = text.replace("\u2019", "'").replace("'", "'").replace("'", "'")
  protected: dict[str, str] = {}

  def protect(match: re.Match) -> str:
    key = f"@@P{len(protected)}@@"
    protected[key] = match.group(0)
    return key

  text = re.sub(r"https?://\S+", protect, text)
  for old, new in PHRASES:
    text = apply_replacement(text, old, new)
  for en, pl in CLASS_NAMES.items():
    for variant in (en.title(), en.capitalize(), en):
      text = apply_replacement(text, variant, pl)
  for en, pl in sorted(names.items(), key=lambda x: len(x[0]), reverse=True):
    if " " not in en and 3 < len(en) <= 24 and en[0].isupper():
      text = apply_replacement(text, en, pl)
  for key, value in protected.items():
    text = text.replace(key, value)
  return text


def html_to_markdown(html_text: str) -> str:
  text = html_text
  text = re.sub(r"<br\s*/?>", "\n", text)
  text = re.sub(r"</p>", "\n\n", text)
  text = re.sub(r"<p[^>]*>", "", text)
  text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.S)
  text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.S)
  text = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda m: f"{'#' * int(m.group(1))} {unescape(m.group(2))}\n\n", text, flags=re.S)
  text = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", text, flags=re.S)
  text = re.sub(r"<tr[^>]*>(.*?)</tr>", lambda m: "| " + " | ".join(
    re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<t[hd][^>]*>.*?</t[hd]>", m.group(1), re.S)
  ) + " |", text, flags=re.S)
  text = re.sub(r"<[^>]+>", "", text)
  text = unescape(text)
  text = re.sub(r"\n{3,}", "\n\n", text)
  return text.strip()


def convert_srd_spell_to_wiki(pl_block: str, en_title: str, pl_title: str) -> str:
  """Convert SRD PL spell block to wikidot-style markdown."""
  lines = pl_block.splitlines()
  meta_line = next((l for l in lines if l.startswith("_") and l.endswith("_")), "")
  # _3. krąg, Wywoływania (Czarownik, Mag)_
  m = re.match(r"_(\d+)\. krąg, (.+?) \((.+?)\)_", meta_line)
  if m:
    level, school, classes = m.group(1), m.group(2), m.group(3)
    header = f"*Poziom {level}, {school} ({classes})*"
  else:
    header = meta_line.strip("_")

  out = [header]
  for line in lines:
    if line.startswith("**Czas rzucania:**"):
      out.append(line)
    elif line.startswith("**Zasięg:**"):
      out.append(line)
    elif line.startswith("**Komponenty:**"):
      out.append(line)
    elif line.startswith("**Czas trwania:**"):
      out.append(line)
  out.append("")
  body_lines = []
  for line in lines:
    if line.startswith("**") or line.startswith("_") or not line.strip():
      continue
    body_lines.append(line)
  out.append("\n".join(body_lines).strip())
  for line in lines:
    if line.startswith("_Użycie"):
      out.append("")
      inner = line.strip().strip("_").replace("._ ", ". ")
      title, _, rest = inner.partition(".")
      out.append(f"**{title}.**{rest}")
  return "\n".join(out)


def compendium_description_to_markdown(html_text: str) -> str:
  text = re.sub(r"<section[^>]*class=\"secret\"[^>]*>.*?</section>", "", html_text, flags=re.S)
  text = re.sub(r"@UUID\[[^\]]+\]\{([^}]+)\}", r"\1", text)
  text = re.sub(r"&amp;Reference\[[^\]]+\](?:\{([^}]+)\})?", lambda m: m.group(1) or "", text)
  text = re.sub(r"<br\s*/?>", "\n", text)
  text = re.sub(r"</p>", "\n\n", text)
  text = re.sub(r"<p[^>]*>", "", text)
  text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.S)
  text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.S)
  text = re.sub(r"<[^>]+>", "", text)
  text = unescape(text)
  text = re.sub(r"\n{3,}", "\n\n", text).strip()
  return text


def load_compendium_feat_bodies() -> dict[str, str]:
  path = COMPENDIUM_DIR / "dnd5e.feats24.json"
  if not path.exists():
    return {}
  bodies: dict[str, str] = {}
  for en_key, entry in load_json(path).get("entries", {}).items():
    desc = entry.get("description")
    if not desc:
      continue
    body = compendium_description_to_markdown(desc)
    if body:
      bodies[slugify(en_key)] = body
  return bodies


def translate_background(slug: str, body: str, names: dict[str, str]) -> str:
  lines = [line for line in body.splitlines() if line.strip() and not line.startswith("Source:")]
  field_lines: list[str] = []
  narrative_lines: list[str] = []
  for line in lines:
    if line.startswith("**") or re.match(r"^Feat:?", line):
      if re.match(r"^Feat:?", line):
        line = re.sub(r"^Feat:\s*", "**Atut:** ", line)
      field_lines.append(line)
    else:
      narrative_lines.append(line)

  out: list[str] = []
  if slug in BACKGROUND_NARRATIVES:
    out.append(BACKGROUND_NARRATIVES[slug])
  elif narrative_lines:
    out.append(translate_phrase(feet_to_meters("\n".join(narrative_lines)), names))

  if out:
    out.append("")
  for line in field_lines:
    out.append(translate_phrase(feet_to_meters(line), names))
  return "\n".join(out).strip()


def translate_spell(title: str, body: str, spell_names: dict[str, str], pl_spells: dict[str, str]) -> str:
  pl_title = spell_names.get(title, title)
  if pl_title in pl_spells:
    return convert_srd_spell_to_wiki(pl_spells[pl_title], title, pl_title)
  return translate_phrase(feet_to_meters(body), spell_names)


def translate_magic_item(title: str, body: str, names: dict[str, str], pl_items: dict[str, str]) -> str:
  pl_title = names.get(title, title)
  for candidate in (pl_title, title):
    if candidate in pl_items:
      block = pl_items[candidate]
      # strip #### header if present in block usage
      return translate_phrase(feet_to_meters(block), names)
  return translate_phrase(feet_to_meters(body), names)


def extract_subclass_from_srd(pl_title: str, pl_classes: dict[str, str]) -> str | None:
  needle = pl_title.casefold()
  for section_text in pl_classes.values():
    for m in re.finditer(
      r"(### Podklasa[^\n]+\n+(?:_[^\n]+_\n+)?)([\s\S]*?)(?=\n### Podklasa|\n## |\Z)",
      section_text,
    ):
      header = m.group(1)
      if needle in header.casefold():
        return (header + m.group(2)).strip()
  return None


def translate_subclass(title: str, body: str, names: dict[str, str], pl_classes: dict[str, str]) -> str:
  pl_title = names.get(title, title)
  srd_block = extract_subclass_from_srd(pl_title, pl_classes)
  if srd_block:
    return srd_block
  return translate_phrase(feet_to_meters(body), names)


def translate_class(slug: str, body: str, names: dict[str, str]) -> str:
  intro = CLASS_INTROS.get(slug)
  if intro:
    lines = body.splitlines()
    rest_start = 0
    for i, line in enumerate(lines):
      if line.startswith("|") or line.startswith("#"):
        rest_start = i
        break
    tail = "\n".join(lines[rest_start:]) if rest_start else ""
    translated_tail = translate_phrase(feet_to_meters(tail), names)
    return intro + "\n\n" + translated_tail
  return translate_phrase(feet_to_meters(body), names)


def split_front_matter(content: str) -> tuple[str, str]:
  parts = content.split("\n---\n", 1)
  if len(parts) == 2:
    return parts[0], parts[1]
  return "", content


def translate_file(
  section: str,
  slug: str,
  title: str,
  content: str,
  path_map: dict,
  names: dict[str, str],
  spell_names: dict[str, str],
  pl_spells: dict[str, str],
  pl_items: dict[str, str],
  pl_feats: dict[str, str],
  pl_classes: dict[str, str],
  pl_origins: dict[str, str],
) -> str:
  front, body = split_front_matter(content)
  pl_title = names.get(title, BACKGROUND_NAMES.get(slug, title))
  if section == "backgrounds":
    pl_title = BACKGROUND_NAMES.get(slug, names.get(title, title))
  elif section == "classes":
    pl_title = CLASS_NAMES.get(slug, names.get(title, title))
  elif section == "feats":
    pl_title = translate_phrase(names.get(title, title), names)

  # translate front matter lines
  fm_lines = []
  for line in front.splitlines():
    if line.startswith("# "):
      fm_lines.append(f"# {pl_title}")
    elif line.startswith("**Source URL:**"):
      fm_lines.append(line.replace("**Source URL:**", "**URL źródła:**"))
    elif line.startswith("**Class:**"):
      cls = re.sub(r"^\*\*Class:\*\*\s*", "", line).strip()
      fm_lines.append(f"**Klasa:** {CLASS_NAMES.get(cls, cls)}")
    elif line.startswith("**Source:**"):
      src = re.sub(r"^\*\*Source:\*\*\s*", "", line).strip()
      fm_lines.append(f"**Źródło:** {translate_phrase(src, names)}")
    elif "http://" in line or "https://" in line:
      fm_lines.append(line.replace("**Source URL:**", "**URL źródła:**"))
    else:
      fm_lines.append(translate_phrase(line, names))
  front_pl = "\n".join(fm_lines)

  body_src = body.strip()
  if body_src.startswith("Source:"):
    body_content = body_src.split("\n", 1)
    source_line = translate_phrase(body_content[0], names)
    main_body = body_content[1] if len(body_content) > 1 else ""
  else:
    source_line = ""
    main_body = body_src

  if section == "backgrounds":
    translated_body = translate_background(slug, main_body.strip(), names)
  elif section == "spells":
    translated_body = translate_spell(title, main_body.strip(), spell_names, pl_spells)
  elif section == "magic-items":
    translated_body = translate_magic_item(title, main_body.strip(), names, pl_items)
  elif section == "feats":
    if slug in FEAT_BODIES:
      translated_body = FEAT_BODIES[slug]
    else:
      pl_feat = names.get(title, title)
      if pl_feat in pl_feats:
        translated_body = translate_phrase(feet_to_meters(pl_feats[pl_feat]), names)
      else:
        translated_body = translate_phrase(feet_to_meters(main_body.strip()), names)
  elif section == "subclasses":
    translated_body = translate_subclass(title, main_body.strip(), names, pl_classes)
  elif section == "species" and pl_title in pl_origins:
    translated_body = pl_origins[pl_title]
  elif section == "classes":
    translated_body = translate_class(slug, main_body.strip(), names)
  else:
    translated_body = translate_phrase(feet_to_meters(main_body.strip()), names)

  if source_line:
    result_body = source_line + "\n\n" + translated_body.strip()
  else:
    result_body = translated_body.strip()

  result = front_pl + "\n\n---\n\n" + result_body + "\n"
  result = rewrite_links(result, section, slug, path_map, names)
  return clean_wikidot_artifacts(result)


def translate_manifest(manifest: dict, names: dict[str, str]) -> dict:
  out = dict(manifest)
  out["source"] = manifest["source"]
  out["language"] = "pl"
  out["translated_from"] = str(SOURCE_DIR.name)
  new_sections = {}
  for section, items in manifest.get("sections", {}).items():
    new_items = []
    for item in items:
      new_item = dict(item)
      title = item["title"]
      slug = item["slug"]
      if section == "backgrounds":
        new_item["title"] = BACKGROUND_NAMES.get(slug, names.get(title, title))
      elif section == "classes":
        new_item["title"] = CLASS_NAMES.get(slug, names.get(title, title))
      else:
        new_item["title"] = translate_phrase(names.get(title, title), names) if section == "feats" else names.get(title, title)
      new_items.append(new_item)
    new_sections[section] = new_items
  out["sections"] = new_sections
  return out


PHRASES: list[tuple[str, str]] = []


def main() -> None:
  global PHRASES
  print("Ładowanie słowników...")
  names = load_compendium_names()
  spell_names = load_spell_name_map(names)
  PHRASES = build_phrase_replacements(names)

  manifest = load_json(SOURCE_DIR / "manifest.json")
  path_map = build_path_map(manifest)

  pl_spells = parse_pl_spells()
  pl_items = parse_pl_magic_items()
  pl_feats = parse_pl_feats()
  pl_classes = parse_pl_classes()
  pl_origins = parse_pl_origins()
  compendium_feats = load_compendium_feat_bodies()
  FEAT_BODIES.update({k: v for k, v in compendium_feats.items() if k not in FEAT_BODIES})

  if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
  OUTPUT_DIR.mkdir(parents=True)

  title_index = {}
  for section, items in manifest["sections"].items():
    for item in items:
      title_index[(section, item["slug"])] = item["title"]

  md_files = list(SOURCE_DIR.rglob("*.md"))
  print(f"Tłumaczenie {len(md_files)} plików...")
  for src in md_files:
    rel = src.relative_to(SOURCE_DIR)
    section = rel.parts[0] if len(rel.parts) > 1 else rel.stem
    slug = src.stem
    title = title_index.get((section, slug), src.stem.replace("-", " ").title())

    content = src.read_text(encoding="utf-8")
    translated = translate_file(
      section, slug, title, content, path_map, names, spell_names,
      pl_spells, pl_items, pl_feats, pl_classes, pl_origins,
    )
    dest = OUTPUT_DIR / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(translated, encoding="utf-8")

  pl_manifest = translate_manifest(manifest, names)
  (OUTPUT_DIR / "manifest.json").write_text(
    json.dumps(pl_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
  )
  print(f"Zapisano do {OUTPUT_DIR}")


if __name__ == "__main__":
  main()
