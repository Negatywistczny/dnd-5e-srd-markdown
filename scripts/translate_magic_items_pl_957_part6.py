#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    (
        "**Ivory Goats (Rare).** These ivory statuettes of goats are always created in sets of three. Each goat looks unique and functions differently from the others. Their properties are as follows:",
        "**Koźlęta z kości słoniowej (rzadkie).** Te kości słoniowe statuetki kóz zawsze powstają w zestawach po trzy. Każda koza wygląda inaczej i działa inaczej niż pozostałe. Ich właściwości są następujące:",
    ),
    ("_Broń (Battleaxe, Greataxe, or Halberd), rzadki (wymaga zestrojenia)_", "_Broń (topór bojowy, topór dwuręczny lub halabarda), rzadki (wymaga zestrojenia)_"),
    ("_Broń (Maul or Warhammer), legendarny (wymaga zestrojenia)_", "_Broń (młot bojowy lub młot wojenny), legendarny (wymaga zestrojenia)_"),
    ("_Zbroja (Chain Mail or Chain Shirt), rzadki_", "_Zbroja (kolczuga lub koszulka kolcza), rzadki_"),
    ("_Zbroja (Half pancerz płytowy or pancerz płytowy), bardzo rzadki_", "_Zbroja (półpancerz płytowy lub pancerz płytowy), bardzo rzadki_"),
    ("_Zbroja (Half pancerz płytowy or pancerz płytowy), legendarny (wymaga zestrojenia)_", "_Zbroja (półpancerz płytowy lub pancerz płytowy), legendarny (wymaga zestrojenia)_"),
    ("_Broń (glevia, miecz dwuręczny, miecz długi, rapier, sekmak, or miecz krótki)", "_Broń (glevia, miecz dwuręczny, miecz długi, rapier, sekmak lub miecz krótki)"),
    ("_Broń (glevia, miecz dwuręczny, miecz długi, or sekmak)", "_Broń (glevia, miecz dwuręczny, miecz długi lub sekmak)"),
    ("_Różdka, niezwykły (+1), rzadki (+2), or bardzo rzadki (+3) (wymaga zestrojenia przez rzucającego czary)_", "_Różdka, niezwykła (+1), rzadka (+2) lub bardzo rzadka (+3) (wymaga zestrojenia przez rzucającego czary)_"),
    # Ring spell table - translate spell names
    ("*Chain elektryczność* (3 charges), *Feather Fall* (0 charges), *Gust of Wind* (2 charges), *Wind Wall* (1 charge)", "*Łańcuch błyskawic* (3 ładunki), *Spowolnione opadanie* (0 ładunków), *Podmuch wiatru* (2 ładunki), *Ściana wiatru* (1 ładunek)"),
    ("*Earthquake* (5 charges), *Stone Shape* (2 charges), *Stoneskin* (3 charges), *Wall of Stone* (3 charges)", "*Trzęsienie ziemi* (5 ładunków), *Kształtowanie kamienia* (2 ładunki), *Kamienna skóra* (3 ładunki), *Ściana kamienia* (3 ładunki)"),
    ("*Burning Hands* (1 charge), *ogieńball* (2 charges), *ogień Storm* (4 charges), *Wall of ogień* (3 charges)", "*Płonące dłonie* (1 ładunek), *Kula ognia* (2 ładunki), *Burza ognia* (4 ładunki), *Ściana ognia* (3 ładunki)"),
    ("*Create or Destroy Water* (1 charge), *Ice Storm* (2 charges), *Tsunami* (5 charges), *Wall of Ice* (3 charges), *Water Walk* (2 charges)", "*Tworzenie lub niszczenie wody* (1 ładunek), *Burza lodowa* (2 ładunki), *Tsunami* (5 ładunków), *Ściana lodu* (3 ładunki), *Chodzenie po wodzie* (2 ładunki)"),
    # Mixed figurine line if any left
    ("przyjazny to you", "przyjazne tobie"),
    ("przyjazny to you and your allies", "przyjazne tobie i twoim sojusznikom"),
    ("następny świt", "następnego świtu"),
    ("a akcję", "akcję"),
    ("a akcję magiczną", "akcję magiczną"),
    ("a akcję dodatkową", "akcję dodatkową"),
    ("a akcję Użycie", "akcję Użycie"),
    ("a reakcję", "reakcję"),
]

def main():
    text = PATH.read_text(encoding="utf-8")
    applied = 0
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            applied += 1
            print(f"Replaced {count}x: {old[:50]}...")
        else:
            print(f"WARNING: not found: {old[:70]}...")
    PATH.write_text(text, encoding="utf-8")
    print(f"Applied {applied}/{len(REPLACEMENTS)} patterns")

if __name__ == "__main__":
    main()
