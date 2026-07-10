#!/usr/bin/env python3
"""Translate UA artificer subclass files to Polish."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"

FILES = {
    "subclass-artificer-alchemist.md": """# Alchemik (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-artificer-alchemist

---

Źródło: [Wynalazca UA (17.12.2024)](https://www.dndbeyond.com/sources/dnd/ua/the-artificer)

*Twórz magiczne eliksiry i mikstury*

Alchemik jest mistrzem łączenia reagentów, by wytwarzać magiczne efekty. Alchemicy używają swoich tworów, by dawać życie i je odbierać.

### Poziom 3: Biegłość w narzędziach

Zyskujesz biegłość w przyborach alchemicznych. Jeśli masz już tę biegłość, zyskujesz biegłość w jednym innym rodzaju narzędzi rzemieślniczych według własnego wyboru.

Ponadto, gdy warzysz miksturę według zasad tworzenia z Podręcznika Mistrza Gry, wymagany czas jest skrócony o połowę.

### Poziom 3: Czary alchemika

Gdy osiągasz poziom wynalazcy wskazany w tabeli Czary alchemika, zawsze masz przygotowane wymienione czary.

### Czary alchemika

| Poziom wynalazcy | Czary |
| --- | --- |
| 3 | [Kojące słowo](../spells/healing-word.md), [Promień zatrucia](../spells/ray-of-sickness.md) |
| 5 | [Płomienna kula](../spells/flaming-sphere.md), [Kwasowa strzała Melfa](../spells/melfs-acid-arrow.md) |
| 9 | [Forma gazowa](../spells/gaseous-form.md), [Masowe kojące słowo](../spells/mass-healing-word.md) |
| 13 | [Osłona przed śmiercią](../spells/death-ward.md), [Vitriolic Sphere](../spells/vitriolic-sphere.md) |
| 17 | [Zabójcza chmura](../spells/cloudkill.md), [Wskrzeszenie](../spells/raise-dead.md) |

### Poziom 3: Eksperymentalny eliksir

Za każdym razem, gdy kończysz Długi odpoczynek, trzymając przybory alchemiczne, możesz użyć tych narzędzi, by magicznie wytworzyć dwa eliksiry. Dla każdego eliksiru rzuć na tabeli Eksperymentalny eliksir, by określić jego efekt, który uruchamia się, gdy ktoś wypije eliksir. Eliksir pojawia się w fiolce, a fiolka znika, gdy eliksir zostanie wypity lub wylany. Jeśli jakikolwiek eliksir pozostanie po zakończeniu Długiego odpoczynku, eliksir i fiolka znikają.

**Picie eliksiru.** Akcją dodatkową istota może wypić eliksir lub podać go innej istocie w promieniu 1,5 metra od siebie.

**Tworzenie dodatkowych eliksirów.** Akcją magiczną, trzymając przybory alchemiczne, możesz zużyć jedną komórkę czaru, by stworzyć kolejny eliksir. Gdy to robisz, wybierasz jego efekt z tabeli Eksperymentalny eliksir zamiast rzucać. Gdy osiągasz określone poziomy wynalazcy, możesz wytworzyć dodatkowy eliksir na końcu każdego Długiego odpoczynku: łącznie trzy na poziomie 5, cztery na poziomie 9 i pięć na poziomie 15.

### Eksperymentalny eliksir

| k6 | Efekt |
| --- | --- |
| 1 | **Leczenie.** Pijący odzyskuje PW równe 2k8 plus twój modyfikator Inteligencji. |
| 2 | **Szybkość.** Prędkość pijącego wzrasta o 3 metry na 1 godzinę. |
| 3 | **Odporność.** Pijący zyskuje premię +1 do KP na 10 minut. |
| 4 | **Śmiałość.** Pijący może rzucić 1k4 i dodać wyrzuconą liczbę do każdego testu ataku i rzutu obronnego, które wykonuje, przez następną minutę. |
| 5 | **Lot.** Pijący zyskuje prędkość lotu 3 metry na 10 minut. |
| 6 | Określasz efekt eliksiru, wybierając jeden z pozostałych wierszy tej tabeli. |

### Poziom 5: Alchemiczny znawca

Za każdym razem, gdy rzucasz czar, używając przyborów alchemicznych jako magicznego fokusu, zyskujesz premię do jednego rzutu tego czaru. Ten rzut musi przywracać PW albo być rzutem obrażeń zadającym obrażenia od kwasu, ognia, nekrotyczne lub trucizny. Premia wynosi twój modyfikator Inteligencji (minimum +1).

### Poziom 9: Regenerujące reagenty

Możesz włączać regenerujące reagenty w część swoich prac, co daje następujące korzyści:

**Wzmocnienie.** Za każdym razem, gdy istota wypije eliksir stworzony cechą Eksperymentalny eliksir, zyskuje tymczasowe PW równe twojemu modyfikatorowi Inteligencji plus twój poziom wynalazcy.

**Przywrócenie.** Możesz rzucić [Mniejsze przywrócenie](../spells/lesser-restoration.md) bez zużywania komórki czaru i bez przygotowywania czaru, pod warunkiem że używasz przyborów alchemicznych jako magicznego fokusu. Możesz to zrobić liczbę razy równą twojemu modyfikatorowi Inteligencji (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 15: Mistrzostwo chemiczne

Zyskujesz następujące korzyści:

**Alchemiczna erupcja.** Gdy rzucasz czar wynalazcy, który zadaje obrażenia od kwasu, ognia, nekrotyczne lub trucizny celowi, możesz również zadać temu celowi 2k8 obrażeń od mocy. Możesz skorzystać z tej korzyści tylko raz w każdej swojej turze.

**Chemiczna odporność.** Zyskujesz odporność na obrażenia od kwasu i trucizny.

**Przywołany kocioł.** Możesz rzucić [Tasha's Bubbling Cauldron](../spells/tasha-s-bubbling-cauldron.md) bez zużywania komórki czaru, bez przygotowywania czaru i bez komponentów materialnych, pod warunkiem że używasz przyborów alchemicznych jako magicznego fokusu. Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",
    "subclass-artificer-armorer.md": """# Pancerznik (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-artificer-armorer

---

Źródło: [Wynalazca UA (17.12.2024)](https://www.dndbeyond.com/sources/dnd/ua/the-artificer)

*Twórz magiczne pancerze wzmacniające twoje zdolności*

Pancerznik modyfikuje zbroję tak, by działała niemal jak druga skóra. Zbroja jest ulepszona, by wzmacniać magię wynalazcy, uwalniać potężne ataki i generować solidną obronę.

### Poziom 3: Narzędzia fachu

Zyskujesz wyszkolenie w pancerzach ciężkich. Zyskujesz też biegłość w narzędziach kowala. Jeśli masz już tę biegłość, zyskujesz biegłość w jednym innym rodzaju narzędzi rzemieślniczych według własnego wyboru.

Ponadto, gdy tworzysz niemagiczną lub magiczną zbroję, wymagany czas jest skrócony o połowę.

### Poziom 3: Czary pancerznika

Gdy osiągasz poziom wynalazcy wskazany w tabeli Czary pancerznika, zawsze masz przygotowane wymienione czary.

### Czary pancerznika

| Poziom wynalazcy | Czary |
| --- | --- |
| 3 | [Magiczna pocisk](../spells/magic-missile.md), [Fala grzmotu](../spells/thunderwave.md) |
| 5 | [Lustrzane odbicia](../spells/mirror-image.md), [Rozbicie](../spells/shatter.md) |
| 9 | [Wzór hipnotyczny](../spells/hypnotic-pattern.md), [Piorunująca warga](../spells/lightning-bolt.md) |
| 13 | [Ognista tarcza](../spells/fire-shield.md), [Większa niewidzialność](../spells/greater-invisibility.md) |
| 17 | [Przejście przez ścianę](../spells/passwall.md), [Ściana mocy](../spells/wall-of-force.md) |

### Poziom 3: Magiczna zbroja

Akcją magiczną, trzymając narzędzia kowala, możesz zamienić noszoną zbroję w Magiczną zbroję. Zbroja pozostaje Magiczną zbroją, dopóki nie założysz innej zbroi lub nie umrzesz.

Dopóki nosisz Magiczną zbroję, zyskujesz następujące korzyści:

**Brak wymogu Siły.** Jeśli zbroja normalnie wymaga Siły, Magiczna zbroja nie ma tego wymogu dla ciebie.

**Szybkie zakładanie i zdejmowanie.** Możesz założyć lub zdjąć zbroję akcją Użycia.

**Druga skóra.** Zbroja przyczepia się do ciebie i nie można jej zdjąć wbrew twojej woli. Rozszerza się też, by okrywać całe ciało, choć hełm możesz chować lub wysuwać akcją dodatkową. Zbroja zastępuje brakujące kończyny, działając identycznie jak zastępowana kończyna.

**Magiczny fokus.** Możesz używać Magicznej zbroi jako magicznego fokusu do czarów wynalazcy.

### Poziom 3: Model zbroi

Możesz dostosować swoją Magiczną zbroję. Gdy to robisz, wybierz jeden z następujących modeli: Dreadnought, Strażnik lub Infiltrator. Wybrany model daje specjalne korzyści, dopóki go nosisz.

Każdy model zawiera specjalną broń. Gdy atakujesz tą bronią, możesz dodać swój modyfikator Inteligencji zamiast modyfikatora Siły lub Zręczności do testów ataku i obrażeń.

Możesz zmienić model zbroi za każdym razem, gdy kończysz Krótki lub Długi odpoczynek, jeśli trzymasz narzędzia kowala.

#### Dreadnought

Projektujesz zbroję tak, by w bitwie stawała się potężnym kolosem. Ma następujące cechy:

**Kolczasty cep.** Na jednej z rękawic zbroi pojawia się żelazna kula na łańcuchu o następujących cechach:

**Kategoria broni:** prosta do walki wręcz

**Obrażenia przy trafieniu:** 1k10 obuchowych plus modyfikator cechy użyty do testu ataku

**Właściwości:** zasięg

**Olbrzymia postura.** Akcją dodatkową przekształcasz i powiększasz zbroję na 1 minutę. Przez ten czas twój zasięg wzrasta o 1,5 metra, a jeśli jesteś mniejszy niż Duży, stajesz się Duży wraz z tym, co nosisz. Jeśli nie ma miejsca, by powiększyć rozmiar, rozmiar się nie zmienia. Możesz użyć tej akcji dodatkowej liczbę razy równą twojemu modyfikatorowi Inteligencji (minimum raz). Odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

**Burzyciel.** Jeśli trafisz istotę co najmniej o jeden rozmiar mniejszą od siebie cepm, możesz odepchnąć ją o do 3 metrów od siebie albo przyciągnąć o do 3 metrów w swoją stronę.

#### Strażnik

Projektujesz zbroję do walki w pierwszej linii. Ma następujące cechy:

**Pancerz grzmotu.** Każda rękawica zbroi ma następujące cechy:

**Kategoria broni:** prosta do walki wręcz

**Obrażenia przy trafieniu:** 1k8 od grzmotu plus modyfikator cechy użyty do testu ataku

**Rozpraszający impuls.** Istota trafiona rękawicą ma utrudnienie do testów ataku przeciwko celom innym niż ty do początku twojej następnej tury.

**Pole obronne.** Gdy jesteś skrwawiony, możesz wykonać akcję dodatkową, by zyskać tymczasowe PW równe twojemu poziomowi wynalazcy. Tracisz te tymczasowe PW, jeśli zdejmiesz zbroję.

#### Infiltrator

Dostosowujesz zbroję do subtelniejszych zadań. Ma następujące cechy:

**Wyrzutnia błyskawic.** Klejnotowy węzeł pojawia się na jednej z rękawic albo na klatce piersiowej zbroi (według twojego wyboru). Ma następujące cechy:

**Kategoria broni:** prosta dystansowa

**Obrażenia przy trafieniu:** 1k6 od błyskawic plus modyfikator cechy użyty do testu ataku

**Właściwości:** miotana (zasięg 27/90 metrów)

**Impuls błyskawicy.** Raz w każdej swojej turze, gdy trafisz istotę Wyrzutnią błyskawic, możesz zadać celowi dodatkowe 1k6 obrażeń od błyskawic.

**Wzmocnione kroki.** Twoja prędkość wzrasta o 1,5 metra.

**Pole tłumiące.** Masz ułatwienie do testów Zręczności (Skradanie). Jeśli zbroja nakłada utrudnienie na takie testy, ułatwienie i utrudnienie się znosi, jak zwykle.

### Poziom 5: Dodatkowy atak

Możesz atakować dwa razy zamiast raz, gdy wykonujesz akcję Ataku w swojej turze.

### Poziom 9: Replikacja zbroi

Uczysz się dodatkowego schematu dla cechy Replikacja przedmiotu magicznego i musi on należeć do kategorii Zbroja. Jeśli zamieniasz ten schemat, musisz zamienić go na inny schemat zbroi.

Ponadto możesz stworzyć dodatkowy przedmiot tą cechą, który również musi należeć do kategorii Zbroja.

### Poziom 15: Doskonała zbroja

Twoja Magiczna zbroja zyskuje dodatkowe korzyści w zależności od modelu, jak opisano poniżej.

**Dreadnought.** Kość obrażeń Kolczastego cepa wzrasta do 2k6 obuchowych. Ponadto, gdy używasz Olbrzymiej postury, twój zasięg wzrasta o 3 metry, rozmiar może wzrosnąć do Dużego lub Ogromnego (według twojego wyboru), a zyskujesz prędkość lotu równą swojej prędkości.

**Strażnik.** Kość obrażeń Pancerza grzmotu wzrasta do 1k10 obrażeń od grzmotu. Ponadto, gdy istota Ogromna lub mniejsza, którą widzisz, kończy turę w promieniu 9 metrów od ciebie, możesz wykorzystać reakcję, by magicznie zmusić ją do rzutu obronnego na Siłę przeciwko ST twoich czarów. Przy nieudanym rzucie przyciągasz istotę o do 7,5 metra w swoją stronę do niezajętej przestrzeni. Jeśli przyciągniesz cel w przestrzeń w promieniu 1,5 metra od siebie, możesz wykonać atak bronią do walki wręcz przeciwko niemu w ramach tej reakcji.

Możesz wykorzystać tę reakcję liczbę razy równą twojemu modyfikatorowi Inteligencji (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

**Infiltrator.** Kość obrażeń Wyrzutni błyskawic wzrasta do 2k6. Każda istota, która otrzyma obrażenia od błyskawic od twojej Wyrzutni błyskawic, migocze magicznym światłem do początku twojej następnej tury. Migocząca istota emituje przyćmione światło w promieniu 1,5 metra i ma utrudnienie do testów ataku przeciwko tobie, gdyż światło ją rażą, jeśli cię atakuje.
""",
}

# Remaining files appended via second write due to size - actually I'll use main() with all content

def main():
    for name, content in FILES.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(FILES)} artificer subclass files (partial batch)")


if __name__ == "__main__":
    main()
