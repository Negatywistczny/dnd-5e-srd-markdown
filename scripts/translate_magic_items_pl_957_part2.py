#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    # Feather tokens
    (
        """This object looks like a feather. Different types of feather tokens exist, each with a different single-use effect. The MG chooses the kind of token or determines it randomly by rolling on the Feather Tokens table. The type of token determines its rarity.
_Anchor (Uncommon)._ You can take a akcję magiczną to touch the token to a boat or ship. For the next 24 hours, the vessel can't be moved by any means. Touching the token to the vessel again ends the effect. When the effect ends, the token disappears.
_Bird (Rare)._ You can take a akcję magiczną to toss the token 5 feet into the air. The token disappears and an enormous, multicolored bird takes its place. The bird has the statistics of a **Roc**, but it can't attack. It obeys your simple commands and can carry up to 500 pounds while flying at its maximum speed (16 miles per hour for a maximum of 144 miles per day, with a 1-hour rest for every 3 hours of flying) or 1,000 pounds at half that speed. The bird disappears after flying its maximum distance for a day or if it drops to 0 PŻ. You can dismiss the bird as a akcję magiczną.
_Fan (Uncommon)._ If you are on a boat or ship, you can take a akcję magiczną to toss the token up to 10 feet in the air. The token disappears, and a giant flapping fan takes its place. The fan floats and creates a strong wind. This wind can fill the sails of one ship, increasing its speed by 5 miles per hour for 8 hours. You can dismiss the fan as a akcję magiczną.
_Swan Boat (Rare)._ You can take a akcję magiczną to touch the token to a body of water at least 60 feet in diameter. The token disappears, and a 50-foot-long, 20-foot-wide boat shaped like a swan takes its place. The boat is self-propelled and moves across water at a speed of 6 miles per hour. You can take a akcję magiczną while on the boat to command it to move or to turn up to 90 degrees. The boat remains for 24 hours and then disappears. You can dismiss the boat as a akcję magiczną.
_Tree (Uncommon)._ You must be outdoors to use this token. You can take a akcję magiczną to touch it to an unoccupied space on the ground. The token disappears, and in its place a nonmagical oak tree springs into existence. The tree is 60 feet tall and has a 5-foot-diameter trunk, and its branches at the top spread out in a 20-foot radius.
_Whip (Rare)._ You can take a akcję magiczną to throw the token to a point within 10 feet of yourself. The token disappears, and a floating whip takes its place. You can then take a akcję dodatkową to make a melee spell attack against a creature within 10 feet of the whip, with an attack bonus of +9. On a hit, the target takes 1d6 + 5 Force damage.
As a akcję dodatkową, you can direct the whip to fly up to 20 feet and repeat the attack against a creature within 10 feet of the whip. The whip disappears after 1 hour, when you take a akcję magiczną to dismiss it, or when you die or have the Incapacitated condition.
**Feather Tokens**""",
        """Ten przedmiot wygląda jak pióro. Istnieją różne rodzaje piórkowych żetonów, z których każdy ma inny jednorazowy efekt. MG wybiera rodzaj żetonu albo określa go losowo, rzucając na tabeli Piórkowych żetonów. Rodzaj żetonu określa jego rzadkość.
_Kotwica (niezwykły)._ Możesz wykonać akcję magiczną, aby dotknąć żetonem łodzi lub statku. Przez następne 24 godziny jednostka nie może zostać poruszona żadnym sposobem. Ponowne dotknięcie żetonem jednostki kończy efekt. Gdy efekt się kończy, żeton znika.
_Ptak (rzadki)._ Możesz wykonać akcję magiczną, aby rzucić żeton na wysokość 1,5 metra. Żeton znika, a na jego miejscu pojawia się ogromny, wielobarwny ptak. Ptak ma statystyki **roka**, ale nie może atakować. Wykonuje twoje proste polecenia i może unieść do 225 kilogramów, lecąc z maksymalną prędkością (25 kilometrów na godzinę, maksymalnie 230 kilometrów dziennie, z 1-godzinnym odpoczynkiem co 3 godziny lotu) albo 450 kilogramów z połową tej prędkości. Ptak znika po przeleceniu maksymalnego dystansu w ciągu dnia albo gdy jego PŻ spadną do 0. Możesz odprawić ptaka akcją magiczną.
_Wentylator (niezwykły)._ Jeśli jesteś na łodzi lub statku, możesz wykonać akcję magiczną, aby rzucić żeton na wysokość do 3 metrów. Żeton znika, a na jego miejscu pojawia się olbrzymi trzepoczący wiatrak. Wiatrak unosi się i tworzy silny wiatr. Wiatr ten może napełnić żagle jednego statku, zwiększając jego prędkość o 8 kilometrów na godzinę przez 8 godzin. Możesz odprawić wiatrak akcją magiczną.
_Łódź łabędzia (rzadki)._ Możesz wykonać akcję magiczną, aby dotknąć żetonem zbiornika wody o średnicy co najmniej 18 metrów. Żeton znika, a na jego miejscu pojawia się 15-metrowa, 6-metrowa łódź w kształcie łabędzia. Łódź napędza się sama i porusza po wodzie z prędkością około 10 kilometrów na godzinę. Będąc na łodzi, możesz wykonać akcję magiczną, aby rozkazać jej ruch albo skręt do 90 stopni. Łódź pozostaje przez 24 godziny, po czym znika. Możesz odprawić łódź akcją magiczną.
_Drzewo (niezwykły)._ Aby użyć tego żetonu, musisz przebywać na zewnątrz. Możesz wykonać akcję magiczną, aby dotknąć nim niezajętej przestrzeni na ziemi. Żeton znika, a na jego miejscu wyrasta niemagiczny dąb. Drzewo ma 18 metrów wysokości, pień o średnicy 1,5 metra, a jego gałęzie u góry rozchodzą się w promieniu 6 metrów.
_Bicz (rzadki)._ Możesz wykonać akcję magiczną, aby rzucić żeton w punkt w promieniu 3 metrów od siebie. Żeton znika, a na jego miejscu pojawia się unoszący się bicz. Następnie możesz wykonać akcję dodatkową, aby wykonać atak czarem wręcz przeciwko stworzeniu w promieniu 3 metrów od bicza, z premią do ataku +9. Przy trafieniu cel otrzymuje 1k6 + 5 obrażeń od mocy.
Jako akcję dodatkową możesz skierować bicz, aby przeleciał do 6 metrów i powtórzył atak przeciwko stworzeniu w promieniu 3 metrów od bicza. Bicz znika po 1 godzinie, gdy odprawisz go akcją magiczną albo gdy umrzesz lub masz stan obezwładniony.
**Piórkowe żetony**""",
    ),
    (
        """<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Token</th>
      <th>Rarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–20</td>
      <td>Anchor</td>
      <td>Uncommon</td>
    </tr>
    <tr>
      <td>21–35</td>
      <td>Bird</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>36–50</td>
      <td>Fan</td>
      <td>Uncommon</td>
    </tr>
    <tr>
      <td>51–65</td>
      <td>Swan boat</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>66–90</td>
      <td>Tree</td>
      <td>Uncommon</td>
    </tr>
    <tr>
      <td>91–00</td>
      <td>Whip</td>
      <td>Rare</td>
    </tr>
  </tbody>
</table>""",
        """<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Żeton</th>
      <th>Rzadkość</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–20</td>
      <td>Kotwica</td>
      <td>niezwykły</td>
    </tr>
    <tr>
      <td>21–35</td>
      <td>Ptak</td>
      <td>rzadki</td>
    </tr>
    <tr>
      <td>36–50</td>
      <td>Wentylator</td>
      <td>niezwykły</td>
    </tr>
    <tr>
      <td>51–65</td>
      <td>Łódź łabędzia</td>
      <td>rzadki</td>
    </tr>
    <tr>
      <td>66–90</td>
      <td>Drzewo</td>
      <td>niezwykły</td>
    </tr>
    <tr>
      <td>91–00</td>
      <td>Bicz</td>
      <td>rzadki</td>
    </tr>
  </tbody>
</table>""",
    ),
    # Figurines intro
    (
        """A _Figurka cudownej mocy_ is a statuette small enough to fit in a pocket. If you take a akcję magiczną to throw the figurine to a point on the ground within 60 feet of yourself, the figurine becomes a living creature specified in the figurine's description below. If the space where the creature would appear is occupied by other creatures or objects, or
if there isn't enough space for the creature, the figurine doesn't become a creature.
The creature is przyjazny to you and your allies. It understands your languages, obeys your commands, and takes its turn immediately after you on your Initiative count. If you issue no commands, the creature defends itself but takes no other actions.
The creature exists for a duration specific to each figurine. At the end of the duration, the creature reverts to its figurine form. It reverts to a figurine early if its creature form drops to 0 PŻ or if you take a akcję magiczną while touching the creature to make it revert to figurine form. When the creature becomes a figurine again, its property can't be used again until a certain amount of time has passed, as specified in the figurine's description.""",
        """_Figurka cudownej mocy_ to statuetka na tyle mała, że mieści się w kieszeni. Jeśli wykonasz akcję magiczną, aby rzucić figurką w punkt na ziemi w promieniu 18 metrów od siebie, figurka zamienia się w żywe stworzenie opisane poniżej. Jeśli przestrzeń, w której miałoby się pojawić stworzenie, jest zajęta przez inne istoty lub przedmioty albo
nie ma wystarczająco miejsca, figurka nie zamienia się w stworzenie.
Stworzenie jest przyjazne tobie i twoim sojusznikom. Rozumie twoje języki, wykonuje twoje polecenia i działa bezpośrednio po tobie w kolejności inicjatywy. Jeśli nie wydasz poleceń, stworzenie broni się, ale nie podejmuje innych działań.
Stworzenie istnieje przez czas określony dla każdej figurki. Po upływie tego czasu wraca do formy statuetki. Wraca wcześniej, jeśli w formie stworzenia jego PŻ spadną do 0 albo jeśli wykonasz akcję magiczną, dotykając stworzenia, aby przywrócić je do formy statuetki. Gdy stworzenie znów staje się statuetką, jej właściwości nie można użyć ponownie, dopóki nie upłynie określony w opisie figurki czas.""",
    ),
    (
        "**Bronze Griffon (Rare).** This bronze statuette is of a griffon rampant. It can become a **Griffon** for up to 6 hours. Once it has been used, it can't be used again until 5 days have passed.",
        "**Brązowy gryf (rzadki).** Ta brązowa statuetka przedstawia wznoszącego się gryfa. Może zamienić się w **gryfa** na maksymalnie 6 godzin. Po użyciu nie można jej użyć ponownie przez 5 dni.",
    ),
    (
        "**Ebony Fly (Rare).** This ebony statuette, carved in the likeness of a horsefly, can become a **Giant Fly** (see the accompanying stat block) for up to 12 hours and can be ridden as a mount. Once it has been used, it can't be used again until 2 days have passed.",
        "**Hebanowa mucha (rzadki).** Ta hebanowa statuetka wykuta w kształcie muchy końskiej może zamienić się w **olbrzymią muchę** (patrz towarzyszący blok statystyk) na maksymalnie 12 godzin i może służyć jako wierzchowiec. Po użyciu nie można jej użyć ponownie przez 2 dni.",
    ),
    (
        "**Golden Lions (Rare).** These gold statuettes of lions are always created in pairs. You can use one figurine or both simultaneously. Each can become a **Lion** for up to 1 hour. Once a lion has been used, it can't be used again until 7 days have passed.",
        "**Złote lwy (rzadkie).** Te złote statuetki lwów zawsze powstają w parach. Możesz użyć jednej figurki albo obu jednocześnie. Każda może zamienić się w **lwa** na maksymalnie 1 godzinę. Po użyciu lwa figurki nie można użyć ponownie przez 7 dni.",
    ),
    (
        """**Goat of Terror.** This figurine can become a **Giant Goat** for up to 3 hours. The goat can't attack, but you can (harmlessly) remove its horns and use them as weapons. One horn becomes a _+1 Lance_, and the other becomes a _+2 Longsword_. Removing a horn requires a Magic action, and the weapons disappear and the horns return when the goat reverts to figurine form. While you ride the goat, any Hostile creature that starts its turn within

a 30-foot Emanation originating from the goat must succeed on a DC 15 Wisdom saving throw or have the Frightened condition for 1 minute, until you are no longer riding the goat, or until the goat reverts to figurine form. The Frightened creature repeats the save at the end of each of its turns, ending the effect on itself on a success. Once it succeeds on the save, a creature is immune to this effect for the next 24 hours. Once the figurine has been used, it can't be used again until 15 days have passed.""",
        """**Kozioł grozy.** Ta figurka może zamienić się w **olbrzymiego kozła** na maksymalnie 3 godziny. Kozioł nie może atakować, ale możesz (bez szkody) zdjąć jego rogi i używać ich jako broni. Jeden róg staje się _+1 kopii_, a drugi _+2 mieczem długim_. Zdjęcie rogu wymaga akcji magicznej, a broń znika, a rogi wracają, gdy kozioł wraca do formy statuetki. Gdy jedziesz na koziole, każde wrogie stworzenie, które rozpoczyna turę w

promieniu 9 metrów wychodzącym od kozła, musi odnieść sukces w rzucie obronnym na Mądrość o ST 15, w przeciwnym razie ma stan przerażony przez 1 minutę, dopóki nie przestaniesz jechać na koziole albo dopóki kozioł nie wróci do formy statuetki. Przerażone stworzenie powtarza rzut na koniec każdej swojej tury, kończąc efekt na sobie w przypadku sukcesu. Po udanym rzucie stworzenie jest niewrażliwe na ten efekt przez następne 24 godziny. Po użyciu figurki nie można jej użyć ponownie przez 15 dni.""",
    ),
    (
        "**Goat of Traveling.** This figurine can become a Large goat with the same statistics as a **Riding Horse**. It has 24 charges, and each hour or portion thereof it spends in goat form costs 1 charge. While it has charges, you can use it as often as you wish. When it runs out of charges, it reverts to a figurine and can't be used again until 7 days have passed, when it regains all expended charges.",
        "**Kozioł podróżny.** Ta figurka może zamienić się w Dużego kozła o takich samych statystykach jak **koń wierzchowy**. Ma 24 ładunki, a każda godzina lub jej część spędzona w formie kozła kosztuje 1 ładunek. Dopóki ma ładunki, możesz używać jej tak często, jak chcesz. Gdy ładunki się wyczerpią, wraca do formy statuetki i nie można jej użyć ponownie przez 7 dni, po czym odzyskuje wszystkie zużyte ładunki.",
    ),
    (
        "**Goat of Travail.** This figurine can become a Giant **Goat** for up to 3 hours. Once it has been used, it can't be used again until 30 days have passed.",
        "**Kozioł trudu.** Ta figurka może zamienić się w **kozła** olbrzymiego rozmiaru na maksymalnie 3 godziny. Po użyciu nie można jej użyć ponownie przez 30 dni.",
    ),
    (
        "**Marble Elephant (Rare).** This marble statuette resembles a trumpeting elephant. It can become an **Elephant** for up to 24 hours. Once it has been used, it can't be used again until 7 days have passed.",
        "**Marmurowy słoń (rzadki).** Ta marmurowa statuetka przedstawia trąbiącego słonia. Może zamienić się w **słonia** na maksymalnie 24 godziny. Po użyciu nie można jej użyć ponownie przez 7 dni.",
    ),
    (
        "**Obsidian Steed (Very Rare).** This polished obsidian horse can become a **Nightmare** for up to 24 hours. The nightmare fights only to defend itself. Once it has been used, it can't be used again until 5 days have passed.",
        "**Obsydianowy rumak (bardzo rzadki).** Ten wypolerowany obsydianowy koń może zamienić się w **koszmara** na maksymalnie 24 godziny. Koszmar walczy tylko w obronie własnej. Po użyciu nie można go użyć ponownie przez 5 dni.",
    ),
    (
        "The figurine has a 10 percent chance each time you use it to ignore your orders, including a command to revert to figurine form. If you mount the nightmare while it is ignoring your orders, you and the nightmare are instantly transported to a random location on the plane of Hades, where the nightmare reverts to figurine form.",
        "Za każdym razem, gdy używasz figurki, istnieje 10 procent szans, że zignoruje twoje polecenia, w tym rozkaz powrotu do formy statuetki. Jeśli dosiadasz koszmara, gdy ignoruje twoje polecenia, ty i koszmar zostajecie natychmiast przeniesieni w losowe miejsce na sferze Hadesu, gdzie koszmar wraca do formy statuetki.",
    ),
    (
        "**Onyx Dog (Rare).** This onyx statuette of a dog can become a **Mastiff** for up to 6 hours. The mastiff has an Intelligence of 8 and can speak Common. It also has Blindsight with a range of 60 feet. Once it has been used, it can't be used again until 7 days have passed.",
        "**Onyksowy pies (rzadki).** Ta onyksowa statuetka psa może zamienić się w **mastifa** na maksymalnie 6 godzin. Mastif ma Inteligencję 8 i mówi po wspólnym. Ma też ślepowidzenie na odległość 18 metrów. Po użyciu nie można jej użyć ponownie przez 7 dni.",
    ),
    (
        "**Serpentine Owl (Rare).** This serpentine statuette of an owl can become a **Giant Owl** for up to 8 hours. The owl can communicate telepathically with you at any range if you and it are on the same plane of existence. Once it has been used, it can't be used again until 2 days have passed.",
        "**Serpentynowa sowa (rzadka).** Ta serpentynowa statuetka sowy może zamienić się w **olbrzymią sowę** na maksymalnie 8 godzin. Sowa może komunikować się z tobą telepatycznie na dowolną odległość, jeśli przebywacie na tej samej sferze egzystencji. Po użyciu nie można jej użyć ponownie przez 2 dni.",
    ),
    (
        "**Silver Raven (Uncommon).** This silver statuette of a raven can become a **Raven** for up to 12 hours. Once it has been used, it can't be used used again until 2 days have passed. While in raven form, the figurine grants you the ability to cast _Zwierzęcy posłaniec_ on it.",
        "**Srebrny kruk (niezwykły).** Ta srebrna statuetka kruka może zamienić się w **kruka** na maksymalnie 12 godzin. Po użyciu nie można jej użyć ponownie przez 2 dni. W formie kruka figurka pozwala ci rzucać na nią _Zwierzęcy posłaniec_.",
    ),
    # Fix typo in source - used used
    (
        "**Silver Raven (Uncommon).** This silver statuette of a raven can become a **Raven** for up to 12 hours. Once it has been used, it can't be used again until 2 days have passed. While in raven form, the figurine grants you the ability to cast _Zwierzęcy posłaniec_ on it.",
        "**Srebrny kruk (niezwykły).** Ta srebrna statuetka kruka może zamienić się w **kruka** na maksymalnie 12 godzin. Po użyciu nie można jej użyć ponownie przez 2 dni. W formie kruka figurka pozwala ci rzucać na nią _Zwierzęcy posłaniec_.",
    ),
    # Giant Fly stat block
    ("_Large Beast, Unaligned_", "_Duża bestia, nieokreślona_"),
    ("**Initiative** +1 (11)", "**Inicjatywa** +1 (11)"),
    ("**Speed** 30 ft., Fly 60 ft.", "**Szybkość** 9 m, lot 18 m"),
    ("<th>MOD</th>", "<th>MOD</th>"),
    ("<th>SAVE</th>", "<th>RB</th>"),
    ("**Senses** Darkvision 60 ft., Passive Perception 10", "**Zmysły** widzenie w ciemności 18 m, bierna Percepcja 10"),
    ("**Languages** None", "**Języki** brak"),
    # Flame tongue, frost brand, giant slayer, gloves
    (
        "While holding this magic weapon, you can take a akcję dodatkową and use a command word to cause flames to engulf the damage-dealing part of the weapon. These flames shed Bright Light in a 40-foot radius and Dim Light for an additional 40 feet. While the weapon is ablaze, it deals an extra 2d6 Fire damage on a hit. The flames last until you take a akcję dodatkową to issue the command again or until you drop, stow, or sheathe the weapon.",
        "Trzymając tę magiczną broń, możesz wykonać akcję dodatkową i wypowiedzieć słowo rozkazu, aby płomienie ogarnęły część broni zadającą obrażenia. Płomienie rzucają jasne światło w promieniu 12 metrów i słabe światło na dodatkowe 12 metrów. Gdy broń płonie, przy trafieniu zadaje dodatkowe 2k6 obrażeń od ognia. Płomienie trwają, dopóki nie wykonasz akcji dodatkowej, aby ponownie wypowiedzieć polecenie, albo dopóki nie upuścisz, nie schowasz ani nie pochowasz broni.",
    ),
    (
        """When you hit with an test ataku using this magic weapon, the target takes an extra 1d6 Cold damage. In addition, while you hold the weapon, you have odporność to Fire damage.
In freezing temperatures, the weapon sheds Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.
When you draw this weapon, you can extinguish all nonmagical flames within 30 feet of yourself. Once used, this property can't be used again for 1 hour.""",
        """Gdy trafisz testem ataku tą magiczną broń, cel otrzymuje dodatkowe 1k6 obrażeń od zimna. Dodatkowo, dopóki trzymasz broń, masz odporność na obrażenia od ognia.
W mroźnych temperaturach broń rzuca jasne światło w promieniu 3 metrów i słabe światło na dodatkowe 3 metry.
Gdy wyciągasz tę broń, możesz zgasić wszystkie niemagiczne płomienie w promieniu 9 metrów od siebie. Po użyciu tej właściwości nie można jej użyć ponownie przez 1 godzinę.""",
    ),
    (
        """You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.
When you hit a Giant with this weapon, the Giant takes an extra 2d6 damage of the weapon's type and must succeed on a ST 15 Siła rzut obronny or have the Prone condition.""",
        """Zyskujesz premię +1 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią.
Gdy trafisz tą bronią olbrzyma, olbrzym otrzymuje dodatkowe 2k6 obrażeń rodzaju broni i musi odnieść sukces w rzucie obronnym na Siłę o ST 15, w przeciwnym razie ma stan powalony.""",
    ),
    (
        "These gloves are imperceptible while worn. While wearing them, you gain a +5 bonus to Zręczność (Sleight of Hand) checks.",
        "Te rękawice są niewidoczne podczas noszenia. Nosząc je, zyskujesz premię +5 do testów Zręczności (Zwinne ręce).",
    ),
]

def main():
    text = PATH.read_text(encoding="utf-8")
    applied = 0
    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new)
            applied += 1
        else:
            print(f"WARNING: not found: {old[:70]}...")
    PATH.write_text(text, encoding="utf-8")
    print(f"Applied {applied}/{len(REPLACEMENTS)}")

if __name__ == "__main__":
    main()
