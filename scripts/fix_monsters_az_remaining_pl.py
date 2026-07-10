#!/usr/bin/env python3
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/monsters-A-Z.md"
text = path.read_text(encoding="utf-8")

REPLACEMENTS = [
    # Broken patterns
    ("truciznyed", "Zatruty"),
    ("Reakcjas", "Reakcje"),
    ("obrażeńd", "uszkodzona"),
    ("rzut obronnys", "rzutów obronnych"),
    ("Magic odporność", "Odporność na magię"),
    ("W przypadku sukcesuful check", "Przy udanym teście"),
    ("bestias", "zwierzętami"),
    ("roślinas", "roślinami"),
    ("dźwiękuwave", "Fala gromu"),
    ("żywiołakism", "Żywiołomagia"),
    ("Wall of ognia", "Ściana ognia"),
    ("szlam Cube", "Kostka szlamu"),
    ("ognia Aura", "Aura ognia"),
    ("ognia Form", "Forma ognia"),
    ("elektryczności Absorption", "Absorpcja elektryczności"),
    ("Lotby", "Lot"),
    ("_Melee or Test ataku dystansowy:_", "_Test ataku wręcz lub dystansowy:_"),
    ("_Tarcza Bash._", "_Uderzenie tarczą._"),
    ("Studded Skórzana zbroja", "Ćwiartowana skórzana zbroja"),
    (", or ", ", lub "),
    (" or zasięg", ", lub zasięg"),
    (" (with ułatwienie", " (z ułatwieniem"),
    ("PD 10,000, or 11,500", "PD 10 000 lub 11 500"),
    ("PD 25,000, or 33,000", "PD 25 000 lub 33 000"),
    ("PD 13,000, or 15,000", "PD 13 000 lub 15 000"),
    ("PD 41,000, or 50,000", "PD 41 000 lub 50 000"),
    ("PD 11,500, or 13,000", "PD 11 500 lub 13 000"),
    ("PD 33,000, or 41,000", "PD 33 000 lub 41 000"),
    ("telepathy", "telepatia"),
    ("Exhaustion", "Wyczerpanie"),
    ("Grappled", "Pochwycony"),
    ("**Języki** None", "**Języki** Brak"),
    ("<td><strong>STR</strong></td>", "<td><strong>SIŁ</strong></td>"),
    ("<td><strong>DEX</strong></td>", "<td><strong>ZRC</strong></td>"),
    ("<td><strong>CON</strong></td>", "<td><strong>KON</strong></td>"),
    ("<td><strong>WIS</strong></td>", "<td><strong>MDR</strong></td>"),
    ("_Średni or Small humanoid (Druid), Neutralny_", "_Średni lub Mały Humanoid (Druid), Neutralny_"),
    ("_Średni or Small humanoid, Neutralny_", "_Średni lub Mały Humanoid, Neutralny_"),
    ("_Mały  fey (Goblinoid)", "_Mały Fey (Goblinoid)"),
    ("_Duży  ", "_Duży "),
    ("_Średni  ", "_Średni "),
    ("_Ogromny  ", "_Ogromny "),
    ("_Mały  ", "_Mały "),
    ("## Drjad\n\n### Drjad", "## Driada\n\n### Driada"),
    ("### Goblin Minion", "### Gobliński sługa"),
    ("### Goblin Warrior", "### Gobliński wojownik"),
    ("### Goblin Boss", "### Gobliński szef"),
    ("### Gnoll Warrior", "### Gnoll wojownik"),
    ("**Wyposażenie** Daggers (3)", "**Wyposażenie** Sztylety (3)"),
    ("**Wyposażenie** Tarcza, Spears (3), Ćwiartowana skórzana zbroja", "**Wyposażenie** Tarcza, Włócznie (3), Ćwiartowana skórzana zbroja"),
    ("**Wyposażenie** Battleaxe, Morningstar", "**Wyposażenie** Topór bojowy, Gwiazda poranna"),
    ("**Języki** Wspólny, Druidic, Sylvan", "**Języki** Wspólny, Druidyczny, Sylfański"),
    ("**Języki** Elvish, Sylvan", "**Języki** Elficki, Sylfański"),
    ("**Języki** Wspólny plus three other languages", "**Języki** Wspólny plus trzy inne języki"),
    ("**Języki** Wspólny plus one other language", "**Języki** Wspólny plus jeden inny język"),
    ("**Języki** Understands Wspólny plus one other language but can't speak", "**Języki** Rozumie Wspólny plus jeden inny język, ale nie może mówić"),
    ("**Języki** Abyssal; telepatia 18 m (works only with creatures that understand Abyssal)", "**Języki** Otchłanny; telepatia 18 m (działa tylko ze stworzeniami rozumiejącymi Otchłanny)"),
    # Bagiennik
    ("**_Porywanie._** Bagiennik needn't spend extra movement to move a creature it is grappling.", "**_Porywanie._** Bagiennik nie musi wydawać dodatkowego ruchu, aby poruszać pochwyconą przez siebie istotę."),
    ("**_Gwiazda poranna._** _Test ataku wręcz:_ +5 (z ułatwieniem, jeśli cel is Grappled by bagiennik), zasięg 3 m _Trafienie:_  12 (2k8 + 3) obrażeń kłutych.", "**_Gwiazda poranna._** _Test ataku wręcz:_ +5 (z ułatwieniem, jeśli cel ma stan Pochwycony od bagiennika), zasięg 3 m _Trafienie:_  12 (2k8 + 3) obrażeń kłutych."),
    ("**_Szybkie chwycenie._** _Rzut obronny na Zręczność:_ ST 13, jedna istota Średnia lub mniejsza bagiennik can see w zasięgu 3 m. _Porażka:_ Cel has the stan Pochwycony (ST ucieczki 13).", "**_Szybkie chwycenie._** _Rzut obronny na Zręczność:_ ST 13, jedna istota Średnia lub mniejsza, którą bagiennik widzi, w zasięgu 3 m. _Porażka:_ Cel otrzymuje stan Pochwycony (ST ucieczki 13)."),
    ("**_Młotek lekki._** _Test ataku wręcz lub dystansowy:_ +4 (z ułatwieniem, jeśli cel is Grappled by bagiennik), zasięg 3 m, lub zasięg 20/18 m _Trafienie:_  9 (3k4 + 2) obrażeń obuchowych.", "**_Młotek lekki._** _Test ataku wręcz lub dystansowy:_ +4 (z ułatwieniem, jeśli cel ma stan Pochwycony od bagiennika), zasięg 3 m, lub zasięg 20/18 m _Trafienie:_  9 (3k4 + 2) obrażeń obuchowych."),
    # Kultysta
    ("**_Rzucanie czarów._** Kultysta casts one of the following spells, używając Mądrości jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 12, +4 do testu ataku czarem):", "**_Rzucanie czarów._** Kultysta rzuca jeden z następujących czarów, używając Mądrości jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 12, +4 do testu ataku czarem):"),
    ("**_Spiritual Weapon (2/Day)._** Kultysta casts the _Duchowa broń_ spell, using the same cechy bazowej rzucania czarów as Spellcasting.", "**_Duchowa broń (2/dzień)._** Kultysta rzuca _Duchową broń_, używając tej samej cechy bazowej rzucania czarów co Rzucanie czarów."),
    # Deva
    ("**_Exalted Restoration._** If the deva dies outside Mount Celestia, its body disappears, a it gains a new body instantly, reviving with all its Punkty Wytrzymałości somewhere in Mount Celestia.", "**_Wzniesione przywracanie._** Jeśli deva umrze poza Górą Celestii, jego ciało znika, a on natychmiast zyskuje nowe ciało, odradzając się ze wszystkimi Punktami Wytrzymałości gdzieś na Górze Celestii."),
    ("**_Holy Mace._** _Test ataku wręcz:_ +8, zasięg 1,5 m. _Trafienie:_  7 (1k6 + 4) obrażeń obuchowych plus 18 (4k8) Radiant obrażeń.", "**_Święty buzdygan._** _Test ataku wręcz:_ +8, zasięg 1,5 m. _Trafienie:_  7 (1k6 + 4) obrażeń obuchowych plus 18 (4k8) obrażeń od światła."),
    ("**_Elemental Restoration._** If the djinni dies outside the Elemental Plane of Air, its body dissolves into mist, a it gains a new body in 1k4 days, reviving with all its Punkty Wytrzymałości somewhere on the Plane of Air.", "**_Przywracanie żywiołaka._** Jeśli dżin umrze poza Żywiołowym Planem Powietrza, jego ciało rozpuszcza się we mgle, a on zyskuje nowe ciało w ciągu 1k4 dni, odradzając się ze wszystkimi Punktami Wytrzymałości gdzieś na Planie Powietrza."),
    # Sobowtór
    ("**_Atak wielokrotny._** The doppelganger makes two Slam attacks and uses Unsettling Visage if available.", "**_Atak wielokrotny._** Sobowtór wykonuje dwa ataki Uderzeniem i, jeśli jest dostępna, używa Niepokojącej twarzy."),
    ("**_Uderzenie._** _Test ataku wręcz:_ +6 (z ułatwieniem podczas the first round of each combat), zasięg 1,5 m. _Trafienie:_  11 (2k6 + 4) obrażeń obuchowych.", "**_Uderzenie._** _Test ataku wręcz:_ +6 (z ułatwieniem podczas pierwszej rundy każdej walki), zasięg 1,5 m. _Trafienie:_  11 (2k6 + 4) obrażeń obuchowych."),
    ("**_Read Thoughts._** The doppelganger casts _Wykrycie myśli_, nie wymagając komponentów and używając Charyzmy jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 12).", "**_Czytanie myśli._** Sobowtór rzuca _Wykrycie myśli_, nie wymagając komponentów i używając Charyzmy jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 12)."),
    ("**_Unsettling Visage (Recharge 6)._** _Rzut obronny na Mądrość:_ ST 12, każda istota na 15-foot Emanacja originating from the doppelganger that can see the doppelganger. _Porażka:_ Cel otrzymuje stan Przestraszony and repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.", "**_Niepokojąca twarz (Ładowanie 6)._** _Rzut obronny na Mądrość:_ ST 12, każda istota w Emanacji 4,5 m pochodzącej od sobowtóra, która widzi sobowtóra. _Porażka:_ Cel otrzymuje stan Przestraszony i ponawia rzut obronny na końcu każdej swojej tury, kończąc efekt na sobie przy sukcesie. Po 1 minucie automatycznie odnosi sukces."),
    ("**_Shape-Shift._** The doppelganger shape-shifts into a Medium or Small Humanoid, or it returns to its true form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed.", "**_Zmiana kształtu._** Sobowtór zmienia kształt w Średniego lub Małego Humanoida albo wraca do swojej prawdziwej formy. Jego statystyki gry, poza rozmiarem, pozostają takie same w każdej formie. Wyposażenie, które nosi lub dźwiga, nie ulega przemianie."),
    # Smoczy żółw
    ("**_Amfibius._** Smok can breathe air and water.", "**_Amfibius._** Smok może oddychać powietrzem i wodą."),
    ("**_Atak wielokrotny._** Smok makes three Bite attacks. It can replace one attack with a Tail attack.", "**_Atak wielokrotny._** Smok wykonuje trzy ataki Ugryzieniem. Może zastąpić jeden atak atakiem Ogonem."),
    ("**_Ogon._** _Test ataku wręcz:_ +13, zasięg 4,5 m _Trafienie:_  18 (2k10 + 7) obrażeń obuchowych. If cel is a Huge or smaller creature, it otrzymuje stan Powalony.", "**_Ogon._** _Test ataku wręcz:_ +13, zasięg 4,5 m _Trafienie:_  18 (2k10 + 7) obrażeń obuchowych. Jeśli celem jest istota Ogromna lub mniejsza, otrzymuje stan Powalony."),
    ("Being underwater doesn't grant Resistance to this obrażeń od ognia.", "Bycie pod wodą nie zapewnia odporności na te obrażenia od ognia."),
    ("**_Steam Breath (Ładowanie 5–6)._**", "**_Oddech pary (Ładowanie 5–6)._**"),
    ("_Porażka lub sukces:_ Bycie pod wodą nie zapewnia odporności na te obrażenia od ognia.", "_Porażka lub sukces:_ Bytie pod wodą nie zapewnia odporności na te obrażenia od ognia."),
    # Dretch
    ("**_Fetid Cloud (1/Day)._** _Rzut obronny na Kondycję:_ ST 11, każda istota na 10-foot Emanacja originating from the dretch. _Porażka:_ Cel otrzymuje stan Zatruty do końca swojej następnej tury. Gdy jest Zatruty, the creature can take either an action or a Akcja dodatkowa on its turn, not both, a it can't take Reakcje.", "**_Cuchnąca chmura (1/dzień)._** _Rzut obronny na Kondycję:_ ST 11, każda istota w Emanacji 3 m pochodzącej od dretcha. _Porażka:_ Cel otrzymuje stan Zatruty do końca swojej następnej tury. Gdy jest Zatruty, istota może w swojej turze podjąć albo akcję, albo akcję dodatkową, nie obie, i nie może podejmować Reakcji."),
]

for old, new in REPLACEMENTS:
    text = text.replace(old, new)

path.write_text(text, encoding="utf-8")
print(f"Applied {len(REPLACEMENTS)} replacements")

# Run batch 2 by re-reading and applying more replacements
from pathlib import Path
path = Path(__file__).resolve().parent.parent / "srd-5.2.1/pl/monsters-A-Z.md"
text = path.read_text(encoding="utf-8")

REPLACEMENTS = [
    ("Bytie pod wodą", "Bycie pod wodą"),
    # Druid
    ("**_Atak wielokrotny._** The druid makes two attacks, using Vine Staff or Verdant Wisp in any combination.", "**_Atak wielokrotny._** Druid wykonuje dwa ataki, używając w dowolnej kombinacji Laski z pnącza lub Zielonej iskry."),
    ("**_Vine Staff._**", "**_Laska z pnącza._**"),
    ("**_Verdant Wisp._** _Test ataku dystansowy:_ +5, range 27 m", "**_Zielona iskra._** _Test ataku dystansowy:_ +5, zasięg 27 m"),
    ("**_Rzucanie czarów._** The druid casts one of the following spells, using Wisdom as the cecha bazowej rzucania czarów (ST rzutu obronnego na czary 13):", "**_Rzucanie czarów._** Druid rzuca jeden z następujących czarów, używając Mądrości jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 13):"),
    ("&emsp;**Na wolności:** _Druidcraft, Speak with Animals_", "&emsp;**Na wolności:** _Druidzkie sztuczki_, _Rozmawianie ze zwierzętami_"),
    ("&emsp;**2/dzień każdy:** _Entangle, Fala gromu_", "&emsp;**2/dzień każdy:** _Oplątanie_, _Fala gromu_"),
    ("&emsp;**1/dzień każdy:** _Animal Messenger, Long-strider, Moonbeam_", "&emsp;**1/dzień każdy:** _Zwierzęcy posłaniec_, _Szybkonogi_, _Księżycowy promień_"),
    # Dryad
    ("**_Odporność na magię._** The dryad ma ułatwienie do rzutów obronnych against czarom i innym magicznym efektom.", "**_Odporność na magię._** Driada ma ułatwienie do rzutów obronnych przeciw czarom i innym magicznym efektom."),
    ("**_Speak with bestias and roślinas._** The dryad can communicate with bestias and roślinas as if they shared a language.", "**_Rozmawianie ze zwierzętami i roślinami._** Driada może komunikować się ze zwierzętami i roślinami, jak gdyby dzieliła z nimi język."),
    ("**_Atak wielokrotny._** The dryad makes one Vine Lash or Thorn Burst attack, and it can use Spellcasting to cast _Zauroczenie potwora_.", "**_Atak wielokrotny._** Driada wykonuje jeden atak Biczem z pnącza lub Wybuchem cierni i może użyć Rzucania czarów, aby rzucić _Zauroczenie potwora_."),
    ("**_Vine Lash._**", "**_Bicz z pnącza._**"),
    ("**_Thorn Burst._** _Test ataku dystansowy:_ +6, range 18 m", "**_Wybuch cierni._** _Test ataku dystansowy:_ +6, zasięg 18 m"),
    ("**_Rzucanie czarów._** The dryad casts one of the following spells, requiring no komponentów materialnych and using Charisma as the cecha bazowej rzucania czarów (ST rzutu obronnego na czary 14):", "**_Rzucanie czarów._** Driada rzuca jeden z następujących czarów, nie wymagając komponentów materialnych i używając Charyzmy jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 14):"),
    ("&emsp;**Na wolności:** _Animal Friendship, Charm Monster_ (lasts 24 hours; ends early if the dryad casts the spell again), _Druidzkie sztuczki_", "&emsp;**Na wolności:** _Przyjaciel zwierząt_, _Zauroczenie potwora_ (trwa 24 godziny; kończy się wcześniej, jeśli driada rzuci ten czar ponownie), _Druidzkie sztuczki_"),
    ("&emsp;**1/dzień każdy:** _Entangle, Pass without Trace_", "&emsp;**1/dzień każdy:** _Oplątanie_, _Przejście bez śladu_"),
    ("**_Spacer między drzewami._** If within 5 feet of a Large or bigger tree, the dryad teleports to an unoccupied space within 5 feet of a second Large or bigger tree that is within 60 feet of the previous tree.", "**_Spacer między drzewami._** Jeśli znajduje się w odległości 1,5 m od Wielkiego lub większego drzewa, driada teleportuje się do niezajętego pola w odległości 1,5 m od drugiego Wielkiego lub większego drzewa, które znajduje się w odległości do 18 m od poprzedniego drzewa."),
    # Earth elemental
    ("**_Earth Glide._** The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.", "**_Przemieszczanie przez ziemię._** Żywiołak może przewiercać niemagiczną, nieobrobioną ziemię i kamień. Podczas tego nie zaburza materiału, przez który się porusza."),
    ("**_Siege Monster._** The elemental deals double obrażeń to objects and structures.", "**_Potwór oblężniczy._** Żywiołak zadaje podwójne obrażenia obiektom i konstrukcjom."),
    ("**_Atak wielokrotny._** The elemental makes two attacks, using Slam or Rock Launch in any combination.", "**_Atak wielokrotny._** Żywiołak wykonuje dwa ataki, używając w dowolnej kombinacji Uderzenia lub Wystrzelenia skały."),
    ("**_Rock Launch._** _Test ataku dystansowy:_ +8, range 18 m _Trafienie:_ 8 (1k6 + 5) obuchowe obrażeń. If cel is a Large or smaller creature, it has stan Powalony.", "**_Wystrzelenie skały._** _Test ataku dystansowy:_ +8, zasięg 18 m _Trafienie:_ 8 (1k6 + 5) obuchowe obrażeń. Jeśli celem jest istota Duża lub mniejsza, otrzymuje stan Powalony."),
    # Efreeti
    ("**_żywiołak Restoration._** If the efreeti dies outside the żywiołak Plane of od ognia, its body dissolves into ash, and it gains a new body in 1k4 days, reviving with all its Punkty Wytrzymałości somewhere on the Plane of od ognia.", "**_Przywracanie żywiołaka._** Jeśli efreet umrze poza Żywiołowym Planem Ognia, jego ciało rozpuszcza się w popiół, a on zyskuje nowe ciało w ciągu 1k4 dni, odradzając się ze wszystkimi Punktami Wytrzymałości gdzieś na Planie Ognia."),
    ("**_Odporność na magię._** The efreeti ma ułatwienie do rzutów obronnych against czarom i innym magicznym efektom.", "**_Odporność na magię._** Efreet ma ułatwienie do rzutów obronnych przeciw czarom i innym magicznym efektom."),
    ("**_Wishes._** The efreeti has a 30 percent chance of knowing the _Życzenie_ spell. If the efreeti knows it, the efreeti can cast it only on behalf of a non-genie creature who communicates a wish in a way the efreeti can understand. If the efreeti casts the spell for istota, the efreeti suffers none of the spell's stress. Once the efreeti has cast it three times, the efreeti can't do so again for 365 days.", "**_Życzenia._** Efreet ma 30 procent szans na znajomość czaru _Życzenie_. Jeśli go zna, może go rzucać wyłącznie w imieniu istoty niebędącej dżinem, która przekaże życzenie w sposób zrozumiały dla efreeta. Jeśli efreet rzuci ten czar dla tej istoty, nie ponosi żadnych negatywnych skutków stresu związanego z czarem. Gdy efreet rzuci ten czar trzy razy, nie może tego zrobić ponownie przez 365 dni."),
    ("**_Atak wielokrotny._** The efreeti makes three attacks, using Heated Blade or Hurl Flame in any combination.", "**_Atak wielokrotny._** Efreet wykonuje trzy ataki, używając w dowolnej kombinacji Rozżarzonego ostrza lub Miotania płomienia."),
    ("**_Heated Blade._**", "**_Rozżarzone ostrze._**"),
    ("**_Hurl Flame._** _Test ataku dystansowy:_ +8, range 36 m", "**_Miotanie płomienia._** _Test ataku dystansowy:_ +8, zasięg 36 m"),
    ("**_Rzucanie czarów._** The efreeti casts one of the following spells, requiring no komponentów materialnych and using Charisma as the cecha bazowej rzucania czarów (ST rzutu obronnego na czary 16):", "**_Rzucanie czarów._** Efreet rzuca jeden z następujących czarów, nie wymagając komponentów materialnych i używając Charyzmy jako cechy bazowej rzucania czarów (ST rzutu obronnego na czary 16):"),
    ("&emsp;**Na wolności:** _Detect Magic, Żywiołomagia_", "&emsp;**Na wolności:** _Wykrycie magii_, _Żywiołomagia_"),
    ("&emsp;**1/dzień każdy:** _Gaseous Form, Invisibility, Major Image, Plane Shift, Tongues, Ściana ognia_ (level 7 version)", "&emsp;**1/dzień każdy:** _Forma gazowa_, _Niewidzialność_, _Wielka iluzja_, _Przejście między planami_, _Języki_, _Ściana ognia_ (wersja 7. kręgu)"),
    # Erinyes
    ("**_Diabelskie przywracanie._** If the erinyes dies outside the Dziewięciu Piekłach, its body disappears in sulfurous smoke, and it gains a new body instantly, reviving with all its Punkty Wytrzymałości somewhere in the Dziewięciu Piekłach.", "**_Diabelskie przywracanie._** Jeśli erynie umrze poza Dziewięcioma Piekłami, jej ciało znika w siarczystym dymie, a ona natychmiast zyskuje nowe ciało, odradzając się ze wszystkimi Punktami Wytrzymałości gdzieś w Dziewięciu Piekłach."),
    ("**_Odporność na magię._** The erinyes ma ułatwienie do rzutów obronnych against czarom i innym magicznym efektom.", "**_Odporność na magię._** Erynie ma ułatwienie do rzutów obronnych przeciw czarom i innym magicznym efektom."),
    ("**_Magic Rope._** The erinyes has a magic rope. While bearing it, the erinyes can use the Entangling Rope action. The rope has AC 20, HP 90, and niewrażliwość to od trucizny and od energii psychicznej obrażeń. The rope turns to dust if reduced to 0 Punkty Wytrzymałości, if it is 5+ feet away from the erinyes for 1 hour or more, or if the erinyes dies. If the rope is uszkodzona or destroyed, the erinyes can fully restore it when finishing a Short or Long Rest.", "**_Magiczna lina._** Erynie ma magiczną linę. Gdy ją nosi, może użyć akcji Pętająca lina. Lina ma KP 20, PW 90 i niewrażliwość na obrażenia od trucizny i od energii psychicznej. Lina zamienia się w pył, jeśli spadnie do 0 Punktów Wytrzymałości, jeśli znajduje się oddalona o co najmniej 1,5 m od erynie przez 1 godzinę lub dłużej, albo jeśli erynie umrze. Jeśli lina zostanie uszkodzona lub zniszczona, erynie może w pełni ją przywrócić po zakończeniu krótkiego lub długiego odpoczynku."),
    ("**_Atak wielokrotny._** The erinyes makes three Withering Sword attacks and can use Entangling Rope.", "**_Atak wielokrotny._** Erynie wykonuje trzy ataki Więdnącym mieczem i może użyć Pętającej liny."),
    ("**_Withering Sword._**", "**_Więdnący miecz._**"),
    ("**_Entangling Rope (Requires Magic Rope)._** _Rzut obronny na Siłę:_ DC 16, one creature the erinyes can see within 120 feet. _Porażka:_ 14 (4k6) od mocy obrażeń, and cel has stan Skrępowany until the rope is destroyed, the erinyes uses a Bonus Action to release cel, or the erinyes uses Entangling Rope again.", "**_Pętająca lina (wymaga Magicznej liny)._** _Rzut obronny na Siłę:_ ST 16, jedno stworzenie, które erynie widzi, w zasięgu 36 m. _Porażka:_ 14 (4k6) obrażeń od mocy, a cel otrzymuje stan Skrępowany, dopóki lina nie zostanie zniszczona, erynie nie użyje akcji dodatkowej, aby uwolnić cel, albo erynie nie użyje ponownie Pętającej liny."),
    ("**_Parowanie._** _Wyzwalacz:_ The erinyes is hit by a melee attack roll while holding a weapon. _Reakcja:_ The erinyes adds 4 to its AC against that attack, possibly causing it to miss.", "**_Parowanie._** _Wyzwalacz:_ Erynie zostaje trafiona testem ataku wręcz, trzymając broń. _Reakcja:_ Erynie dodaje 4 do swojego KP przeciw temu atakowi, co może spowodować chybienie."),
]

for old, new in REPLACEMENTS:
    if old in text:
        text = text.replace(old, new)
    else:
        print(f"MISSING: {old[:60]}...")

path.write_text(text, encoding="utf-8")
print(f"Batch 2: {len(REPLACEMENTS)} patterns")
