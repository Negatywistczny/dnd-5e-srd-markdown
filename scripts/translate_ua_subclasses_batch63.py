#!/usr/bin/env python3
"""Translate UA cleric + druid preservation subclasses (batch 63)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"

FILES = {
    "subclass-cleric-arcana-domain.md": """# Domena arkanów (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-cleric-arcana-domain

---

Źródło: [UA6 — Podklasy arkaniczne (26.06.2025)](https://www.dndbeyond.com/sources/dnd/ua/arcane-subclasses)

*Splataj przekonanie z mocą arkaniczną*

Magia przenika multiwersum i napędza zarówno zniszczenie, jak i stworzenie. Klerycy tej domeny postrzegają wiedzę magiczną nie jako władzę do osobistych celów, lecz jako dar, za który odpowiadają przed innymi.

Bogowie związani z Domeną arkanów znają sekrety i potencjał magii. Często łączą się z wiedzą, bo nauka i moc arkaniczna idą w parze, albo z tajemnicą i władzą.

### Poziom 3: Czary domeny arkanów

Twoje powiązanie z tą boską domeną zapewnia, że zawsze masz przygotowane określone czary. Gdy osiągasz poziom kleryka wskazany w tabeli Czary domeny arkanów, zawsze masz przygotowane wymienione czary.

### Czary domeny arkanów

| Poziom kleryka | Przygotowane czary |
| --- | --- |
| 3 | [Wykrywanie magii](../spells/detect-magic.md), [Magiczny pocisk](../spells/magic-missile.md), [Magiczna broń](../spells/magic-weapon.md), [Magiczna aura Nystula](../spells/nystul-s-magic-aura.md) |
| 5 | [Przeciwdziałanie](../spells/counterspell.md), [Rozproszenie magii](../spells/dispel-magic.md) |
| 7 | [Magiczne oko](../spells/arcane-eye.md), [Sekretny kufer Leomunda](../spells/leomunds-secret-chest.md) |
| 9 | [Dłoń Bigby'ego](../spells/bigby-s-hand.md), [Krąg teleportacyjny](../spells/teleportation-circle.md) |

### Poziom 3: Inicjacja arkaniczna

Zyskujesz następujące korzyści.

**Wiedza arkaniczna.** Zyskujesz biegłość w umiejętności Wiedza tajemna, jeśli jej jeszcze nie masz. Masz też w niej biegłość ekspercką.

**Sztuczki.** Uczysz się dwóch sztuczek maga według własnego wyboru. Za każdym razem, gdy zyskujesz poziom kleryka, możesz zamienić jedną z tych sztuczek na inną sztuczkę maga.

### Poziom 3: Modyfikacja magii

Możesz używać Aktu wiary, by zmieniać swoje czary w chwili rzucania. Gdy rzucasz czar, możesz wydać jedno użycie Aktu wiary i zmienić czar jednym z poniższych sposobów (nie wymaga akcji).

**Wzmacniający czar.** Jeden cel czaru zyskuje tymczasowe PW równe 2k8 plus twój poziom kleryka.

**Uporczywy czar.** Gdy rzucasz czar zmuszający istotę do rzutu obronnego, wybierz jeden cel czaru, który widzisz. Rzuć 1k6 i zastosuj wyrzuconą liczbę jako karę do rzutu obronnego celu.

### Poziom 6: Odzyskanie przez rozproszenie

Natychmiast po rzuceniu czaru z komórką czaru, który przywraca PW istocie albo kończy stan u istoty, możesz rzucić [Rozproszenie magii](../spells/dispel-magic.md) na tę istotę akcją dodatkową bez zużywania komórki czaru.

Możesz użyć tej cechy liczbę razy równą twojemu modyfikatorowi Mądrości (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 17: Mistrzostwo arkaniczne

Uczysz się czterech czarów maga — po jednym z kręgów 6, 7, 8 i 9. Zawsze masz te czary przygotowane. Za każdym razem, gdy zyskujesz poziom kleryka, możesz zamienić jeden z tych czarów na inny czar maga tego samego kręgu.
""",
    "subclass-cleric-grave-domain.md": """# Domena grobu (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-cleric-grave-domain

---

Źródło: [UA4 — Podklasy grozy (06.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/horror-subclasses)

*Uosabiaj boskie siły śmierci*

Domena grobu dotyczy granicy między życiem a śmiercią. Dla tych, którzy czerpią moc tej domeny, śmierć jest naturalną i nieuniknioną częścią multiwersum. Tacy klerycy niszczą nieumarłych i prowadzą duchy w zaświaty — niezależnie od tego, czy te duchy tego chcą.

Magia tej domeny pozwala klerykom również na chwilowe odwleczenie śmierci, zwłaszcza dla tych, którzy mają jeszcze wielkie dzieło do wykonania. Jest to jednak tylko zwłoka, nie zaprzeczenie — grób zawsze odbierze swoją należność.

### Poziom 3: Krąg śmiertelności

Zyskujesz zdolność manipulowania równowagą między życiem a śmiercią. Zyskujesz następujące korzyści.

**Pociąg śmierci.** Raz na turę, gdy rzucasz czar albo trafiasz testem ataku i zadajesz obrażenia skrwawionej istocie, ta istota otrzymuje dodatkowe 1k4 obrażeń nekrotycznych.

**Powrót do życia.** Gdy normalnie miałbyś rzucić jedną lub więcej kości, by przywrócić PW istocie z 0 PW czarem lub Aktem wiary, nie rzucasz tych kości na leczenie; zamiast tego używasz najwyższej możliwej liczby dla każdej kości. Na przykład zamiast przywrócić 2k4 PW istocie z 0 PW czarem, przywracasz 8.

### Poziom 3: Czary domeny grobu

Twoje powiązanie z tą boską domeną zapewnia, że zawsze masz przygotowane określone czary. Gdy osiągasz poziom kleryka wskazany w tabeli Czary domeny grobu, zawsze masz przygotowane wymienione czary.

### Czary domeny grobu

| Poziom kleryka | Czary |
| --- | --- |
| 3 | [Zguba](../spells/bane.md), [Przeszywający dotyk](../spells/chill-touch.md), [Wykrycie dobra i zła](../spells/detect-evil-and-good.md), [Bezpieczny spoczynek](../spells/gentle-repose.md), [Promień osłabienia](../spells/ray-of-enfeeblement.md) |
| 5 | [Ożywienie](../spells/revivify.md), [Wampiryczny dotyk](../spells/vampiric-touch.md) |
| 7 | [Zaraza](../spells/blight.md), [Rozproszenie dobra i zła](../spells/dispel-evil-and-good.md) |
| 9 | [Unieruchomienie potwora](../spells/hold-monster.md), [Wskrzeszenie](../spells/raise-dead.md) |

### Poziom 3: Ścieżka do grobu

Akcją dodatkową prezentujesz symbol wiary i zużywasz użycie Aktu wiary, by przekląć jedną istotę, którą widzisz w promieniu 9 metrów od siebie, do początku twojej następnej tury. Dopóki jest przeklęta, istota ma utrudnienie do testów ataku i rzutów obronnych.

Gdy ty lub sojusznik, którego widzisz, traficie przeklęty cel testem ataku, możesz wcześniej zakończyć klątwę (nie wymaga akcji), by sprawić, że atak zada dodatkowe obrażenia nekrotyczne lub promieniste (według twojego wyboru) równe 1k8 plus twój poziom kleryka.

### Poziom 6: Strażnik u progu śmierci

Gdy ty lub skrwawiona istota, którą widzisz w promieniu 9 metrów od siebie, zostaniecie trafieni testem ataku, możesz wykorzystać reakcję, by zmniejszyć obrażenia tego ataku o połowę.

Możesz skorzystać z tej cechy liczbę razy równą twojemu modyfikatorowi Mądrości (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 17: Boski żniwiarz

Twoje głębokie powiązanie z tą domeną czyni cię uświęconym zwiastunem śmierci. Zyskujesz następujące korzyści.

**Wzmocniona nekromancja.** Gdy rzucasz czar 5. kręgu lub niższego ze szkoły Nekromancji, który ma jeden cel, albo czar z tabeli Czary domeny grobu, możesz zużyć użycie Aktu wiary, by wycelować w drugą istotę w zasięgu czaru. Jeśli czar wymaga kosztownych lub zużywanych komponentów materialnych, musisz dostarczyć komponenty dla każdego celu.

**Strażnik dusz.** Gdy wróg umiera w promieniu 18 metrów od ciebie, ty lub jedna istota, którą widzisz w promieniu 18 metrów od siebie, odzyskujecie PW równe trzykrotności twojego poziomu kleryka. Nie możesz skorzystać z tej cechy, jeśli masz stan obezwładniony. Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Krótkiego lub Długiego odpoczynku.
""",
    "subclass-cleric-knowledge-domain.md": """# Domena wiedzy (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-cleric-knowledge-domain

---

Źródło: [UA — Podklasy Zapomnianych Krain (28.01.2025)](https://www.dndbeyond.com/sources/dnd/ua/forgotten-realms-subclasses)

*Odkrywaj sekrety i opanuj umysł*

Domena wiedzy ceni naukę i zrozumienie ponad wszystko. Klerycy czerpiący z tej domeny studiują ezoteryczną wiedzę, gromadzą stare tomy, zagłębiają się w tajne miejsca i badają procesy umysłu.

Bogowie wiedzy sięgają od mistrzów magii arkanicznej po patronów rzemiosła i wynalazków. Dla nich wiedza jest cenniejsza niż bogactwo materialne, a uczenie się jest aktem kultu. Biblioteki, uniwersytety i inne instytucje edukacyjne również czerpią moc Domeny wiedzy.

W Faerûn klerycy Domeny wiedzy czczą bóstwa nauki i pomysłowości, takie jak Oghma i Gond. Inne potężne bóstwa — Asmodeus, Mystra, Savras i Jergal — również mają wśród wyznawców kleryków tej domeny, podobnie jak rzadsze, na przykład Deneir, Skryba Oghmy, i Azuth, sługa Mystry.

### Poziom 3: Błogosławieństwa wiedzy

Zyskujesz biegłość w jednym rodzaju narzędzi rzemieślniczych według własnego wyboru oraz w dwóch z następujących umiejętności według własnego wyboru: Wiedza tajemna, Historia, Natura lub Religia. Masz w nich biegłość ekspercką.

### Poziom 3: Czary domeny wiedzy

Gdy osiągasz poziom kleryka wskazany w tabeli Czary domeny wiedzy, zawsze masz przygotowane wymienione czary.

### Czary domeny wiedzy

| Poziom kleryka | Przygotowane czary |
| --- | --- |
| 3 | [Rozkaz](../spells/command.md), [Rozumienie języków](../spells/comprehend-languages.md), [Wykrywanie magii](../spells/detect-magic.md), [Wykrywanie myśli](../spells/detect-thoughts.md), [Identyfikacja](../spells/identify.md), [Mind Spike](../spells/mind-spike.md) |
| 5 | [Rozproszenie magii](../spells/dispel-magic.md), [Niewykrywalność](../spells/nondetection.md), [Języki](../spells/tongues.md) |
| 7 | [Magiczne oko](../spells/arcane-eye.md), [Wypędzenie](../spells/banishment.md), [Dezorientacja](../spells/confusion.md) |
| 9 | [Legendarna wiedza](../spells/legend-lore.md), [Wizja](../spells/scrying.md), [Synaptic Static](../spells/synaptic-static.md) |

### Poziom 3: Magia umysłu

Akcją magiczną możesz wydać jedno użycie Aktu wiary, by ujawnić swoją magiczną wiedzę. Wybierz jeden czar z tabeli Czary domeny wiedzy, który masz przygotowany. W ramach tej akcji rzucasz ten czar bez zużywania komórki czaru i bez komponentów materialnych.

### Poziom 6: Nieskrępowany umysł

Zyskujesz telepatię na odległość 18 metrów. Gdy używasz tej telepatii, możesz jednocześnie kontaktować się z liczbą istot równą twojemu modyfikatorowi Mądrości (minimum jedną).

Ponadto, jeśli wynik twojego testu Inteligencji jest niższy niż twoja wartość Mądrości, możesz użyć tej wartości Mądrości zamiast wyniku testu.

### Poziom 17: Boska przewidująca wiedza

Akcją dodatkową magicznie rozszerzasz swój umysł w przyszłość. Przez 1 godzinę masz ułatwienie do testów K20. Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku. Możesz też odzyskać użycie, wydając komórkę czaru 6. kręgu lub wyższego (nie wymaga akcji).
""",
    "subclass-cleric-pestilence-domain.md": """# Domena zarazy (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-cleric-pestilence-domain

---

Źródło: [UA12 — Złoczyńcze opcje (02.04.2026)](https://www.dndbeyond.com/posts/2150-designer-insights-from-unearthed-arcana-villainous)

*Rozpalaj plagę i rozkład*

Klerycy Domeny zarazy wykorzystują nadnaturalną plagę i rozkład, by niszczyć witalność wrogów. Choć pospólstwo często postrzega zarazę jako siłę niepohamowanego zniszczenia, klerycy tej domeny władają nią z chirurgiczną precyzją.

Domena zarazy wiąże się z bogami trucizny, chorób, głodu i rozkładu. Te bóstwa używają zwiędłych plonów, magicznych epidemii oraz rojów owadów i szkodników, by motywować lub karać śmiertelników zgodnie ze swoją doktryną. Wyznawcami są aptekarze, lekarze, truciciele i degustatorzy królewscy. Inni oddają cześć bogu zarazy, by oszczędzić swoje społeczności lub bliskich.

### Poziom 3: Tkacz zarazy

Zyskujesz następujące korzyści.

**Zaszczepiona dusza.** Masz odporność na obrażenia nekrotyczne i truciznę oraz nie możesz zarazić się magicznymi chorobami.

**Gnicie i ropień.** Obrażenia z twoich czarów kleryka i cech kleryka ignorują odporność na obrażenia nekrotyczne i truciznę. Ponadto, gdy rzucasz czar kleryka albo używasz cechy kleryka zadającej obrażenia nekrotyczne lub trucizną, możesz zmienić te obrażenia na drugi typ.

### Poziom 3: Czary domeny zarazy

Twoje powiązanie z tą boską domeną zapewnia, że zawsze masz przygotowane określone czary. Gdy osiągasz poziom kleryka wskazany w tabeli Czary domeny zarazy, zawsze masz przygotowane wymienione czary.

### Czary domeny zarazy

| Poziom kleryka | Czary |
| --- | --- |
| 3 | [Wykrycie trucizny i choroby](../spells/detect-poison-and-disease.md), [Ochrona przed trucizną](../spells/protection-from-poison.md), [Promień osłabienia](../spells/ray-of-enfeeblement.md), [Promień zatrucia](../spells/ray-of-sickness.md) |
| 5 | [Śmierdząca chmura](../spells/stinking-cloud.md), [Wampiryczny dotyk](../spells/vampiric-touch.md) |
| 7 | [Zaraza](../spells/blight.md), [Olbrzymie owady](../spells/giant-insect.md) |
| 9 | [Zarażenie](../spells/contagion.md), [Plaga owadów](../spells/insect-plague.md) |

### Poziom 3: Błogosławieństwo plagi

Akcją magiczną możesz prezentować symbol wiary i wydać użycie Aktu wiary, by manifestować promień 1,5 metra wychodzący od ciebie albo od chętnej istoty, którą dotykasz, wypełniony niszczącą plagą przez 1 minutę. Efekt kończy się wcześniej, jeśli go rozwiążesz (nie wymaga akcji), manifestujesz ponownie albo masz stan obezwładniony.

Każda istota według twojego wyboru, która rozpoczyna turę w emanacji, musi odnieść sukces w rzucie obronnym na Kondycję przeciwko ST twoich czarów, inaczej zyskuje 1 poziom wyczerpania. Ta cecha nie może podnieść poziomu wyczerpania istoty powyżej poziomu równego twojemu modyfikatorowi Mądrości (minimum 1 poziom wyczerpania). Na przykład przy Mądrości 16 cecha nie podniesie poziomu wyczerpania istoty powyżej 3.

Plaga rozprzestrzeniana tą cechą manifestuje się określonym objawem. Wybierz go z tabeli Objawy plagi albo wylosuj.

##### Objawy plagi

| 1k6 | Zakażona istota… |
| --- | --- |
| 1 | Traci wszystkie kolory i wygląda w monochromatycznych odcieniach szarości. |
| 2 | Zrzuca metaliczne, rdzawo-czerwone płatki i skrzypi podczas ruchu. |
| 3 | Wydziela cuchnącą śluz. |
| 4 | Jest otoczona chmurą brzęczących owadów. |
| 5 | Wyrasta z jej ciała grzyb lub inna roślinność. |
| 6 | Jest pokryta świecącymi krostami. |

### Poziom 6: Wirulentny wybuch

Gdy wróg w promieniu 18 metrów od ciebie spada do 0 PW, możesz wykorzystać reakcję, by sprawić, że z jego ciała wybuchnie plaga, rozprzestrzeniając się w promieniu 3 metrów wychodzącym od wroga; jeśli wróg miał co najmniej 1 poziom wyczerpania, promień wzrasta do 6 metrów.

Każda istota według twojego wyboru w emanacji wykonuje rzut obronny na Kondycję przeciwko ST twoich czarów. Przy nieudanym rzucie cel doświadcza jednego z poniższych efektów:

**Gnilny wstrząs.** Cel ma stan obezwładniony do końca swojej następnej tury. Dopóki jest obezwładniony, jego prędkość wynosi 0.

**Toksyczna infekcja.** Cel otrzymuje 3k6 obrażeń nekrotycznych lub trucizną (według twojego wyboru).

Możesz użyć tej cechy liczbę razy równą twojemu modyfikatorowi Mądrości (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 17: Forma robactwa

Akcją dodatkową możesz przemienić się w Średni rój Drobných szkodników, takich jak karaluchy, larwy albo szczury. W tej formie zachowujesz ogólny kształt, osobowość, wspomnienia i zdolność mówienia; wyposażenie, które nosisz lub trzymasz, nie przemienia się z tobą, ale możesz nadal z niego korzystać. Twoje statystyki gry pozostają takie same, z wyjątkiem poniższych zmian:

**Niewrażliwości na stany.** Masz niewrażliwość na stany schwytany, sparaliżowany, powalony i unieruchomiony.

**Odporności na obrażenia.** Masz odporność na obrażenia obuchowe, kłute i sieczne.

**Ruch.** Możesz wejść na przestrzeń innej istoty i odwrotnie. Ponadto masz prędkość wspinaczki równą swojej prędkości i możesz wspinać się po trudnych powierzchniach — w tym po suficie — bez wykonywania testu cechy.

**Plaga ugryzień.** Za każdym razem, gdy wchodzisz na przestrzeń wroga, ta istota otrzymuje obrażenia równe twojemu modyfikatorowi Mądrości; obrażenia są nekrotyczne, kłute lub trucizną (według twojego wyboru). Istota otrzymuje te obrażenia również, gdy wchodzi na twoją przestrzeń albo kończy tam turę. Istota otrzymuje te obrażenia tylko raz na turę.

Wracasz do prawdziwej formy po 10 minutach, gdy zdecydujesz się zakończyć przemianę (nie wymaga akcji), gdy masz stan obezwładniony albo gdy umrzesz.

Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku, chyba że wydasz komórkę czaru 5. kręgu lub wyższego (nie wymaga akcji), by odzyskać użycie.
""",
    "subclass-druid-circle-of-preservation.md": """# Krąg Ochrony (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-druid-circle-of-preservation

---

Źródło: [UA7 — Podklasy apokaliptyczne (21.08.2025)](https://www.dndbeyond.com/sources/dnd/ua/apocalyptic-subclasses)

*Chroń naturę i uzdrawiaj świat*

Druidzi Kręgu Ochrony niestrudzenie dbają o zachowanie zasobów naturalnych i odbudowę miejsc zniszczonych przez chciwość i wyzysk. Łącząc ochronę z magią regeneracji, druidzi tego zakonu osłaniają życie i rozprzestrzeniają je po kraju. Najpotężniejsi członkowie zakonu potrafią przywracać witalność jałowym polom, zamieniając pustkowia z powrotem w kwitnącą dzicz.

### Poziom 3: Czary kręgu ochrony

Gdy osiągasz poziom druida wskazany w tabeli Czary kręgu ochrony, zawsze masz przygotowane wymienione czary.

### Czary kręgu ochrony

| Poziom druida | Czary |
| --- | --- |
| 3 | [Błogosławieństwo](../spells/bless.md), [Mniejsze przywrócenie](../spells/lesser-restoration.md), [Ochrona przed trucizną](../spells/protection-from-poison.md), [Sanktuarium](../spells/sanctuary.md) |
| 5 | [Promień nadziei](../spells/beacon-of-hope.md), [Rozrost roślin](../spells/plant-growth.md) |
| 7 | [Aura życia](../spells/aura-of-life.md), [Osłona przed śmiercią](../spells/death-ward.md) |
| 9 | [Większe przywrócenie](../spells/greater-restoration.md), [Konsekracja](../spells/hallow.md) |

### Poziom 3: Chroniona ziemia

Akcją dodatkową możesz wydać użycie Dzikiej postaci, by wypełnić sześcian o boku 4,5 metra wychodzący z punktu na ziemi, który widzisz w promieniu 36 metrów od siebie, ożywczą energią. Efekt trwa 1 minutę albo dopóki nie masz stanu obezwładniony, nie oddalisz się o więcej niż 36 metrów od sześcianu albo nie umrzesz.

Za każdym razem, gdy istota (w tym ty) kończy turę w sześcianie, możesz przyznać jej jedną z poniższych korzyści:

**Wzmocnienie.** Istota zyskuje tymczasowe PW równe 1k4 plus twój poziom druida.

**Oczyszczenie.** Kończysz u istoty jeden efekt powodujący stan przerażony lub zatruty.

Ponadto na ziemi w sześcianie wyrasta niemagiczna roślinność typowa dla regionu. Roślinność znika, gdy efekt się kończy.

Akcją dodatkową w kolejnych turach możesz przesunąć sześcian o do 9 metrów w inne miejsce na ziemi w promieniu 36 metrów od siebie.

### Poziom 3: Uczeń ochrony

Twoje studia poprawiły zrozumienie porządku i odporności natury, co daje następujące korzyści.

**Oszczędne rzucanie.** Gdy rzucasz czar druida, możesz zrobić to bez komponentów materialnych, z wyjątkiem komponentów zużywanych przez czar albo mających koszt podany w opisie czaru.

Ponadto, gdy rzucasz czar druida wymagający komponentu materialnego zużywanego przez czar, istnieje 10% szans, że komponent nie zostanie zużyty przy tym rzuceniu.

**Biegłość w narzędziach.** Zyskujesz biegłość w jednym rodzaju narzędzi rzemieślniczych według własnego wyboru.

### Poziom 6: Ulepszona ochrona

Twoja Chroniona ziemia staje się potężniejsza w następujący sposób.

**Wzmocnienie obrońców.** Dopóki ty i sojusznicy jesteście w sześcianie stworzonym przez Chronioną ziemię, zyskujecie premię do rzutów obronnych na Kondycję równą twojemu modyfikatorowi Mądrości (minimum +1).

**Odrzucenie profanatorów.** Za każdym razem, gdy sześcian stworzony przez Chronioną ziemię wchodzi na przestrzeń wroga albo gdy wróg wchodzi do sześcianu albo kończy w nim turę, ten wróg wykonuje rzut obronny na Mądrość przeciwko ST twoich czarów. Przy nieudanym rzucie wróg otrzymuje 2k10 obrażeń promienistych, a jego prędkość jest zmniejszona o połowę do końca następnej tury, gdy nowy wzrost hamuje jego ruch. Przy udanym rzucie wróg otrzymuje tylko połowę tyle obrażeń. Wróg wykonuje ten rzut tylko raz na turę.

### Poziom 10: Ułatwione przywracanie

Możesz rzucić [Mniejsze przywrócenie](../spells/lesser-restoration.md) albo [Większe przywrócenie](../spells/greater-restoration.md) bez zużywania komórki czaru i bez komponentów czaru. Możesz użyć tej cechy w ten sposób liczbę razy równą twojemu modyfikatorowi Mądrości (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 14: Święta ziemia

Rozmiar sześcianu stworzonego przez Chronioną ziemię wzrasta do 9 metrów.

Ponadto, gdy istota, którą widzisz w obszarze Chronionej ziemi, zostanie trafiona testem ataku, możesz wykorzystać reakcję, by zmniejszyć obrażenia tego ataku wobec tej istoty o połowę.
""",
}


def main():
    for name, content in FILES.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(FILES)} files (cleric + preservation)")


if __name__ == "__main__":
    main()
