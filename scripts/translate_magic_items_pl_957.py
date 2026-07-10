#!/usr/bin/env python3
"""Translate remaining English in srd-5.2.1/pl/magic-items.md from ~line 957 onward."""
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

# Order matters for overlapping strings. Longer/more specific first.
REPLACEMENTS = [
    # --- Torba sztuczek ---
    (
        """This bag made from gray, rust, or tan cloth appears empty. Reaching inside the bag, however, reveals the presence of a small, fuzzy object.
You can take a akcję magiczną to pull the fuzzy object from the bag and throw it up to 20 feet. When the object lands, it transforms into a creature you determine by rolling on the table that corresponds to the bag's color. See „Potwory” for the creature's stat block. The creature vanishes at the następny świt or when it is reduced to 0 PŻ.
The creature is przyjazny to you and your allies, and it acts immediately after you on your Initiative count. You can take a akcję dodatkową to command how the creature moves and what action it takes on its next turn, such as attacking an enemy. In the absence of such orders, the creature acts in a fashion appropriate to its nature.
Once three fuzzy objects have been pulled from the bag, the bag can't be used again until the następny świt.
**Gray Bag of Tricks**""",
        """Ta torba z szarego, rdzawego lub beżowego materiału wydaje się pusta. Sięgnięcie do środka ujawnia jednak obecność małego, puszystego przedmiotu.
Możesz wykonać akcję magiczną, aby wyciągnąć puszysty przedmiot z torby i rzucić nim na odległość do 6 metrów. Gdy przedmiot wyląduje, zamienia się w stworzenie, które określasz rzutem na tabeli odpowiadającej kolorowi torby. Blok statystyk stworzenia znajduje się w rozdziale „Potwory”. Stworzenie znika o następnym świcie albo gdy jego PŻ spadną do 0.
Stworzenie jest przyjazne tobie i twoim sojusznikom i działa bezpośrednio po tobie w kolejności inicjatywy. Możesz wykonać akcję dodatkową, aby rozkazać mu, jak się porusza i jaką akcję podejmie w swojej następnej turze, na przykład atakując wroga. W braku takich rozkazów stworzenie działa zgodnie ze swoją naturą.
Gdy z torby wyciągniesz trzy puszyste przedmioty, nie można jej użyć ponownie do następnego świtu.
**Szara torba sztuczek**""",
    ),
    ("**Rust Bag of Tricks**", "**Rdzawa torba sztuczek**"),
    ("**Tan Bag of Tricks**", "**Beżowa torba sztuczek**"),
    ("<td>Weasel</td>", "<td>Łasica</td>"),
    ("<td>Giant Rat</td>", "<td>Olbrzymi szczur</td>"),
    ("<td>Badger</td>", "<td>Borsuk</td>"),
    ("<td>Boar</td>", "<td>Dzik</td>"),
    ("<td>Panther</td>", "<td>Pantera</td>"),
    ("<td>Giant Badger</td>", "<td>Olbrzymi borsuk</td>"),
    ("<td>Dire Wolf</td>", "<td>Straszliwy wilk</td>"),
    ("<td>Giant Elk</td>", "<td>Olbrzymi łoś</td>"),
    ("<td>Rat</td>", "<td>Szczur</td>"),
    ("<td>Giant Goat</td>", "<td>Olbrzymi kozioł</td>"),
    ("<td>Owl</td>", "<td>Sowa</td>"),
    ("<td>Giant Boar</td>", "<td>Olbrzymi dzik</td>"),
    ("<td>Mastiff</td>", "<td>Mastif</td>"),
    ("<td>Lion</td>", "<td>Lew</td>"),
    ("<td>Goat</td>", "<td>Koza</td>"),
    ("<td>Brown Bear</td>", "<td>Niedźwiedź brunatny</td>"),
    ("<td>Jackal</td>", "<td>Szakal</td>"),
    ("<td>Ape</td>", "<td>Małpa człekokształtna</td>"),
    ("<td>Black Bear</td>", "<td>Niedźwiedź czarny</td>"),
    ("<td>Giant Weasel</td>", "<td>Olbrzymia łasica</td>"),
    ("<td>Baboon</td>", "<td>Pawian</td>"),
    ("<td>Giant Hyena</td>", "<td>Olbrzymia hiena</td>"),
    ("<td>Tiger</td>", "<td>Tygrys</td>"),
    # --- Koralik pożywienia ---
    (
        "This flavorless, gelatinous bead dissolves on your tongue and provides as much nourishment as 1 day of Rations.",
        "Ten bezsłowny, galaretowaty koralik rozpuszcza się na języku i zapewnia tyle samo pożywienia, co jeden dzień racji żywnościowych.",
    ),
    # --- Pas olbrzymiej siły ---
    (
        """While wearing this belt, your Siła changes to a score granted by the belt. The type of giant determines the score (see the table below). The item has no effect on you if your Siła without the belt is equal to or greater than the belt's score.

<table>
  <thead>
    <tr>
      <th>Belt</th>
      <th>Str.</th>
      <th>Rarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Belt of Giant Strength (hill)</td>
      <td>21</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>Belt of Giant Strength (frost or stone)</td>
      <td>23</td>
      <td>Very Rare</td>
    </tr>
    <tr>
      <td>Belt of Giant Strength (fire)</td>
      <td>25</td>
      <td>Very Rare</td>
    </tr>
    <tr>
      <td>Belt of Giant Strength (cloud)</td>
      <td>27</td>
      <td>Legendary</td>
    </tr>
    <tr>
      <td>Belt of Giant Strength (storm)</td>
      <td>29</td>
      <td>Legendary</td>
    </tr>
  </tbody>
</table>""",
        """Nosząc ten pas, twoja Siła przyjmuje wartość przyznaną przez pas. Rodzaj olbrzyma określa tę wartość (patrz tabela poniżej). Przedmiot nie ma na ciebie wpływu, jeśli twoja Siła bez pasa jest równa wartości pasa lub wyższa.

<table>
  <thead>
    <tr>
      <th>Pas</th>
      <th>Siła</th>
      <th>Rzadkość</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pas olbrzymiej siły (wzgórzowy)</td>
      <td>21</td>
      <td>rzadki</td>
    </tr>
    <tr>
      <td>Pas olbrzymiej siły (lodowy lub kamienny)</td>
      <td>23</td>
      <td>bardzo rzadki</td>
    </tr>
    <tr>
      <td>Pas olbrzymiej siły (ogniowy)</td>
      <td>25</td>
      <td>bardzo rzadki</td>
    </tr>
    <tr>
      <td>Pas olbrzymiej siły (chmurowy)</td>
      <td>27</td>
      <td>legendarny</td>
    </tr>
    <tr>
      <td>Pas olbrzymiej siły (burzowy)</td>
      <td>29</td>
      <td>legendarny</td>
    </tr>
  </tbody>
</table>""",
    ),
    # --- Topór berserkera ---
    (
        """You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. In addition, while you are attuned to this weapon, your Hit Point maximum increases by 1 for each level you have attained.
_Curse._ This weapon is cursed, and becoming attuned to it extends the curse to you. As long as you remain cursed, you are unwilling to part with the weapon, keeping it within reach at all times. You also have Disadvantage on attack rolls with weapons other than this one.
Whenever another creature damages you while the weapon is in your possession, you must succeed on a ST 15 Mądrość rzut obronny or go berserk. This berserk state ends when you start your turn and there are no creatures within 60 feet of you that you can see or hear.
While berserk, you regard the creature nearest to you that you can see or hear as your enemy. If there are multiple possible creatures, choose one at random. On each of your turns, you must move as close to the creature as possible and take the Attack action, targeting the creature. If you're unable to get close enough to the creature to attack it with the weapon, your turn ends after you've used up all your available movement. If the creature dies or can no longer be seen or heard by you, the next nearest creature that you can see or hear becomes your new target.""",
        """Zyskujesz premię +1 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią. Dodatkowo, dopóki jesteś z nią zestrojony, twoje maksimum PW wzrasta o 1 za każdy osiągnięty poziom.
_Klątwa._ Ta broń jest przeklęta, a zestrojenie się z nią rozszerza klątwę na ciebie. Dopóki pozostajesz przeklęty, nie chcesz się z nią rozstawać i zawsze trzymasz ją w zasięgu ręki. Masz też utrudnienie w testach ataku bronią inną niż ta.
Ilekroć inne stworzenie zada ci obrażenia, gdy broń jest w twoim posiadaniu, musisz odnieść sukces w rzucie obronnym na Mądrość o ST 15, w przeciwnym razie wpadasz w szał. Stan szału kończy się, gdy rozpoczynasz turę i nie ma w promieniu 18 metrów od ciebie stworzeń, które widzisz lub słyszysz.
Będąc w szałzie, uznajesz najbliższe stworzenie, które widzisz lub słyszysz, za swojego wroga. Jeśli jest kilku możliwych kandydatów, wybierz jednego losowo. W każdej swojej turze musisz zbliżyć się do tego stworzenia tak bardzo, jak to możliwe, i wykonać akcję Ataku, celując w nie. Jeśli nie możesz podejść wystarczająco blisko, aby zaatakować je tą bronią, twoja tura kończy się po wykorzystaniu całego dostępnego ruchu. Jeśli stworzenie umrze albo przestaniesz je widzieć lub słyszeć, twoim nowym celem staje się kolejne najbliższe stworzenie, które widzisz lub słyszysz.""",
    ),
    # --- Świeca inwokacji table ---
    ("<th>Outer Plan</th>", "<th>Sfera zewnętrzna</th>"),
    ("<td>Beastlands</td>", "<td>Krainy Bestii</td>"),
    ("<td>Mount Celestia</td>", "<td>Góra Celestii</td>"),
    ("<td>Nine Hells</td>", "<td>Dziewięć Piekieł</td>"),
    # --- Latający dywan ---
    (
        """You can make this carpet hover and fly by taking a akcję magiczną and using the carpet's command word. It moves according to your directions if you are within 30 feet of it.
Four sizes of _Latający dywan_ exist. The MG chooses the size of a given carpet or determines it randomly by rolling on the following table. A carpet can carry up to twice the weight shown on the table, but its Fly Speed is halved if it carries more than its normal capacity.

<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Size</th>
      <th>Capacity</th>
      <th>Fly Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–20</td>
      <td>3 ft. × 5 ft.</td>
      <td>200 lb.</td>
      <td>80 feet</td>
    </tr>
    <tr>
      <td>21–55</td>
      <td>4 ft. × 6 ft.</td>
      <td>400 lb.</td>
      <td>60 feet</td>
    </tr>
    <tr>
      <td>56–80</td>
      <td>5 ft. × 7 ft.</td>
      <td>600 lb.</td>
      <td>40 feet</td>
    </tr>
    <tr>
      <td>81–00</td>
      <td>6 ft. × 9 ft.</td>
      <td>800 lb.</td>
      <td>30 feet</td>
    </tr>
  </tbody>
</table>""",
        """Możesz sprawić, że dywan unosi się i leci, wykonując akcję magiczną i wypowiadając słowo rozkazu dywanu. Porusza się według twoich poleceń, jeśli znajdujesz się w promieniu 9 metrów od niego.
Istnieją cztery rozmiary _Latającego dywanu_. MG wybiera rozmiar danego dywanu albo określa go losowo, rzucając na poniższej tabeli. Dywan może unieść do dwukrotności wagi podanej w tabeli, ale jego szybkość lotu jest zmniejszona o połowę, jeśli przewozi więcej niż normalna pojemność.

<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Rozmiar</th>
      <th>Pojemność</th>
      <th>Szybkość lotu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–20</td>
      <td>90 cm × 1,5 m</td>
      <td>90 kg</td>
      <td>24 metry</td>
    </tr>
    <tr>
      <td>21–55</td>
      <td>1,2 m × 1,8 m</td>
      <td>180 kg</td>
      <td>18 metrów</td>
    </tr>
    <tr>
      <td>56–80</td>
      <td>1,5 m × 2,1 m</td>
      <td>270 kg</td>
      <td>12 metrów</td>
    </tr>
    <tr>
      <td>81–00</td>
      <td>1,8 m × 2,7 m</td>
      <td>360 kg</td>
      <td>9 metrów</td>
    </tr>
  </tbody>
</table>""",
    ),
    # --- Płaszcz niewidzialności ---
    (
        """This cloak has 3 charges and regains 1d3 expended charges daily at dawn. While wearing the cloak, you can take a akcję magiczną to pull its hood over your
head and expend 1 charge to give yourself the Invisible condition for 1 hour. The effect ends early if you pull the hood down (no action required) or cease wearing the cloak.""",
        """Ten płaszcz ma 3 ładunki i codziennie o świcie odzyskuje 1k3 zużytych ładunków. Nosząc płaszcz, możesz wykonać akcję magiczną, aby zaciągnąć kaptur na
głowę i wydać 1 ładunek, aby nadać sobie stan niewidzialny na 1 godzinę. Efekt kończy się wcześniej, jeśli zdejmiesz kaptur (nie wymaga akcji) albo przestaniesz nosić płaszcz.""",
    ),
    # --- Sześcian mocy spell table ---
    ("<td>Mage Armor</td>", "<td>Pancerz maga</td>"),
    ("<td>Shield</td>", "<td>Tarcza</td>"),
    ("<td>Tiny Hut</td>", "<td>Mała chatka Leomunda</td>"),
    ("<td>Private Sanctum</td>", "<td>Osobiste sanktuarium</td>"),
    ("<td>Resilient Sphere</td>", "<td>Odporna sfera</td>"),
    # --- Tańczący miecz ---
    (
        """You can take a akcję dodatkową to toss this magic weapon into the air. When you do so, the weapon begins to hover, flies up to 30 feet, and attacks one creature of your choice within 5 feet of itself. The weapon uses your test ataku and adds your ability modifier to damage rolls.
While the weapon hovers, you can take a akcję dodatkową to cause it to fly up to 30 feet to another spot within 30 feet of you. As part of the same akcję dodatkową, you can cause the weapon to attack one creature within 5 feet of the weapon.
After the hovering weapon attacks for the fourth time, it flies back to you and tries to return to your hand. If you have no hand free, the weapon falls to the ground in your space. If the weapon has no unobstructed path to you, it moves as close to you as it can and then falls to the ground. It also ceases to hover if you grasp it or are more than 30 feet away from it.""",
        """Możesz wykonać akcję dodatkową, aby wyrzucić tę magiczną broń w powietrze. Wtedy broń zaczyna unosić się, leci na odległość do 9 metrów i atakuje jedno wybrane przez ciebie stworzenie w promieniu 1,5 metra od siebie. Broń używa twojego testu ataku i dodaje twój modyfikator z cechy do rzutów na obrażenia.
Dopóki broń unosi się w powietrzu, możesz wykonać akcję dodatkową, aby sprawić, że przeleci na odległość do 9 metrów w inne miejsce w promieniu 9 metrów od ciebie. W ramach tej samej akcji dodatkowej możesz sprawić, że broń zaatakuje jedno stworzenie w promieniu 1,5 metra od siebie.
Po czwartym ataku unoszącej się broni wraca ona do ciebie i próbuje wpaść z powrotem do twojej dłoni. Jeśli nie masz wolnej ręki, broń spada na ziemię w twojej przestrzeni. Jeśli broń nie ma wolnej drogi do ciebie, zbliża się tak bardzo, jak może, a potem spada na ziemię. Przestaje też unosić się, jeśli ją chwycisz albo oddalisz się od niej o więcej niż 9 metrów.""",
    ),
    # --- Talia iluzji table ---
    ("<th>Illusion*</th>", "<th>Iluzja*</th>"),
    ("<td>The card drawer</td>", "<td>Właściciel talii</td>"),
    (
        '\\*Stat blocks for these creatures (except the card drawer) appear in "Monsters."',
        "\\*Bloki statystyk tych stworzeń (z wyjątkiem właściciela talii) znajdują się w rozdziale „Potwory”.",
    ),
    ("<td>Adult Red Dragon</td>", "<td>Dorosły czerwony smok</td>"),
    ("<td>Archmage</td>", "<td>Arcymag</td>"),
    ("<td>Assassin</td>", "<td>Zabójca</td>"),
    ("<td>Bandit Captain</td>", "<td>Kapitan bandytów</td>"),
    ("<td>Basilisk</td>", "<td>Bazyliszek</td>"),
    ("<td>Berserker</td>", "<td>Berserker</td>"),
    ("<td>Bugbear Warrior</td>", "<td>Wojownik bugbeara</td>"),
    ("<td>Cloud Giant</td>", "<td>Gigant chmurowy</td>"),
    ("<td>Druid</td>", "<td>Druid</td>"),
    ("<td>Erinyes</td>", "<td>Erynia</td>"),
    ("<td>Ettin</td>", "<td>Ettin</td>"),
    ("<td>ogień Giant</td>", "<td>Gigant ogniowy</td>"),
    ("<td>Frost Giant</td>", "<td>Gigant lodowy</td>"),
    ("<td>Gnoll Warrior</td>", "<td>Wojownik gnolla</td>"),
    ("<td>Goblin Warrior</td>", "<td>Wojownik goblina</td>"),
    ("<td>Guardian Naga</td>", "<td>Obserwator</td>"),
    ("<td>Hill Giant</td>", "<td>Gigant wzgórzowy</td>"),
    ("<td>Hobgoblin Warrior</td>", "<td>Wojownik hobgoblina</td>"),
    ("<td>Incubus</td>", "<td>Inkub</td>"),
    ("<td>Iron Golem</td>", "<td>Żelazny golem</td>"),
    ("<td>Knight</td>", "<td>Rycerz</td>"),
    ("<td>Kobold Warrior</td>", "<td>Wojownik kobolda</td>"),
    ("<td>Lich</td>", "<td>Lisz</td>"),
    ("<td>Medusa</td>", "<td>Meduza</td>"),
    ("<td>Night Hag</td>", "<td>Nocna wiedźma</td>"),
    ("<td>Ogre</td>", "<td>Ogr</td>"),
    ("<td>Oni</td>", "<td>Oni</td>"),
    ("<td>Priest</td>", "<td>Kapłan</td>"),
    ("<td>Succubus</td>", "<td>Sukkub</td>"),
    ("<td>Troll</td>", "<td>Troll</td>"),
    ("<td>Veteran Warrior</td>", "<td>Weteran</td>"),
    ("<td>Wyvern</td>", "<td>Wiwerna</td>"),
    # --- Obrońca ---
    (
        """You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon.
The first time you attack with the weapon on each of your turns, you can transfer some or all of the weapon's bonus to your KP. For example, you could reduce the bonus to your attack rolls and damage rolls to +1 and gain a +2 bonus to KP. The adjusted bonuses remain in effect until the start of your next turn, although you must hold the weapon to gain a bonus to KP from it.""",
        """Zyskujesz premię +3 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią.
Za pierwszym razem w każdej swojej turze, gdy atakujesz tą bronią, możesz przenieść część lub całość premii broni na swoją KP. Na przykład możesz zmniejszyć premię do testów ataku i rzutów na obrażenia do +1 i zyskać premię +2 do KP. Dostosowane premie obowiązują do początku twojej następnej tury, choć musisz trzymać broń, aby korzystać z premii do KP.""",
    ),
    # --- Kula smoka ---
    (
        """An orb is an etched crystal globe about 10 inches in diameter. When used, it grows to about 20 inches in diameter, and mist swirls inside it.
While attuned to an orb, you can take a akcję magiczną to peer into the orb's depths. You must then make a ST 15 Charyzma rzut obronny. On a successful save, you control the orb for as long as you remain attuned to it. On a failed save, the orb imposes the Charmed condition on you for as long as you remain attuned to it.
While you are Charmed by the orb, you can't voluntarily end your Attunement to it, and the orb casts _Sugestia_ on you at will (save ST 18), urging you to work toward the evil ends it desires. The dragon essence within the orb might want many things: the annihilation of a particular society or organization, freedom from the orb, to spread suffering in the world, to advance the worship of Tiamat, or something else the MG decides.
_Spells._ The orb has 7 charges and regains 1d4 + 3 expended charges daily at dawn. If you control the orb, you can cast one of the spells on the following table from it. The table indicates how many charges you must expend to cast the spell.

<table>
  <thead>
    <tr>
      <th>Czar</th>
      <th>Koszt ładunku</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cure Wounds (level 9 version)</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Daylight</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Death Ward</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Detect Magic</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Scrying (save DC 18)</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

_Call smoki._ While you control the orb, you can take a Magic action to cause the orb to issue a telepathic call that extends in all directions for 40 miles. Chromatic dragons in range feel compelled to come to the orb as soon as possible by the most direct route. Dragon deities such as Tiamat are unaffected by this call. Chromatic dragons drawn to the orb might be Hostile toward you for compelling them against their will. Once you have used this property, it can't be used again for 1 hour.

_Destroying an Orb._ A _Dragon Orb_ has AC 20 and is destroyed if it takes damage from a +3 _Weapon_ or a _Dezintegracja_ spell. Nothing else can harm it.""",
        """Kula to wyryty kryształowy glob o średnicy około 25 centymetrów. Po użyciu powiększa się do około 50 centymetrów średnicy, a w środku wiruje mgła.
Będąc zestrojonym z kulą, możesz wykonać akcję magiczną, aby zajrzeć w jej głębiny. Następnie musisz wykonać rzut obronny na Charyzmę o ST 15. W przypadku sukcesu kontrolujesz kulę, dopóki pozostajesz z nią zestrojony. W przypadku niepowodzenia kula nakłada na ciebie stan zauroczony, dopóki pozostajesz z nią zestrojony.
Gdy jesteś zauroczony przez kulę, nie możesz dobrowolnie zakończyć z nią zestrojenia, a kula na wolno rzuca na ciebie _Sugestia_ (ST 18), nakłaniając cię do działań na rzecz złych celów, których pragnie. Esencja smoka w kuli może pragnąć wielu rzeczy: unicestwienia określonego społeczeństwa lub organizacji, wolności od kuli, szerzenia cierpienia na świecie, rozpowszechniania kultu Tiamat albo czegoś innego, co zdecyduje MG.
_Czary._ Kula ma 7 ładunków i codziennie o świcie odzyskuje 1k4 + 3 zużytych ładunków. Jeśli kontrolujesz kulę, możesz rzucić z niej jeden z czarów z poniższej tabeli. Tabela wskazuje, ile ładunków musisz wydać, aby rzucić czar.

<table>
  <thead>
    <tr>
      <th>Czar</th>
      <th>Koszt ładunku</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Leczenie ran (wersja 9. kręgu)</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Światło dzienne</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Ochrona przed śmiercią</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Wykrycie magii</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Podgląd (ST 18)</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

_Przyzwanie smoków._ Dopóki kontrolujesz kulę, możesz wykonać akcję magiczną, aby kula wydała telepatyczne wezwanie rozchodzące się we wszystkich kierunkach na odległość 65 kilometrów. Smoki chromatyczne w zasięgu czują przymus, by jak najszybciej dotrzeć do kuli najkrótszą drogą. Smocze bóstwa, takie jak Tiamat, nie reagują na to wezwanie. Smoki chromatyczne przyzwane do kuli mogą być wobec ciebie wrogie z powodu zmuszenia ich wbrew woli. Po użyciu tej właściwości nie można jej użyć ponownie przez 1 godzinę.

_Zniszczenie kuli._ _Kula smoka_ ma KP 20 i zostaje zniszczona, jeśli otrzyma obrażenia od broni +3 lub czaru _dezintegracja_. Nic innego nie może jej zranić.""",
    ),
    # --- Zbroja z łusek smoka table ---
    ("<th>Dragon</th>", "<th>Smok</th>"),
    ("<th>Resistance</th>", "<th>Odporność</th>"),
    ("<td>Black</td>", "<td>Czarny</td>"),
    ("<td>Gold</td>", "<td>Złoty</td>"),
    ("<td>Blue</td>", "<td>Niebieski</td>"),
    ("<td>Green</td>", "<td>Zielony</td>"),
    ("<td>Brass</td>", "<td>Mosiężny</td>"),
    ("<td>Red</td>", "<td>Czerwony</td>"),
    ("<td>Bronze</td>", "<td>Brązowy</td>"),
    ("<td>Silver</td>", "<td>Srebrny</td>"),
    ("<td>Copper</td>", "<td>Miedziany</td>"),
    ("<td>White</td>", "<td>Biały</td>"),
    # --- Pogromca smoków ---
    (
        """You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.
The weapon deals an extra 3d6 damage of the weapon's type if the target is a Dragon.""",
        """Zyskujesz premię +1 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią.
Broń zadaje dodatkowe 3k6 obrażeń swojego rodzaju, jeśli celem jest smok.""",
    ),
    # --- Krasnoludzki miotak attunement ---
    (
        "_Broń (Warhammer), bardzo rzadki (wymaga zestrojenia by a Dwarf or a Creature Attuned to a Belt of Dwarvenkind)_",
        "_Broń (młot bojowy), bardzo rzadki (wymaga zestrojenia przez krasnoluda lub istotę zestrojoną z pasem krasnoludów)_",
    ),
    # --- Ifryt w butelce ---
    (
        "<td>The efreeti attacks you. After fighting for 5 rounds, the efreeti disappears, and the bottle loses its magic.</td>",
        "<td>Ifryt atakuje cię. Po 5 rundach walki ifryt znika, a butelka traci magię.</td>",
    ),
    (
        "<td>The efreeti understands your languages and obeys your commands for 1 hour, after which it returns to the bottle, and a new stopper contains it. The stopper can't be removed for 24 hours. The next two times the bottle is opened, the same effect occurs. If the bottle is opened a fourth time, the efreeti escapes and disappears, and the bottle loses its magic.</td>",
        "<td>Ifryt rozumie twoje języki i wykonuje twoje polecenia przez 1 godzinę, po czym wraca do butelki, a nowy korek go zatrzymuje. Koreka nie można wyjąć przez 24 godziny. Przy kolejnych dwóch otwarciach butelki występuje ten sam efekt. Jeśli butelkę otworzysz po raz czwarty, ifryt ucieka i znika, a butelka traci magię.</td>",
    ),
    (
        "<td>The efreeti understands your languages and can cast Wish once for you. It disappears when it grants the wish or after 1 hour, and the bottle loses its magic.</td>",
        "<td>Ifryt rozumie twoje języki i może raz rzucić dla ciebie _Życzenie_. Znika, gdy spełni życzenie albo po 1 godzinie, a butelka traci magię.</td>",
    ),
    # --- Klejnot żywiołów ---
    (
        """This gem contains a mote of elemental energy. When you take a akcję Użycie to break the gem, an elemental is summoned (see „Potwory” for its stat block), and the gem ceases to be magical. The elemental appears in an unoccupied space as close to the broken gem as possible, understands your languages, obeys your commands, and takes its turn immediately after you on your Initiative count. The elemental disappears after 1 hour, when it dies, or when you dismiss it as a akcję dodatkową. The type of gem determines the elemental, as shown in the following table.

<table>
  <thead>
    <tr>
      <th>Gem</th>
      <th>Summoned Elemental</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Blue sapphire</td>
      <td>Air Elemental</td>
    </tr>
    <tr>
      <td>Emerald</td>
      <td>Water Elemental</td>
    </tr>
    <tr>
      <td>Red corundum</td>
      <td>ogień Elemental</td>
    </tr>
    <tr>
      <td>Yellow diamond</td>
      <td>Earth Elemental</td>
    </tr>
  </tbody>
</table>""",
        """Ten klejnot zawiera cząstkę energii żywiołowej. Gdy wykonasz akcję Użycie, aby rozbić klejnot, zostaje przywołany żywiołak (blok statystyk znajduje się w rozdziale „Potwory”), a klejnot przestaje być magiczny. Żywiołak pojawia się w niezajętej przestrzeni tak blisko rozbitego klejnotu, jak to możliwe, rozumie twoje języki, wykonuje twoje polecenia i działa bezpośrednio po tobie w kolejności inicjatywy. Żywiołak znika po 1 godzinie, gdy umrze albo gdy odprawisz go akcją dodatkową. Rodzaj klejnotu określa żywiołaka, jak pokazano w poniższej tabeli.

<table>
  <thead>
    <tr>
      <th>Klejnot</th>
      <th>Przywołany żywiołak</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Niebieski szafir</td>
      <td>Żywiołak powietrza</td>
    </tr>
    <tr>
      <td>Szmaragd</td>
      <td>Żywiołak wody</td>
    </tr>
    <tr>
      <td>Czerwony korund</td>
      <td>Żywiołak ognia</td>
    </tr>
    <tr>
      <td>Żółty diament</td>
      <td>Żywiołak ziemi</td>
    </tr>
  </tbody>
</table>""",
    ),
    # --- Eliksir zdrowia ---
    (
        """When you drink this potion, you are cured of all magical contagions. In addition, the following conditions end on you: Blinded, Deafened, Paralyzed, and Poisoned.
The clear, red liquid has tiny bubbles of light in it.""",
        """Gdy wypijesz tę miksturę, zostajesz wyleczony ze wszystkich magicznych zakażeń. Dodatkowo na tobie kończą się następujące stany: oślepiony, ogłuszony, sparaliżowany i zatruty.
Przezroczysty, czerwony płyn zawiera maleńkie bąbelki światła.""",
    ),
    # --- Łuk energii ---
    (
        """You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon, which has no string. Each time you pull your arm back in a firing motion, a magical arrow made of golden energy appears nocked and ready to fire. An arrow produced by this weapon deals Force damage instead of Piercing damage on a hit, and it disappears after it hits or misses its target. Until it disappears, the arrow emits Bright Light in a 20-foot radius and Dim Light for an additional 20 feet.
This weapon has the following additional properties.
_Arrow of Restraint._ Whenever you use this weapon to make a ranged attack against a creature, you can try to restrain the target instead of dealing damage to it. If the arrow hits, the target must succeed on a ST 15 Siła rzut obronny or have the Restrained condition for 1 minute. As an action, a creature Restrained by an arrow can make a ST 20 Siła (Athletics) check to try to break the restraint, ending the effect on itself on a successful check.
_Arrow of Transport._ As a akcję magiczną, you can fire one energy arrow from this weapon at a target you can see within 60 feet of yourself. The target can be either a willing Medium or smaller creature or an object that isn't being worn or carried, provided the object is small enough to fit inside a 5-foot Cube. The arrow teleports the target to an unoccupied space you can see within 10 feet of you.
_Energy Ladder._ As a akcję magiczną, you can loose a flurry of energy arrows from this weapon at a wall up to 60 feet away from yourself. The arrows become glowing rungs that stick out of the wall, forming a magical ladder up to 60 feet long on the wall. This ladder lasts for 1 minute before disappearing.""",
        """Zyskujesz premię +1 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią, która nie ma cięciwy. Za każdym razem, gdy cofasz ramię w ruchu strzału, pojawia się naciągnięta magiczna strzała ze złotej energii, gotowa do wystrzału. Strzała z tej broni przy trafieniu zadaje obrażenia od mocy zamiast obrażeń kłutych i znika po trafieniu lub pudle. Dopóki istnieje, strzała emituje jasne światło w promieniu 6 metrów i słabe światło na dodatkowe 6 metrów.
Ta broń ma następujące dodatkowe właściwości.
_Strzała powstrzymania._ Ilekroć używasz tej broni do ataku dystansowego przeciwko stworzeniu, możesz spróbować unieruchomić cel zamiast zadać mu obrażenia. Jeśli strzała trafi, cel musi odnieść sukces w rzucie obronnym na Siłę o ST 15, w przeciwnym razie ma stan pochwycony przez 1 minutę. W ramach akcji stworzenie pochwytane strzałą może wykonać test Siły (Atletyka) o ST 20, aby spróbować uwolnić się z pochwycenia, kończąc efekt na sobie w przypadku sukcesu.
_Strzała transportu._ Jako akcję magiczną możesz wystrzelić z tej broni jedną strzałę energii w cel, który widzisz w promieniu 18 metrów od siebie. Celem może być chętne stworzenie Średnie lub mniejsze albo przedmiot, który nie jest noszony ani trzymany, pod warunkiem że mieści się w sześcianie o boku 1,5 metra. Strzała teleportuje cel do niezajętej przestrzeni, którą widzisz w promieniu 3 metrów od siebie.
_Drabina energii._ Jako akcję magiczną możesz wystrzelić z tej broni salwę strzał energii w ścianę w odległości do 18 metrów od siebie. Strzały stają się świecącymi szczeblami wystającymi ze ściany i tworzą magiczną drabinę o długości do 18 metrów na ścianie. Drabina utrzymuje się przez 1 minutę, po czym znika.""",
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
            print(f"WARNING: pattern not found ({old[:60]}...)")
    PATH.write_text(text, encoding="utf-8")
    print(f"Applied {applied}/{len(REPLACEMENTS)} replacements")

if __name__ == "__main__":
    main()
