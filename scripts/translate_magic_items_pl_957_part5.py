#!/usr/bin/env python3
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/magic-items.md"

REPLACEMENTS = [
    # Ring of Elemental Command
    (
        """Each _Pierścień władania żywiołami_ is linked to one of the four Elemental Planes. The MG chooses or randomly determines the linked plane. For example, a _Pierścień władania żywiołami_ (air) is linked to the Elemental Plane of Air.
Every _Pierścień władania żywiołami_ has the following two properties:
**Elemental Bane.** While wearing the ring, you have ułatwienie on attack rolls against Elementals and they have Disadvantage on attack rolls against you.
**Elemental Compulsion.** While wearing the ring, you can take a akcję magiczną to try to compel an Elemental you see within 60 feet of yourself. The Elemental makes a ST 18 Mądrość rzut obronny. On a failed save, the Elemental has the Charmed condition until the start your next turn, and you determine what it does with its move and action on its next turn.
_Elemental Focus._ While wearing the ring, you benefit from additional properties corresponding to the ring's linked Elemental Plane:
**Air.** You know Auran, you have odporność to Lightning damage, and you have a Fly Speed equal to your Speed and can hover.
**Earth.** You know Terran, and you have odporność to Acid damage. Terrain composed of rubble, rocks, or dirt isn't Difficult Terrain for you. In addition, you can move through solid earth or rock as if those areas were Difficult Terrain without disturbing the matter through which you pass. If you end your turn in solid earth or rock, you are shunted out to the nearest unoccupied space you last occupied.
**Fire.** You know Ignan, and you have niewrażliwość to Fire damage.
**Water.** You know Aquan, you gain a Swim Speed of 60 feet, and you can breathe underwater.
_Spellcasting._ The ring has 5 charges and regains 1d4 + 1 expended charges daily at dawn. While wearing the ring, you can cast a spell from it. Choose the spell from the list of available spells based on the Elemental Plane the ring is linked to, as shown in the following table. The table indicates how many charges you must expend to cast the spell, which has a save DC of 18.""",
        """Każdy _Pierścień władania żywiołami_ jest powiązany z jedną z czterech Sfer Żywiołów. MG wybiera albo losowo określa powiązaną sferę. Na przykład _Pierścień władania żywiołami_ (powietrze) jest powiązany ze Sferą Żywiołu Powietrza.
Każdy _Pierścień władania żywiołami_ ma następujące dwie właściwości:
**Zmora żywiołaków.** Nosząc pierścień, masz ułatwienie w testach ataku przeciw żywiołakom, a one mają utrudnienie w testach ataku przeciwko tobie.
**Przymus żywiołaka.** Nosząc pierścień, możesz wykonać akcję magiczną, aby spróbować zmusić żywiołaka, którego widzisz w promieniu 18 metrów od siebie. Żywiołak wykonuje rzut obronny na Mądrość o ST 18. W przypadku niepowodzenia ma stan zauroczony do początku twojej następnej tury i sam decydujesz, co zrobi swoim ruchem i akcją w następnej turze.
_Fokus żywiołowy._ Nosząc pierścień, korzystasz z dodatkowych właściwości odpowiadających powiązanej Sferze Żywiołu:
**Powietrze.** Znasz auran, masz odporność na obrażenia od elektryczności oraz szybkość lotu równą swojej szybkości chodzenia i możesz unosić się w powietrzu.
**Ziemia.** Znasz terran i masz odporność na obrażenia od kwasu. Teren z gruzów, skał lub ziemi nie jest dla ciebie trudnym terenem. Dodatkowo możesz przechodzić przez lite ziemie lub skały tak, jakby były trudnym terenem, nie zaburzając materii, przez którą przechodzisz. Jeśli kończysz turę w litej ziemi lub skale, zostajesz wypchnięty do najbliższej niezajętej przestrzeni, którą ostatnio zajmowałeś.
**Ogień.** Znasz ignan i masz niewrażliwość na obrażenia od ognia.
**Woda.** Znasz aquan, zyskujesz szybkość pływania 18 metrów i możesz oddychać pod wodą.
_Rzucanie czarów._ Pierścień ma 5 ładunków i codziennie o świcie odzyskuje 1k4 + 1 zużytych ładunków. Nosząc pierścień, możesz rzucić z niego czar. Wybierz czar z listy dostępnych czarów zależnie od powiązanej Sfery Żywiołu, jak pokazano w poniższej tabeli. Tabela wskazuje, ile ładunków musisz wydać, aby rzucić czar o ST 18.""",
    ),
    ("<th>Plan</th>", "<th>Sfera</th>"),
    ("<th>Czars (Charges)</th>", "<th>Czary (ładunki)</th>"),
    ("<td>Air</td>", "<td>Powietrze</td>"),
    ("<td>Earth</td>", "<td>Ziemia</td>"),
    ("<td>Water</td>", "<td>Woda</td>"),
    # Ring of resistance
    (
        "You have odporność to one damage type while wearing this ring. The gemstone in the ring indicates the type, which the MG chooses or determines randomly by rolling on the following table.",
        "Nosząc ten pierścień, masz odporność na jeden rodzaj obrażeń. Kamień szlachetny w pierścieniu wskazuje rodzaj, który MG wybiera albo określa losowo, rzucając na poniższej tabeli.",
    ),
    ("<td>Pearl</td>", "<td>Perła</td>"),
    ("<td>Tourmaline</td>", "<td>Turmalin</td>"),
    ("<td>Garnet</td>", "<td>Granat</td>"),
    ("<td>Sapphire</td>", "<td>Szafir</td>"),
    ("<td>Citrine</td>", "<td>Cytryn</td>"),
    ("<td>Jet</td>", "<td>Jaźń</td>"),
    ("<td>Amethyst</td>", "<td>Ametyst</td>"),
    ("<td>Jade</td>", "<td>Jadeit</td>"),
    ("<td>Topaz</td>", "<td>Topaz</td>"),
    ("<td>Spinel</td>", "<td>Spinel</td>"),
    ("<th>Number of Spheres</th>", "<th>Liczba kul</th>"),
    ("<th>elektryczność Damage</th>", "<th>Obrażenia od elektryczności</th>"),
    # Prayer beads table
    ("<th>Bead</th>", "<th>Koralik</th>"),
    ("<td>Bead of Blessing</td>", "<td>Koralik błogosławieństwa</td>"),
    ("<td>Bless</td>", "<td>Błogosławieństwo</td>"),
    ("<td>Bead of Curing</td>", "<td>Koralik leczenia</td>"),
    ("<td>Cure Wounds (level 2 version)</td>", "<td>Leczenie ran (wersja 2. kręgu)</td>"),
    ("<td>Bead of Favor</td>", "<td>Koralik łaski</td>"),
    ("<td>Greater Restoration</td>", "<td>Większe przywrócenie</td>"),
    ("<td>Bead of Smiting</td>", "<td>Koralik ugodzenia</td>"),
    ("<td>Bead of Summons</td>", "<td>Koralik przywołania</td>"),
    ("<td>Guardian of Faith</td>", "<td>Strażnik wiary</td>"),
    ("<td>Bead of Wind Walking</td>", "<td>Koralik chodzenia po wietrze</td>"),
    ("<td>Wind Walk</td>", "<td>Chodzenie po wietrze</td>"),
    (
        "_Cudowny przedmiot, rzadki (wymaga zestrojenia by a Cleric, Druid, or Paladin)_",
        "_Cudowny przedmiot, rzadki (wymaga zestrojenia przez kleryka, druida lub paladyna)_",
    ),
    # Robe of useful items
    ("<th>Patch</th>", "<th>Łata</th>"),
    ("<td>Bag of 100 GP</td>", "<td>Worek 100 sz</td>"),
    ("<td>Silver coffer (1 foot long, 6 inches wide and deep) worth 500 GP</td>", "<td>Srebrna skrzynia (30 cm długości, 15 cm szerokości i głębokości) warta 500 sz</td>"),
    ("<td>Iron door (up to 10 feet wide and 10 feet high, barred on one side of your choice), which you can place in an opening you can reach; it conforms to fit the opening, attaching and hinging itself</td>", "<td>Żelazne drzwi (do 3 m szerokości i 3 m wysokości, zabarykadowane z wybranej przez ciebie strony), które możesz umieścić w otworze, do którego sięgasz; dopasowują się do otworu, same się mocując i zawieszając</td>"),
    ("<td>10 gems worth 100 GP each</td>", "<td>10 klejnotów wartych po 100 sz</td>"),
    ("<td>Wooden ladder (24 feet long)</td>", "<td>Drewniana drabina (7,2 m długości)</td>"),
    ("<td>Riding Horse with a Riding Saddle</td>", "<td>Koń wierzchowy z siodłem</td>"),
    ("<td>Open pit (a 10-foot Cube), which you can place on the ground within 10 feet of yourself</td>", "<td>Otwarta jama (sześcian o boku 3 m), którą możesz umieścić na ziemi w promieniu 3 metrów od siebie</td>"),
    ("<td>4 Potions of Healing</td>", "<td>4 mikstury leczenia</td>"),
    ("<td>Rowboat (12 feet long)</td>", "<td>Łódź wiosłowa (3,6 m długości)</td>"),
    ("<td>Czar Scroll containing one spell of level 1, 2, or 3 (your choice)</td>", "<td>Zwój z czarem zawierający jeden czar 1., 2. lub 3. kręgu (do wyboru)</td>"),
    ("<td>2 Mastiffs</td>", "<td>2 mastify</td>"),
    ("<td>Window (2 feet by 4 feet, up to 2 feet deep), which you can place on a vertical surface you can reach</td>", "<td>Okno (60 × 120 cm, do 60 cm głębokości), które możesz umieścić na pionowej powierzchni, do której sięgasz</td>"),
    ("<td>Portable Ram</td>", "<td>Przenośny taran</td>"),
    # Rod of Resurrection
    (
        """The rod has 5 charges. While you hold it, you can cast one of the following spells from it: _Uleczenie_ (expends 1 charge) or _Zmartwychwstanie_ (expends 5 charges).
The rod regains 1 expended charge daily at dawn. If you expend the last charge, roll 1d20. On a 1, the rod disappears in a harmless burst of radiance.""",
        """Berło ma 5 ładunków. Trzymając je, możesz rzucić z niego jeden z następujących czarów: _uleczenie_ (zużywa 1 ładunek) albo _zmartwychwstanie_ (zużywa 5 ładunków).
Berło codziennie o świcie odzyskuje 1 zużyty ładunek. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 berło znika w nieszkodliwym rozbłysku światła.""",
    ),
    # Sending stones
    (
        """_Kamienie przesyłania_ come in pairs, with each stone carved to match the other so the pairing is easily recognized. While you touch one stone, you can cast _Nadanie wiadomości_ from it. The target is the bearer of the other stone. If no creature bears the other stone, you know that fact as soon as you use the stone, and you don't cast the spell.
Once _Nadanie wiadomości_ is cast using either stone, the stones can't be used again until the następny świt. If one of the stones in a pair is destroyed, the other one becomes nonmagical.""",
        """_Kamienie przesyłania_ występują parami; każdy kamień jest wyrzeźbiony tak, by pasował do drugiego, co ułatwia rozpoznanie pary. Dotykając jednego kamienia, możesz rzucić z niego _Nadanie wiadomości_. Celem jest nosiciel drugiego kamienia. Jeśli nikt nie nosi drugiego kamienia, wiesz o tym od razu po użyciu kamienia i nie rzucasz czaru.
Gdy _Nadanie wiadomości_ zostanie rzucone za pomocą któregokolwiek kamienia, kamieni nie można użyć ponownie do następnego świtu. Jeśli jeden kamień z pary zostanie zniszczony, drugi traci magię.""",
    ),
    # Shields
    (
        "While holding this Shield, you have ułatwienie on Initiative rolls and Mądrość (Perception) checks. The Shield is emblazoned with a symbol of an eye.",
        "Trzymając tę tarczę, masz ułatwienie w rzutach na inicjatywę i testach Mądrości (Percepcja). Na tarczy widnieje symbol oka.",
    ),
    (
        "_Zbroja (Tarcza), niezwykły (+1), rzadki (+2), or bardzo rzadki (+3)_",
        "_Zbroja (tarcza), niezwykły (+1), rzadki (+2) lub bardzo rzadki (+3)_",
    ),
    (
        "While holding this Shield, you have a bonus to KP determined by the Shield's rarity, in addition to the Shield's normal bonus to KP.",
        "Trzymając tę tarczę, masz premię do KP określoną rzadkością tarczy, oprócz jej normalnej premii do KP.",
    ),
    (
        """While holding this Shield, you have a +2 bonus to KP. This bonus is in addition to the Shield's normal bonus to KP.
The Shield has the following additional properties that you can use while holding it.
_Forceful Bash._ When you take the Attack action, you can make one of the attack rolls using the Shield against a target within 5 feet of yourself. Apply your premię do biegłości and Siła modifier to the test ataku. On a hit, the Shield deals Force damage to the target equal to 2d6 + 2 plus your Siła modifier, and if the target is a creature, you can push it up to 10 feet directly away from yourself. If the creature is your size or smaller, you can also knock it down, giving it the Prone condition.
_Protective Field._ As a reakcję, when you or an ally you can see within 5 feet of you is targeted by an attack or makes a rzut obronny against an area of effect, you can use the Shield to create an immobile 5-foot Emanation originating from you. When the Emanation appears, any creatures or objects not fully contained within it are pushed into the nearest unoccupied spaces outside it. The attack or area of effect that triggered the reakcję has no effect on creatures and objects inside the Emanation, which lasts as long as you maintain Concentration, up to 1 minute. Nothing can pass into or out of the Emanation. A creature or object inside the Emanation can't be damaged by attacks or effects originating from outside, nor can a creature inside the Emanation damage anything outside it. Once this property is used, it can't be used again until the następny świt.""",
        """Trzymając tę tarczę, masz premię +2 do KP. Premia ta dodaje się do normalnej premii tarczy do KP.
Tarcza ma następujące dodatkowe właściwości, z których możesz korzystać, trzymając ją.
_Siłowe uderzenie._ Gdy wykonujesz akcję Ataku, możesz wykonać jeden z testów ataku tarczą przeciwko celowi w promieniu 1,5 metra od siebie. Zastosuj swoją premię do biegłości i modyfikator Siły do testu ataku. Przy trafieniu tarcza zadaje celowi obrażenia od mocy równe 2k6 + 2 plus twój modyfikator Siły, a jeśli celem jest stworzenie, możesz odepchnąć je do 3 metrów prosto od siebie. Jeśli stworzenie ma twój rozmiar lub mniejszy, możesz też powalić je, nadając mu stan powalony.
_Pole ochronne._ Jako reakcję, gdy ty albo sojusznik, którego widzisz w promieniu 1,5 metra od siebie, jest celem ataku albo wykonuje rzut obronny przeciw obszarowi działania, możesz użyć tarczy, aby stworzyć nieruchomy promień o zasięgu 1,5 metra wychodzący od ciebie. Gdy promień się pojawia, wszelkie stworzenia i przedmioty niezawarte w całości w nim zostają odepchnięte do najbliższych wolnych przestrzeni na zewnątrz. Atak lub obszar działania, który wywołał reakcję, nie ma wpływu na stworzenia i przedmioty w promieniu, który utrzymuje się tak długo, jak koncentrujesz się na nim, maksymalnie przez 1 minutę. Nic nie może wejść do promienia ani z niego wyjść. Stworzenie lub przedmiot w promieniu nie może otrzymać obrażeń od ataków lub efektów z zewnątrz, ani stworzenie w promieniu nie może zranić czegokolwiek na zewnątrz. Po użyciu tej właściwości nie można jej użyć ponownie do następnego świtu.""",
    ),
    # Spell scroll
    (
        """A _Zwój z czarem_ bears the words of a single spell, written in a mystical cipher. If the spell is on your spell list, you can read the scroll and cast its spell without Material components. Otherwise, the scroll is unintelligible. Casting the spell by reading the scroll requires the spell's normal casting time. Once the spell is cast, the scroll crumbles to dust. If the casting is interrupted, the scroll isn't lost.
If the spell is on your spell list but of a higher level than you can normally cast, you make an ability check using your spellcasting ability to determine whether you cast the spell. The DC equals 10 plus the spell's level. On a failed check, the spell disappears from the scroll with no other effect.
The level of the spell on the scroll determines the spell's rzut obronny DC and attack bonus, as well as the scroll's rarity, as shown in the following table.""",
        """_Zwój z czarem_ zawiera słowa jednego czaru zapisane mistycznym szyfrem. Jeśli czar jest na twojej liście czarów, możesz odczytać zwój i rzucić jego czar bez komponentów materialnych. W przeciwnym razie zwój jest niezrozumiały. Rzucenie czaru przez odczytanie zwoju wymaga normalnego czasu rzucania tego czaru. Gdy czar zostanie rzucony, zwój kruszy się w pył. Jeśli rzucanie zostanie przerwane, zwój nie przepada.
Jeśli czar jest na twojej liście, ale z wyższego kręgu niż ten, który normalnie potrafisz rzucić, wykonujesz test cechy używanej do rzucania czarów, aby ustalić, czy rzuciłeś czar. ST wynosi 10 plus krąg czaru. W przypadku niepowodzenia czar znika ze zwoju bez innego efektu.
Krąg czaru na zwoju określa ST rzutu przeciw czarom i premię do ataku czarem oraz rzadkość zwoju, jak pokazano w poniższej tabeli.""",
    ),
    ("<th>Czar Level</th>", "<th>Krąg czaru</th>"),
    ("<th>Save DC</th>", "<th>ST</th>"),
    ("<th>Attack Bonus</th>", "<th>Premia do ataku</th>"),
    ("<td>Cantrip</td>", "<td>Sztuczka</td>"),
    ("<td>Common</td>", "<td>pospolity</td>"),
    ("<td>Uncommon</td>", "<td>niezwykły</td>"),
    ("<td>Rare</td>", "<td>rzadki</td>"),
    ("<td>Very Rare</td>", "<td>bardzo rzadki</td>"),
    ("<td>Legendary</td>", "<td>legendarny</td>"),
    (
        "_Copying a Scroll into a Czarbook._ A Wizard spell on a _Czar Scroll_ can be copied into a spellbook. When a spell is copied in this way, the copier must succeed on an Intelligence (Arcana) check with a DC equal to 10 plus the spell's level. On a successful check, the spell is copied. Whether the check succeeds or fails, the _Czar Scroll_ is destroyed.",
        "_Kopiowanie zwoju do księgi czarów._ Czar Maga z _Zwoju z czarem_ można przepisać do księgi czarów. Gdy czar jest kopiowany w ten sposób, kopiujący musi odnieść sukces w teście Inteligencji (Wiedza tajemna) o ST równym 10 plus krąg czaru. W przypadku sukcesu czar zostaje przepisany. Niezależnie od wyniku testu _Zwój z czarem_ zostaje zniszczony.",
    ),
    ("_Scroll, zmienna rzadkość_", "_Zwój, zmienna rzadkość_"),
    # Sphere of annihilation
    ("<th>Result</th>", "<th>Skutek</th>"),
    ("<td>The sphere is destroyed.</td>", "<td>Kula zostaje zniszczona.</td>"),
    ("<td>The sphere moves through the portal or into the extradimensional space.</td>", "<td>Kula przechodzi przez portal lub do przestrzeni pozawymiarowej.</td>"),
    (
        "<td>A spatial rift sends the sphere and each creature and object within 180 feet of the sphere to a random plane of existence.</td>",
        "<td>Szczelina przestrzenna wysyła kulę oraz każde stworzenie i przedmiot w promieniu 55 metrów od kuli do losowej sfery egzystencji.</td>",
    ),
    # Regaining charges (1k20 variant)
    (
        "_Regaining Charges._ The staff regains 1k6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 1, the staff crumbles into cinders and is destroyed.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur rozpada się w popiół i zostaje zniszczony.",
    ),
    (
        "_Regaining Charges._ The staff regains 1k6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 1, the staff turns to water and is destroyed.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur zamienia się w wodę i zostaje zniszczony.",
    ),
    (
        "_Regaining Charges._ The staff regains 1k6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 1, the staff vanishes in a flash of light, lost forever.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur znika w błysku światła i zostaje na zawsze utracony.",
    ),
    (
        "_Regaining Charges._ The staff regains 2d8 + 4 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 1, the staff retains its +2 bonus to attack rolls and damage rolls but loses all other properties. On a 20, the staff regains 1k8 + 2 charges.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 2k8 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 kostur zachowuje premię +2 do testów ataku i obrażeń, ale traci wszystkie inne właściwości. Przy wyniku 20 kostur odzyskuje 1k8 + 2 ładunki.",
    ),
    (
        "_Regaining Charges._ The staff regains 4d6 + 2 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 20, the staff regains 1k12 + 1 charges.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 4k6 + 2 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 20 kostur odzyskuje 1k12 + 1 ładunków.",
    ),
    (
        "_Regaining Charges._ The staff regains 1k6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1k20. On a 1, a swarm of insects consumes and destroys the staff, then disperses.",
        "_Odzyskiwanie ładunków._ Kostur codziennie o świcie odzyskuje 1k6 + 4 zużytych ładunków. Jeśli zużyjesz ostatni ładunek, rzuć k20. Przy wyniku 1 rój owadów pożera i niszczy kostur, po czym się rozprasza.",
    ),
    # Staff heal table
    ("<td>1 charge per spell level (maximum 4 for a level 4 spell)</td>", "<td>1 ładunek za krąg czaru (maksymalnie 4 za czar 4. kręgu)</td>"),
    ("<td>*Lesser Restoration*</td>", "<td>*Mniejsze przywrócenie*</td>"),
    ("<td>*Mass Cure Wounds*</td>", "<td>*Masowe leczenie ran*</td>"),
    # Attunement fixes
    ("_Broń (łuk długi or Shortbow), bardzo rzadki (wymaga zestrojenia)_", "_Broń (łuk długi lub krótki łuk), bardzo rzadki (wymaga zestrojenia)_"),
    ("_Kostur, rzadki (wymaga zestrojenia by a Bard, Cleric, Druid, Sorcerer, Warlock, or Wizard)_", "_Kostur, rzadki (wymaga zestrojenia przez barda, kleryka, druida, zaklinacza, czarownika lub maga)_"),
    ("_Kostur, bardzo rzadki (wymaga zestrojenia przez druida, Sorcerer, Warlock, or Wizard)_", "_Kostur, bardzo rzadki (wymaga zestrojenia przez druida, zaklinacza, czarownika lub maga)_"),
    ("_Kostur, rzadki (wymaga zestrojenia by a Bard, Cleric, or Druid)_", "_Kostur, rzadki (wymaga zestrojenia przez barda, kleryka lub druida)_"),
    # Wand of the War Mage
    (
        "While holding this wand, you gain a bonus to spell attack rolls determined by the wand's rarity. In addition, you ignore Half Cover when making a spell test ataku.",
        "Trzymając tę różdżkę, zyskujesz premię do testów ataku czarem określoną rzadkością różdżki. Dodatkowo ignorujesz połowiczną osłonę, wykonując test ataku czarem.",
    ),
    # Silver Raven if still English
    (
        "**Silver Raven (Uncommon).** This silver statuette of a raven can become a **Raven** for up to 12 hours. Once it has been used, it can't be used again until 2 days have passed. While in raven form, the figurine grants you the ability to cast _Zwierzęcy posłaniec_ on it.",
        "**Srebrny kruk (niezwykły).** Ta srebrna statuetka kruka może zamienić się w **kruka** na maksymalnie 12 godzin. Po użyciu nie można jej użyć ponownie przez 2 dni. W formie kruka figurka pozwala ci rzucać na nią _Zwierzęcy posłaniec_.",
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
