#!/usr/bin/env python3
"""Translate UA feat files in dnd2024-wikidot-pl/ua/."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"
FEATS = ROOT / "dnd2024-wikidot-pl/feats"

EBERRON_SRC = (
    "Źródło: [UA3 — Aktualizacja Eberron (27.02.2025)]"
    "(https://www.dndbeyond.com/sources/dnd/ua/eberron-updates)"
)
PSION_SRC = (
    "Źródło: [UA5 — Psionik (27.05.2025)]"
    "(https://www.dndbeyond.com/sources/dnd/ua/the-psion)"
)
VILLAIN_SRC = (
    "Źródło: [UA12 — Opcje złoczyńców (02.04.2026)]"
    "(https://www.dndbeyond.com/posts/2150-designer-insights-from-unearthed-arcana-villainous)"
)
VILLAIN2_SRC = (
    "Źródło: [UA14 — Opcje złoczyńców, ponownie (18.06.2026)]"
    "(https://www.dndbeyond.com/posts/2194-designer-insights-from-unearthed-arcana-villainous)"
)

MARK_STEMS = [
    "mark-of-detection", "mark-of-finding", "mark-of-handling", "mark-of-healing",
    "mark-of-hospitality", "mark-of-making", "mark-of-passage", "mark-of-scribing",
    "mark-of-sentinel", "mark-of-shadow", "mark-of-storm", "mark-of-warding",
]


def adapt_mark(stem: str) -> str:
    content = (FEATS / f"{stem}.md").read_text(encoding="utf-8")
    title = content.split("\n", 1)[0][2:]
    content = content.replace(content.split("\n", 1)[0], f"# {title} (UA)", 1)
    content = re.sub(
        r"\*\*URL źródła:\*\* http://dnd2024\.wikidot\.com/feat:[^\n]+",
        f"**URL źródła:** http://dnd2024.wikidot.com/ua:feat-{stem}",
        content,
    )
    content = content.replace("Źródło: Eberron — Kuźnia Wynalazcy", EBERRON_SRC)
    if stem == "mark-of-detection":
        content = content.replace(
            "Gdy wykonujesz test Inteligencja (Śledztwo) albo Mądrość (Intuicja),",
            "Gdy wykonujesz test Mądrość (Intuicja) albo Mądrość (Percepcja),",
        )
    return content.strip() + "\n"


GREATER_MARKS = {
"feat-greater-mark-of-detection.md": f"""# Większe piętno wykrywania (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-detection

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno wykrywania](feat-mark-of-detection.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja dedukcyjna z atutu Piętno wykrywania, możesz rzucić 1k6 zamiast 1k4.

**Ulepszone wykrywanie.** Gdy rzucasz [Widzenie niewidzialnego](../spells/see-invisibility.md), możesz zmodyfikować czar tak, by przez jego czas trwania miałeś ułatwienie w rzutach na inicjatywę, a wrogowie rzucający inicjatywę w promieniu 9 metrów od ciebie nie mogą zyskać ułatwienia w tym rzucie. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-finding.md": f"""# Większe piętno tropienia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-finding

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno tropienia](feat-mark-of-finding.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja myśliwego z atutu Piętno tropienia, możesz rzucić 1k6 zamiast 1k4.

**Ulepszone tropienie.** Gdy rzucasz [Znak myśliwego](../spells/hunter-s-mark.md), możesz zmodyfikować czar tak, by cel nie mógł korzystać ze stanu niewidzialny przez czas trwania zaklęcia. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-handling.md": f"""# Większe piętno opiekuna (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-handling

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno opiekuna](feat-mark-of-handling.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja dzikiego z atutu Piętno opiekuna, możesz rzucić 1k6 zamiast 1k4.

**Ulepszona opieka.** Gdy jesteś na wierzchowcu, zaraz po trafieniu celu w zasięgu 1,5 metra od twojego wierzchowca atakiem wręcz twój wierzchowiec może reakcją przemieścić się na odległość równą swojej prędkości albo wykonać akcję Atak, by wykonać jeden atak (twój wybór).
""",

"feat-greater-mark-of-healing.md": f"""# Większe piętno leczenia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-healing

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno leczenia](feat-mark-of-healing.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja medyczna z atutu Piętno leczenia, możesz rzucić 1k6 zamiast 1k4.

**Ulepszone leczenie.** Gdy rzucasz [Leczenie ran](../spells/cure-wounds.md) i rzucasz kośćmi, by określić liczbę odzyskanych PW, możesz traktować każdy wynik 1 albo 2 jako 3.
""",

"feat-greater-mark-of-hospitality.md": f"""# Większe piętno gościnności (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-hospitality

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno gościnności](feat-mark-of-hospitality.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Zawsze gościnny z atutu Piętno gościnności, możesz rzucić 1k6 zamiast 1k4.

**Natchniona gościnność.** Gdy rzucasz [Oczyśćczenie jedzenia i napoju](../spells/purify-food-and-drink.md), możesz zmodyfikować czar tak, by każda wybrana przez ciebie istota w promieniu 9 metrów od ciebie została magicznie odświeżona. U każdej dotkniętej istoty poziom wyczerpania spada o 1, a istota zyskuje tymczasowe PW równe twojej premii z biegłości plus modyfikator Inteligencji, Mądrości albo Charyzmy (wybierz przy wyborze atutu). Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-making.md": f"""# Większe piętno tworzenia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-making

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno tworzenia](feat-mark-of-making.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja rzemieślnika z atutu Piętno tworzenia, możesz rzucić 1k6 zamiast 1k4.

**Ulepszone tworzenie.** Gdy rzucasz [Magiczna broń](../spells/magic-weapon.md), możesz zmodyfikować czar tak, by za każdym razem, gdy po raz pierwszy w turze atakujesz tą bronią, przenieść część lub całą premię broni na swoją klasę pancerza. Na przykład przy premii +2 możesz obniżyć premię do ataków i obrażeń do +1 i zyskać +1 do KP. Dostosowana premia obowiązuje do początku twojej następnej tury; musisz trzymać broń, by korzystać z premii do KP. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-passage.md": f"""# Większe piętno przemijania (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-passage

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno przemijania](feat-mark-of-passage.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicyjny ruch z atutu Piętno przemijania, możesz rzucić 1k6 zamiast 1k4.

**Natchnione przemijanie.** Gdy rzucasz [Krok przez mgłę](../spells/misty-step.md), możesz zmodyfikować czar tak, by zabrać ze sobą jedną chętną istotę, której dotykasz. Ta istota teleportuje się na wolne miejsce według twojego wyboru w promieniu 1,5 metra od miejsca docelowego. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-scribing.md": f"""# Większe piętno pisma (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-scribing

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno pisma](feat-mark-of-scribing.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Utalentowany skryba z atutu Piętno pisma, możesz rzucić 1k6 zamiast 1k4.

**Natchnione pismo.** Gdy rzucasz [Zrozumienie języków](../spells/comprehend-languages.md), możesz zmodyfikować czar tak, by nad istotą, którą widzisz w promieniu 9 metrów od siebie, pojawił się sygiel trwający przez czas trwania zaklęcia. Gdy sygiel istnieje, twoi wrogowie w promieniu 9 metrów od tej istoty muszą wydać 60 centymetrów ruchu za każde 30 centymetrów zbliżenia się do niej. Sygiel znika, gdy istota wykona test ataku, rzuci czar albo zada obrażenia.
""",

"feat-greater-mark-of-sentinel.md": f"""# Większe piętno strażnika (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-sentinel

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno strażnika](feat-mark-of-sentinel.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja strażnika z atutu Piętno strażnika, możesz rzucić 1k6 zamiast 1k4.

**Ulepszony strażnik.** Gdy rzucasz [Tarcza](../spells/shield.md), możesz zmodyfikować czar tak, by magicznie oznaczyć istotę, którą widzisz w promieniu 9 metrów od siebie, do końca jej następnej tury. Gdy jest oznaczona, cel musi wydać 60 centymetrów ruchu za każde 30 centymetrów oddalenia się od ciebie.
""",

"feat-greater-mark-of-shadow.md": f"""# Większe piętno cienia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-shadow

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno cienia](feat-mark-of-shadow.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Przebiegła intuicja z atutu Piętno cienia, możesz rzucić 1k6 zamiast 1k4.

**Ulepszony cień.** Gdy rzucasz [Niewidzialność](../spells/invisibility.md) na siebie, możesz zmodyfikować czar tak, by objął też jedną chętną istotę w promieniu 1,5 metra od siebie. Stan niewidzialny natychmiast kończy się u dotkniętej istoty po wykonaniu testu ataku, zadaniu obrażeń albo rzuceniu czaru. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-storm.md": f"""# Większe piętno burzy (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-storm

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno burzy](feat-mark-of-storm.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja wiatromistrza z atutu Piętno burzy, możesz rzucić 1k6 zamiast 1k4.

**Ulepszona burza.** Gdy rzucasz [Podmuch wiatru](../spells/gust-of-wind.md), modyfikujesz czar tak, by zyskać prędkość lotu równą połowie swojej prędkości (zaokrąglając w dół) przez czas trwania zaklęcia. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",

"feat-greater-mark-of-warding.md": f"""# Większe piętno ochrony (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-mark-of-warding

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Piętno ochrony](feat-mark-of-warding.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Intuicja strażnika z atutu Piętno ochrony, możesz rzucić 1k6 zamiast 1k4.

**Ulepszona ochrona.** Gdy rzucasz [Magiczny pancerz](../spells/mage-armor.md) na siebie, możesz zmodyfikować czar tak, by objął też jedną chętną istotę, którą widzisz w promieniu 9 metrów od siebie. Po zmodyfikowaniu czaru tą korzyścią nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",
}

OTHER = {
"feat-aberrant-dragonmark.md": f"""# Aberacyjne piętno smoka (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-aberrant-dragonmark

---

{EBERRON_SRC}

*Atut piętna smoka (warunek wstępny: kampania Eberron, nie możesz mieć innego atutu piętna smoka)*

Zyskujesz następujące korzyści.

**Aberacyjna wytrzymałość.** Gdy wykonujesz rzut obronny na Kondycję, możesz rzucić 1k4 i dodać wynik do rzutu. Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Aberacyjna magia.** Znasz jedną sztuczkę według własnego wyboru z [listy czarów zaklinacza](../spell-lists/sorcerer.md). Wybierz też czar 1. kręgu z tej listy. Zawsze masz ten czar przygotowany. Możesz rzucić go raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Krótkiego albo Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Kondycja jest twoją cechą bazową przy rzucaniu tego czaru.

**Aberacyjny impuls.** Gdy rzucasz czar 1. kręgu z tego atutu, możesz wydać jedną ze swoich kości PW i ją rzucić. Jeśli wyrzucisz liczbę parzystą, zyskujesz tymczasowe PW równe wyrzuconej wartości. Jeśli wyrzucisz liczbę nieparzystą, jedna istota w promieniu 9 metrów od ciebie (z wyłączeniem ciebie) otrzymuje obrażenia od mocy równe wyrzuconej wartości. Jeśli w zasięgu nie ma innych istot, obrażenia otrzymujesz ty.
""",

"feat-greater-aberrant-mark.md": f"""# Większe aberracyjne piętno (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-greater-aberrant-mark

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, atut [Aberacyjne piętno smoka](feat-aberrant-dragonmark.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Kondycji o 1, maksymalnie do 20.

**Ulepszona intuicja.** Gdy używasz korzyści Aberacyjna wytrzymałość z atutu Aberacyjne piętno smoka, możesz rzucić 1k6 zamiast 1k4.

**Piętno inspiracji.** Gdy rzucasz sztuczkę, możesz wydać jedną ze swoich kości PW i ją rzucić. Zyskujesz tymczasowe PW równe wyrzuconej wartości, a jedna wybrana przez ciebie istota w promieniu 9 metrów od ciebie (z wyłączeniem ciebie) otrzymuje obrażenia od mocy równe wyrzuconej wartości. Możesz skorzystać z tej korzyści liczbę razy równą modyfikatorowi Kondycji (minimum raz); wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.
""",

"feat-potent-dragonmark.md": f"""# Potężne piętno smoka (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-potent-dragonmark

---

{EBERRON_SRC}

*Atut ogólny (wymaganie: poziom 4+, dowolny atut piętna smoka)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ cechę bazową używaną przez twój atut piętna smoka o 1, maksymalnie do 20.

**Przygotowanie piętna.** Zawsze masz przygotowane czary z listy Czary piętna twojego atutu piętna smoka (jeśli taką posiadasz).

**Rzucanie czarów piętna.** Masz jedną dodatkową komórkę czaru do rzucania czarów z atutu piętna smoka. Krąg tej komórki wynosi połowę twojego poziomu (zaokrąglając w górę), maksymalnie 5. kręgu. Odzyskujesz wydaną komórkę po zakończeniu Krótkiego albo Długiego odpoczynku. Możesz użyć tej komórki wyłącznie do rzucenia czaru, który masz przygotowany dzięki atutowi piętna smoka albo korzyści Przygotowanie piętna z tego atutu.
""",

"feat-boon-of-siberys.md": f"""# Dar Syberisa (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-boon-of-siberys

---

{EBERRON_SRC}

*Epicki dar (warunek wstępny: poziom 19+, kampania Eberron)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 30.

**Aberacyjna magia.** Wybierz czar dowolnego kręgu z listy czarów zaklinacza albo czar z tabeli Piętna Syberisa. Zawsze masz ten czar przygotowany. Możesz rzucić go raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Krótkiego albo Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową przy rzucaniu tego czaru (wybierz przy zdobyciu atutu).

**Piętna Syberisa**

| Piętno | Czar |
| --- | --- |
| Wykrywania | [Prawdziwe widzenie](../spells/true-seeing.md) |
| Tropienia | [Teleportacja](../spells/teleport.md) |
| Opiekuna | [Zwierzęce kształty](../spells/animal-shapes.md) |
| Leczenia | [Regeneracja](../spells/regenerate.md) |
| Gościnności | [Uczta bohaterów](../spells/heroes-feast.md) |
| Tworzenia | [Półpłaszczyzna](../spells/demiplane.md) |
| Przemijania | [Przesunięcie płaszczyzny](../spells/plane-shift.md) |
| Pisma | [Symbol](../spells/symbol.md) |
| Strażnika | [Pustka umysłu](../spells/mind-blank.md) |
| Cienia | [Projekcja obrazu](../spells/project-image.md) |
| Burzy | [Kontrola pogody](../spells/control-weather.md) |
| Ochrony | [Labirynt](../spells/maze.md) |
""",
}

OTHER.update({
"feat-death-knight-initiate.md": f"""# Inicjacja rycerza śmierci (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-death-knight-initiate

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: poziom 4+, zdolność Mistrzostwo broni)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Siły albo Charyzmy o 1, maksymalnie do 20.

**Punkty śmierci.** Twoje oddanie ścieżce rycerza śmierci daje ci dostęp do profanacyjnych mocy nieumarłych. Zdolność korzystania z nich reprezentują punkty śmierci. Masz ich liczbę równą swojej premii z biegłości. Wszystkie wydane punkty śmierci odzyskujesz po zakończeniu Długiego odpoczynku.

Możesz wydawać punkty śmierci, by korzystać z niektórych korzyści ścieżki rycerza śmierci. Ten atut daje ci jedną z nich: Przerażające uderzenie.

**Przerażające uderzenie.** Zawsze masz przygotowany czar [Gniewne uderzenie](../spells/wrathful-smite.md). Charyzma jest twoją cechą bazową przy rzucaniu tego czaru. Możesz rzucić go bez użycia komórki czaru, wydając 1 punkt śmierci. Gdy wydajesz punkty śmierci na rzucenie [Gniewne uderzenie](../spells/wrathful-smite.md), cel ma utrudnienie w rzutach obronnych na Mądrość, by uniknąć efektu czaru albo go zakończyć. Możesz też rzucać ten czar, używając posiadanych komórek czaru.
""",

"feat-death-knight-ascension.md": f"""# Wniebowstąpienie rycerza śmierci (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-death-knight-ascension

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: poziom 12+, dwa atuty ścieżki rycerza śmierci)*

Twoja ścieżka do zostania rycerzem śmierci dobiega końca.

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Siły albo Charyzmy o 1, maksymalnie do 20.

**Nieumarły.** Twój typ istoty to nieumarły.

**Profana anatomia.** Masz odporność na obrażenia nekrotyczne i od trucizny. Nie zyskujesz poziomów wyczerpania z odwodnienia, niedożywienia ani uduszenia.

**Kula piekielnego ognia.** Akcją magiczną możesz wydać 1–5 punktów śmierci, by miotnąć kulą czystego piekielnego ognia w punkt, który widzisz w promieniu 36 metrów. Każda istota w sferze o promieniu 6 metrów ze środkiem w wybranym punkcie wykonuje rzut obronny na Zręczność (ST = 8 + modyfikator Charyzmy + premia z biegłości). Przy nieudanym rzucie cel otrzymuje 2k6 obrażeń od ognia i 2k6 obrażeń nekrotycznych za każdy wydany punkt śmierci. Przy udanym — połowę obrażeń.
""",

"feat-deathly-presence.md": f"""# Obecność śmierci (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-deathly-presence

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: poziom 8+, atut [Inicjacja rycerza śmierci](feat-death-knight-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Siły, Kondycji albo Charyzmy o 1, maksymalnie do 20.

**Przerażająca obecność.** Zawsze masz przygotowany czar [Strach](../spells/fear.md). Charyzma jest twoją cechą bazową przy rzucaniu tego czaru. Możesz rzucić go bez użycia komórki czaru, wydając 1 punkt śmierci. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy wydajesz punkty śmierci na rzucenie [Strach](../spells/fear.md), każda istota, która nie odniesie sukcesu w rzucie obronnym przeciwko czarowi, otrzymuje dodatkowo 7 (2k6) obrażeń psychicznych oprócz normalnych efektów zaklęcia.
""",

"feat-dread-authority.md": f"""# Przerażająca władza (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-dread-authority

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: atut [Inicjacja rycerza śmierci](feat-death-knight-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Kondycji albo Charyzmy o 1, maksymalnie do 20.

**Przerażające rozkazanie.** Zawsze masz przygotowany czar [Rozkaz](../spells/command.md). Charyzma jest twoją cechą bazową przy rzucaniu tego czaru. Możesz rzucić go bez użycia komórki czaru, wydając 1 punkt śmierci. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy wydajesz punkty śmierci na rzucenie [Rozkaz](../spells/command.md), nieumarli będący celem mają utrudnienie w rzucie obronnym przeciwko czarowi.
""",

"feat-harbinger-of-doom.md": f"""# Zwiastun zagłady (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-harbinger-of-doom

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: atut [Inicjacja rycerza śmierci](feat-death-knight-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Siły, Kondycji albo Charyzmy o 1, maksymalnie do 20.

**Zły omen.** Zawsze masz przygotowany czar [Klątwa](../spells/bane.md). Charyzma jest twoją cechą bazową przy rzucaniu tego czaru. Możesz rzucić go bez użycia komórki czaru, wydając 1 punkt śmierci. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy wydajesz punkty śmierci na rzucenie [Klątwa](../spells/bane.md), dotknięte cele odejmują 1k6 od testów ataku i rzutów obronnych zamiast 1k4.
""",

"feat-unholy-steed.md": f"""# Nieświęty wierzchowiec (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-unholy-steed

---

{VILLAIN_SRC}

*Atut ścieżki rycerza śmierci (warunek wstępny: poziom 8+, atut [Inicjacja rycerza śmierci](feat-death-knight-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Siły albo Kondycji o 1, maksymalnie do 20.

**Widmowy wierzchowiec.** Zawsze masz przygotowany czar [Znalezienie wierzchowca](../spells/find-steed.md). Charyzma jest twoją cechą bazową przy rzucaniu tego czaru. Możesz rzucić go bez użycia komórki czaru, wydając 1 punkt śmierci. Gdy wydajesz punkty śmierci na rzucenie [Znalezienie wierzchowca](../spells/find-steed.md), przywołany wierzchowiec to fiend, a cele według twojego wyboru mają utrudnienie w rzucie obronnym na Mądrość przeciwko jego Upiornemu spojrzeniu. Możesz też rzucać ten czar, używając posiadanych komórek czaru.
""",

"feat-lich-initiate.md": f"""# Inicjacja licha (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-lich-initiate

---

{VILLAIN_SRC}

*Atut ścieżki licha (warunek wstępny: poziom 4+, zdolność Rzucanie czarów albo Magia paktu)*

Stawiasz pierwsze kroki ku lichdomowi — tworzysz sferment duchowy, magiczne naczynie kotwiczące twoją duszę w świecie żywych na wypadek zniszczenia ciała.

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Inteligencji, Mądrości albo Charyzmy o 1, maksymalnie do 20.

**Tworzenie sfermentu duchowego.** Wybierz drobny przedmiot o wielkim znaczeniu dla ciebie. Rzucić na tabeli Sfermenty duchowe albo wybrać z niej inspirację. Spędzasz Długi odpoczynek, kotwicząc duszę w tym przedmiocie i zyskując zdolność pochłaniania dusz żywych, by wzmacniać własną moc. Możesz mieć tylko jeden sferment duchowy naraz. Gdy tworzysz drugi, stary zostaje zniszczony.

**Sfermenty duchowe**

| 1k6 | Twój sferment duchowy to… |
| --- | --- |
| 1 | Żołądź z lasu zniszczonego dawno temu. |
| 2 | List miłosny od zmarłego kochanka albo kochanki. |
| 3 | Kałamarz, którym zapisałeś swój pierwszy czar albo modlitwę. |
| 4 | Zbezczeszczony symbol bóstwa, które wyparłeś. |
| 5 | Dzwonek, którego dźwięk staje się niższy z każdą pochłoniętą duszą. |
| 6 | Wysuszona część ciała — oko, palec albo róg — która kiedyś należała do ciebie albo kogoś, kogo znałeś. |

**Zniszczenie sfermentu duchowego.** KP sfermentu duchowego równa się ST twoich czarów, a PW — modyfikatorowi cechy bazowej plus poziom postaci. Gdy sferment zostanie zniszczony, zyskujesz 2 poziomy wyczerpania i nie możesz korzystać z Wysysania duszy, dopóki nie stworzysz nowego.

**Wysysanie duszy.** Gdy sprowadzasz humanoidalnego wroga do 0 PW, możesz pochłonąć jego duszę i zyskać impuls mocy (bez akcji). W swojej następnej turze pierwsza istota, którą trafisz atakiem, otrzymuje dodatkowe obrażenia nekrotyczne równe 1k6 plus modyfikator cechy bazowej. Korzyść działa też, gdy ktoś inny sprowadza humanoidalnego wroga w promieniu 3 metrów od ciebie do 0 PW. Dusza pochłonięta w ten sposób może wrócić tylko dzięki [Prawdziwemu wskrzeszeniu](../spells/true-resurrection.md) albo [Życzeniu](../spells/wish.md).
""",

"feat-lich-ascension.md": f"""# Wniebowstąpienie licha (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-lich-ascension

---

{VILLAIN_SRC}

*Atut ścieżki licha (warunek wstępny: poziom 12+, co najmniej dwa atuty ścieżki licha)*

Twoja ścieżka ku lichdomowi dobiega końca. Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Inteligencji, Mądrości albo Charyzmy o 1, maksymalnie do 20.

**Nieumarły.** Twój typ istoty to nieumarły.

**Profana anatomia.** Masz odporność na obrażenia nekrotyczne i od trucizny. Nie zyskujesz poziomów wyczerpania z odwodnienia, niedożywienia ani uduszenia.

**Przerażające spojrzenie.** Uczysz się czaru [Strach](../spells/fear.md), jeśli go nie znasz, i zawsze masz go przygotowany. Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową przy tym czarze (wybierz przy wyborze atutu). Możesz rzucić go bez użycia komórki czaru liczbę razy równą modyfikatorowi cechy bazowej (minimum raz); wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Odrodzenie.** Jeśli umrzesz, odradzasz się w ciągu 1k10 dni, o ile masz sferment duchowy i nie zostałeś wcześniej wskrzeszony. Zyskujesz nowe ciało ze wszystkimi PW na najbliższym wolnym miejscu w promieniu 1,5 metra od sfermentu duchowego.
""",

"feat-arcane-restoration.md": f"""# Tajemne odnowienie (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-arcane-restoration

---

{VILLAIN_SRC}

*Atut ścieżki licha (warunek wstępny: atut [Inicjacja licha](feat-lich-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Inteligencji, Mądrości albo Charyzmy o 1, maksymalnie do 20.

**Odświeżenie esencji.** Gdy używasz Wysysania duszy, by pochłonąć duszę, możesz odzyskać jedną lub więcej wydanych komórek czaru. Łączny krąg odzyskanych komórek nie może przekroczyć 4. Po użyciu tej zdolności nie możesz zrobić tego ponownie, dopóki nie zakończysz Krótkiego albo Długiego odpoczynku.
""",

"feat-transfer-life.md": f"""# Transfer życia (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-transfer-life

---

{VILLAIN_SRC}

*Atut ścieżki licha (warunek wstępny: atut [Inicjacja licha](feat-lich-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Inteligencji, Mądrości albo Charyzmy o 1, maksymalnie do 20.

**Transfer duszy.** Gdy używasz Wysysania duszy, by pochłonąć duszę, możesz wybrać istotę w promieniu 18 metrów od siebie, która zyskuje tymczasowe PW równe twojej premii z biegłości plus modyfikator cechy bazowej (minimum 1 tymczasowe PW).
""",

"feat-undead-grasp.md": f"""# Chwyt nieumarłego (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-undead-grasp

---

{VILLAIN_SRC}

*Atut ścieżki licha (warunek wstępny: atut [Inicjacja licha](feat-lich-initiate.md))*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość Inteligencji, Mądrości albo Charyzmy o 1, maksymalnie do 20.

**Paraliżujący dotyk.** Znasz sztuczkę [Zimny dotyk](../spells/chill-touch.md). Jeśli już ją znasz, uczysz się innej sztuczki według własnego wyboru. Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową przy tym czarze (wybierz przy wyborze atutu).

Gdy zadajesz obrażenia [Zimnym dotykiem](../spells/chill-touch.md), możesz wydać komórkę czaru co najmniej 1. kręgu, by spróbować sparaliżować cel. Cel otrzymuje dodatkowo 1k10 obrażeń nekrotycznych za każdy krąg wydanej komórki i musi odnieść sukces w rzucie obronnym na Kondycję przeciwko ST twoich czarów, albo ma stan sparaliżowany do początku twojej następnej tury.
""",

"feat-boon-of-unwavering-devotion.md": f"""# Dar niezachwianej oddaności (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-boon-of-unwavering-devotion

---

{VILLAIN2_SRC}

*Epicki dar (warunek wstępny: poziom 19+)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 30.

**Niepodatność na opętanie.** Automatycznie odnosisz sukces w rzutach obronnych, by uniknąć opętania albo je zakończyć.

**Widzenie przez iluzje.** Wizualne iluzje wydają ci się przezroczyste i automatycznie odnosisz sukces w rzutach obronnych przeciwko nim.

**Niepodważalna pewność siebie.** Zaraz po tym, gdy istota, którą widzisz, odniesie sukces w rzucie obronnym na Mądrość przeciwko efektowi, który stworzyłeś, możesz wykonać reakcję i zmusić ją do powtórzenia rzutu — musi użyć nowego wyniku. Po użyciu tej korzyści nie możesz zrobić tego ponownie, dopóki nie rzucisz inicjatywy albo nie zakończysz Krótkiego albo Długiego odpoczynku.
""",

"feat-boon-of-the-cleansed-heart.md": f"""# Dar oczyszczonego serca (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-boon-of-the-cleansed-heart

---

{VILLAIN2_SRC}

*Epicki dar (warunek wstępny: poziom 19+)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 30.

**Oczyszczenie serca.** Możesz rzucić [Rozproszenie dobra i zła](../spells/dispel-evil-and-good.md) bez użycia komórki czaru. Nie możesz użyć specjalnej funkcji Odesłanie tego czaru, gdy rzucasz go w ten sposób.

**Promieniste odbicie.** Masz odporność na obrażenia nekrotyczne. Gdy miałbyś otrzymać obrażenia nekrotyczne i nie masz stanu obezwładniony, możesz zadać 2k8 obrażeń od promieni każdej wybranej istocie w emanacji 3 metrów promieniującej od ciebie.
""",

"feat-boon-of-the-bandit-king.md": f"""# Dar króla bandytów (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-boon-of-the-bandit-king

---

{VILLAIN2_SRC}

*Epicki dar (warunek wstępny: poziom 19+)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 30.

**Podstępny urok.** Masz ułatwienie w testach Zręczność (Zwinne ręce), by okraść kogoś.

Gdy taki test zakończy się sukcesem, możesz sprawić, że cel dobrowolnie odda przedmiot i ma stan zauroczony przez 1 minutę albo do otrzymania obrażeń. Po użyciu tej korzyści nie możesz zrobić tego ponownie, dopóki nie zakończysz Krótkiego albo Długiego odpoczynku.

**Nieuchwytny.** Nie prowokujesz ataków okazji, gdy wychodzisz z zasięgu istoty.
""",

"feat-boon-of-the-hunter-s-eye.md": f"""# Dar oka myśliwego (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-boon-of-the-hunter-s-eye

---

{VILLAIN2_SRC}

*Epicki dar (warunek wstępny: poziom 19+)*

Zyskujesz następujące korzyści.

**Zwiększenie wartości cechy.** Zwiększ wartość dowolnej cechy o 1, maksymalnie do 30.

**Szybkie pojmanie.** Gdy zadajesz obrażenia istocie, którą zamierzasz powalić, a nie zabić, jeśli cel ma 20 PW albo mniej po zadaniu obrażeń, spada do 0 PW.

**Badany łowca.** Gdy rzucasz inicjatywę, możesz wybrać istotę, którą widzisz; wiesz, czy ma jakiekolwiek odporności, niepodatności albo podatności, a jeśli tak — jakie.
""",

"feat-atoner-s-grace.md": f"""# Łaska pokutnika (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-atoner-s-grace

---

{VILLAIN2_SRC}

*Atut pochodzenia*

Zyskujesz następujące korzyści.

**Rozbrojenie obecności.** Wrogi stosunek istoty nie nakłada utrudnienia na twoje testy Charyzma (Perswazja), by na nią wpływać.

**Rozmowa.** Gdy wykonujesz akcję Odwrót albo Wpływ, każda wybrana przez ciebie istota w promieniu 1,5 metra od ciebie ma ułatwienie w następnym teście cechy albo rzucie obronnym przed początkiem twojej następnej tury.
""",

"feat-raised-by-cultists.md": f"""# Wychowany przez kultystów (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-raised-by-cultists

---

{VILLAIN2_SRC}

*Atut pochodzenia*

Zyskujesz następujące korzyści.

**Krwawe objawienie.** Gdy stajesz się ranny, możesz reakcją zyskać heroiczną inspirację.

**Wspólne rzucanie.** Gdy sojusznik w promieniu 1,5 metra od ciebie wykonuje rzut obronny na Kondycję, by utrzymać koncentrację, możesz reakcją dać mu ułatwienie w tym rzucie.
""",

"feat-trapper.md": f"""# Traper (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-trapper

---

{VILLAIN2_SRC}

*Atut pochodzenia*

Zyskujesz następujące korzyści.

**Oko do szczegółu.** Masz ułatwienie w każdym teście Inteligencja (Śledztwo) wykonywanym w ramach akcji Badaj.

**Szybki trop.** Nie masz utrudnienia w testach Mądrość (Percepcja) albo Mądrość (Przetrwanie) podczas podróży w szybkim tempie i masz ułatwienie w takich testach podczas podróży w normalnym tempie.

**Ekspert pułapek.** Możesz akcją dodatkową, zamiast akcji Wykorzystaj, ustawić pułapkę myśliwską. Gdy ją ustawiasz, dodajesz swoją premię z biegłości do ST rzutu obronnego, by uniknąć pułapki, oraz ST testu cechy, by się z niej uwolnić.
""",

"feat-cryokinesis.md": f"""# Kriokineza (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-cryokinesis

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Manipulacja lodem.** Raz na turę, gdy rzucasz czar albo trafiasz testem ataku i zadajesz obrażenia obuchowe, przeszywające, sieczne albo psychiczne, możesz zmienić typ obrażeń na obrażenia od zimna.

**Talent psioniczny.** Znasz sztuczkę [Promień mrozu](../spells/ray-of-frost.md). Zawsze masz też przygotowane czary [Pancerz Agathys](../spells/armor-of-agathys.md) i [Lodowy nóż](../spells/ice-knife.md). Każdy z nich możesz rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać te czary, używając posiadanych komórek czaru. Gdy je rzucasz, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).
""",

"feat-pyrokinesis.md": f"""# Pyrokineza (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-pyrokinesis

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Podpalacz.** Raz na turę, gdy rzucasz czar albo trafiasz testem ataku i zadajesz obrażenia obuchowe, przeszywające, sieczne albo psychiczne, możesz zmienić typ obrażeń na obrażenia od ognia.

**Talent psioniczny.** Znasz sztuczkę [Stworzenie płomienia](../spells/produce-flame.md). Zawsze masz też przygotowany czar [Płonące dłonie](../spells/burning-hands.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Palący promień](../spells/scorching-ray.md) i możesz rzucać go w ten sam sposób.
""",

"feat-atmokinesis.md": f"""# Atmokineza (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-atmokinesis

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Wstrząs błyskawicy.** Raz na turę, gdy rzucasz czar albo trafiasz testem ataku i zadajesz obrażenia obuchowe, przeszywające, sieczne albo psychiczne, możesz zmienić typ obrażeń na obrażenia od błyskawic.

**Talent psioniczny.** Znasz sztuczkę [Porażający chwyt](../spells/shocking-grasp.md). Zawsze masz też przygotowany czar [Chmura mgły](../spells/fog-cloud.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Podmuch wiatru](../spells/gust-of-wind.md) i możesz rzucać go w ten sam sposób.
""",

"feat-biokinesis.md": f"""# Biokineza (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-biokinesis

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Zgięcie energii życiowej.** Gdy rzucany przez ciebie czar przywraca PW istocie, możesz rzucić 1k4 i dodać wynik do łącznej liczby odzyskanych PW. Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Znasz sztuczkę [Oszczędzenie umierającemu](../spells/spare-the-dying.md). Zawsze masz też przygotowany czar [Słowo leczenia](../spells/healing-word.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Tajemna witalność](../spells/arcane-vigor.md) i możesz rzucać go w ten sam sposób.
""",

"feat-clairsentience.md": f"""# Klairsentencja (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-clairsentience

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Drobna przedwiedza.** Gdy wykonujesz akcję Szukaj, możesz zyskać ułatwienie w dowolnym teście cechy wykonywanym w ramach tej akcji. Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Znasz sztuczkę [Wsparcie](../spells/guidance.md). Zawsze masz też przygotowany czar [Wykrycie dobra i zła](../spells/detect-evil-and-good.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Widzenie niewidzialnego](../spells/see-invisibility.md) i możesz rzucać go w ten sam sposób.
""",

"feat-empath.md": f"""# Empat (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-empath

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Wyczuwanie emocji.** Gdy wykonujesz akcję Wpływ, możesz zyskać ułatwienie w dowolnym teście cechy wykonywanym w ramach tej akcji. Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Zawsze masz przygotowany czar [Osoba urocza](../spells/charm-person.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy go rzucasz, nie wymaga komponentów werbalnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Uspokojenie emocji](../spells/calm-emotions.md) i możesz rzucać go w ten sam sposób.
""",

"feat-flesh-morpher.md": f"""# Kształtownik ciała (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-flesh-morpher

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Elastyczne ciało.** Gdy wykonujesz test Zręczność (Akrobatyka) albo Zręczność (Zwinne ręce), zyskujesz premię równą modyfikatorowi Inteligencji (minimum +1). Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Zawsze masz przygotowany czar [Długobieg](../spells/longstrider.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru odpowiedniego kręgu. Gdy go rzucasz, nie wymaga komponentów werbalnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).

Gdy osiągniesz poziom postaci 3, zawsze masz też przygotowany czar [Alteracja własnej postaci](../spells/alter-self.md) i możesz rzucać go w ten sam sposób.
""",

"feat-mind-whisperer.md": f"""# Szeptacz umysłu (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-mind-whisperer

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Ograniczona telepatia.** Akcją magiczną wybierz jedną istotę, którą widzisz w promieniu 36 metrów od siebie. Nawiązujesz z nią telepatyczne połączenie. Przez 1 godzinę ty i wybrana istota możecie komunikować się telepatycznie, będąc w promieniu 36 metrów od siebie. Aby się zrozumieć, każdy z was musi mentalnie używać języka znane drugiej stronie. Po użyciu tej korzyści nie możesz zrobić tego ponownie, dopóki nie zakończysz Krótkiego albo Długiego odpoczynku.

**Talent psioniczny.** Znasz sztuczkę [Odłamek umysłu](../spells/mind-sliver.md). Zawsze masz też przygotowany czar [Rozdarcujące szepty](../spells/dissonant-whispers.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).
""",

"feat-psi-trickster.md": f"""# Psi-oszust (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-psi-trickster

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Przebiegły umysł.** Gdy wykonujesz test Charyzma (Oszustwo) albo Charyzma (Perswazja), zyskujesz premię równą modyfikatorowi Inteligencji (minimum +1). Możesz skorzystać z tej korzyści liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Znasz sztuczkę [Drobna iluzja](../spells/minor-illusion.md). Zawsze masz też przygotowany czar [Przebranie](../spells/disguise-self.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy rzucasz te czary, nie wymagają komponentów werbalnych ani materialnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).
""",

"feat-psykineticist.md": f"""# Psykineticysta (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:feat-psykineticist

---

{PSION_SRC}

*Atut dzikiego talentu (warunek wstępny: nie możesz mieć innego atutu dzikiego talentu)*

Zyskujesz następujące korzyści.

**Psi-wzmocnienie.** Gdy wykonujesz akcję Dash, możesz zwiększyć swoją prędkość o 3 metry do początku swojej następnej tury. Możesz to zrobić liczbę razy równą twojej premii z biegłości; wszystkie zużyte użycia odzyskujesz po zakończeniu Długiego odpoczynku.

**Talent psioniczny.** Znasz sztuczkę [Telekinetyczne miotnięcie](spell-telekinetic-fling.md) (z tego UA). Zawsze masz też przygotowany czar [Fala dźwiękowa](../spells/thunderwave.md). Możesz go rzucić raz bez użycia komórki czaru, a możliwość takiego rzucenia odzyskujesz po zakończeniu Długiego odpoczynku. Możesz też rzucać ten czar, używając posiadanych komórek czaru. Gdy rzucasz te czary, nie wymagają komponentów werbalnych; Inteligencja, Mądrość albo Charyzma jest twoją cechą bazową (wybierz przy wyborze atutu).
""",
})


def main():
    for stem in MARK_STEMS:
        path = UA / f"feat-{stem}.md"
        path.write_text(adapt_mark(stem), encoding="utf-8")
        print("Wrote", path.name)

    for name, content in GREATER_MARKS.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
        print("Wrote", name)

    for name, content in OTHER.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
        print("Wrote", name)


if __name__ == "__main__":
    main()
