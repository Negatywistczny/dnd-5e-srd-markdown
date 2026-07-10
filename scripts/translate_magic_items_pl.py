#!/usr/bin/env python3
"""Apply Polish translations to remaining English fragments in magic-items.md"""
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

# Order matters for overlapping strings — longer/more specific first
REPLACEMENTS = [
    # Amulet obieżysfera table
    ("<td>Random location on the plane you named</td>",
     "<td>Losowe miejsce w sferze egzystencji, którą wymieniłeś</td>"),
    ("<td>Random location on an Inner Plan determined by rolling 1k6: on a 1, the Plan of Air; on a 2, the Plan of Earth; on a 3, the Plan of ogień; on a 4, the Plan of Water; on a 5, the wróżkiwild; on a 6, the Shadowfell</td>",
     "<td>Losowe miejsce w sferze wewnętrznej określone rzutem 1k6: przy 1 — Sfera Powietrza; przy 2 — Sfera Ziemi; przy 3 — Sfera Ognia; przy 4 — Sfera Wody; przy 5 — Dziki kraj wróżek; przy 6 — Cieniomróz</td>"),
    ("<td>Random location on an Outer Plan determined by rolling 1k8: on a 1, Arborea; on a 2, Arcadia; on a 3, the Beastlands; on a 4, Bytopia; on a 5, Elysium; on a 6, Mechanus; on a 7, Mount Celestia; on an 8, Ysgard</td>",
     "<td>Losowe miejsce w sferze zewnętrznej określone rzutem 1k8: przy 1 — Arborea; przy 2 — Arkadia; przy 3 — Kraina Bestii; przy 4 — Bytopia; przy 5 — Elysium; przy 6 — Mechanus; przy 7 — Góra Celestii; przy 8 — Ysgard</td>"),
    ("<td>Random location on an Outer Plan determined by rolling 1k8: on a 1, the Abyss; on a 2, Acheron; on a 3, Carceri; on a 4, Gehenna; on a 5, Hades; on a 6, Limbo; on a 7, the Nine Hells; on an 8, Pandemonium</td>",
     "<td>Losowe miejsce w sferze zewnętrznej określone rzutem 1k8: przy 1 — Otchłań; przy 2 — Acheron; przy 3 — Carceri; przy 4 — Gehenna; przy 5 — Hades; przy 6 — Limbo; przy 7 — Dziewięć Piekieł; przy 8 — Pandemonium</td>"),
    ("<td>Random location on the Astral Plan</td>",
     "<td>Losowe miejsce w Sferze Astralnej</td>"),
    # Amfibionator duplicate EN table
    ("<td>Legs extend, allowing the apparatus to walk and swim.</td>",
     "<td>Nogi i ogon wysuwają się, umożliwiając urządzeniu chodzenie i pływanie.</td>"),
    ("<td>Legs retract, reducing the apparatus's Speed and Swim Speed to 0 and making it unable to benefit from bonuses to speed.</td>",
     "<td>Nogi i ogon chowają się, sprowadzając szybkość urządzenia do 0 i uniemożliwiając mu korzystanie z premii do szybkości.</td>"),
    ("<td>Forward window shutter opens.</td>",
     "<td>Otwiera się osłona przedniego okna.</td>"),
    ("<td>Forward window shutter closes.</td>",
     "<td>Zamyka się osłona przedniego okna.</td>"),
    ("<td>Side window shutters open (two per side).</td>",
     "<td>Otwierają się osłony bocznych okien (dwie z każdej strony).</td>"),
    ("<td>Side window shutters close (two per side).</td>",
     "<td>Zamykają się osłony bocznych okien (dwie z każdej strony).</td>"),
    ("<td>Two claws extend from the front side of the apparatus.</td>",
     "<td>Z przednich boków urządzenia wysuwają się dwie pary szczypiec.</td>"),
    ("<td>The claws retract.</td>",
     "<td>Szczypce chowają się.</td>"),
    ("<td>Each extended claw makes the following melee attack: +8 to hit, reach 5 ft. Hit: 7 (2d6) obuchowe damage.</td>",
     "<td>Każde wysunięte szczypce wykonują następujący atak bronią wręcz: +8 do trafienia, strefa ataku 1,5 m, jeden cel. Trafienie: 7 (2k6) obrażeń obuchowych.</td>"),
    ("<td>Each extended claw makes the following melee attack: +8 to hit, reach 5 ft. Hit: The target has the Grappled condition (escape DC 15).</td>",
     "<td>Każde wysunięte szczypce wykonują następujący atak bronią wręcz: +8 do trafienia, strefa ataku 1,5 m, jeden cel. Trafienie: cel zostaje pochwycony (ST 15, aby się uwolnić).</td>"),
    ("<td>The apparatus walks or swims forward provided its legs are extended.</td>",
     "<td>Amfibionator porusza się do przodu lub płynie naprzód, o ile nogi są wysunięte.</td>"),
    ("<td>The apparatus walks or swims backward provided its legs are extended.</td>",
     "<td>Amfibionator porusza się do tyłu lub płynie wstecz, o ile nogi są wysunięte.</td>"),
    ("<td>The apparatus turns 90 degrees counterclockwise provided its legs are extended.</td>",
     "<td>Amfibionator obraca się o 90 stopni w lewo, o ile nogi są wysunięte.</td>"),
    ("<td>The apparatus turns 90 degrees clockwise provided its legs are extended.</td>",
     "<td>Amfibionator obraca się o 90 stopni w prawo, o ile nogi są wysunięte.</td>"),
    ("<td>Eyelike fixtures emit Bright Light in a 30-foot radius and Dim Light for an additional 30 feet.</td>",
     "<td>Podobne do oczu urządzenia emitują jasne światło w promieniu 9 metrów i słabe światło na dodatkowe 9 metrów.</td>"),
    ("<td>The light turns off.</td>",
     "<td>Światło gaśnie.</td>"),
    ("<td>The apparatus sinks up to 20 feet if it's in liquid.</td>",
     "<td>Amfibionator opada w cieczy o maksymalnie 6 metrów.</td>"),
    ("<td>The apparatus rises up to 20 feet if it's in liquid.</td>",
     "<td>Amfibionator unosi się w cieczy o maksymalnie 6 metrów.</td>"),
    ("<td>The rear hatch unseals and opens.</td>",
     "<td>Tylny właz rozszczelnia się i otwiera.</td>"),
    ("<td>The rear hatch closes and seals.</td>",
     "<td>Tylny właz zamyka się i uszczelnia.</td>"),
    # Armor of Resistance
    ("#### Armor of Resistance",
     "#### Zbroja odporności"),
    ("You have odporność to one type of damage while you wear this armor. The MG chooses the type or determines it randomly by rolling on the following table.",
     "Kiedy nosisz tę zbroję, masz odporność na jeden rodzaj obrażeń. MG wybiera typ lub określa go losowo, rzucając na poniższą tabelę."),
    # Bean bag table
    ("<td>5d4 toadstools sprout. If a creature eats a toadstool, roll any die. On an odd roll, the eater must succeed on a DC 15 Constitution saving throw or take 5d6 trucizna damage and have the truciznaed condition for 1 hour. On an even roll, the eater gains 5d6 Temporary Hit Points for 1 hour.</td>",
     "<td>Wyrastają muchomory (5k4). Jeśli istota zje muchomora, rzuć dowolną kością. Przy nieparzystym wyniku jedzący musi wykonać udany rzut obronny na Kondycję o ST 15, w przeciwnym razie otrzymuje 5k6 obrażeń od trucizny i ma stan zatrucia przez 1 godzinę. Przy parzystym wyniku jedzący zyskuje 5k6 tymczasowych PW na 1 godzinę.</td>"),
    ("<td>A geyser erupts and spouts water, beer, mayonnaise, tea, vinegar, wine, or oil (GM's choice) 30 feet into the air for 1k4 minutes.</td>",
     "<td>Wybucha gejzer i wytryskuje wodę, piwo, majonez, herbatę, ocet, wino lub olej (wybór MG) na wysokość 9 metrów przez 1k4 minuty.</td>"),
    ("<td>A Treant sprouts. Roll any die. On an odd roll, the treant is Chaotic Evil. On an even roll, the treant is Chaotic Good.</td>",
     "<td>Wyrasta treant. Rzuć dowolną kością. Przy nieparzystym wyniku treant ma charakter Chaotyczny Zły. Przy parzystym wyniku treant ma charakter Chaotyczny Dobry.</td>"),
    ("<td>An animate but immobile stone statue in your likeness rises and makes verbal threats against you. If you leave it and others come near, it describes you as the most heinous of villains and directs the newcomers to find and attack you. If you are on the same plane of existence as the statue, it knows where you are. The statue becomes inanimate after 24 hours.</td>",
     "<td>Wznosi się ożywiony, lecz nieruchomy kamienny posąg przedstawiający ciebie i wypowiada werbalne groźby pod twoim adresem. Jeśli go opuścisz, a inni się zbliżą, opisuje cię jako najpodlejszego złoczyńcę i nakłania nowicjuszy, by cię odnaleźli i zaatakowali. Jeśli jesteś na tej samej sferze egzystencji co posąg, wie, gdzie się znajdujesz. Posąg staje się nieożywiony po 24 godzinach.</td>"),
    ("<td>A campfire with green flames springs forth and burns for 24 hours or until it is extinguished.</td>",
     "<td>Pojawia się ognisko z zielonymi płomieniami i płonie przez 24 godziny albo do chwili zgaszenia.</td>"),
    ("<td>Three Shrieker Fungi sprout.</td>",
     "<td>Wyrastają trzy wrzaskliwe grzyby.</td>"),
    ("<td>1k4 + 4 bright-pink toads crawl forth. Whenever a toad is touched, it transforms into a Large or smaller monster of the GM's choice that acts in accordance with its alignment and nature. The monster remains for 1 minute, then disappears in a puff of bright-pink smoke.</td>",
     "<td>Wypełzają jaskraworóżowe ropuchy (1k4 + 4). Za każdym razem, gdy dotknie się ropuchy, zamienia się ona w potwora Dużego lub mniejszego według wyboru MG, który działa zgodnie ze swoim charakterem i naturą. Potwór pozostaje przez 1 minutę, po czym znika w obłoku jaskraworóżowego dymu.</td>"),
    ("<td>A hungry Bulette burrows up and attacks.</td>",
     "<td>Wykopuje się głodny bulette i atakuje.</td>"),
    ("<td>A fruit tree grows. It has 1k10 + 20 fruit, 1k8 of which act as randomly determined potions. The tree vanishes after 1 hour. Picked fruit remains, retaining any magic for 30 days.</td>",
     "<td>Wyrasta drzewo owocowe. Ma 1k10 + 20 owoców, z których 1k8 działa jak losowo określone mikstury. Drzewo znika po 1 godzinie. Zerwane owoce pozostają, zachowując magię przez 30 dni.</td>"),
    ("<td>A nest of 1k4 + 3 rainbow-colored eggs springs up. Any creature that eats an egg makes a DC 20 Constitution saving throw. On a successful save, a creature permanently increases its lowest ability score by 1, randomly choosing among equally low scores. On a failed save, the creature takes 10d6 moc damage from an internal explosion.</td>",
     "<td>Pojawia się gniazdo tęczowych jaj (1k4 + 3). Każda istota, która zje jajko, wykonuje rzut obronny na Kondycję o ST 20. W przypadku sukcesu istota na stałe zwiększa swoją najniższą wartość cechy o 1, losując wśród równie niskich wyników. W przypadku niepowodzenia istota otrzymuje 10k6 obrażeń od mocy z powodu wewnętrznej eksplozji.</td>"),
    ("<td>A pyramid with a 60-foot-square base bursts upward. Inside is a burial chamber containing a Mummy, a Mummy Lord, or some other nieumarli of the GM's choice. Its sarcophagus contains treasure of the GM's choice.</td>",
     "<td>W górę wybucha piramida o podstawie kwadratu o boku 18 metrów. W środku znajduje się komora grobowa z mumiami, władcą mumii lub innym nieumarłym według wyboru MG. Sarkofag zawiera skarb według wyboru MG.</td>"),
    ("<td>A giant beanstalk sprouts, growing to a height of the GM's choice. The top leads where the GM chooses, such as to a great view, a cloud giant's castle, or another plane of existence.</td>",
     "<td>Wyrasta gigantyczna łodyga fasoli, rosnąc na wysokość według wyboru MG. Jej wierzchołek prowadzi tam, gdzie wybierze MG — na przykład na wspaniały widok, do zamku olbrzyma chmur albo na inną sferę egzystencji.</td>"),
]

def main():
    text = PATH.read_text(encoding="utf-8")
    original = text
    count = 0
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
            count += 1
    if text != original:
        PATH.write_text(text, encoding="utf-8")
    print(f"Applied {count} replacements in batch 1")

if __name__ == "__main__":
    main()
