#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    ("_Broń (dowolna prosta lub wojskowa), legendarny (wymaga zestrojenia by a Paladin)_", "_Broń (dowolna prosta lub wojskowa), legendarny (wymaga zestrojenia przez paladyna)_"),
    ("<th>Horn Type</th>", "<th>Rodzaj rogu</th>"),
    ("<th>Spirits</th>", "<th>Duchy</th>"),
    ("<th>Requirement</th>", "<th>Wymaganie</th>"),
    ("<td>None</td>", "<td>Brak</td>"),
    ("<td>Proficiency with all Simple weapons</td>", "<td>Biegłość we wszystkich prostych broniach</td>"),
    ("<td>Training with all Medium armor</td>", "<td>Szkolenie we wszystkich średnich zbrojach</td>"),
    ("<td>Iron</td>", "<td>Żelazny</td>"),
    ("<td>Proficiency with all Martial weapons</td>", "<td>Biegłość we wszystkich wojskowych broniach</td>"),
    # Deck of Many Things intro
    (
        """Usually found in a box or pouch, this deck contains a number of cards made of ivory or vellum. Most (75 percent) of these decks have thirteen cards, but some have twenty-two. Use the appropriate column of the Mysterious Deck table when randomly determining cards drawn from the deck.
Before you draw a card, you must declare how many cards you intend to draw and then draw them randomly. Any cards drawn in excess of this number have no effect. Otherwise, as soon as you draw a card from the deck, its magic takes effect. You must draw each card no more than 1 hour after the previous draw. If you fail to draw the chosen number, the remaining number of cards fly from the deck on their own and take effect all at once.
Once a card is drawn, it disappears. Unless the card is the Fool or Jester, the card reappears in the deck, making it possible to draw the same card twice. (Once the Fool or Jester has left the deck, reroll on the table if that card comes up again.)
**Mysterious Deck**""",
        """Zwykle znajduje się w pudełku lub sakiewce; talia zawiera karty z kości słoniowej lub pergaminu. Większość (75 procent) talii ma trzynaście kart, niektóre mają dwadzieścia dwie. Przy losowym wyciąganiu kart używaj odpowiedniej kolumny tabeli Tajemniczej talii.
Zanim wyciągniesz kartę, musisz zadeklarować, ile kart zamierzasz wyciągnąć, a następnie losować je. Karty wyciągnięte ponad tę liczbę nie mają efektu. W przeciwnym razie, gdy tylko wyciągniesz kartę z talii, jej magia zaczyna działać. Każdą kartę musisz wyciągnąć nie później niż 1 godzinę po poprzedniej. Jeśli nie wyciągniesz zadeklarowanej liczby kart, pozostałe same wylatują z talii i działają jednocześnie.
Po wyciągnięciu karta znika. O ile nie jest to Głupiec lub Błazen, karta wraca do talii, co pozwala wyciągnąć tę samą kartę dwukrotnie. (Gdy Głupiec lub Błazen opuści talię, przy ponownym wylosowaniu tej karty rzuć ponownie na tabeli.)
**Tajemnicza talia**""",
    ),
    ("<td>Balance</td>", "<td>Równowaga</td>"),
    ("<td>Comet</td>", "<td>Kometa</td>"),
    ("<td>Donjon</td>", "<td>Loch</td>"),
    ("<td>Fates</td>", "<td>Przeznaczenie</td>"),
    ("<td>Flames</td>", "<td>Płomienie</td>"),
    ("<td>Fool</td>", "<td>Głupiec</td>"),
    ("<td>Gem</td>", "<td>Klejnot</td>"),
    ("<td>Jester</td>", "<td>Błazen</td>"),
    ("<td>Key</td>", "<td>Klucz</td>"),
    ("<td>Moon</td>", "<td>Księżyc</td>"),
    ("<td>Puzzle</td>", "<td>Zagadka</td>"),
    ("<td>Rogue</td>", "<td>Łotr</td>"),
    ("<td>Ruin</td>", "<td>Ruina</td>"),
    ("<td>Sage</td>", "<td>Mędrzec</td>"),
    ("<td>Skull</td>", "<td>Czaszka</td>"),
    ("<td>Star</td>", "<td>Gwiazda</td>"),
    ("<td>Sun</td>", "<td>Słońce</td>"),
    ("<td>Talons</td>", "<td>Szpony</td>"),
    ("<td>Throne</td>", "<td>Tron</td>"),
    ("<td>Void</td>", "<td>Pustka</td>"),
    ("Each card's effect is described below.", "Efekt każdej karty opisano poniżej."),
    # Card effects
    (
        "_Balance._ You can increase one of your ability scores by 2, to a maximum of 22, provided you also decrease another one of your ability scores by 2. You can't decrease an ability that has a score of 5 or lower. Alternatively, you can choose not to adjust your ability scores, in which case this card has no effect.",
        "_Równowaga._ Możesz zwiększyć jedną ze swoich cech o 2, maksymalnie do 22, pod warunkiem że jednocześnie zmniejszysz inną cechę o 2. Nie możesz zmniejszyć cechy, której wartość wynosi 5 lub mniej. Alternatywnie możesz nie zmieniać cech — wtedy karta nie ma efektu.",
    ),
    (
        "_Comet._ The next time you enter combat against one or more Hostile creatures, you can select one of them as your foe when you roll Initiative. If you reduce your foe to 0 Hit Points during that combat, you have Advantage on Death Saving Throws for 1 year. If someone else reduces your chosen foe to 0 Hit Points or you don't choose a foe, this card has no effect.",
        "_Kometa._ Następnym razem, gdy wejdziesz do walki z jednym lub większą liczbą wrogich stworzeń, możesz wybrać jedno z nich jako swojego wroga przy rzucie na inicjatywę. Jeśli w tej walce obniżysz PW wroga do 0, masz ułatwienie w rzutach obronnych na śmierć przez 1 rok. Jeśli ktoś inny obniży PW wybranego wroga do 0 albo nie wybierzesz wroga, karta nie ma efektu.",
    ),
    (
        "_Donjon._ You disappear and become entombed in a state of suspended animation in an extradimensional sphere. Everything you're wearing and carrying disappears with you except for Artifacts, which stay behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the sphere. You can't be located by any Divination magic, but a _Życzenie_ spell can reveal the location of your prison. You draw no more cards.",
        "_Loch._ Znikasz i zostajesz pogrzebany w stanie zawieszonej animacji w pozawymiarowej sferze. Wszystko, co nosisz i trzymasz, znika wraz z tobą, z wyjątkiem artefaktów, które pozostają w miejscu, które zajmowałeś. Pozostajesz uwięziony, dopóki nie zostaniesz odnaleziony i wydobyty ze sfery. Nie można cię zlokalizować żadną magią wróżbiarską, ale czar _Życzenie_ może ujawnić położenie twojego więzienia. Nie wyciągasz już więcej kart.",
    ),
    (
        "_Euryale._ The card's medusa-like visage curses you. You take a −2 penalty to saving throws while cursed in this way. Only a god or the magic of the Fates card can end this curse.",
        "_Euryale._ Meduzowate oblicze karty przeklina cię. Dopóki jesteś przeklęty w ten sposób, masz karę −2 do rzutów obronnych. Tylko bóstwo albo magia karty Przeznaczenie może zakończyć tę klątwę.",
    ),
    (
        "_Fates._ Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.",
        "_Przeznaczenie._ Tkanka rzeczywistości się rozpina i splata na nowo, pozwalając ci uniknąć lub wymazać jedno wydarzenie, tak jakby nigdy nie nastąpiło. Możesz użyć magii karty zaraz po jej wyciągnięciu albo w dowolnym innym momencie przed śmiercią.",
    ),
    (
        "_Flames._ A powerful devil becomes your enemy. The devil seeks your ruin and torments you, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies.",
        "_Płomienie._ Potężny diabeł staje się twoim wrogiem. Diabeł dąży do twojej zguby i cię dręczy, rozkoszując się twoim cierpieniem, zanim spróbuje cię zabić. Ta wrogość trwa, dopóki nie zginiesz ty albo diabeł.",
    ),
    (
        "_Fool._ You have Disadvantage on D20 Tests for the next 72 hours. Draw another card; this draw doesn't count as one of your declared draws.",
        "_Głupiec._ Masz utrudnienie w testach k20 przez następne 72 godziny. Wyciągnij kolejną kartę; to losowanie nie liczy się jako jedno z zadeklarowanych.",
    ),
    (
        "_Gem._ Twenty-five pieces of jewelry worth 2,000 GP each or fifty gems worth 1,000 GP each appear at your feet.",
        "_Klejnot._ U twoich stóp pojawia się dwadzieścia pięć elementów biżuterii wartych po 2000 sz każdy albo pięćdziesiąt klejnotów wartych po 1000 sz każdy.",
    ),
    (
        "_Jester._ You have Advantage on D20 Tests for the next 72 hours, or you can draw two additional cards beyond your declared draws.",
        "_Błazen._ Masz ułatwienie w testach k20 przez następne 72 godziny albo możesz wyciągnąć dwie dodatkowe karty ponad zadeklarowaną liczbę.",
    ),
    (
        "_Key._ A Rare or rarer magic weapon with which you are proficient appears on your person. The GM chooses the weapon.",
        "_Klucz._ Na twojej osobie pojawia się rzadka lub rzadsza magiczna broń, w której masz biegłość. MG wybiera broń.",
    ),
    (
        "_Knight._ You gain the service of a **Knight**, who magically appears in an unoccupied space you choose within 30 feet of yourself. The knight has the same alignment as you and serves you loyally until death, believing the two of you have been drawn together by fate. Work with your GM to create a name and backstory for this NPC. The GM can use a different stat block to represent the knight, as desired.",
        "_Rycerz._ Zyskujesz służbę **rycerza**, który magicznie pojawia się w wybranej przez ciebie niezajętej przestrzeni w promieniu 9 metrów od ciebie. Rycerz ma taki sam charakter jak ty i służy ci wiernie aż do śmierci, wierząc, że los was połączył. Wspólnie z MG stwórz imię i historię tej postaci. MG może użyć innego bloku statystyk dla rycerza, jeśli uzna to za stosowne.",
    ),
    (
        "_Moon._ You gain the ability to cast _Życzenie_ 1k3 times.",
        "_Księżyc._ Zyskujesz zdolność rzucania _Życzenie_ 1k3 razy.",
    ),
    (
        "_Puzzle._ Permanently reduce your Intelligence or Wisdom by 1k4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws.",
        "_Zagadka._ Trwale zmniejszasz Inteligencję lub Mądrość o 1k4 + 1 (minimum 1). Możesz wyciągnąć jedną dodatkową kartę ponad zadeklarowaną liczbę.",
    ),
    (
        "_Rogue._ An NPC of the GM's choice becomes Hostile toward you. You don't know the identity of this NPC until they or someone else reveals it. Nothing less than a _Życzenie_ spell or divine intervention can end the NPC's hostility toward you.",
        "_Łotr._ NPC wybrany przez MG staje się wobec ciebie wrogi. Nie znasz tożsamości tej postaci, dopóki ona sama albo ktoś inny jej nie ujawni. Nic krótszego niż czar _Życzenie_ lub boska interwencja nie może zakończyć wrogości tej postaci wobec ciebie.",
    ),
    (
        "_Ruin._ All forms of wealth that you carry or own, other than magic items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.",
        "_Ruina._ Tracisz wszelkie formy bogactwa, które nosisz lub posiadasz, poza magicznymi przedmiotami. Ruchomy majątek znika. Firmy, budynki i ziemie, które posiadasz, przepadają w sposób najmniej zmieniający rzeczywistość. Wszelkie dokumenty potwierdzające własność utraconego majątku również znikają.",
    ),
    (
        "_Sage._ At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question.",
        "_Mędrzec._ W dowolnym momencie w ciągu roku od wyciągnięcia tej karty możesz w medytacji zadać pytanie i mentalnie otrzymać prawdziwą odpowiedź.",
    ),
    (
        """_Skull._ An **Avatar of Death** (see the accompanying stat block) appears in an unoccupied space as close to you as possible. The avatar targets only you with its attacks, appearing as a ghostly skeleton clad in a tattered black robe and carrying a spectral scythe. The avatar disappears when it drops to 0 Hit Points or you die. If an ally of yours deals damage to the avatar, that ally summons another **Avatar of Death**. The new avatar appears in an unoccupied space as close to that ally as possible and targets only that ally with its attacks. You and your allies can each summon only one avatar as a consequence of this draw. A creature slain by an avatar can't be restored to life.""",
        """_Czaszka._ **Awatar śmierci** (patrz towarzyszący blok statystyk) pojawia się w niezajętej przestrzeni tak blisko ciebie, jak to możliwe. Awatar atakuje wyłącznie ciebie i wygląda jak upiorny szkielet w podartej czarnej szacie, dzierżący widmową kosę. Awatar znika, gdy jego PW spadną do 0 albo gdy umrzesz. Jeśli twój sojusznik zada awatarowi obrażenia, ten sojusznik przyzywa kolejnego **Awatara śmierci**. Nowy awatar pojawia się w niezajętej przestrzeni tak blisko tego sojusznika, jak to możliwe, i atakuje wyłącznie jego. Ty i twoi sojusznicy możecie w ten sposób przyzwać każdy tylko jednego awatara. Stworzenie zabite przez awatara nie może zostać przywrócone do życia.""",
    ),
    (
        "_Star._ Increase one of your ability scores by 2, to a maximum of 24.",
        "_Gwiazda._ Zwiększ jedną ze swoich cech o 2, maksymalnie do 24.",
    ),
    (
        "_Sun._ A magic item (chosen by the GM) appears on your person. In addition, you gain 10 Temporary Hit Points daily at dawn until you die.",
        "_Słońce._ Na twojej osobie pojawia się magiczny przedmiot (wybrany przez MG). Dodatkowo codziennie o świcie zyskujesz 10 tymczasowych PW, dopóki nie umrzesz.",
    ),
    (
        "_Talons._ Every magic item you wear or carry disintegrates. Artifacts in your possession vanish instead.",
        "_Szpony._ Każdy magiczny przedmiot, który nosisz lub trzymasz, ulega dezintegracji. Artefakty w twoim posiadaniu zamiast tego znikają.",
    ),
    (
        "_Throne._ You gain proficiency and Expertise in your choice of History, Insight, Intimidation, or Persuasion. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently home to one or more monsters, which must be cleared out before you can claim the keep as yours.",
        "_Tron._ Zyskujesz biegłość i ekspertyzę w wybranej przez siebie umiejętności: Historia, Wnikliwość, Zastraszanie lub Perswazja. Dodatkowo zyskujesz prawowite własność małego zamku gdzieś na świecie. Obecnie w zamku mieszka jedno lub więcej potworów, które musisz wypędzić, zanim uznasz zamek za swój.",
    ),
    (
        "_Void._ Your soul is drawn from your body and contained in an object in a place of the GM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is inert, ceases aging, and requires no food, air, or water. A _Życzenie_ spell can't return your soul to your body, but the spell reveals the location of the object that holds your soul. You draw no more cards.",
        "_Pustka._ Twoja dusza zostaje wyrwana z ciała i zamknięta w przedmiocie w miejscu wybranym przez MG. Miejsce strzeże jedno lub więcej potężnych istot. Dopóki twoja dusza jest uwięziona w ten sposób, twoje ciało jest obojętne, przestaje się starzeć i nie wymaga jedzenia, powietrza ani wody. Czar _Życzenie_ nie może zwrócić twojej duszy do ciała, ale ujawnia położenie przedmiotu, w którym jest zamknięta. Nie wyciągasz już więcej kart.",
    ),
    # Avatar of Death stat block
    ("_Medium Undead, Neutral Evil_", "_Średni nieumarły, neutralny zły_"),
    ("**PŻ** Half the PŻ maximum of its summoner <br>", "**PŻ** połowa maksimum PW przyzywającego <br>"),
    ("**Speed** 60 ft., Fly 60 ft. (hover) <br>", "**Szybkość** 18 m, lot 18 m (unosi się) <br>"),
    ("**Immunities** nekrotyczne, trucizna; Charmed, Exhaustion, Frightened, Paralyzed, Petrified, truciznaed, Unconscious<br>", "**Niewrażliwości** obrażenia nekrotyczne i od trucizny; zauroczony, wyczerpany, przerażony, sparaliżowany, skamieniały, zatruty, nieprzytomny<br>"),
    ("**Senses** Truesight 60 ft., Passive Perception 13<br>", "**Zmysły** prawdziwe widzenie 18 m, bierna Percepcja 13<br>"),
    ("**Languages** All languages known to its summoner<br>", "**Języki** wszystkie języki znane przyzywającemu<br>"),
    ("**CR** None (XP 0; PB equals its summoner's)", "**SW** brak (PD 0; PB równa PB przyzywającego)"),
    ("**_Incorporeal Movement._** The avatar can move through other creatures and objects as if they were Difficult Terrain. It takes 5 (1k10) moc damage if it ends its turn inside an object.", "**_Ruch bezcielesny._** Awatar może przechodzić przez inne stworzenia i przedmioty tak, jakby były trudnym terenem. Otrzymuje 5 (1k10) obrażeń od mocy, jeśli kończy turę wewnątrz obiektu."),
    ("**_Multiattack._** The avatar makes a number of Reaping Scythe attacks equal to half the summoner's Proficiency Bonus (rounded up).", "**_Atak wielokrotny._** Awatar wykonuje liczbę ataków Żniwną kosą równą połowie premii do biegłości przyzywającego (zaokrąglone w górę)."),
    ("**_Reaping Scythe._** _Melee Attack Roll:_ Automatic hit, reach 5 ft. _Hit:_ 7 (1k8 + 3) sieczne damage plus 4 (1k8) nekrotyczne damage.", "**_Żniwna kosa._** _Test ataku wręcz:_ automatyczne trafienie, zasięg 1,5 m. _Trafienie:_ 7 (1k8 + 3) obrażeń siecznych plus 4 (1k8) obrażeń nekrotycznych."),
    # Golem manual table
    ("<th>Time</th>", "<th>Czas</th>"),
    ("<th>Cost</th>", "<th>Koszt</th>"),
    ("<td>Clay Golem</td>", "<td>Golem gliniany</td>"),
    ("<td>30 days</td>", "<td>30 dni</td>"),
    ("<td>Flesh Golem</td>", "<td>Golem cieśniowy</td>"),
    ("<td>60 days</td>", "<td>60 dni</td>"),
    ("<td>Iron Golem</td>", "<td>Golem żelazny</td>"),
    ("<td>120 days</td>", "<td>120 dni</td>"),
    ("<td>Stone Golem</td>", "<td>Golem kamienny</td>"),
    ("<td>90 days</td>", "<td>90 dni</td>"),
    # Potions giant strength
    (
        """When you drink this potion, your Siła score changes for 1 hour. The type of giant determines the score (see the table below). The potion has no effect on you if your Siła is equal to or greater than that score.
This potion's transparent liquid has floating in it a sliver of light resembling a giant's fingernail.

<table>
  <thead>
    <tr>
      <th>Potion</th>
      <th>Str.</th>
      <th>Rarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Potion of Giant Strength (hill)</td>
      <td>21</td>
      <td>Uncommon</td>
    </tr>
    <tr>
      <td>Potion of Giant Strength (frost or stone)</td>
      <td>23</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>Potion of Giant Strength (fire)</td>
      <td>25</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>Potion of Giant Strength (cloud)</td>
      <td>27</td>
      <td>Very Rare</td>
    </tr>
    <tr>
      <td>Potion of Giant Strength (storm)</td>
      <td>29</td>
      <td>Legendary</td>
    </tr>
  </tbody>
</table>""",
        """Gdy wypijesz tę miksturę, twoja Siła zmienia się na 1 godzinę. Rodzaj olbrzyma określa wartość (patrz tabela poniżej). Mikstura nie ma na ciebie wpływu, jeśli twoja Siła jest równa tej wartości lub wyższa.
Przezroczysty płyn mikstury zawiera unoszącą się w nim smugę światła przypominającą paznokieć olbrzyma.

<table>
  <thead>
    <tr>
      <th>Mikstura</th>
      <th>Siła</th>
      <th>Rzadkość</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mikstura olbrzymiej siły (wzgórzowy)</td>
      <td>21</td>
      <td>niezwykła</td>
    </tr>
    <tr>
      <td>Mikstura olbrzymiej siły (lodowy lub kamienny)</td>
      <td>23</td>
      <td>rzadka</td>
    </tr>
    <tr>
      <td>Mikstura olbrzymiej siły (ogniowy)</td>
      <td>25</td>
      <td>rzadka</td>
    </tr>
    <tr>
      <td>Mikstura olbrzymiej siły (chmurowy)</td>
      <td>27</td>
      <td>bardzo rzadka</td>
    </tr>
    <tr>
      <td>Mikstura olbrzymiej siły (burzowy)</td>
      <td>29</td>
      <td>legendarna</td>
    </tr>
  </tbody>
</table>""",
    ),
    (
        """You regain PŻ when you drink this potion. The number of PŻ depends on the potion's rarity, as shown in the table below.
Whatever its potency, the potion's red liquid glimmers when agitated.

<table>
  <thead>
    <tr>
      <th>Potion</th>
      <th>HP Regained</th>
      <th>Rarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Potion of Healing</td>
      <td>2d4 + 2</td>
      <td>Common</td>
    </tr>
    <tr>
      <td>Potion of Healing (greater)</td>
      <td>4d4 + 4</td>
      <td>Uncommon</td>
    </tr>
    <tr>
      <td>Potion of Healing (superior)</td>
      <td>8d4 + 8</td>
      <td>Rare</td>
    </tr>
    <tr>
      <td>Potion of Healing (supreme)</td>
      <td>10d4 + 20</td>
      <td>Very Rare</td>
    </tr>
  </tbody>
</table>""",
        """Po wypiciu tej mikstury odzyskujesz PŻ. Liczba PŻ zależy od rzadkości mikstury, jak pokazano w tabeli poniżej.
Niezależnie od mocy, czerwony płyn mikstury mieni się po wstrząśnięciu.

<table>
  <thead>
    <tr>
      <th>Mikstura</th>
      <th>Odzyskane PŻ</th>
      <th>Rzadkość</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mikstura leczenia</td>
      <td>2k4 + 2</td>
      <td>pospolita</td>
    </tr>
    <tr>
      <td>Mikstura leczenia (większa)</td>
      <td>4k4 + 4</td>
      <td>niezwykła</td>
    </tr>
    <tr>
      <td>Mikstura leczenia (znakomita)</td>
      <td>8k4 + 8</td>
      <td>rzadka</td>
    </tr>
    <tr>
      <td>Mikstura leczenia (najwyższa)</td>
      <td>10k4 + 20</td>
      <td>bardzo rzadka</td>
    </tr>
  </tbody>
</table>""",
    ),
    (
        "For 1 minute after you drink this potion, you have odporność to all damage.\nThis potion's syrupy liquid looks like liquefied iron.",
        "Przez 1 minutę po wypiciu tej mikstury masz odporność na wszystkie obrażenia.\nSyropowaty płyn mikstury wygląda jak roztopione żelazo.",
    ),
    (
        """When you drink this potion, your physical age is reduced by 1d6 + 6 years, to a minimum of 13 years. Each time you subsequently drink a _Mikstura długowieczności_, there is 10 percent cumulative chance that you instead age by 1d6 + 6 years.
Suspended in this amber liquid is a tiny heart that, against all reason, is still beating. These ingredients vanish when the potion is opened.""",
        """Gdy wypijesz tę miksturę, twój fizyczny wiek zmniejsza się o 1k6 + 6 lat, minimum do 13 lat. Za każdym kolejnym wypiciem _Mikstury długowieczności_ istnieje łączna 10-procentowa szansa, że zamiast tego zestarzejesz się o 1k6 + 6 lat.
W bursztynowym płynie unosi się maleńkie serce, które wbrew rozumowi wciąż bije. Składniki znikają po otwarciu mikstury.""",
    ),
    (
        "When you drink this potion, you have odporność to one type of damage for 1 hour. The MG chooses the type or determines it randomly by rolling on the following table.",
        "Gdy wypijesz tę miksturę, masz odporność na jeden rodzaj obrażeń przez 1 godzinę. MG wybiera rodzaj albo określa go losowo, rzucając na poniższej tabeli.",
    ),
    (
        """When you drink this potion, it removes any Exhaustion levels you have and ends the Poisoned condition on you. For the next 24 hours, you regain the maximum number of PŻ for any Hit Point Die you spend.
This potion's crimson liquid regularly pulses with dull light, calling to mind a heartbeat.""",
        """Gdy wypijesz tę miksturę, usuwa wszystkie twoje poziomy wyczerpania i kończy na tobie stan zatruty. Przez następne 24 godziny odzyskujesz maksymalną liczbę PŻ za każdą wydaną Kość Wytrzymałości.\nKarmazynowy płyn mikstury regularnie pulsuje przyćmionym światłem, przypominając bicie serca.""",
    ),
    # Quarterstaff of Acrobacy
    (
        """You have a +2 bonus to attack rolls and damage rolls made with this magic weapon.
While holding this weapon, you can cause it to emit green Dim Light out to 10 feet, either as a akcję dodatkową or after you roll Initiative, or you can extinguish the light as a akcję dodatkową.
While holding this weapon, you can take a akcję dodatkową to alter its form, turning it into a 6-inch rod (for ease of storage) or a 10-foot pole, or reverting it a Quarterstaff; the weapon will elongate only as far as the surrounding space allows.
In certain forms, the weapon has the following additional properties.
_Acrobatic Assist (Quarterstaff and 10-Foot Pole Forms Only)._ While holding this weapon, you have ułatwienie on Zręczność (Acrobatics) checks.
_Attack Deflection (Quarterstaff Form Only)._ When you are hit by an attack while holding the weapon, you can take a reakcję to twirl the weapon around you, gaining a +5 bonus to your KP against the triggering attack, potentially causing the attack to miss you. You can't use this property again until you finish a Short or Long Rest.
_Ranged Weapon (Quarterstaff Form Only)._ This weapon has the Thrown property with a normal range of 30 feet and a long range of 120 feet. Immediately after you make a ranged attack with the weapon, it flies back to your hand.""",
        """Masz premię +2 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią.
Trzymając tę broń, możesz sprawić, że emituje zielone słabe światło w promieniu 3 metrów — jako akcję dodatkową albo po rzucie na inicjatywę — albo zgasić światło akcją dodatkową.
Trzymając tę broń, możesz wykonać akcję dodatkową, aby zmienić jej formę, zamieniając ją w 15-centymetrowy pręt (dla wygody przechowywania) albo 3-metrowy kij, albo przywracając formę kostura; broń wydłuża się tylko tak daleko, jak pozwala otaczająca przestrzeń.
W określonych formach broń ma następujące dodatkowe właściwości.
_Pomoc akrobatyczna (tylko forma kostura i 3-metrowego kija)._ Trzymając tę broń, masz ułatwienie w testach Zręczności (Akrobatyka).
_Odbicie ataku (tylko forma kostura)._ Gdy zostaniesz trafiony atakiem, trzymając broń, możesz wykonać reakcję, aby zakręcić nią wokół siebie, zyskując premię +5 do KP przeciw wywołującemu atakowi, co może sprawić, że atak cię nie trafi. Nie możesz ponownie użyć tej właściwości, dopóki nie ukończysz krótkiego lub długiego odpoczynku.
_Broń rzucana (tylko forma kostura)._ Ta broń ma właściwość Rzucana ze zwykłym zasięgiem 9 metrów i dalekim 36 metrów. Zaraz po ataku dystansowym tą bronią wraca ona do twojej dłoni.""",
    ),
    ("_Broń (Quarterstaff), bardzo rzadki (wymaga zestrojenia)_", "_Broń (kostur), bardzo rzadki (wymaga zestrojenia)_"),
    # Regaining Charges / Retributive Strike - generic patterns
    (
        "_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff crumbles into cinders and is destroyed.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur rozpada się w popiół i zostaje zniszczony.",
    ),
    (
        "_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff turns to water and is destroyed.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur zamienia się w wodę i zostaje zniszczony.",
    ),
    (
        "_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff vanishes in a flash of light, lost forever.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur znika w błysku światła i zostaje na zawsze utracony.",
    ),
    (
        "_Regaining Charges._ The staff regains 2d8 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff retains its +2 bonus to attack rolls and damage rolls but loses all other properties. On a 20, the staff regains 1d8 + 2 charges.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 2k8 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur zachowuje premię +2 do testów ataku i obrażeń, ale traci wszystkie inne właściwości. Przy wyniku 20 kostur odzyskuje 1k8 + 2 ładunki.",
    ),
    (
        "_Regaining Charges._ The staff regains 4d6 + 2 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 20, the staff regains 1d12 + 1 charges.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 4k6 + 2 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 20 kostur odzyskuje 1k12 + 1 ładunków.",
    ),
    (
        "_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, a swarm of insects consumes and destroys the staff, then disperses.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 rój owadów pożera i niszczy kostur, po czym się rozprasza.",
    ),
    (
        "_Retributive Strike._ You can take a Magic action to break the staff over your knee or against a solid surface. The staff is destroyed and releases its magic in an explosion that fills a 30-foot Emanation originating from itself. You have a 50 percent chance to instantly travel to a random plane of existence, avoiding the explosion. If you fail to avoid the effect, you take moc damage equal to 16 times the number of charges in the staff. Each other creature in the area makes a DC 17 Dexterity saving throw. On a failed save, a creature takes moc damage equal to 4 times the number of charges in the staff. On a successful save, a creature takes half as much damage.",
        "_Karzące uderzenie._ Możesz wykonać akcję magiczną, aby złamać kostur na kolanie lub o twardą powierzchnię. Kostur zostaje zniszczony i uwalnia magię w eksplozji wypełniającej promień o zasięgu 9 metrów wychodzący od niego. Masz 50 procent szans na natychmiastowe przeniesienie się do losowej sfery egzystencji, unikając eksplozji. Jeśli nie unikniesz efektu, otrzymujesz obrażenia od mocy równe 16 × liczba ładunków w kosturze. Każde inne stworzenie w obszarze wykonuje rzut obronny na Zręczność o ST 17. W przypadku niepowodzenia stworzenie otrzymuje obrażenia od mocy równe 4 × liczba ładunków w kosturze. W przypadku sukcesu otrzymuje połowę obrażeń.",
    ),
    (
        "_Retributive Strike._ You can take a Magic action to break the staff over your knee or against a solid surface. The staff is destroyed and releases its magic in an explosion that fills a 30-foot Emanation originating from itself. You have a 50 percent chance to instantly travel to a random plane of existence, avoiding the explosion. If you fail to avoid the effect, you take moc damage equal to 16 times the number of charges in the staff. Each other creature in the area makes a DC 17 Dexterity saving throw. On a failed save, a creature takes moc damage equal to 6 times the number of charges in the staff. On a successful save, a creature takes half as much damage.",
        "_Karzące uderzenie._ Możesz wykonać akcję magiczną, aby złamać kostur na kolanie lub o twardą powierzchnię. Kostur zostaje zniszczony i uwalnia magię w eksplozji wypełniającej promień o zasięgu 9 metrów wychodzący od niego. Masz 50 procent szans na natychmiastowe przeniesienie się do losowej sfery egzystencji, unikając eksplozji. Jeśli nie unikniesz efektu, otrzymujesz obrażenia od mocy równe 16 × liczba ładunków w kosturze. Każde inne stworzenie w obszarze wykonuje rzut obronny na Zręczność o ST 17. W przypadku niepowodzenia stworzenie otrzymuje obrażenia od mocy równe 6 × liczba ładunków w kosturze. W przypadku sukcesu otrzymuje połowę obrażeń.",
    ),
    (
        "_Shooting Stars._ You can expend 1 to 3 charges as a Magic action. For every charge you expend, you launch a glowing mote of light from the ring at a point you can see within 60 feet of yourself. Each creature in a 15-foot Cube originating from that point is showered in sparks and makes a DC 15 Dexterity saving throw, taking 5d4 promieniujące damage on a failed save or half as much damage on a successful one.",
        "_Spadające gwiazdy._ Możesz wydać od 1 do 3 ładunków jako akcję magiczną. Za każdy wydany ładunek wystrzeliwujesz z pierścienia świecącą iskierkę w punkt, który widzisz w promieniu 18 metrów od siebie. Każde stworzenie w sześcianie o boku 4,5 metra wychodzącym z tego punktu zostaje pokryte iskrami i wykonuje rzut obronny na Zręczność o ST 15, otrzymując 5k4 obrażeń od promieniowania w przypadku niepowodzenia albo połowę obrażeń w przypadku sukcesu.",
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
