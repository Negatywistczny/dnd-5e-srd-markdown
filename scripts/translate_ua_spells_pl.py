#!/usr/bin/env python3
"""Write fully translated UA spell files."""
from pathlib import Path

UA = Path(__file__).resolve().parents[1] / "dnd2024-wikidot-pl/ua"

SPELLS = {
"spell-bleeding-darkness.md": """# Krwawiąca ciemność (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-bleeding-darkness

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*3. krąg, wywoływania (psionik, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 18 metrów

**Komponenty:** W, S, M (fiolka rzadkiego atramentu wartości 50+ sz)

**Czas trwania:** Koncentracja, do 1 minuty

Tworzysz atramentową pustkę — sferę o promieniu 3 metrów — w punkcie nad sobą, który widzisz w zasięgu.

Gdy rzucasz zaklęcie, magiczna ciemność wylewa się ze sfery, wypełniając walec o promieniu 3 metrów i wysokości 12 metrów ze sfery jako środka do początku twojej następnej tury. Walec to trudny teren; żadne światło — magiczne ani niemagiczne — nie oświetla tego obszaru. Gdy ciemność się pojawia, każda istota w obszarze musi odnieść sukces w rzucie obronnym na Kondycję, albo otrzymuje 3k8 obrażeń od zimna i ma stan oślepienia do końca swojej następnej tury. Istota powtarza ten rzut, gdy po raz pierwszy w turze wchodzi w obszar zaklęcia albo kończy w nim turę. Każda istota robi ten rzut tylko raz na turę.

Do końca czasu trwania akcją magiczną możesz przesunąć sferę o 6 metrów w poziomie i sprawić, że znowu wylewa ciemność do początku twojej następnej tury.

**Użycie komórki czaru wyższego kręgu.** Obrażenia rosną o 1k8 za każdy krąg komórki powyżej 3.
""",

"spell-thought-form.md": """# Forma myśli (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-thought-form

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*6. krąg, przemian (psionik)*

**Czas rzucania:** Akcja dodatkowa

**Zasięg:** Ty

**Komponenty:** W, M (materiał mózgowy w naczyniu wartości 500+ sz)

**Czas trwania:** Koncentracja, do 1 minuty

Na chwilę przemieniasz się w psionicznego ducha. Do końca czasu trwania zyskujesz:

**Duchowa forma.** Masz odporność na obrażenia od trucizny i psychiczne oraz niepodatność na stan wyczerpania.

**Ruch bez ciała.** Masz prędkość lotu 18 metrów i możesz unosić się. Możesz poruszać się przez zajęte pola jak przez trudny teren. Gdy kończysz turę w takim polu, otrzymujesz 1k10 obrażeń od mocy. Jeśli zaklęcie kończy się w takim polu, wracasz na ostatnie wolne miejsce, na którym stałeś.

**Psioniczna regeneracja.** Akcją magiczną możesz dotknąć istoty (w tym siebie) i rzucić 1k6. Istota odzyskuje jedno zużyte miejsce na czar o poziomie równym połowie wyniku (zaokrąglone w górę) lub niższym. Istota nie może skorzystać z tego ponownie przed długim odpoczynkiem.
""",

"spell-telekinetic-crush.md": """# Telekinetyczne zgniecenie (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-telekinetic-crush

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*4. krąg, wywoływania (psionik, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 18 metrów

**Komponenty:** W, S

**Czas trwania:** Natychmiastowy

Tworzysz pole miażdżącej siły telekinetycznej — sześcian o boku 9 metrów w zasięgu. Każda istota w obszarze wykonuje rzut obronny na Siłę. Przy nieudanym rzucie cel otrzymuje 5k6 obrażeń od mocy i ma stan powalony. Przy udanym — połowę obrażeń.
""",

"spell-tasha-s-mind-whip.md": """# Mentalny bicz Tashy (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-tasha-s-mind-whip

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*2. krąg, uroku (psionik, zaklinacz, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 27 metrów

**Komponenty:** W

**Czas trwania:** Natychmiastowy

Psychicznie uderzasz jedną istotę, którą widzisz w zasięgu. Cel musi odnieść sukces w rzucie obronnym na Inteligencję. Przy nieudanym rzucie otrzymuje 3k6 obrażeń psychicznych i do końca swojej następnej tury nie może wykonywać ataków okazji. Ponadto w swojej następnej turze może wykonać albo akcję, albo akcję dodatkową — nie obie. Przy udanym rzucie otrzymuje połowę obrażeń.

**Użycie komórki czaru wyższego kręgu.** Możesz wycelować w jedną dodatkową istotę za każdy krąg komórki powyżej 2.
""",

"spell-tasha-s-mind-whip2.md": """# Mentalny bicz Tashy (UA9 — 02.10.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-tasha-s-mind-whip2

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*2. krąg, uroku (psionik, zaklinacz, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 27 metrów

**Komponenty:** W

**Czas trwania:** Natychmiastowy

Psychicznie uderzasz jedną istotę, którą widzisz w zasięgu. Cel musi odnieść sukces w rzucie obronnym na Inteligencję. Przy nieudanym rzucie otrzymuje 3k6 obrażeń psychicznych i do końca swojej następnej tury nie może wykonywać ataków okazji. W swojej następnej turze może wybrać tylko jedno z trzech: ruch, akcję lub akcję dodatkową. Przy udanym rzucie otrzymuje połowę obrażeń.

**Użycie komórki czaru wyższego kręgu.** Możesz wycelować w jedną dodatkową istotę za każdy krąg komórki powyżej 2.
""",

"spell-summon-astral-entity.md": """# Przywołanie astralnej istoty (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-summon-astral-entity

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*3. krąg, przywoływania (psionik, zaklinacz, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 27 metrów

**Komponenty:** W, S, M (klejnot lub kryształ wartości 300+ sz)

**Czas trwania:** Koncentracja, do 1 godziny

Przywołujesz ducha psionicznej istoty. Materializuje się on na wolnym miejscu, które widzisz w zasięgu, i korzysta z bloku statystyk **Duch psioniczny**. Rzucając zaklęcie, wybierz: istotę kryształową, ektoplazmową lub duchową. Istota przypomina astralną istotę tego typu, co wpływa na szczegóły bloku. Znika po spadku do 0 PW lub gdy zaklęcie się kończy.

Istota jest sojusznikiem ciebie i twoich sojuszników. W walce dzieli z tobą wynik inicjatywy, lecz działa bezpośrednio po twojej turze. Wykonuje twoje polecenia werbalne (bez zużywania twojej akcji). Bez rozkazu wykonuje akcję Unik i używa ruchu, by unikać zagrożenia.

**Użycie komórki czaru wyższego kręgu.** Użyj poziomu komórki czaru jako poziomu zaklęcia w bloku statystyk.

##### Duch psioniczny

| | |
| --- | --- |
| *Średnia aberracja, bezstronna* | |
| **KP:** 11 + poziom zaklęcia + 2 (tylko istota kryształowa) | |
| **PW:** 40 + 10 za każdy krąg powyżej 3 | |
| **Szybkość:** 9 metrów, lot 9 metrów (tylko istota duchowa) | |
| **SIŁ** 16 (+3/+3) | |
| **Odporność:** psychiczne | |
| **Zmysły:** widzenie w ciemności 18 metrów, pasywna Percepcja 11 | |
| **Języki:** głęboka mowa, telepatia 18 metrów | |
| **Premia do biegłości:** równa twojej premii do biegłości | |

**Cechy**

**Przejście bez ciała (tylko istota ektoplazmowa i duchowa).** Duch może poruszać się przez inne istoty i obiekty jak przez trudny teren. Gdy kończy turę w takim polu, zostaje wypchnięty na najbliższe wolne miejsce i otrzymuje 1k10 obrażeń od mocy za każde 1,5 metra przesunięcia.

**Akcje**

**Wieloatak.** Duch wykonuje liczbę ataków równą połowie poziomu tego zaklęcia (zaokrąglone w dół).

**Uderzenie kryształowe (tylko istota kryształowa).** *Test ataku wręcz:* premia równa premii z twojego testu ataku czarem, zasięg 1,5 metra. *Trafienie:* 1k10 + 3 + poziom zaklęcia obrażeń od przeszywających.

**Rozprysk ektoplazmy (tylko istota ektoplazmowa).** *Test ataku dystansowego:* premia równa premii z twojego testu ataku czarem, zasięg 9 metrów. *Trafienie:* 1k6 + 3 + poziom zaklęcia obrażeń psychicznych. *Trafienie lub chybienie:* każda istota w emanacji 1,5 metra ze środka w celu ma zmniejszoną prędkość o 1,5 metra do końca swojej następnej tury.

**Promień ulotny (tylko istota duchowa).** *Test ataku dystansowego:* premia równa premii z twojego testu ataku czarem, zasięg 36 metrów. *Trafienie:* 1k8 + 3 + poziom zaklęcia obrażeń psychicznych.

**Reakcje**

**Rój odłamków (tylko istota kryształowa).** *Wyzwalacz:* duch zostaje trafiony atakiem wręcz. *Odpowiedź:* duch zmniejsza o połowę (zaokrąglone w dół) obrażenia z tego ataku, po czym może teleportować się na wolne miejsce w promieniu 9 metrów od siebie, które widzi.
""",

"spell-raulothim-s-psychic-lance.md": """# Psychiczna lanca Raulothima (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-raulothim-s-psychic-lance

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*4. krąg, uroku (bard, psionik, zaklinacz, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 36 metrów

**Komponenty:** W

**Czas trwania:** Natychmiastowy

Z czoła wypuszczasz migoczącą lancę mocy psychicznej w istotę, którą widzisz w zasięgu. Alternatywnie wymawiasz imię istoty (pseudonim, tytuł lub przezwisko nie wystarczą). Jeśli wymieniona istota jest w zasięgu, staje się celem nawet bez widoczności. Jeśli nie jest w zasięgu lub imię jest nieprawidłowe, lanca rozprasza się bez efektu.

Cel musi odnieść sukces w rzucie obronnym na Inteligencję. Przy nieudanym rzucie otrzymuje 7k6 obrażeń psychicznych i ma stan obezwładniony do początku twojej następnej tury. Przy udanym — połowę obrażeń.

**Użycie komórki czaru wyższego kręgu.** Obrażenia rosną o 1k6 za każdy krąg komórki powyżej 4.
""",

"spell-psychic-scream.md": """# Psychiczny krzyk (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-psychic-scream

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*9. krąg, uroku (bard, psionik, zaklinacz, czarownik)*

**Czas rzucania:** Akcja

**Zasięg:** 27 metrów

**Komponenty:** S

**Czas trwania:** Natychmiastowy

Uwalniasz moc umysłu, by uderzyć w inteligencję do dziesięciu wybranych istot, które widzisz w zasięgu. Istoty o wyniku Inteligencji 2 lub niższym nie są dotknięte.

Każdy cel wykonuje rzut obronny na Inteligencję. Przy nieudanym rzucie otrzymuje 14k6 obrażeń psychicznych i ma stan ogłuszony. Przy udanym — połowę obrażeń. Jeśli cel spada do 0 PW od tych obrażeń, jego głowa eksploduje — o ile ma głowę.

Na końcu każdej swojej tury ogłuszony cel powtarza rzut; sukces kończy stan.
""",

"spell-mental-prison.md": """# Mentalne więzienie (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-mental-prison

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*6. krąg, iluzji (bard, psionik, zaklinacz, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 18 metrów

**Komponenty:** S

**Czas trwania:** Koncentracja, do 1 minuty

Próbujesz uwięzić istotę w iluzorycznej celi, którą widzi tylko ona. Jedna istota, którą widzisz w zasięgu, musi odnieść sukces w rzucie obronnym na Inteligencję, albo otrzymuje 8k10 obrażeń psychicznych i ma stan zauroczony przez czas trwania. Przy udanym rzucie otrzymuje połowę obrażeń i zaklęcie się kończy.

Gdy jest zauroczony, cel ma stan skrępowany i postrzega przestrzeń wokół siebie jako niebezpieczną — w formie, którą wybierasz: ogień, unoszące się brzytwy, paszcze pełne kapiących zębów itd. Nie widzi ani nie słyszy niczego poza iluzją. Jeśli cel zostanie przesunięty z iluzji, wykona atak wręcz przez nią albo wyciągnie przez nią część ciała, otrzymuje 5k10 obrażeń psychicznych i zaklęcie się kończy.
""",

"spell-life-inversion-field.md": """# Pole odwrócenia życia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-life-inversion-field

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*4. krąg, odwracania (kleryk, psionik, zaklinacz)*

**Czas rzucania:** Akcja

**Zasięg:** Ty

**Komponenty:** W, S

**Czas trwania:** Koncentracja, do 1 minuty

Aura promieniuje od ciebie emanacją 9 metrów przez czas trwania. Gdy tworzysz aurę, odzyskujesz 4k8 PW. Za każdym razem, gdy odzyskujesz PW, możesz wybrać istotę, którą widzisz w aurze, i zmusić ją do rzutu obronnego na Kondycję. Przy nieudanym rzucie otrzymuje obrażenia nekrotyczne równe połowie odzyskanych PW (zaokrąglone w górę). Istota robi ten rzut tylko raz na turę.

**Użycie komórki czaru wyższego kręgu.** Leczenie rośnie o 1k8 za każdy krąg komórki powyżej 4.
""",

"spell-intellect-fortress.md": """# Twierdza intelektu (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-intellect-fortress

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion) i [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*3. krąg, odwracania (wynalazca, bard, psionik, zaklinacz, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 9 metrów

**Komponenty:** W

**Czas trwania:** Koncentracja, do 1 godziny

Przez czas trwania jedna chętna istota, którą widzisz w zasięgu, ma odporność na obrażenia psychiczne oraz ułatwienie w rzutach obronnych na Inteligencję, Mądrość i Charyzmę.

**Użycie komórki czaru wyższego kręgu.** Możesz wycelować w jedną dodatkową istotę za każdy krąg komórki powyżej 3.
""",

"spell-abi-dalzim-s-horrid-wilting.md": """# Ohydne więdnięcie Abi-Dalzima (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-abi-dalzim-s-horrid-wilting

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*8. krąg, nekromancji (psionik, zaklinacz, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 45 metrów

**Komponenty:** W, S, M (kawałek gąbki)

**Czas trwania:** Natychmiastowy

Wysysasz wilgoć z każdej istoty w sześcianie o boku 9 metrów ze środkiem w punkcie w zasięgu. Każda istota w obszarze wykonuje rzut obronny na Kondycję — przy nieudanym otrzymuje 12k8 obrażeń nekrotycznych, przy udanym połowę.

Konstrukty automatycznie odnoszą sukces w rzucie; rośliny automatycznie go nie udają.

Niemagiczne rośliny w obszarze, które nie są istotami (drzewa, krzewy), więdną i giną natychmiast.
""",

"spell-telekinetic-fling.md": """# Telekinetyczne miotnięcie (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-telekinetic-fling

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion)

*Sztuczka, wywoływania (psionik)*

**Czas rzucania:** Akcja

**Zasięg:** 18 metrów

**Komponenty:** W, M (strzała, bełt, pocisk lub igła wartości co najmniej 1 ss)

**Czas trwania:** Natychmiastowy

Wymachujesz amunicją używaną do rzucenia tego zaklęcia i wystrzeliwujesz ją psioniczną energią w istotę w zasięgu. Wykonaj dystansowy test ataku czarem. Trafienie: 1k10 obrażeń od mocy; amunicja zostaje zniszczona.

**Ulepszenie sztuczki.** Obrażenia rosną o 1k10 na 5. (2k10), 11. (3k10) i 17. (4k10) poziomie.
""",

"spell-telekinetic-fling2.md": """# Telekinetyczne miotnięcie (UA9 — 02.10.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-telekinetic-fling2

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*Sztuczka, wywoływania (psionik)*

**Czas rzucania:** Akcja

**Zasięg:** 18 metrów

**Komponenty:** S

**Czas trwania:** Natychmiastowy

Wybierz jeden niemagiczny przedmiot o masie 0,5–2 kg w promieniu 3 metrów od siebie, który nie jest noszony ani trzymany. Otaczasz go psioniczną energią i wystrzeliwasz w istotę w zasięgu. Wykonaj dystansowy test ataku czarem. Trafienie: 1k10 obrażeń od mocy. Trafienie lub chybienie: przedmiot spada na ziemię nietknięty.

**Ulepszenie sztuczki.** Obrażenia rosną o 1k10 na 5. (2k10), 11. (3k10) i 17. (4k10) poziomie.
""",

"spell-ectoplasmic-trail.md": """# Ektoplazmowy ślad (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-ectoplasmic-trail

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*2. krąg, nekromancji (psionik, czarownik)*

**Czas rzucania:** Akcja dodatkowa

**Zasięg:** Ty

**Komponenty:** W, S

**Czas trwania:** Natychmiastowy

Otaczasz się duchami, które do końca twojej tury zostawiają ektoplazmę. Gdy jesteś otoczony, możesz poruszać się przez zajęte pola jak przez trudny teren; ruch nie prowokuje ataków okazji. Gdy kończysz turę w takim polu, wracasz na ostatnie wolne miejsce.

Gdy wchodzisz w pole istoty, pokrywa ją ektoplazma do końca twojej następnej tury. Pokryta istota ma zmniejszoną prędkość o 3 metry i na początku swojej tury otrzymuje 2k8 obrażeń nekrotycznych. Istota może być pokryta ektoplazmą tylko raz na turę.

**Użycie komórki czaru wyższego kręgu.** Twoja prędkość rośnie o 3 metry za każdy krąg komórki powyżej 2, dopóki jesteś otoczony.
""",

"spell-psionic-blast.md": """# Psioniczny wybuch (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-psionic-blast

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*6. krąg, wywoływania (psionik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** Ty

**Komponenty:** W, S, M

**Czas trwania:** Natychmiastowy

Uwalniasz wstrząsającą falę psionicznej energii.

Każda istota w stożku o długości 18 metrów wychodzącym od ciebie wykonuje rzut obronny na Inteligencję. Przy nieudanym rzucie otrzymuje 6k8 obrażeń psychicznych i ma stan ogłuszony do początku twojej następnej tury. Przy udanym — połowę obrażeń.

**Użycie komórki czaru wyższego kręgu.** Obrażenia rosną o 1k8 za każdy krąg komórki powyżej 6.
""",

"spell-homunculus-servant.md": """# Sługa homunkulusa (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-homunculus-servant

---

Źródło: [UA wynalazcy (17.12.2024)](https://www.dndbeyond.com/sources/dnd/ua/the-artificer) i [UA aktualizacji Eberron (27.02.2025)](https://www.dndbeyond.com/sources/dnd/ua/eberron-updates)

*2. krąg, przywoływania (wynalazca)*

**Czas rzucania:** 1 godzina lub rytuał

**Zasięg:** 3 metry

**Komponenty:** W, S, M (klejnot lub kryształ wartości 100+ sz, który zaklęcie zużywa)

**Czas trwania:** Natychmiastowy

Przywołujesz specjalnego homunkulusa na wolnym miejscu w zasięgu. Korzysta z bloku statystyk **Sługa homunkulusa**. Jeśli masz już homunkulusa z tego czaru, zostaje zastąpiony nowym. Ustalasz wygląd homunkulusa, na przykład mechanicznego ptaka, skrzydeł z probówek albo miniaturowego ożywionego kotła.

##### Sługa homunkulusa

| | |
| --- | --- |
| *Drobna istota, konstrukt, bezstronny* | |
| **KP:** 13 | |
| **PW:** 5 + 5 za każdy krąg czaru (homunkulus ma tyle k4 PW, ile wynosi krąg czaru) | |
| **Szybkość:** 6 metrów, lot 9 metrów | |
| **SIŁ** 4 (−3/−3) | |
| **Niepodatność:** trucizna; wyczerpanie, zatruty | |
| **Zmysły:** widzenie w ciemności 18 metrów, pasywna Percepcja 10 | |
| **Języki:** telepatia 1,6 kilometra (działa tylko z tobą) | |
| **Premia do biegłości:** równa twojej premii do biegłości | |

**Cechy**

**Wymijanie.** Jeśli homunkulus podlega efektowi, który pozwala mu wykonać rzut obronny na Zręczność, by otrzymać tylko połowę obrażeń, nie otrzymuje obrażeń przy udanym rzucie i tylko połowę przy nieudanym. Nie może skorzystać z tej cechy, jeśli ma stan obezwładniony.

**Magiczna więź.** Dodaj krąg czaru do każdego testu cechy albo rzutu obronnego wykonywanego przez homunkulusa.

**Akcje**

**Uderzenie mocy.** *Test ataku wręcz albo dystansowego:* premia równa premii z twojego testu ataku czarem, zasięg 1,5 metra albo 9 metrów. *Trafienie:* 1k6 + krąg czaru obrażeń od mocy.

**Reakcje**

**Kierowanie magii.** *Wyzwalacz:* rzucasz czar o zasięgu dotyk, gdy homunkulus jest w promieniu 36 metrów od ciebie. *Odpowiedź:* homunkulus dostarcza czar dotykiem.

**Walka**

Homunkulus jest sojusznikiem ciebie i twoich sojuszników. W walce dzieli z tobą wynik inicjatywy, lecz działa w turze bezpośrednio po twojej. Wykonuje twoje polecenia (bez zużywania twojej akcji). Jeśli nie wydasz żadnego, wykonuje akcję Unik i używa ruchu, by unikać zagrożenia.

**Użycie komórki czaru wyższego kręgu.** Użyj kręgu komórki jako kręgu czaru w bloku statystyk.
""",

"spell-life-siphon.md": """# Syfon życia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-life-siphon

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*1. krąg, wywoływania (psionik)*

**Czas rzucania:** Akcja

**Zasięg:** 36 metrów

**Komponenty:** S

**Czas trwania:** Natychmiastowy

Wystrzeliwujesz kulę psionicznej energii zasilanej twoją siłą życiową w istotę, którą widzisz w zasięgu. Wykonaj dystansowy test ataku czarem. Trafienie: 1k10 obrażeń psychicznych; możesz wydać jedną kość wytrzymałości, by zwiększyć obrażenia o 1k10.

**Użycie komórki czaru wyższego kręgu.** Obrażenia rosną o 1k10, a liczba kości wytrzymałości, które możesz wydać, rośnie o jedną za każdy krąg komórki powyżej 1.
""",

"spell-enemies-abound.md": """# Wrogowie wszędzie (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-enemies-abound

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*3. krąg, uroku (bard, psionik, zaklinacz, czarownik, mag)*

**Czas rzucania:** Akcja

**Zasięg:** 36 metrów

**Komponenty:** W, S

**Czas trwania:** Koncentracja, do 1 minuty

Wybierz istotę, którą widzisz w zasięgu. Cel musi odnieść sukces w rzucie obronnym na Inteligencję, albo ma stan przerażony przez czas trwania.

Gdy jest przerażony, traci zdolność rozróżniania przyjaciół od wrogów i działa tak:

• Uznaje wszystkie widziane istoty za wrogów.

• Gdy wybiera cel inny niż siebie do ataku, czaru lub innej zdolności, musi wybrać losowo spośród istot widzianych w zasięgu tego ataku, czaru lub zdolności.

• Musi wykonać atak okazji za każdym razem, gdy może.

Za każdym razem, gdy cel otrzymuje obrażenia, powtarza rzut obronny na Inteligencję. Sukces kończy zaklęcie.
""",

"spell-ego-whip.md": """# Bicz ego (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:spell-ego-whip

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*2. krąg, uroku (psionik)*

**Czas rzucania:** Reakcja, wykonywana gdy istota, którą widzisz w promieniu 9 metrów od siebie, wykonuje test cechy lub rzut obronny oparty na Charyzmie

**Zasięg:** 36 metrów

**Komponenty:** W

**Czas trwania:** Natychmiastowy

Istota wykonuje rzut obronny na Charyzmę. Przy nieudanym rzucie odejmuje 1k8 od testu cechy lub rzutu obronnego.
""",
}

def main():
    for name, content in SPELLS.items():
        path = UA / name
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print("Wrote", name)

if __name__ == "__main__":
    main()
