#!/usr/bin/env python3
"""Replace bastions.md section: Special Facility Descriptions through Workshop."""
from pathlib import Path

PL = Path(__file__).resolve().parents[1] / "dnd2024-wikidot-pl/misc/bastions.md"

REPLACEMENT = r'''# Opisy specjalnych obiektów

Specjalne obiekty przedstawiono w porządku alfabetycznym. Tabela poniżej wymienia wszystkie obiekty z tej sekcji wraz z wymaganiami wstępnymi i rozkazami. Niektóre obiekty dają dodatkowe korzyści opisane w ich opisach.

| Poziom | Specjalny obiekt | Wymaganie wstępne | Rozkaz |
| --- | --- | --- | --- |
| 5 | [Gabinet arkaniczny](#Arcane-Study) | Umiejętność używania magicznego fokusu lub narzędzia jako fokusu rzucania czarów | Wytwórz |
| 5 | [Zbrojownia](#Armory) | Brak | Handluj |
| 5 | [Koszary](#Barrack) | Brak | Rekrutuj |
| 5 | [Ogród](#Garden) | Brak | Zbierz |
| 5 | [Biblioteka](#Library) | Brak | Badaj |
| 5 | [Sanktuarium](#Sanktuarium) | Umiejętność używania symbolu wiary lub druidzkiego fokusu jako fokusu rzucania czarów | Wytwórz |
| 5 | [Kuźnia](#Smithy) | Brak | Wytwórz |
| 5 | [Magazyn](#Storehouse) | Brak | Handluj |
| 5 | [Warsztat](#Workshop) | Brak | Wytwórz |
| 9 | [Hala gier](#Gaming-Hall) | Brak | Handluj |
| 9 | [Szklarnia](#Greenhouse) | Brak | Zbierz |
| 9 | [Laboratorium](#Laboratory) | Brak* | Wytwórz |
| 9 | [Sakristia](#Sacristy) | Umiejętność używania symbolu wiary lub druidzkiego fokusu jako fokusu rzucania czarów | Wytwórz |
| 9 | [Skryptorium](#Scriptorium) | Brak* | Wytwórz |
| 9 | [Stajnia](#Stable) | Brak | Handluj |
| 9 | [Krąg teleportacji](#Teleportation-Circle) | Brak | Rekrutuj |
| 9 | [Teatr](#Theatre) | Brak | Wzmocnij |
| 9 | [Plac treningowy](#Training-Area) | Brak | Wzmocnij |
| 9 | [Sala trofeów](#Trophy-Room) | Brak | Badaj |
| 13 | [Archiwum](#Archive) | Brak | Badaj |
| 13 | [Komnata medytacji](#Meditation-Chamber) | Brak | Wzmocnij |
| 13 | [Menageria](#Menagerie) | Brak | Rekrutuj |
| 13 | [Obserwatorium](#Observatory) | Umiejętność używania fokusu rzucania czarów | Wzmocnij |
| 13 | [Gospoda](#Pub) | Brak | Badaj |
| 13 | [Relikwiarz](#Reliquary) | Umiejętność używania symbolu wiary lub druidzkiego fokusu jako fokusu rzucania czarów | Zbierz |
| 17 | [Demisfera](#Demiplane) | Umiejętność używania magicznego fokusu lub narzędzia jako fokusu rzucania czarów | Wzmocnij |
| 17 | [Gildia](#Guildhall) | Znawstwo w umiejętności | Rekrutuj |
| 17 | [Sanktum](#Sanctum) | Umiejętność używania symbolu wiary lub druidzkiego fokusu jako fokusu rzucania czarów | Wzmocnij |
| 17 | [Sala wojenna](#War-Room) | cecha stylu walki lub cecha obrony bez pancerza | Rekrutuj |

*Niektóre rozkazy wydawane tym obiektom mają dodatkowe wymagania wstępne.

### Gabinet arkaniczny []()

*Obiekt bastionu, 5. poziom*

**Warunek wstępny:** Umiejętność używania magicznego fokusu lub narzędzia jako fokusu rzucania czarów

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Wytwórz

Gabinet arkaniczny to miejsce cichej nauki z biurkami i regałami na książki.

**Urok gabinetu arkanicznego.** Po spędzeniu długiego odpoczynku w bastionie zyskujesz magiczny urok (patrz „Dary nadprzyrodzone”), który trwa 7 dni lub do momentu użycia. Urok pozwala rzucić [Zidentyfikuj](../spells/identify.md) bez zużywania miejsca na czar ani komponentów materialnych. Nie możesz zyskać tego uroku ponownie, dopóki go posiadasz.

**Opcje wytwarzania.** Gdy wydajesz rozkaz Wytwórz temu obiektowi, wybierz jedną z poniższych opcji:

**Wytwórz: magiczny fokus.** Zlecasz najemnikowi wytworzenie magicznego fokusu. Praca trwa 7 dni i nie kosztuje pieniędzy. Fokus pozostaje w bastionie, dopóki go nie odbierzesz.

**Wytwórz: książka.** Zlecasz najemnikowi wytworzenie pustej książki. Praca trwa 7 dni i kosztuje 10 sz. Książka pozostaje w bastionie, dopóki jej nie odbierzesz.

**Wytwórz: magiczny przedmiot (wiedza tajemna).** Jeśli masz 9. poziom lub wyższy, możesz zlecić najemnikowi wytworzenie pospolitego lub niepospolitego magicznego przedmiotu z tabel wiedzy tajemnej z rozdziału 7. Obiekt ma narzędzie wymagane do wytworzenia przedmiotu, a najemnik ma biegłość w tym narzędziu oraz w umiejętności Wiedza tajemna. Patrz sekcja „Tworzenie magicznych przedmiotów” w rozdziale 7, by poznać czas i koszt. Jeśli przedmiot pozwala rzucać z niego czary, musisz wytworzyć go sam (najemnik może pomagać) i mieć wszystkie te czary przygotowane każdego dnia tworzenia.

### Archiwum []()

*Obiekt bastionu, 13. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Badaj

Archiwum to skarbiec cennych książek, map i zwojów. Zwykle przylega do biblioteki za zamkniętymi lub tajnymi drzwiami.

**Badaj: pomocna wiedza.** Gdy wydajesz rozkaz Badaj temu obiektowi, zlecasz najemnikowi przeszukanie archiwum w poszukiwaniu pomocnej wiedzy. Praca trwa 7 dni. Najemnik zdobywa wiedzę, jakby rzucił czar [Legendarna wiedza](../spells/legend-lore.md), i dzieli się nią z tobą przy następnej rozmowie.

**Księga referencyjna.** Archiwum zawiera jeden egzemplarz rzadkiej i cennej księgi referencyjnej, która daje korzyść, gdy ty i księga jesteście w bastionie. Możesz wybrać jedną z poniższych opcji (MG może udostępnić więcej):

**Kodeks wiedzy tajemnej Bigby'ego.** Masz ułatwienie w testach Inteligencji (Wiedza tajemna), gdy wykonujesz akcję Nauka, by przypomnieć sobie wiedzę o czarach, magicznych przedmiotach, eldrycznych symbolach, tradycjach magicznych i planach istnienia.

**Kroniki Chronepsisa.** Masz ułatwienie w testach Inteligencji (Historia), gdy wykonujesz akcję Nauka, by przypomnieć sobie wiedzę o wydarzeniach historycznych, legendarnych postaciach, starożytnych królestwach, dawnych sporach, wojnach i zaginionych cywilizacjach.

**Śledztwa inquisytywnego.** Masz ułatwienie w testach Inteligencji (Śledztwo), gdy wykonujesz akcję Nauka, by wyciągać wnioski z tropów lub dowodów albo przypomnieć sobie wiedzę o pułapkach, szyfrach, zagadkach i gadżetach.

**Materialne rozważania o naturze świata.** Masz ułatwienie w testach Inteligencji (Przyroda), gdy wykonujesz akcję Nauka, by przypomnieć sobie wiedzę o terenie, roślinach, zwierzętach i pogodzie.

**Stara wiara i inne religie.** Masz ułatwienie w testach Inteligencji (Religia), gdy wykonujesz akcję Nauka, by przypomnieć sobie wiedzę o bóstwach, obrzędach i modlitwach, hierarchiach, symbolach świętych i praktykach tajnych kultów.

**Powiększanie obiektu.** Możesz powiększyć archiwum do powierzchni Ogromny, wydając 2000 sz. Wtedy zyskujesz dwie dodatkowe księgi referencyjne z powyższej listy.

### Zbrojownia []()

*Obiekt bastionu, 5. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Handluj

Zbrojownia ma manekiny na zbroje, haki na tarcze, stojaki na broń i skrzynie na amunicję.

**Handluj: zaopatrzenie zbrojowni.** Gdy wydajesz rozkaz Handluj temu obiektowi, zlecasz najemnikowi zaopatrzenie zbrojowni w zbroje, tarcze, broń i amunicję. Wyposażenie kosztuje 100 sz plus dodatkowe 100 sz za każdego obrońcę bastionu. Jeśli bastion ma kuźnię, całkowity koszt jest o połowę niższy.

Gdy zbrojownia jest zaopatrzona, obrońcy bastionu trudniej giną. Gdy jakieś wydarzenie wymaga rzutu kośćmi, by ustalić, ilu obrońców bastionu ginie (patrz „Wydarzenia bastionu” na końcu rozdziału), rzucaj 1k8 zamiast każdej k6. Po zakończeniu wydarzenia wyposażenie w zbrojowni jest zużyte — niezależnie od liczby obrońców — i zbrojownia pozostaje pusta, dopóki ponownie nie wydasz rozkazu Handluj i nie zapłacisz za uzupełnienie.

### Koszary []()

*Obiekt bastionu, 5. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Rekrutuj

Bastion może mieć więcej niż jedne koszary; każde służą jako sypialnie dla maksymalnie dwunastu obrońców bastionu.

**Rekrutuj: obrońcy bastionu.** Za każdym razem, gdy wydajesz rozkaz Rekrutuj temu obiektowi, do bastionu rekrutuje się maksymalnie czterech obrońców bastionu i zakwaterowuje w tych koszarach. Rekrutacja nie kosztuje pieniędzy. Nie możesz wydać rozkazu Rekrutuj, jeśli koszary są pełne.

Śledź obrońców bastionu w każdych koszarach. Gdy tracisz obrońców, odejmij ich z listy. Nadawaj im imiona i osobowości według uznania.

**Powiększanie obiektu.** Możesz powiększyć koszary do powierzchni Ogromny, wydając 2000 sz. Ogromne koszary mieszczą do dwudziestu pięciu obrońców bastionu.

### Demisfera []()

*Obiekt bastionu, 17. poziom*

**Warunek wstępny:** Umiejętność używania magicznego fokusu lub narzędzia jako fokusu rzucania czarów

**Powierzchnia:** Ogromny

**Najemnicy:** 1

**Rozkaz:** Wzmocnij

Drzwi o szerokości do 1,5 metra i wysokości 3 metrów pojawiają się na płaskiej, twardej powierzchni w jednym z innych obiektów bastionu. Ty wybierasz miejsce. Jeśli przebywasz w bastionie w turze bastionu, możesz przenieść te drzwi do innego obiektu.

Tylko ty i najemnicy bastionu możecie otworzyć drzwi prowadzące do demisfery w postaci kamiennego pomieszczenia. Demisfera istnieje w przestrzeni międzywymiarowej i nie jest fizycznie połączona z resztą bastionu. Ani demisfery, ani jej drzwi nie można rozproszyć.

**Wzmocnij: arkaniczna odporność.** Gdy wydajesz rozkaz Wzmocnij temu obiektowi, magiczne runy pojawiają się na ścianach demisfery i trwają 7 dni. Dopóki runy nie znikną, zyskujesz tymczasowe PW równe pięciokrotności twojego poziomu po spędzeniu całego długiego odpoczynku w demisferze.

**Fabrykacja.** Będąc w demisferze, możesz wykonać akcję magiczną, by stworzyć z niczego niemagiczny przedmiot według wyboru — pojawia się on na wolnym polu w demisferze. Przedmiot nie może być większy niż 1,5 metra w żadnym wymiarze, mieć wartości powyżej 5 sz ani być zrobiony z czegoś innego niż drewno, kamień, glina, porcelana, szkło, papier, niecenne kryształy lub niecenne metale. Musisz zakończyć długi odpoczynek, zanim użyjesz tej akcji ponownie.

### Hala gier []()

*Obiekt bastionu, 9. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Ogromny

**Najemnicy:** 4

**Rozkaz:** Handluj

Hala gier oferuje rozrywkę — szachy, rzutki, karty lub kości.

**Handluj: sala hazardu.** Gdy wydajesz rozkaz Handluj temu obiektowi, najemnicy zamieniają halę gier w jadłodajnię hazardową na 7 dni. Po siódmym dniu rzuć 1k100 i sprawdź tabelę, by ustalić twój udział w wygranej kasyna.

| 1k100 | Wygrana |
| --- | --- |
| 01–50 | 1k6 × 10 sz |
| 51–85 | 2k6 × 10 sz |
| 86–95 | 4k6 × 10 sz |
| 96–00 | 10k6 × 10 sz |

### Ogród []()

*Obiekt bastionu, 5. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Zbierz

Bastion może mieć więcej niż jeden ogród. Za każdym razem, gdy dodajesz ogród, wybierz jego typ z tabeli typów ogrodów.

Będąc w bastionie, możesz polecić najemnikowi zmianę typu ogrodu. Praca trwa 21 dni, w których obiekt nie może wykonywać innych działań.

**Zbierz: plon ogrodu.** Gdy wydajesz rozkaz Zbierz temu obiektowi, zlecasz najemnikowi zebranie przedmiotów z ogrodu, jak w tabeli typów ogrodów. Praca trwa 7 dni i nie kosztuje pieniędzy.

**Powiększanie obiektu.** Możesz powiększyć ogród do powierzchni Ogromny, wydając 2000 sz. Ogromny ogród odpowiada dwóm ogrodom o powierzchni Przestronny i może zawierać dwa ogrody tego samego typu lub dwa różne. Gdy wydajesz rozkaz Zbierz ogromnemu ogrodowi, każdy składnik produkuje własny plon. Ogromny ogród zyskuje jednego dodatkowego najemnika.

| Typ ogrodu | Opis | Plon |
| --- | --- | --- |
| Dekoracyjny | Estetyczny ogród pełen kwiatów i topiarów | Dziesięć wykwintnych bukietów (po 5 sz każdy), dziesięć fiolek perfum lub dziesięć świec |
| Żywnościowy | Ogród smacznych grzybów lub warzyw | Racje żywnościowe na 100 dni |
| Ziołowy | Ogród rzadkich ziół, część ma zastosowanie lecznicze | Zioła do stworzenia dziesięciu zestawów uzdrowiciela lub jednej [mikstury leczenia](../magic-items/potion-of-healing.md) |
| Trujący | Ogród roślin i grzybów, z których wydobywa się trucizny i antytoksynę | Rośliny do stworzenia dwóch fiolek antytoksyny lub jednej fiolki podstawowej trucizny |

### Szklarnia []()

*Obiekt bastionu, 9. poziom*

**Warunek wstępny:** Brak

**Powierzchnia:** Przestronny

**Najemnicy:** 1

**Rozkaz:** Zbierz

Szklarnia to ogrodzony teren, w którym rzadkie rośliny i grzyby rosną w kontrolowanym klimacie.

**Owoc odnowy.** Na jednej roślinie w szklarni rosną trzy magiczne owoce. Istota, która zje jeden, zyskuje efekt czaru [Mniejsze przywrócenie](../spells/lesser-restoration.md). Owoce niezjedzone w ciągu 24 godzin od zerwania tracą magię. Roślina co świt odnawia zerwane owoce i ginie przy próbie przesadzenia.

**Opcje zbierania.** Gdy wydajesz rozkaz Zbierz temu obiektowi, wybierz jedną z poniższych opcji:

**Zbierz: zioła lecznicze.** Zlecasz najemnikowi stworzenie [mikstury leczenia (większej)](../magic-items/potion-of-healing.md) z ziół leczniczych. Praca trwa 7 dni i nie kosztuje pieniędzy.

**Zbierz: trucizna.** Zlecasz najemnikowi wydobycie jednej dawki trucizny z rzadkich roślin lub grzybów. Wybierz typ: krew skrytobójcy, złośliwość, blade tonikum lub serum prawdy. Patrz „Trucizny” w rozdziale 3, by poznać efekty. Po zebraniu truciznę można umieścić w fiolce. Praca trwa 7 dni i nie kosztuje pieniędzy.

### Gildia []()

*Obiekt bastionu, 17. poziom*

**Warunek wstępny:** Znawstwo w umiejętności

**Powierzchnia:** Ogromny

**Najemnicy:** 1

**Rozkaz:** Rekrutuj

Gildia wiąże się z cechą, której jesteś mistrzem. Wybierz typ z tabeli przykładowych gildii albo wspólnie z MG stwórz nową. Obiekt to sala spotkań, w której członkowie gildii omawiają ważne sprawy w twojej obecności.

Gildia ma około pięćdziesięciu członków — wykwalifikowanych ludzi mieszkających i pracujących poza bastionem, zwykle w pobliskich osadach.

**Rekrutuj: zadanie gildii.** Za każdym razem, gdy wydajesz rozkaz Rekrutuj temu obiektowi, zlecasz najemnikowi werbowanie członków gildii do specjalnego zadania. Każda gildia w tabeli określa charakter zadania. Za zgodą MG możesz tworzyć nowe zadania.

**Przykładowe gildie**

| Gildia | Symbol | Zadanie |
| --- | --- | --- |
| Gildia poszukiwaczy przygód | Płonąca pochodnia | Wysyłasz poszukiwaczy, by tropili bestię o ST 2 lub niższym znane z legowiska w promieniu 80 km od bastionu. Zabijają lub łapią stworzenie (twój wybór) w 1k6 + 1 dni. Jeśli bestia ginie, a bastion ma salę trofeów, możesz dodać trofeum. Jeśli zostaje schwytana, a bastion ma menagerię z miejscem, możesz ją tam umieścić. |
| Gildia piekarzy | Ciasto | Piekarze przygotowują wypieki na prestiżowe wydarzenie w ciągu 7 dni. Możesz otrzymać zapłatę (500 sz) lub przysługę gospodarza — szczegóły ustalasz z MG. |
| Gildia browarników | Pienzący się kufel | Browarnicy dostarczają pięćdziesiąt beczek po 150 litrów piwa (po 10 sz każda) do bastionu w 7 dni. |
| Gildia murarzy | Kamienna maska | Murarze dodają mur obronny do bastionu bez kosztu. Albo wykonują pracę dla bastionu innej postaci w promieniu 1,5 km. Każdy kwadrat 1,5 metra muru buduje się 1 dzień zamiast 10 (patrz „Mapa bastionu”). |
| Gildia stoczniowców | Skrzyżowane wiosła | Stoczniowcy budują jeden pojazd z tabeli pojazdów powietrznych i wodnych z Podręcznika Gracza. Płacisz pełną cenę; praca trwa 1 dzień na każde 1000 sz kosztu (łódź wiosłowa można zbudować w 1 dzień). |
| Gildia złodziei | Biały klucz | Złodzieje włamują się do lokacji w promieniu 80 km i kradną niemagiczny przedmiot. Przedmiot nie może być większy niż 1,5 metra w żadnym wymiarze i trafia do bastionu w 1k6 + 1 dni. MG może uznać, że grozi ci zemsta stróżów prawa lub ofiary. |

'''

# Part 2 will be appended in same script - for now split file write
PART2_START = "### Laboratorium"

def main():
    base = Path(__file__).resolve().parent
    part1 = REPLACEMENT
    part2 = (base / "bastions_facilities_pl_part2.md").read_text(encoding="utf-8")
    part3 = (base / "bastions_facilities_pl_part3.md").read_text(encoding="utf-8")
    replacement = part1 + "\n" + part2 + "\n" + part3 + "\n"
    text = PL.read_text(encoding="utf-8")
    start = text.index("# Specjalna Facility Descriptions")
    end = text.index("# Forgotten Realms: Heroes of Faerun Facilities")
    text = text[:start] + replacement + text[end:]
    PL.write_text(text, encoding="utf-8")
    print(f"Replaced {end - start} chars with {len(replacement)} chars")

if __name__ == "__main__":
    main()
