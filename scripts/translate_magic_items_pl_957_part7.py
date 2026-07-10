#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    # Weapon/armor type lines
    ("_Broń (Any Melee Broń), legendarny (wymaga zestrojenia)_", "_Broń (dowolna broń do walki wręcz), legendarny (wymaga zestrojenia)_"),
    ("_Broń (Any Melee Broń), rzadki (wymaga zestrojenia)_", "_Broń (dowolna broń do walki wręcz), rzadki (wymaga zestrojenia)_"),
    ("_Broń (miecz dwuręczny, miecz długi, rapier, sekmak, or miecz krótki), bardzo rzadki (wymaga zestrojenia)_", "_Broń (miecz dwuręczny, miecz długi, rapier, sekmak lub miecz krótki), bardzo rzadki (wymaga zestrojenia)_"),
    ("_Broń (glevia, miecz dwuręczny, miecz długi, rapier, sekmak, sierp, or miecz krótki), legendarny (wymaga zestrojenia)_", "_Broń (glevia, miecz dwuręczny, miecz długi, rapier, sekmak, sierp lub miecz krótki), legendarny (wymaga zestrojenia)_"),
    # Avatar stat block
    ("**KP** 20 **Initiative** +3 (13) <br>", "**KP** 20 **Inicjatywa** +3 (13) <br>"),
    # Ioun stone
    ("w odległości 1k3 stóp,", "w odległości 1k3 × 30 centymetrów,"),
    # Ring spell table - correct Polish spell names from spells.md
    ("*Łańcuch błyskawic* (3 ładunki), *Spowolnione opadanie* (0 ładunków), *Podmuch wiatru* (2 ładunki), *Ściana wiatru* (1 ładunek)",
     "*Łańcuch błyskawic* (3 ładunki), *Piórkospadanie* (0 ładunków), *Poryw wiatru* (2 ładunki), *Ściana wichru* (1 ładunek)"),
    ("*Trzęsienie ziemi* (5 ładunków), *Kształtowanie kamienia* (2 ładunki), *Kamienna skóra* (3 ładunki), *Ściana kamienia* (3 ładunki)",
     "*Trzęsienie ziemi* (5 ładunków), *Kamienny kształt* (2 ładunki), *Kamienna skóra* (3 ładunki), *Ściana kamienia* (3 ładunki)"),
    ("*Tworzenie lub niszczenie wody* (1 ładunek), *Burza lodowa* (2 ładunki), *Tsunami* (5 ładunków), *Ściana lodu* (3 ładunki), *Chodzenie po wodzie* (2 ładunki)",
     "*Stworzenie lub zniszczenie wody* (1 ładunek), *Burza lodu* (2 ładunki), *Tsunami* (5 ładunków), *Ściana lodu* (3 ładunki), *Spacer po wodzie* (2 ładunki)"),
    # Staff of Fire table
    ("<td>*Burning Hands*</td>", "<td>*Płonące dłonie*</td>"),
    ("<td>*Wall of ogień*</td>", "<td>*Ściana ognia*</td>"),
    ("<td>*ogieńball*</td>", "<td>*Kula ognia*</td>"),
    # Staff of Frost table
    ("<td>*Cone of zimno*</td>", "<td>*Stożek zimna*</td>"),
    ("<td>*Ice Storm*</td>", "<td>*Burza lodu*</td>"),
    ("<td>*Fog Cloud*</td>", "<td>*Chmura mgły*</td>"),
    ("<td>*Wall of Ice*</td>", "<td>*Ściana lodu*</td>"),
    # Staff of Healing table
    ("<td>*Cure Wounds*</td>", "<td>*Leczenie ran*</td>"),
    # Staff of Power table
    ("<td>*ogieńball* (level 5 version)</td>", "<td>*Kula ognia* (wersja 5. kręgu)</td>"),
    ("<td>*Globe of Invulnerability*</td>", "<td>*Sfera niepodatności*</td>"),
    ("<td>*Hold Monster*</td>", "<td>*Unieruchomienie potwora*</td>"),
    ("<td>*Levitate*</td>", "<td>*Lewitacja*</td>"),
    ("<td>*elektryczność Bolt* (level 5 version)</td>", "<td>*Piorun* (wersja 5. kręgu)</td>"),
    ("<td>*Magic Missile*</td>", "<td>*Magiczny pocisk*</td>"),
    ("<td>*Ray of Enfeeblement*</td>", "<td>*Promień osłabienia*</td>"),
    ("<td>*Wall of moc*</td>", "<td>*Ściana energii*</td>"),
    # Staff of Swarming Insects table
    ("<td>*Giant Insect*</td>", "<td>*Olbrzymie owady*</td>"),
    ("<td>*Insect Plague*</td>", "<td>*Plaga owadów*</td>"),
    # Staff of the Magi table
    ("<td>*Arcane Lock*</td>", "<td>*Magiczny zamek*</td>"),
    ("<td>*Conjure Elemental*</td>", "<td>*Przywołanie żywiołaka*</td>"),
    ("<td>*Detect Magic*</td>", "<td>*Wykrycie magii*</td>"),
    ("<td>*Dispel Magic*</td>", "<td>*Rozproszenie magii*</td>"),
    ("<td>*Enlarge/Reduce*</td>", "<td>*Powiększenie/Pomniejszenie*</td>"),
    ("<td>*ogieńball* (level 7 version)</td>", "<td>*Kula ognia* (wersja 7. kręgu)</td>"),
    ("<td>*Flaming Sphere*</td>", "<td>*Płomienna kula*</td>"),
    ("<td>*Invisibility*</td>", "<td>*Niewidzialność*</td>"),
    ("<td>*Knock*</td>", "<td>*Kołatka*</td>"),
    ("<td>*Light*</td>", "<td>*Światło*</td>"),
    ("<td>*elektryczność Bolt* (level 7 version)</td>", "<td>*Piorun* (wersja 7. kręgu)</td>"),
    ("<td>*Passwall*</td>", "<td>*Przejście w murze*</td>"),
    ("<td>*Plan Shift*</td>", "<td>*Sferalny przeskok*</td>"),
    ("<td>*Protection from Evil and Good*</td>", "<td>*Ochrona przed dobrem i złem*</td>"),
    ("<td>*Telekinesis*</td>", "<td>*Telekineza*</td>"),
    ("<td>*Web*</td>", "<td>*Pajęczyna*</td>"),
    # Staff of the Woodlands table
    ("<td>*Animal Friendship*</td>", "<td>*Przyjaciel zwierząt*</td>"),
    ("<td>*Awaken*</td>", "<td>*Przebudzenie*</td>"),
    ("<td>*Barkskin*</td>", "<td>*Korowa skóra*</td>"),
    ("<td>*Locate Animals or rośliny*</td>", "<td>*Odnalezienie zwierząt lub roślin*</td>"),
    ("<td>*Pass without Trace*</td>", "<td>*Przejście bez śladu*</td>"),
    ("<td>*Speak with Animals*</td>", "<td>*Rozmawianie ze zwierzętami*</td>"),
    ("<td>*Speak with rośliny*</td>", "<td>*Rozmawianie z roślinami*</td>"),
    ("<td>*Wall of Thorns*</td>", "<td>*Ściana cierni*</td>"),
    # Wands
    ("<td>*Hold Person*</td>", "<td>*Unieruchomienie osoby*</td>"),
    ("<td>*Command* (flee or grovel only)</td>", "<td>*Rozkaz* (tylko ucieczka lub padnij na ziemię)</td>"),
    ("<td>*Fear* (60-foot Cone)</td>", "<td>*Strach* (stożek 18 metrów)</td>"),
]

def main():
    text = PATH.read_text(encoding="utf-8")
    applied = 0
    for old, new in REPLACEMENTS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            applied += 1
            print(f"Replaced {count}x: {old[:55]}...")
        else:
            print(f"WARNING: not found: {old[:70]}...")
    PATH.write_text(text, encoding="utf-8")
    print(f"Applied {applied}/{len(REPLACEMENTS)} patterns")

if __name__ == "__main__":
    main()
