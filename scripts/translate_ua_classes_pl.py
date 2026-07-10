#!/usr/bin/env python3
"""Translate UA class files: psion + artificer."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"
CLASSES = ROOT / "dnd2024-wikidot-pl/classes"

PSION5 = """# Psionik (UA5 — 27.05.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:class-psion

---

Źródło: [UA5 — Psionik (27.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/the-psion)

*Mistrz mocy psionicznej*

Psionicy splatają magię i nadludzkie moce siłą umysłu. Rozwijają go jako źródło mocy, które manifestuje czary i rośnie wraz z karierą poszukiwacza przygód. W kolejnych sekcjach znajdziesz wszystko, czego potrzebujesz, by grać jednym z tych psionicznych potentatów.

| Podstawowe cechy psionika |
| --- |
| **Cecha podstawowa** | Inteligencja |
| **Kość wytrzymałości** | K6 na poziom psionika |
| **Biegłości w rzutach obronnych** | Inteligencja i Mądrość |
| **Biegłości w umiejętnościach** | Wybierz 2: Wiedza tajemna, Intuicja, Zastraszanie, Śledztwo, Medycyna, Percepcja albo Perswazja |
| **Biegłości w broniach** | Broń prosta |
| **Wyszkolenie w pancerzach** | Brak |
| **Wyposażenie startowe** | Wybierz A albo B: (A) włócznia, 2 sztylety, lekka kusza, 20 bełtów, futerał, zestaw badacza podziemi i 6 sz; albo (B) 50 sz |

# Zostanie psionikiem …

## Jako postać 1. poziomu

- Zyskaj wszystkie cechy z tabeli Podstawowe cechy psionika.
- Zyskaj cechy psionika 1. poziomu wymienione w tabeli Cech psionika.

## Jako postać wieloklasowa

- Zyskaj kość wytrzymałości z tabeli Podstawowe cechy psionika.
- Zyskaj cechy psionika 1. poziomu wymienione w tabeli Cech psionika. Zobacz zasady wieloklasowości w Podręczniku Gracza, aby ustalić dostępne komórki czaru, dodając wszystkie poziomy psionika.

# Cechy klasy psionika

Jako psionik zyskujesz poniższe cechy klasy po osiągnięciu wskazanych poziomów psionika. Cechy wymieniono w tabeli Cech psionika.

###### Cechy psionika (część A)

| Poziom | Premia z biegłości | Cechy klasy | Kość energii | Liczba kości |
| --- | --- | --- | --- | --- |
| 1 | +2 | Rzucanie czarów, Moc psioniczna, Subtelna telekineza | K6 | 4 |
| 2 | +2 | Dyscyplina psioniczna, Tryby psioniczne | K6 | 4 |
| 3 | +2 | Podklasa psionika | K6 | 4 |
| 4 | +2 | Zwiększenie wartości cechy | K6 | 4 |
| 5 | +3 | Psioniczna regeneracja | K8 | 6 |
| 6 | +3 | Cecha podklasy | K8 | 6 |
| 7 | +3 | Psioniczny impuls | K8 | 6 |
| 8 | +3 | Zwiększenie wartości cechy | K8 | 6 |
| 9 | +4 | — | K8 | 8 |
| 10 | +4 | Dyscyplina psioniczna, cecha podklasy | K8 | 8 |
| 11 | +4 | — | K10 | 8 |
| 12 | +4 | Zwiększenie wartości cechy | K10 | 8 |
| 13 | +5 | — | K10 | 10 |
| 14 | +5 | Cecha podklasy | K10 | 10 |
| 15 | +5 | — | K10 | 10 |
| 16 | +5 | Zwiększenie wartości cechy | K10 | 10 |
| 17 | +6 | Dyscyplina psioniczna | K12 | 12 |
| 18 | +6 | — | K12 | 12 |
| 19 | +6 | Epicki dar | K12 | 12 |
| 20 | +6 | Rozpalona siła życiowa | K12 | 12 |

###### Cechy psionika (część B)

| Poziom | Sztuczki | Przygotowane czary | 1. | 2. | 3. | 4. | 5. | 6. | 7. | 8. | 9. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 4 | 2 | — | — | — | — | — | — | — | — |
| 2 | 2 | 5 | 3 | — | — | — | — | — | — | — | — |
| 3 | 2 | 6 | 4 | 2 | — | — | — | — | — | — | — |
| 4 | 2 | 7 | 4 | 3 | — | — | — | — | — | — | — |
| 5 | 2 | 9 | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | 2 | 10 | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | 2 | 11 | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | 2 | 12 | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | 2 | 14 | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | 3 | 15 | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | 3 | 16 | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | 3 | 16 | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | 3 | 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | 4 | 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | 4 | 18 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | 4 | 18 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | 4 | 19 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | 4 | 20 | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | 4 | 21 | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | 4 | 22 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

### Poziom 1: Rzucanie czarów

Nauczyłeś się kierować energią magiczną siłą umysłu. Zobacz Podręcznik Gracza, aby poznać zasady rzucania czarów. Poniższe informacje opisują, jak stosujesz te zasady do czarów psionika z listy czarów psionika w opisie klasy.

**Sztuczki.** Znasz dwie sztuczki psionika według własnego wyboru. Zalecane są [Pomniejsza iluzja](../spells/minor-illusion.md) i [Telekinetyczne miotnięcie](spell-telekinetic-fling.md).

Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jedną sztuczkę z tej cechy na inną sztuczkę psionika według własnego wyboru.

Gdy osiągniesz poziomy psionika 10 i 14, uczysz się kolejnej sztuczki psionika według własnego wyboru, zgodnie z kolumną Sztuczki w tabeli Cech psionika.

**Komórki czaru.** Tabela Cech psionika pokazuje, ile masz komórek czaru do rzucania czarów 1. kręgu i wyższych. Odzyskujesz wszystkie zużyte komórki po zakończeniu Długiego odpoczynku.

**Przygotowane czary 1. kręgu i wyższych.** Przygotowujesz listę czarów 1. kręgu i wyższych dostępnych do rzucenia tą cechą. Na początku wybierz cztery czary psionika 1. kręgu. Zalecane są [Osoba urocza](../spells/charm-person.md), [Rozkaz](../spells/command.md), [Rozdarcujące szepty](../spells/dissonant-whispers.md) i [Zbroja maga](../spells/mage-armor.md).

Liczba czarów na liście rośnie wraz z poziomami psionika, zgodnie z kolumną Przygotowane czary w tabeli Cech psionika. Za każdym razem, gdy ta liczba rośnie, wybieraj dodatkowe czary psionika, aż liczba czarów na liście odpowiada wartości w tabeli. Wybrane czary muszą być o kręgu, do którego masz komórki czaru. Na przykład jako psionik 3. poziomu twoja lista może obejmować sześć czarów psionika 1. i 2. kręgu w dowolnej kombinacji.

Jeśli inna cecha psionika daje ci czary, które zawsze masz przygotowane, nie wliczają się one do liczby czarów przygotowywanych tą cechą, ale w pozostałym zakresie liczą się jako czary psionika.

**Zmiana przygotowanych czarów.** Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jeden czar na liście na inny czar psionika kwalifikującego się kręgu.

**Cecha bazowa rzucania czarów.** Inteligencja jest twoją cechą bazową przy rzucaniu czarów psionika.

**Psioniczne rzucanie czarów.** Gdy rzucasz czar psionika, nie wymaga on komponentów werbalnych ani materialnych, nawet jeśli w wpisie „Komponenty” ma oznaczenia W albo M — z wyjątkiem komponentów materialnych zużywanych przez czar albo mających podaną cenę.

### Poziom 1: Moc psioniczna

W sobie nosisz źródło energii psionicznej reprezentowane przez kości energii psionicznej. Poziom psionika określa rozmiar kości i ich liczbę, zgodnie z kolumnami Kość energii i Liczba kości w tabeli Cech psionika.

Kości energii psionicznej wzmacniają lub zasilają niektóre cechy psionika. Zaczynasz z dwiema takimi cechami: Telekinetyczne pchnięcie i Telepatyczne połączenie (opis poniżej). Niektóre moce wydają kości, zgodnie z opisem; nie możesz użyć mocy wymagającej kości, gdy wszystkie zostały wydane.

Odzyskujesz jedną wydaną kość energii psionicznej po zakończeniu Krótkiego odpoczynku i wszystkie po zakończeniu Długiego odpoczynku.

Niektóre cechy używające kości energii psionicznej wymagają od celu rzutu obronnego. ST równa się ST twoich czarów z cechy Rzucanie czarów.

**Telekinetyczne pchnięcie.** Akcją dodatkową wybierz jedną istotę inną niż ty, którą widzisz w promieniu 9 metrów od siebie, i rzucić jedną kość energii psionicznej. Cel musi odnieść sukces w rzucie obronnym na Siłę, albo zostaje pchnięty albo pociągnięty (twój wybór) w linii prostej od ciebie na odległość w stopach równą pięciokrotności wyrzuconej wartości. Kość zostaje wydana tylko przy nieudanym rzucie.

**Telepatyczne połączenie.** Masz telepatię o zasięgu 1,5 metra. Akcją dodatkową możesz wydać jedną kość energii psionicznej i ją rzucić. Przez liczbę minut równą twojemu poziomowi psionika zasięg telepatii rośnie o liczbę stóp równą dziesięciokrotności wyrzuconej wartości.

### Poziom 1: Subtelna telekineza

Znasz sztuczkę [Magiczna dłoń](../spells/mage-hand.md). Możesz rzucać ją bez komponentów somatycznych i sprawić, że widmowa dłoń jest niewidzialna.

### Poziom 2: Dyscyplina psioniczna

Uczysz się dalszych technik psionicznych zasilanych kośćmi energii psionicznej. Zyskujesz dwie dyscypliny według własnego wyboru, na przykład Rozszerzona świadomość i Podpowiedź id. Dyscypliny opisano w [Opcjach dyscyplin psionicznych (UA5)](class-psion-disciplines.md).

Możesz użyć tylko jednej dyscypliny na turę i tylko raz na turę, chyba że opcja stanowi inaczej.

Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jedną z dyscyplin psionicznych na inną, której nie znasz. Zyskujesz dwie kolejne opcje na poziomie psionika 10 i dwie na poziomie 17.

### Poziom 2: Tryby psioniczne

Wyostrzyłeś moce psioniczne, by w walce służyły jako tarcza i broń. Akcją dodatkową wybierasz jeden z poniższych trybów, zyskując korzyści na 1 minutę albo do ponownego użycia tej cechy:

**Tryb ataku.** Obrażenia z twoich ataków bronią, czarów psionika i cech psionika ignorują odporność na obrażenia psychiczne. Dodatkowo, gdy rzucasz kośćmi obrażeń czaru, możesz wydać jedną kość energii psionicznej, by przerzucić liczbę kości obrażeń do modyfikatora Inteligencji (minimum jedną), i musisz użyć nowych wyników.

**Tryb obrony.** Masz odporność na obrażenia psychiczne. Gdy nie odniesiesz sukcesu w rzucie obronnym na Inteligencję, Mądrość albo Charyzmę, możesz reakcją wydać jedną kość energii psionicznej, rzucić ją i dodać wynik do rzutu, potencjalnie zamieniając niepowodzenie w sukces.

Możesz użyć tej cechy dwa razy; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

### Poziom 3: Podklasa psionika

Zyskujesz podklasę psionika według własnego wyboru. Podklasy Metamorfa, Przekształcacz psi, Psykineticysta i Telepata opisano poniżej w sekcji podklas.

Podklasa to specjalizacja dająca cechy na określonych poziomach psionika. Przez resztę kariery zyskujesz każdą cechę podklasy odpowiadającą twojemu poziomowi psionika lub niższą.

### Poziom 4: Zwiększenie wartości cechy

Zyskujesz atut [Zwiększenie wartości cechy](../feats/ability-score-improvement.md) lub inny atut według własnego wyboru, do którego się kwalifikujesz. Zyskujesz tę cechę ponownie na poziomach psionika 8, 12 i 16.

### Poziom 5: Psioniczna regeneracja

Po zakończeniu Krótkiego odpoczynku możesz odzyskać wydane kości energii psionicznej, ale nie więcej niż połowę ich liczby (zaokrąglając w dół). Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.

### Poziom 7: Psioniczny impuls

Gdy rzucasz inicjatywę, możesz wydać jedną ze swoich kości PW i odzyskać jedno zużyte użycie Trybów psionicznych.

Dodatkowo po rzuceniu jednej lub większej liczby kości energii psionicznej możesz wydać jedną kość PW i traktować każdy wynik 1, 2 albo 3 na tych kościach energii psionicznej jako 4.

### Poziom 19: Epicki dar

Zyskujesz atut epickiego daru lub inny atut według własnego wyboru, do którego się kwalifikujesz. Zalecany jest [Dar odporności na energię](../feats/boon-of-energy-resistance.md).

### Poziom 20: Rozpalona siła życiowa

Raz na turę, gdy wydajesz jedną kość energii psionicznej i rzucasz ją dla cechy psionika albo dyscypliny psionicznej, możesz wydać dwie swoje kości PW, rzucić dwie dodatkowe kości energii psionicznej i dodać wyniki do sumy.
"""

PSION9 = """# Psionik (UA9 — 02.10.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:class-psion2

---

Źródło: [UA9 — Aktualizacja psionika (02.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/psion-update)

*Mistrz mocy psionicznej*

Psionicy splatają magię i nadludzkie moce siłą umysłu. Rozwijają go jako źródło mocy, które manifestuje czary i rośnie wraz z karierą poszukiwacza przygód. W kolejnych sekcjach znajdziesz wszystko, czego potrzebujesz, by grać jednym z tych psionicznych potentatów.

| Podstawowe cechy psionika |
| --- |
| **Cecha podstawowa** | Inteligencja |
| **Kość wytrzymałości** | K6 na poziom psionika |
| **Biegłości w rzutach obronnych** | Inteligencja i Mądrość |
| **Biegłości w umiejętnościach** | Wybierz 2: Wiedza tajemna, Intuicja, Zastraszanie, Śledztwo, Medycyna, Percepcja albo Perswazja |
| **Biegłości w broniach** | Broń prosta |
| **Wyszkolenie w pancerzach** | Brak |
| **Wyposażenie startowe** | Wybierz A albo B: (A) włócznia, 2 sztylety, lekka kusza, 20 bełtów, futerał, zestaw badacza podziemi i 6 sz; albo (B) 50 sz |

# Zostanie psionikiem …

## Jako postać 1. poziomu

- Zyskaj wszystkie cechy z tabeli Podstawowe cechy psionika.
- Zyskaj cechy psionika 1. poziomu wymienione w tabeli Cech psionika.

## Jako postać wieloklasowa

- Zyskaj kość wytrzymałości z tabeli Podstawowe cechy psionika.
- Zyskujesz cechy psionika 1. poziomu wymienione w tabeli Cech psionika. Zobacz zasady wieloklasowości w Podręczniku Gracza, aby ustalić dostępne komórki czaru, dodając wszystkie poziomy psionika.

# Cechy klasy psionika

Jako psionik zyskujesz poniższe cechy klasy po osiągnięciu wskazanych poziomów psionika. Cechy wymieniono w tabeli Cech psionika.

###### Cechy psionika (część A)

| Poziom | Premia z biegłości | Cechy klasy | Kości energii |
| --- | --- | --- | --- |
| 1 | +2 | Moc psioniczna, Rzucanie czarów, Subtelna telekineza | 4K6 |
| 2 | +2 | Dyscyplina psioniczna | 4K6 |
| 3 | +2 | Podklasa psionika | 4K6 |
| 4 | +2 | Zwiększenie wartości cechy | 4K6 |
| 5 | +3 | Dyscyplina psioniczna, Psioniczna regeneracja | 6K8 |
| 6 | +3 | Cecha podklasy | 6K8 |
| 7 | +3 | Psioniczny impuls | 6K8 |
| 8 | +3 | Zwiększenie wartości cechy | 6K8 |
| 9 | +4 | — | 8K8 |
| 10 | +4 | Dyscyplina psioniczna, cecha podklasy | 8K8 |
| 11 | +4 | — | 8K10 |
| 12 | +4 | Zwiększenie wartości cechy | 8K10 |
| 13 | +5 | Dyscyplina psioniczna | 10K10 |
| 14 | +5 | Cecha podklasy | 10K10 |
| 15 | +5 | — | 10K10 |
| 16 | +5 | Zwiększenie wartości cechy | 10K10 |
| 17 | +6 | Dyscyplina psioniczna | 12K12 |
| 18 | +6 | Rezerwy psioniczne | 12K12 |
| 19 | +6 | Epicki dar | 12K12 |
| 20 | +6 | Rozpalona siła życiowa | 12K12 |

###### Cechy psionika (część B)

| Poziom | Sztuczki | Przygotowane czary | 1. | 2. | 3. | 4. | 5. | 6. | 7. | 8. | 9. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 4 | 2 | — | — | — | — | — | — | — | — |
| 2 | 2 | 5 | 3 | — | — | — | — | — | — | — | — |
| 3 | 2 | 6 | 4 | 2 | — | — | — | — | — | — | — |
| 4 | 3 | 7 | 4 | 3 | — | — | — | — | — | — | — |
| 5 | 3 | 9 | 4 | 3 | 2 | — | — | — | — | — | — |
| 6 | 3 | 10 | 4 | 3 | 3 | — | — | — | — | — | — |
| 7 | 3 | 11 | 4 | 3 | 3 | 1 | — | — | — | — | — |
| 8 | 3 | 12 | 4 | 3 | 3 | 2 | — | — | — | — | — |
| 9 | 3 | 14 | 4 | 3 | 3 | 3 | 1 | — | — | — | — |
| 10 | 4 | 15 | 4 | 3 | 3 | 3 | 2 | — | — | — | — |
| 11 | 4 | 16 | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 12 | 4 | 16 | 4 | 3 | 3 | 3 | 2 | 1 | — | — | — |
| 13 | 4 | 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 14 | 4 | 17 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | — | — |
| 15 | 4 | 18 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 16 | 4 | 18 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | — |
| 17 | 4 | 19 | 4 | 3 | 3 | 3 | 2 | 1 | 1 | 1 | 1 |
| 18 | 4 | 20 | 4 | 3 | 3 | 3 | 3 | 1 | 1 | 1 | 1 |
| 19 | 4 | 21 | 4 | 3 | 3 | 3 | 3 | 2 | 1 | 1 | 1 |
| 20 | 4 | 22 | 4 | 3 | 3 | 3 | 3 | 2 | 2 | 1 | 1 |

### Poziom 1: Moc psioniczna

W sobie nosisz źródło energii psionicznej reprezentowane przez kości energii psionicznej. Poziom psionika określa rozmiar kości i ich liczbę, zgodnie z kolumną Kości energii w tabeli Cech psionika.

Kości energii psionicznej wzmacniają lub zasilają niektóre cechy psionika. Zaczynasz z dwiema takimi cechami: Telekinetyczne pchnięcie i Telepatyczne połączenie (opis poniżej). Niektóre moce wydają kości, zgodnie z opisem; nie możesz użyć mocy wymagającej kości, gdy wszystkie zostały wydane.

Odzyskujesz jedną wydaną kość energii psionicznej po zakończeniu Krótkiego odpoczynku i wszystkie po zakończeniu Długiego odpoczynku.

Niektóre cechy używające kości energii psionicznej wymagają od celu rzutu obronnego. ST równa się ST twoich czarów z cechy Rzucanie czarów.

**Telekinetyczne pchnięcie.** Akcją dodatkową wybierz jedną istotę inną niż ty o rozmiarze Duży lub mniejszym, którą widzisz w promieniu 9 metrów od siebie. Cel musi odnieść sukces w rzucie obronnym na Siłę, albo zostaje przesunięty o 1,5 metra w linii prostej w twoim kierunku albo od ciebie. Alternatywnie, gdy wykonujesz tę akcję dodatkową, możesz rzucić jedną kość energii psionicznej — odległość przesunięcia wynosi wtedy pięciokrotność wyrzuconej wartości w metrach. Kość zostaje wydana tylko przy nieudanym rzucie.

**Telepatyczne połączenie.** Masz telepatię o zasięgu 9 metrów. Akcją dodatkową możesz rzucić jedną kość energii psionicznej. Przez następną godzinę zasięg telepatii rośnie o liczbę metrów równą dziesięciokrotności wyrzuconej wartości. Pierwszy raz po każdym Długim odpoczynku, gdy używasz tej akcji dodatkowej, nie wydajesz kości energii psionicznej. Przy każdym kolejnym użyciu wydajesz kość.

### Poziom 1: Rzucanie czarów

Nauczyłeś się kierować energią magiczną siłą umysłu. Zobacz Podręcznik Gracza, aby poznać zasady rzucania czarów. Poniższe informacje opisują, jak stosujesz te zasady do czarów psionika.

**Sztuczki.** Znasz dwie sztuczki psionika według własnego wyboru. Zalecane są [Pomniejsza iluzja](../spells/minor-illusion.md) i [Telekinetyczne miotnięcie](spell-telekinetic-fling2.md).

Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jedną sztuczkę z tej cechy na inną sztuczkę psionika według własnego wyboru.

Gdy osiągniesz poziomy psionika 4 i 10, uczysz się kolejnej sztuczki psionika według własnego wyboru, zgodnie z kolumną Sztuczki w tabeli Cech psionika.

**Komórki czaru.** Tabela Cech psionika pokazuje, ile masz komórek czaru do rzucania czarów 1. kręgu i wyższych. Odzyskujesz wszystkie zużyte komórki po zakończeniu Długiego odpoczynku.

**Przygotowane czary 1. kręgu i wyższych.** Przygotowujesz listę czarów 1. kręgu i wyższych dostępnych do rzucenia tą cechą. Na początku wybierz cztery czary psionika 1. kręgu. Zalecane są [Osoba urocza](../spells/charm-person.md), [Rozkaz](../spells/command.md), [Rozdarcujące szepty](../spells/dissonant-whispers.md) i [Zbroja maga](../spells/mage-armor.md).

Liczba czarów na liście rośnie wraz z poziomami psionika, zgodnie z kolumną Przygotowane czary w tabeli Cech psionika. Za każdym razem, gdy ta liczba rośnie, wybieraj dodatkowe czary psionika, aż liczba czarów na liście odpowiada wartości w tabeli. Wybrane czary muszą być o kręgu, do którego masz komórki czaru.

Jeśli inna cecha psionika daje ci czary, które zawsze masz przygotowane, nie wliczają się one do liczby czarów przygotowywanych tą cechą, ale w pozostałym zakresie liczą się jako czary psionika.

**Zmiana przygotowanych czarów.** Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jeden czar na liście na inny czar psionika kwalifikującego się kręgu.

**Cecha bazowa rzucania czarów.** Inteligencja jest twoją cechą bazową przy rzucaniu czarów psionika.

**Psioniczne rzucanie czarów.** Gdy rzucasz czar psionika, nie wymaga on komponentów werbalnych ani materialnych, nawet jeśli w wpisie „Komponenty” ma oznaczenia W albo M — z wyjątkiem komponentów materialnych zużywanych przez czar albo mających podaną cenę.

### Poziom 1: Subtelna telekineza

Znasz sztuczkę [Magiczna dłoń](../spells/mage-hand.md). Możesz rzucać ją bez komponentów somatycznych i sprawić, że widmowa dłoń jest niewidzialna.

### Poziom 2: Dyscyplina psioniczna

Uczysz się dalszych technik psionicznych zasilanych kośćmi energii psionicznej. Zyskujesz dwie dyscypliny według własnego wyboru, na przykład Rozszerzona świadomość i Podpowiedź id. Dyscypliny opisano w [Opcjach dyscyplin psionicznych (UA9)](class-psion-disciplines2.md).

Możesz użyć tylko jednej dyscypliny na turę i tylko raz na turę, chyba że opcja stanowi inaczej.

Za każdym razem, gdy zyskujesz poziom psionika, możesz zamienić jedną z dyscyplin psionicznych na inną, której nie znasz. Zyskujesz jedną kolejną opcję na poziomach psionika 5, 10, 13 i 17.

### Poziom 3: Podklasa psionika

Zyskujesz podklasę psionika według własnego wyboru. Podklasy Metamorfa, Psykineticysta i Telepata opisano poniżej w sekcji podklas.

Podklasa to specjalizacja dająca cechy na określonych poziomach psionika. Przez resztę kariery zyskujesz każdą cechę podklasy odpowiadającą twojemu poziomowi psionika lub niższą.

### Poziom 4: Zwiększenie wartości cechy

Zyskujesz atut [Zwiększenie wartości cechy](../feats/ability-score-improvement.md) lub inny atut według własnego wyboru, do którego się kwalifikujesz. Zyskujesz tę cechę ponownie na poziomach psionika 8, 12 i 16.

### Poziom 5: Psioniczna regeneracja

Możesz medytować przez 1 minutę, koncentrując umysł. Po zakończeniu odzyskujesz wydane kości energii psionicznej. Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.

### Poziom 7: Psioniczny impuls

Możesz pchnąć moce psioniczne kosztem siły życiowej. Po rzuceniu jednej lub większej liczby kości energii psionicznej możesz wydać jedną kość PW i traktować każdy wynik 1, 2 albo 3 na tych kościach energii psionicznej jako 4.

### Poziom 18: Rezerwy psioniczne

Gdy rzucasz inicjatywę, odzyskujesz wydane kości energii psionicznej, aż masz ich cztery, jeśli masz ich mniej.

### Poziom 19: Epicki dar

Zyskujesz atut epickiego daru lub inny atut według własnego wyboru, do którego się kwalifikujesz. Zalecany jest [Dar odporności na energię](../feats/boon-of-energy-resistance.md).

### Poziom 20: Rozpalona siła życiowa

Płacisz siłą życiową za większą moc psioniczną. Raz na turę, gdy rzucasz jedną lub więcej kości energii psionicznej dla cechy psionika albo dyscypliny psionicznej, możesz wydać jedną lub dwie swoje kości PW. Za każdą wydaną kość PW rzucasz dodatkową kość energii psionicznej i dodajesz wyniki do sumy. To dodatkowe rzuty nie wydają kości energii psionicznej.
"""


def adapt_artificer2():
    content = (CLASSES / "artificer.md").read_text(encoding="utf-8")
    content = re.sub(
        r"# Wynalazca\n\n\*\*Klasa:\*\*.*?\n\n---\n\nŹródło:.*?\n\n",
        """# Wynalazca (UA3 — 27.02.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:class-artificer2

---

Źródło: [UA3 — Aktualizacja Eberron (27.02.2025)](https://www.dndbeyond.com/sources/dnd/ua/eberron-updates)

Rzemieślnik magiczny i wynalazca cudów. Mistrzowie wynalazków używają pomysłowości i magii, by tchnąć niezwykłe możliwości w przedmioty. Postrzegają magię jako złożony system czekający na rozszyfrowanie, a potem wykorzystanie w swoich czarach i wynalazkach.

## Uwaga projektowa: aktualizacje wynalazcy

Oto główne zmiany w tej klasie od pojawienia się w Unearthed Arcana: The Artificer:

- **Magia majsterkowicza** (dawniej magiczna majsterkowiczność) daje teraz sztuczkę [Naprawa](../spells/mending.md), a przedmioty z tej cechy trwają do końca Długiego odpoczynku.
- Tabele **Replikacji przedmiotu magicznego** zostały poprawione. Różdżkę albo broń stworzoną tą cechą możesz używać jako magiczny fokus.
- **Majsterkowanie przedmiotem magicznym** rozszerzono o ładowanie przedmiotów magicznych przez wydawanie komórek czaru oraz przemianę jednego przedmiotu magicznego w inny.
- **Dusza sztuki wynalazczej** pozwala teraz rozproszyć dowolną liczbę przedmiotów, by zwiększyć odzyskane PW, i umożliwia pewniejsze korzystanie z Błysku geniuszu.

""",
        content,
        count=1,
        flags=re.DOTALL,
    )
    content = re.sub(
        r"### Poziom 3: Podklasa wynalazcy\n\n.*?(?=### Poziom 4:)",
        """### Poziom 3: Podklasa wynalazcy

Zyskujesz podklasę wynalazcy według własnego wyboru. Podklasa Kartograf opisana jest poniżej w sekcji podklas. Podklasa to specjalizacja, która daje ci cechy na określonych poziomach wynalazcy. Przez resztę kariery zyskujesz każdą cechę swojej podklasy, która odpowiada twojemu poziomowi wynalazcy lub jest niższa.

#### Podklasy wynalazcy

| Nazwa |
| --- |
| [Kartograf](subclass-artificer-cartographer.md) |

""",
        content,
        count=1,
        flags=re.DOTALL,
    )
    content = content.replace(
        """### Poziom 14: Zaawansowana sztuka wynalazcza

Zyskujesz następujące korzyści.

_Uczony przedmiotów magicznych._ Możesz być dostrojony jednocześnie do maksymalnie pięciu magicznych przedmiotów.

_Odświeżony geniusz._ Po zakończeniu Krótkiego odpoczynku odzyskujesz jedno zużyte użycie cechy Błysk geniuszu.""",
        """### Poziom 14: Zaawansowana sztuka wynalazcza

Możesz być dostrojony jednocześnie do maksymalnie pięciu magicznych przedmiotów zamiast trzech.""",
    )
    content = content.replace(
        """### Poziom 20: Dusza sztuki wynalazczej

Rozwinąłeś mistyczne połączenie ze swoimi przedmiotami magicznymi, z którego możesz czerpać pomoc. Zyskujesz następujące korzyści.

_Oszukanie śmierci._ Jeśli twoje punkty wytrzymałości spadną do 0, ale nie zostaniesz zabity natychmiast, możesz rozproszyć dowolną liczbę niezwykłych lub rzadkich przedmiotów magicznych stworzonych cechą Replikacja przedmiotu magicznego. Jeśli to zrobisz, twoje punkty wytrzymałości zmieniają się zamiast tego na liczbę równą 20 razy liczbie rozproszonych przedmiotów magicznych.

_Magiczne prowadzenie._ Po zakończeniu Krótkiego odpoczynku odzyskujesz wszystkie zużyte użycia cechy Błysk geniuszu, jeśli jesteś dostrojony do co najmniej jednego przedmiotu magicznego.""",
        """### Poziom 20: Dusza sztuki wynalazczej

Rozwinąłeś mistyczne połączenie ze swoimi przedmiotami magicznymi, z którego możesz czerpać pomoc. Zyskujesz następujące korzyści.

_Oszukanie śmierci._ Jeśli twoje PW spadną do 0, ale nie zostaniesz zabity natychmiast, możesz rozproszyć dowolną liczbę niezwykłych lub rzadkich przedmiotów magicznych stworzonych cechą Replikacja przedmiotu magicznego. Jeśli to zrobisz, spadasz zamiast tego do liczby PW równej 20 razy liczbie rozproszonych przedmiotów magicznych.

_Magiczne prowadzenie._ Gdy używasz Błysku geniuszu i dotknięty test cechy albo rzut obronny nadal kończy się niepowodzeniem, to użycie Błysku geniuszu nie zostaje wydane, jeśli jesteś dostrojony do co najmniej jednego przedmiotu magicznego.""",
    )
    # UA magic items in ua/ folder
    ua_items = {
        "../magic-items/manifold-tool.md": "magic-item-manifold-tool.md",
        "../magic-items/repeating-shot.md": "magic-item-repeating-shot.md",
        "../magic-items/returning-weapon.md": "magic-item-returning-weapon.md",
        "../magic-items/boots-of-the-winding-path.md": "magic-item-boots-of-the-winding-path.md",
        "../magic-items/mind-sharpener.md": "magic-item-mind-sharpener.md",
        "../magic-items/repulsion-shield.md": "magic-item-repulsion-shield.md",
        "../magic-items/spell-refueling-ring.md": "magic-item-spell-refueling-ring.md",
    }
    for old, new in ua_items.items():
        content = content.replace(old, new)
    if "radiant-weapon" not in content.lower():
        content = content.replace(
            "[Dazzling Weapon](../magic-items/dazzling-weapon.md)",
            "[Promienna broń](magic-item-radiant-weapon.md)",
        )
    return content.strip() + "\n"


def main():
    (UA / "class-psion.md").write_text(PSION5.strip() + "\n", encoding="utf-8")
    (UA / "class-psion2.md").write_text(PSION9.strip() + "\n", encoding="utf-8")
    (UA / "class-artificer2.md").write_text(adapt_artificer2(), encoding="utf-8")
    print("Wrote class-psion.md, class-psion2.md, class-artificer2.md")


if __name__ == "__main__":
    main()
