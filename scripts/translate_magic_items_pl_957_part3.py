#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    # Hat of Many Spells
    (
        """This pointed hat has the following properties.
_Spellcasting Focus._ While holding the hat, you can use it as a Spellcasting Focus for your Wizard spells. Any spell you cast using the hat gains a special Somatic component: you must reach into the hat and "pull" the spell out of it.
_Unknown Spell._ While holding the hat, you can try to cast a level 1+ spell you don't know. The spell must be on the Wizard spell list, it must be of a level you can cast, and it can't have Material components costing more than 1,000 sz. Once you decide on the spell, you must expend a spell slot of the spell's level. Then, to determine whether you cast the spell, make an Inteligencja (Wiedza tajemna) check (ST 10 plus the spell's level). On a successful check, you cast the spell using its normal casting time, and you can't use this property again until you finish a Short or Long Rest. On a failed check, you fail to cast the spell and a random effect occurs instead, determined by rolling on the following table.
Any spell you cast from the hat uses your spell save DC and spell attack bonus.""",
        """Ten spiczasty kapelusz ma następujące właściwości.
_Fokus rzucania czarów._ Trzymając kapelusz, możesz używać go jako fokusu rzucania czarów do czarów Maga. Każdy czar rzucony za jego pomocą zyskuje specjalny komponent somatyczny: musisz sięgnąć do kapelusza i „wyciągnąć” z niego czar.
_Nieznany czar._ Trzymając kapelusz, możesz spróbować rzucić czar 1. kręgu lub wyższego, którego nie znasz. Czar musi znajdować się na liście czarów Maga, musi być z kręgu, który potrafisz rzucić, i nie może mieć komponentów materialnych o koszcie powyżej 1000 sz. Gdy zdecydujesz się na czar, musisz wydać komórkę czaru odpowiedniego kręgu. Następnie, aby ustalić, czy rzuciłeś czar, wykonaj test Inteligencji (Wiedza tajemna) o ST 10 plus krąg czaru. W przypadku sukcesu rzucasz czar z normalnym czasem rzucania i nie możesz ponownie użyć tej właściwości, dopóki nie ukończysz krótkiego lub długiego odpoczynku. W przypadku niepowodzenia nie udaje ci się rzucić czaru i zamiast tego występuje losowy efekt określony rzutem na poniższej tabeli.
Każdy czar rzucony z kapelusza używa twojego ST rzutu przeciw czarom i premii do ataku czarem.""",
    ),
    (
        '<td>You cast a random spell determined by rolling 1k10: on a **1**, *Enlarge/Reduce* (enlarge effect); on a **2**, *Enlarge/Reduce* (reduce effect); on a **3**, *Faerie ogień*; on a **4**, *ogieńball*; on a **5**, *Gust of Wind*; on a **6**, *Invisibility* (cast on yourself); on a **7**, *elektryczność Bolt*; on an **8**, *Phantasmal moc*; on a **9**, *Polymorph*; on a **10**, *Stinking Cloud*.</td>',
        '<td>Rzucasz losowy czar określony rzutem 1k10: przy **1** — _powiększenie/pomniejszenie_ (efekt powiększający); przy **2** — _powiększenie/pomniejszenie_ (efekt pomniejszający); przy **3** — _blask wróżki_; przy **4** — _kula ognia_; przy **5** — _podmuch wiatru_; przy **6** — _niewidzialność_ (na siebie); przy **7** — _piorun_; przy **8** — _fantasmalna siła_; przy **9** — _polimorfia_; przy **10** — _śmierdząca chmura_.</td>',
    ),
    (
        '<td>You have the Stunned condition until the end of your next turn, believing something awesome just happened.</td>',
        '<td>Masz stan ogłuszony do końca swojej następnej tury, wierząc, że właśnie stało się coś niesamowitego.</td>',
    ),
    (
        '<td>A harmless swarm of butterflies fills a 10-foot Cube within 30 feet of yourself. The swarm disperses after 1 minute.</td>',
        '<td>Nieszkodliwy rój motyli wypełnia sześcian o boku 3 metry w promieniu 9 metrów od ciebie. Rój rozprasza się po 1 minucie.</td>',
    ),
    (
        '<td>You pull a nonmagical object out of the hat. Roll 1k4 to determine the object: on a **1**, a vial of kwas; on a **2**, a flask of Alchemist\'s ogień; on a **3**, a Crowbar; on a **4**, a lit Torch.</td>',
        '<td>Wyciągasz z kapelusza niemagiczny przedmiot. Rzuć 1k4, aby określić przedmiot: przy **1** — fiolka kwasu; przy **2** — flaszka ognia alchemicznego; przy **3** — łom; przy **4** — zapalona pochodnia.</td>',
    ),
    (
        '<td>You suffer a bout of magic sickness and have the truciznaed condition for 1 hour.</td>',
        '<td>Dostajesz ataku magicznej choroby i masz stan zatruty przez 1 godzinę.</td>',
    ),
    (
        '<td>You have the Petrified condition until the end of your next turn.</td>',
        '<td>Masz stan skamieniały do końca swojej następnej tury.</td>',
    ),
    (
        '<td>You pull a nonmagical object out of the hat. Roll 1k4 to determine the object: on a **1**, a Dagger; on a **2**, a Rope with a Grappling Hook tied to one end; on a **3**, a bag of Caltrops; on a **4**, a gem worth 50 GP.</td>',
        '<td>Wyciągasz z kapelusza niemagiczny przedmiot. Rzuć 1k4, aby określić przedmiot: przy **1** — sztylet; przy **2** — lina z hakiem wspinaczkowym przywiązanym do jednego końca; przy **3** — worek kolców; przy **4** — klejnot wart 50 sz.</td>',
    ),
    (
        '<td>A creature appears in an unoccupied space as close to you as possible. The creature isn\'t under your control and acts as it normally would, and it disappears after 1 hour or when it drops to 0 Hit Points. Roll 1k4 to determine the creature: on a **1**, a **Camel**; on a **2**, a **Constrictor Snake**; on a **3**, an **Elephant**; on a **4**, a **Mule**.</td>',
        '<td>Stworzenie pojawia się w niezajętej przestrzeni tak blisko ciebie, jak to możliwe. Nie jest pod twoją kontrolą i działa normalnie, znikając po 1 godzinie albo gdy jego PW spadną do 0. Rzuć 1k4, aby określić stworzenie: przy **1** — **wielbłąd**; przy **2** — **wąż dusiciel**; przy **3** — **słoń**; przy **4** — **muł**.</td>',
    ),
    (
        '<td>A Hostile **Swarm of Bats** flies out of the hat, occupies your space, and attacks you.</td>',
        '<td>Wrogi **rój nietoperzy** wylatuje z kapelusza, zajmuje twoją przestrzeń i cię atakuje.</td>',
    ),
    (
        '<td>A vertical, 10-foot-diameter, two-way portal to another plane of existence opens in an unoccupied space within 30 feet of you and remains open until the end of your next turn. The GM determines where it leads.</td>',
        '<td>Pionowy, dwukierunkowy portal o średnicy 3 metry do innej sfery egzystencji otwiera się w niezajętej przestrzeni w promieniu 9 metrów od ciebie i pozostaje otwarty do końca twojej następnej tury. MG określa, dokąd prowadzi.</td>',
    ),
    (
        '<td>You pull a magic item out of the hat. Roll 1k6 to determine the item\'s rarity: on a **1–3**, Common; on a **4–5**, Uncommon; on a **6**, Rare. The GM chooses the item, which disappears after 1 hour if it\'s not consumed or destroyed before then.</td>',
        '<td>Wyciągasz z kapelusza magiczny przedmiot. Rzuć 1k6, aby określić jego rzadkość: przy **1–3** — pospolity; przy **4–5** — niezwykły; przy **6** — rzadki. MG wybiera przedmiot, który znika po 1 godzinie, jeśli wcześniej nie zostanie zużyty lub zniszczony.</td>',
    ),
    (
        "_Cudowny przedmiot, bardzo rzadki (wymaga zestrojenia by a Wizard)_",
        "_Cudowny przedmiot, bardzo rzadki (wymaga zestrojenia przez maga)_",
    ),
    # Holy Avenger
    (
        """You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. When you hit a Fiend or an Undead with it, that creature takes an extra 2d10 Radiant damage.
While you hold the drawn weapon, it creates a 10-foot Emanation originating from you. You and all creatures przyjazny to you in the Emanation have ułatwienie on saving throws against spells and other magical effects. If you have 17 or more levels in the Paladin class, the size of the Emanation increases to 30 feet.""",
        """Zyskujesz premię +3 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią. Gdy trafisz nią czarta lub nieumarłego, to stworzenie otrzymuje dodatkowe 2k10 obrażeń od światłości.
Gdy trzymasz wyciągniętą broń, tworzy ona promień o zasięgu 3 metrów wychodzący od ciebie. Ty i wszystkie przyjazne ci stworzenia w tym promieniu macie ułatwienie w rzutach obronnych przeciw czarom i innym magicznym efektom. Jeśli masz co najmniej 17 poziomów w klasie paladyna, zasięg promienia wzrasta do 9 metrów.""",
    ),
    (
        "_Cudowny przedmiot, legendarny (wymaga zestrojenia by a Paladin)_",
        "_Cudowny przedmiot, legendarny (wymaga zestrojenia przez paladyna)_",
    ),
    # Horn of Valhalla
    (
        """You can take a akcję magiczną to blow this horn. In response, warrior spirits from the plane of Ysgard appear in unoccupied spaces within 60 feet of you. Each spirit uses the **Berserker** stat block and returns to Ysgard after 1 hour or when it drops to 0 PŻ. The spirits look like living, breathing warriors, and they have niewrażliwość to the Charmed and Frightened conditions. Once you use the horn, it can't be used again until 7 days have passed.
Four types of _Róg Valhalli_ are known to exist, each made of a different metal. The horn's type determines how many spirits it summons, as well as the requirement for its use. The MG chooses the horn's type or determines it randomly by rolling on the following table.
If you blow the horn without meeting its requirement, the summoned spirits attack you. If you meet the requirement, they are przyjazny to you and your allies and follow your commands.""",
        """Możesz wykonać akcję magiczną, aby zadąć w ten róg. W odpowiedzi duchy wojowników z sfery Ysgard pojawiają się w niezajętych przestrzeniach w promieniu 18 metrów od ciebie. Każdy duch używa bloku statystyk **berserkera** i wraca do Ysgardu po 1 godzinie albo gdy jego PŻ spadną do 0. Duchy wyglądają jak żywi, oddychający wojownicy i mają niewrażliwość na stany zauroczony i przerażony. Po użyciu rogu nie można go użyć ponownie przez 7 dni.
Znane są cztery rodzaje _Rogu Valhalli_, każdy z innego metalu. Rodzaj rogu określa liczbę przyzywanych duchów oraz wymaganie do jego użycia. MG wybiera rodzaj rogu albo określa go losowo, rzucając na poniższej tabeli.
Jeśli zagrasz na rogu bez spełnienia wymagania, przyzwane duchy cię atakują. Jeśli spełnisz wymaganie, są przyjazne tobie i twoim sojusznikom i wykonują twoje polecenia.""",
    ),
    (
        """<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Horn Type</th>
      <th>Spirits</th>
      <th>Requirement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–40</td>
      <td>Silver</td>
      <td>2</td>
      <td>None</td>
    </tr>
    <tr>
      <td>41–75</td>
      <td>Brass</td>
      <td>3</td>
      <td>Proficiency with all Simple weapons</td>
    </tr>
    <tr>
      <td>76–90</td>
      <td>Bronze</td>
      <td>4</td>
      <td>Training with all Medium armor</td>
    </tr>
    <tr>
      <td>91–00</td>
      <td>Iron</td>
      <td>5</td>
      <td>Proficiency with all Martial weapons</td>
    </tr>
  </tbody>
</table>""",
        """<table>
  <thead>
    <tr>
      <th>1k100</th>
      <th>Rodzaj rogu</th>
      <th>Duchy</th>
      <th>Wymaganie</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>01–40</td>
      <td>Srebrny</td>
      <td>2</td>
      <td>Brak</td>
    </tr>
    <tr>
      <td>41–75</td>
      <td>Mosiężny</td>
      <td>3</td>
      <td>Biegłość we wszystkich prostych broniach</td>
    </tr>
    <tr>
      <td>76–90</td>
      <td>Brązowy</td>
      <td>4</td>
      <td>Szkolenie we wszystkich średnich zbrojach</td>
    </tr>
    <tr>
      <td>91–00</td>
      <td>Żelazny</td>
      <td>5</td>
      <td>Biegłość we wszystkich wojskowych broniach</td>
    </tr>
  </tbody>
</table>""",
    ),
    (
        "_Cudowny przedmiot, rzadki (Silver or Brass), bardzo rzadki (Bronze), or legendarny (Iron)_",
        "_Cudowny przedmiot, rzadki (srebrny lub mosiężny), bardzo rzadki (brązowy) lub legendarny (żelazny)_",
    ),
    # Ioun Stones intro + properties
    (
        """Roughly marble sized, _Ioun Stones_ are named after Ioun, a god of knowledge and prophecy revered on some worlds. Many types of _Ioun Stones_ exist, each type a distinct combination of shape and color.
When you take a akcję magiczną to toss an _Kamień Iouna_ into the air, the stone orbits your head at a distance of 1d3 feet, conferring its benefit to you while doing so. You can have up to three _Ioun Stones_ orbiting your head at the same time.
Each _Kamień Iouna_ orbiting your head is considered to be an object you are wearing. The orbiting stone avoids contact with other creatures and objects, adjusting its orbit to avoid collisions and thwarting all attempts by other creatures to attack or snatch it.
As a akcję Użycie, you can seize and stow any number of _Ioun Stones_ orbiting your head. If your Attunement to an _Kamień Iouna_ ends while it's orbiting your head, the stone falls as though you had dropped it.
The type of stone determines its rarity and effects.""",
        """_Kamienie Iouna_ mają mniej więcej rozmiar kuli bilardowej i nazwane są od Ioun, bóstwa wiedzy i proroctwa czczoną na niektórych światach. Istnieje wiele rodzajów _Kamieni Iouna_, z których każdy to odrębna kombinacja kształtu i koloru.
Gdy wykonasz akcję magiczną, aby podrzucić _Kamień Iouna_ w powietrze, kamień krąży wokół twojej głowy w odległości 1k3 stóp, zapewniając ci swoją korzyść. Możesz mieć jednocześnie do trzech _Kamieni Iouna_ krążących wokół głowy.
Każdy _Kamień Iouna_ krążący wokół twojej głowy uznaje się za przedmiot, który nosisz. Krążący kamień unika kontaktu z innymi stworzeniami i przedmiotami, dostosowując orbitę, aby uniknąć kolizji, i udaremnia wszelkie próby ataku lub wyrwania go przez inne stworzenia.
Jako akcję Użycie możesz chwycić i schować dowolną liczbę _Kamieni Iouna_ krążących wokół głowy. Jeśli twoje zestrojenie z _Kamieniem Iouna_ kończy się, gdy krąży on wokół głowy, kamień spada, jakbyś go upuścił.
Rodzaj kamienia określa jego rzadkość i efekty.""",
    ),
    (
        "_Absorption (Very Rare)_. While this pale lavender ellipsoid orbits your head, you can take a reakcję to cancel a spell of level 4 or lower cast by a creature you can see. A canceled spell has no effect, and any resources used to cast it are wasted. Once the stone has canceled 20 levels of spells, it burns out, turns dull gray, and loses its magic.",
        "_Absorpcja (bardzo rzadki)._ Dopóki ten blado-lawendowy elipsoid krąży wokół twojej głowy, możesz wykonać reakcję, aby anulować czar 4. kręgu lub niższego rzucony przez stworzenie, które widzisz. Anulowany czar nie ma efektu, a wszelkie zasoby użyte do jego rzucenia przepadają. Gdy kamień anuluje łącznie 20 kręgów czarów, wypala się, szarzeje i traci magię.",
    ),
    (
        "_Agility (Very Rare)_. Your Zręczność increases by 2, to a maximum of 20, while this deep-red sphere orbits your head.",
        "_Zwinność (bardzo rzadki)._ Twoja Zręczność wzrasta o 2, maksymalnie do 20, dopóki ta głęboko czerwona sfera krąży wokół twojej głowy.",
    ),
    (
        "_Awareness (Rare)_. While this dark-blue rhomboid orbits your head, you have ułatwienie on Initiative rolls and Mądrość (Perception) checks.",
        "_Czujność (rzadki)._ Dopóki ten ciemnoniebieski romb krąży wokół twojej głowy, masz ułatwienie w rzutach na inicjatywę i testach Mądrości (Percepcja).",
    ),
    (
        "_Fortitude (Very Rare)_. Your Kondycja increases by 2, to a maximum of 20, while this pink rhomboid orbits your head.",
        "_Hart (bardzo rzadki)._ Twoja Kondycja wzrasta o 2, maksymalnie do 20, dopóki ten różowy romb krąży wokół twojej głowy.",
    ),
    (
        "_Greater Absorption (Legendary)_. While this marbled lavender and green ellipsoid orbits your head, you can take a reakcję to cancel a spell of level 8 or lower cast by a creature you can see. A canceled spell has no effect, and any resources used to cast it are wasted. Once the stone has canceled 20 levels of spells, it burns out, turns dull gray, and loses its magic.",
        "_Większa absorpcja (legendarny)._ Dopóki ten marmurkowy lawendowo-zielony elipsoid krąży wokół twojej głowy, możesz wykonać reakcję, aby anulować czar 8. kręgu lub niższego rzucony przez stworzenie, które widzisz. Anulowany czar nie ma efektu, a wszelkie zasoby użyte do jego rzucenia przepadają. Gdy kamień anuluje łącznie 20 kręgów czarów, wypala się, szarzeje i traci magię.",
    ),
    (
        "_Insight (Very Rare)_. Your Mądrość increases by 2, to a maximum of 20, while this incandescent blue sphere orbits your head.",
        "_Wnikliwość (bardzo rzadki)._ Twoja Mądrość wzrasta o 2, maksymalnie do 20, dopóki ta żarząco niebieska sfera krąży wokół twojej głowy.",
    ),
    (
        "_Intellect (Very Rare)_. Your Inteligencja increases by 2, to a maximum of 20, while this marbled scarlet and blue sphere orbits your head.",
        "_Intelekt (bardzo rzadki)._ Twoja Inteligencja wzrasta o 2, maksymalnie do 20, dopóki ta marmurkowa szkarłatno-niebieska sfera krąży wokół twojej głowy.",
    ),
    (
        "_Leadership (Very Rare)_. Your Charyzma increases by 2, to a maximum of 20, while this marbled pink and green sphere orbits your head.",
        "_Przywództwo (bardzo rzadki)._ Twoja Charyzma wzrasta o 2, maksymalnie do 20, dopóki ta marmurkowa różowo-zielona sfera krąży wokół twojej głowy.",
    ),
    (
        "_Mastery (Legendary)._ Your premię do biegłości increases by 1 while this pale green prism orbits your head.",
        "_Mistrzostwo (legendarny)._ Twoja premia do biegłości wzrasta o 1, dopóki ten bladozielony pryzmat krąży wokół twojej głowy.",
    ),
    (
        "_Protection (Rare)._ You gain a +1 bonus to KP while this dusty-rose prism orbits your head.",
        "_Ochrona (rzadki)._ Zyskujesz premię +1 do KP, dopóki ten pyłowo-różowy pryzmat krąży wokół twojej głowy.",
    ),
    (
        "_Regeneration (Legendary)._ You regain 15 PŻ at the end of each hour this pearly white spindle orbits your head if you have at least 1 Hit Point.",
        "_Regeneracja (legendarny)._ Odzyskujesz 15 PŻ na koniec każdej godziny, dopóki ten perłowo biały wrzecionowaty kamień krąży wokół twojej głowy, pod warunkiem że masz co najmniej 1 PW.",
    ),
    (
        """_Reserve (Rare)._ This vibrant purple prism stores spells cast into it, holding them until you use them. The stone can store up to 4 levels of spells at a time. When found, it contains 1d4 levels of stored spells chosen by the MG.
Any creature can cast a spell of level 1 through 4 into the stone by touching it as the spell is cast. The spell has no effect, other than to be stored in the stone. If the stone can't hold the spell, the spell is expended without effect. The level of the slot used to cast the spell determines how much space it uses.
While this stone orbits your head, you can cast any spell stored in it. The spell uses the slot level, spell save DC, spell attack bonus, and spellcasting ability of the original caster but is otherwise treated as if you cast the spell. The spell cast from the stone is no longer stored in it, freeing up space.""",
        """_Rezerwa (rzadki)._ Ten żywy fioletowy pryzmat przechowuje w niego rzucone czary, trzymając je do chwili użycia. Kamień może przechowywać jednocześnie do 4 kręgów czarów. Po znalezieniu zawiera 1k4 kręgów zapisanych czarów wybranych przez MG.
Każde stworzenie może rzucić w kamień czar 1.–4. kręgu, dotykając go podczas rzucania. Czar nie wywołuje efektu poza zapisaniem w kamieniu. Jeśli kamień nie może go pomieścić, czar zostaje zmarnowany. Krąg komórki użytej do rzucenia określa, ile miejsca zajmuje.
Dopóki ten kamień krąży wokół twojej głowy, możesz rzucić dowolny zapisany w nim czar. Czar używa kręgu komórki, ST rzutu przeciw czarom, premii do ataku czarem i cechy bazowej pierwotnego rzucającego, ale poza tym jest traktowany tak, jakbyś rzucił go ty. Czar rzucony z kamienia nie jest już w nim przechowywany, co zwalnia miejsce.""",
    ),
    (
        "_Strength (Very Rare)._ Your Siła increases by 2, to a maximum of 20, while this pale blue rhomboid orbits your head.",
        "_Siła (bardzo rzadki)._ Twoja Siła wzrasta o 2, maksymalnie do 20, dopóki ten bladoniebieski romb krąży wokół twojej głowy.",
    ),
    (
        "_Sustenance (Rare)._ You don't need to eat or drink while this clear spindle orbits your head.",
        "_Utrzymanie (rzadki)._ Nie musisz jeść ani pić, dopóki ten przezroczysty wrzecionowaty kamień krąży wokół twojej głowy.",
    ),
    # Iron Bands
    (
        """This rusty iron sphere measures 3 inches in diameter and weighs 1 pound. You can take a akcję magiczną to throw the sphere at a Huge or smaller creature you can see within 60 feet of yourself. As the sphere moves through the air, it opens into a tangle of metal bands.
Make a ranged test ataku with an attack bonus equal to your Zręczność modifier plus your premię do biegłości. On a hit, the target has the Restrained condition until you take a akcję dodatkową to issue a command that releases it. Doing so or missing with the attack causes the bands to contract and become a sphere once more.
A creature that can touch the bands, including the one Restrained, can take an action to make a ST 20 Siła (Athletics) check to break the iron bands. On a successful check, the item is destroyed, and the Restrained creature is freed. On a failed check, any further attempts made by that creature automatically fail until 24 hours have elapsed.
Once the bands are used, they can't be used again until the następny świt.""",
        """Ta zardzewiała żelazna kula ma 7,5 centymetra średnicy i waży około 0,5 kilograma. Możesz wykonać akcję magiczną, aby rzucić kulą w olbrzymie lub mniejsze stworzenie, które widzisz w promieniu 18 metrów od siebie. Gdy kula przemieszcza się w powietrzu, rozwija się w splątanie metalowych obręczy.
Wykonaj dystansowy test ataku z premią równą twojemu modyfikatorowi ze Zręczności plus twojej premii do biegłości. Przy trafieniu cel ma stan pochwycony, dopóki nie wykonasz akcji dodatkowej, aby wydać polecenie uwolnienia go. To działanie albo pudło powoduje, że obręcze kurczą się i znów stają się kulą.
Stworzenie, które może dotknąć obręczy, w tym pochwytone, może wykonać akcję i test Siły (Atletyka) o ST 20, aby zerwać żelazne obręcze. W przypadku sukcesu przedmiot zostaje zniszczony, a pochwytone stworzenie zostaje uwolnione. W przypadku niepowodzenia wszelkie dalsze próby tego stworzenia kończą się automatyczną porażką przez następne 24 godziny.
Po użyciu obręczy nie można ich użyć ponownie do następnego świtu.""",
    ),
    # Luck Blade
    (
        """You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. While the weapon is on your person, you also gain a +1 bonus to saving throws.
_Luck._ If the weapon is on your person, you can call on its luck (no action required) to reroll one failed D20 Test if you don't have the Incapacitated condition. You must use the second roll. Once used, this property can't be used again until the następny świt.
_Wish._ The weapon has 1d3 charges. While holding it, you can expend 1 charge and cast _Życzenie_ from it. Once used, this property can't be used again until the następny świt. The weapon loses this property if it has no charges.""",
        """Zyskujesz premię +1 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią. Dopóki broń jest przy tobie, zyskujesz też premię +1 do rzutów obronnych.
_Szczęście._ Jeśli broń jest przy tobie, możesz (bez akcji) odwołać się do jej szczęścia i przerzucić jeden nieudany test k20, pod warunkiem że nie masz stanu obezwładniony. Musisz użyć drugiego wyniku. Po użyciu tej właściwości nie można jej użyć ponownie do następnego świtu.
_Życzenie._ Broń ma 1k3 ładunków. Trzymając ją, możesz wydać 1 ładunek i rzucić z niej _Życzenie_. Po użyciu tej właściwości nie można jej użyć ponownie do następnego świtu. Broń traci tę właściwość, gdy nie ma ładunków.""",
    ),
    # Mithral armor
    (
        "Mithral is a light, flexible metal. Armor made of this substance can be worn under normal clothes. If the armor normally imposes Disadvantage on Zręczność (Stealth) checks or has a Siła requirement, the mithral version of the armor doesn't.",
        "Mithril to lekki, elastyczny metal. Zbroję z tego materiału można nosić pod zwykłym ubraniem. Jeśli zbroja normalnie nakłada utrudnienie w testach Zręczności (Skradanie się) albo ma wymaganie Siły, wersja mithrilowa tego pancerza nie ma tych ograniczeń.",
    ),
    # Nine Lives Stealer
    (
        """You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon.
**_Life Stealing._** The weapon has 1d8 + 1 charges. When you attack a creature that has fewer than 100 PŻ with this weapon and roll a 20 on the d20 for the test ataku, the creature must succeed on a ST 15 Kondycja rzut obronny or be slain instantly as the sword tears its life force from its body. Constructs and Undead succeed on the save automatically. The weapon loses 1 charge if the creature is slain. When the weapon has no charges remaining, it loses this property.""",
        """Zyskujesz premię +2 do testów ataku i rzutów na obrażenia zadawanych tą magiczną bronią.
**_Kradzież życia._** Broń ma 1k8 + 1 ładunków. Gdy atakujesz tą bronią stworzenie mające mniej niż 100 PŻ i wyrzucisz 20 na k20 w teście ataku, stworzenie musi odnieść sukces w rzucie obronnym na Kondycję o ST 15, w przeciwnym razie ginie natychmiast, gdy miecz wyrwie z niego siłę życiową. Konstrukty i nieumarli odnoszą sukces w tym rzucie automatycznie. Broń traci 1 ładunek, jeśli stworzenie zostaje zabite. Gdy broń nie ma pozostałych ładunków, traci tę właściwość.""",
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
