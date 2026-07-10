#!/usr/bin/env python3
"""Convert imperial units to metric using PG (Galaktyka) game-rounded values."""

from __future__ import annotations

import re

# PG: 5 ft → 1,5 m (×0,3). Not exact SI conversion.
FEET_TO_METERS_FACTOR = 0.3

# PG: 1 lb → 0,5 kg in equipment tables.
LB_TO_KG_FACTOR = 0.5

# PG: 1 pint → 0,5 l; 1 gallon → 4 l.
GALLON_TO_LITERS = 4
PINT_TO_LITERS = 0.5

# 1 ft³ ≈ 28 l (used in PG bucket: 0,5 ft³ = 14 l).
CUBIC_FOOT_TO_LITERS = 28

# PG: 1 mile → 1,5 km (travel rounding).
MILE_TO_KM = 1.5

# PG: 1 inch → 2,5 cm.
INCH_TO_CM = 2.5


def _fmt_num(value: float) -> str:
    if abs(value - round(value)) < 0.05:
        return str(int(round(value)))
    text = f"{value:.1f}".rstrip("0").rstrip(".")
    return text.replace(".", ",")


def feet_to_meters_value(feet: float) -> float:
    return round(feet * FEET_TO_METERS_FACTOR, 1)


def feet_to_meters_text(feet: float) -> str:
    meters = feet_to_meters_value(feet)
    n = _fmt_num(meters)
    if meters == 1:
        return "1 metr"
    last = int(meters) % 10
    last2 = int(meters) % 100
    if last in (2, 3, 4) and last2 not in (12, 13, 14):
        form = "metry"
    else:
        form = "metrów"
    return f"{n} {form}"


def lb_to_kg_text(lb: float) -> str:
    kg = lb * LB_TO_KG_FACTOR
    if kg < 1 and kg > 0:
        grams = int(round(kg * 1000))
        if grams == 1:
            return "1 gram"
        last = grams % 10
        last2 = grams % 100
        if last in (2, 3, 4) and last2 not in (12, 13, 14):
            return f"{grams} gramy"
        return f"{grams} gramów"
    n = _fmt_num(kg)
    if kg == 1:
        return "1 kilogram"
    last = int(round(kg)) % 10
    last2 = int(round(kg)) % 100
    if last in (2, 3, 4) and last2 not in (12, 13, 14):
        return f"{n} kilogramy"
    return f"{n} kilogramów"


def liters_text(liters: float) -> str:
    n = _fmt_num(liters)
    if liters == 1:
        return "1 litr"
    last = int(round(liters)) % 10
    last2 = int(round(liters)) % 100
    if last in (2, 3, 4) and last2 not in (12, 13, 14):
        return f"{n} litry"
    return f"{n} litrów"


def _replace_feet_distance(match: re.Match[str]) -> str:
    feet = float(match.group(1).replace(",", "."))
    return feet_to_meters_text(feet)


def _replace_lb(match: re.Match[str]) -> str:
    lb = float(match.group(1).replace(",", "."))
    return lb_to_kg_text(lb)


def _replace_gallons(match: re.Match[str]) -> str:
    gallons = float(match.group(1).replace(",", "."))
    return liters_text(gallons * GALLON_TO_LITERS)


def _replace_pints(match: re.Match[str]) -> str:
    pints = float(match.group(1).replace(",", "."))
    return liters_text(pints * PINT_TO_LITERS)


def _replace_cubic_feet(match: re.Match[str]) -> str:
    feet = float(match.group(1).replace(",", "."))
    return liters_text(feet * CUBIC_FOOT_TO_LITERS)


PHRASE_REPLACEMENTS: list[tuple[str, str]] = [
    # Udźwig
    (
        "Twój rozmiar i wynik Siły określają maksymalną wagę w funtach, którą możesz unieść",
        "Twój rozmiar i wynik Siły określają maksymalną wagę w kilogramach, którą możesz unieść",
    ),
    ("<td>Si. × 7,5 lb.</td>", "<td>Si. × 3,75 kg</td>"),
    ("<td>Si. × 15 lb.</td>", "<td>Si. × 7,5 kg</td>"),
    ("<td>Si. × 30 lb.</td>", "<td>Si. × 15 kg</td>"),
    ("<td>Si. × 60 lb.</td>", "<td>Si. × 30 kg</td>"),
    ("<td>Si. × 120 lb.</td>", "<td>Si. × 60 kg</td>"),
    ("<td>Si. × 240 lb.</td>", "<td>Si. × 120 kg</td>"),
    # Woda / jedzenie (dzienne zapotrzebowanie)
    ("<td>1/4 galonu</td>", "<td>1 litr</td>"),
    ("<td>4 galony</td>", "<td>16 litrów</td>"),
    ("<td>1 galon</td>", "<td>4 litry</td>"),
    ("<td>16 galonów</td>", "<td>64 litry</td>"),
    ("<td>64 galony</td>", "<td>256 litrów</td>"),
    ("<td>1/4 funta</td>", "<td>125 gramów</td>"),
    ("<td>4 funty</td>", "<td>2 kilogramy</td>"),
    ("<td>1 funt</td>", "<td>0,5 kilograma</td>"),
    ("<td>16 funtów</td>", "<td>8 kilogramów</td>"),
    ("<td>64 funty</td>", "<td>32 kilogramy</td>"),
    # Wyczerpanie (5 ft = 1,5 m na poziom)
    (
        "_Zmniejszona prędkość._ Twoja prędkość zostaje zmniejszona o liczbę stóp równą 5-krotności twojego poziomu wyczerpania.",
        "_Zmniejszona prędkość._ Twoja prędkość zostaje zmniejszona o 1,5 metra za każdy poziom wyczerpania.",
    ),
    # Skoki (PG 5.1)
    (
        "**Skok wzwyż.** Kiedy wykonujesz Skok wzwyż, wyskakujesz w powietrze na liczbę stóp równą 3 plus twój modyfikator Siły (minimum 0,0 metra), jeśli przed skokiem przebiegniesz co najmniej 3 metra. Kiedy wykonujesz Skok wzwyż z miejsca, możesz skoczyć tylko na połowę tej odległości. W obu przypadkach każda stopa skoku kosztuje stopę ruchu.",
        "**Skok wzwyż.** Kiedy wykonujesz Skok wzwyż, skaczesz w górę na wysokość równą 90 centymetrów plus 30 centymetrów za każdy punkt modyfikatora z Siły (minimum 0), jeśli przed skokiem przebiegniesz co najmniej 3 metry. Kiedy wykonujesz Skok wzwyż z miejsca, możesz wyskoczyć tylko na połowę tej wysokości. W obu przypadkach każdy metr, na który podskoczysz, kosztuje metr twojej szybkości.",
    ),
    (
        "**Skok w dal.** Kiedy wykonujesz Skok w dal, skaczesz poziomo na liczbę stóp równą twojej wartości Siły, jeśli przed skokiem przebiegniesz co najmniej 3 metra. Kiedy wykonujesz Skok w dal z miejsca, możesz skoczyć tylko na połowę tej odległości. W obu przypadkach każda stopa skoku kosztuje stopę ruchu.",
        "**Skok w dal.** Kiedy wykonujesz Skok w dal, pokonujesz maksymalnie odległość wynoszącą wartość twojej Siły × 30 centymetrów, jeśli przed skokiem przebiegniesz co najmniej 3 metry. Kiedy wykonujesz Skok w dal z miejsca, możesz przeskoczyć tylko połowę tej odległości. W obu przypadkach każdy metr, który przeskoczysz, kosztuje metr twojej szybkości.",
    ),
    # Ruch
    (
        "Jeśli obszar jest Trudnym Terenem, każda stopa ruchu na tym obszarze kosztuje 1 dodatkową stopę.",
        "Jeśli obszar jest Trudnym Terenem, każdy metr ruchu na tym obszarze kosztuje 1 dodatkowy metr.",
    ),
    (
        "Podczas wspinaczki każda stopa ruchu kosztuje 1 dodatkową stopę (2 dodatkowe stopy w trudnym terenie).",
        "Podczas wspinaczki każdy metr ruchu kosztuje 1 dodatkowy metr (2 dodatkowe metry w trudnym terenie).",
    ),
    (
        "Podczas czołgania się każda stopa ruchu kosztuje 1 dodatkową stopę (2 dodatkowe stopy w trudnym terenie).",
        "Podczas czołgania się każdy metr ruchu kosztuje 1 dodatkowy metr (2 dodatkowe metry w trudnym terenie).",
    ),
    (
        "Podczas pływania każda stopa ruchu kosztuje 1 dodatkową stopę (2 dodatkowe stopy w trudnym terenie).",
        "Podczas pływania każdy metr ruchu kosztuje 1 dodatkowy metr (2 dodatkowe metry w trudnym terenie).",
    ),
    (
        "każda stopa ruchu na tym obszarze kosztuje 1 dodatkową stopę",
        "każdy metr ruchu na tym obszarze kosztuje 1 dodatkowy metr",
    ),
    (
        "every foot of movement costs it 1 extra foot",
        "every meter of movement costs it 1 extra meter",
    ),
    # Wyposażenie — typowe pojemniki
    (
        "Plecak mieści do 30 funtów w objętości 1 stopy sześciennej.",
        "Plecak mieści do 15 kilogramów w objętości 28 litrów.",
    ),
    (
        "Beczka mieści do 40 galonów cieczy lub do 4 stóp sześciennych suchych towarów.",
        "Beczka mieści do 160 litrów cieczy lub do 112 litrów suchych towarów.",
    ),
    (
        "Kosz mieści do 40 funtów w objętości 2 stóp sześciennych.",
        "Kosz mieści do 20 kilogramów w objętości 56 litrów.",
    ),
    (
        "Gdy rozbrzmi w ramach akcji \"Użycie obiektu\", wydaje dźwięk słyszalny w odległości do 60 stóp.",
        "Gdy rozbrzmi w ramach akcji \"Użycie obiektu\", wydaje dźwięk słyszalny w odległości do 18 metrów.",
    ),
    (
        "Wiadro mieści do pół stopy sześciennej (do 14 litrów) zawartości.",
        "Wiadro mieści do 14 litrów zawartości.",
    ),
    (
        "Kufer mieści do 12 stóp sześciennych (340 litrów) zawartości.",
        "Kufer mieści do 336 litrów zawartości.",
    ),
    (
        "Flaszka mieści do 1 pinta.",
        "Flaszka mieści do 0,5 litra.",
    ),
    (
        "Jako Akcja Użycie Obiektu możesz rzucić Hakiem wspinaczkowym w poręcz, występ lub inne zaczepienie w promieniu 50 stóp od siebie",
        "Jako Akcja Użycie Obiektu możesz rzucić Hakiem wspinaczkowym w poręcz, występ lub inne zaczepienie w promieniu 15 metrów od siebie",
    ),
    (
        "Atrament jest dostarczany w butelce o pojemności 1 uncji, która zapewnia wystarczającą ilość atramentu do zapisania około 500 stron.",
        "Atrament jest dostarczany w butelce o pojemności 30 mililitrów, która zapewnia wystarczającą ilość atramentu do zapisania około 500 stron.",
    ),
    (
        "Dzban mieści do 1 galona.",
        "Dzban mieści do 4 litrów.",
    ),
    (
        "Lampa spala olej jako paliwo i zapewnia jasne światło w promieniu 15 stóp oraz słabe światło na dodatkowe 9 metrów.",
        "Lampa spala olej jako paliwo i zapewnia jasne światło w promieniu 4,5 metra oraz słabe światło na dodatkowe 9 metrów.",
    ),
    (
        "Latarnia kierunkowa rzuca Jasne światło w stożku o promieniu 60 stóp i Słabe światło w promieniu kolejnych 60 stóp. Po zapaleniu pali się przez 6 godzin na jednej kolbie (1 pinta) oleju.",
        "Latarnia kierunkowa rzuca Jasne światło w stożku o promieniu 18 metrów i Słabe światło w promieniu kolejnych 18 metrów. Po zapaleniu pali się przez 6 godzin na jednej butelce (0,5 litra) oleju.",
    ),
    (
        "Latarnia zamykana spala Olej jako paliwo, rzucając Jasne światło w promieniu 30 stóp i Słabe światło na dodatkowe 30 stóp. Zapalona, pali się przez 6 godzin na na jednym flakonie (1 pinta)  Oleju.",
        "Latarnia zamykana spala olej jako paliwo, rzucając Jasne światło w promieniu 9 metrów i Słabe światło na dodatkowe 9 metrów. Zapalona, pali się przez 6 godzin na jednej butelce (0,5 litra) oleju.",
    ),
    (
        "Perfumy znajdują się w fiolce o pojemności 4 uncji.",
        "Perfumy znajdują się w fiolce o pojemności 120 mililitrów.",
    ),
    (
        "Żelazny garnek mieści do 1 galona.",
        "Żelazny garnek mieści do 4 litrów.",
    ),
    (
        "Torba mieści do 6 funtów w objętości jednej piątej stopy sześciennej.",
        "Torba mieści do 3 kilogramów w objętości 5,6 litra.",
    ),
    (
        "Worek mieści do 30 funtów w objętości 1 stopy sześciennej.",
        "Worek mieści do 15 kilogramów w objętości 28 litrów.",
    ),
    (
        "Fiolka mieści do 4 uncji.",
        "Fiolka mieści do 120 mililitrów.",
    ),
    (
        "Bukłak mieści do 4 pintów.",
        "Bukłak mieści do 2 litrów.",
    ),
    (
        "Typowa mikstura to 1 uncja płynu w fiolce.",
        "Typowa mikstura to 30 mililitrów płynu w fiolce.",
    ),
    (
        "Typowa laska waży od 2 do 5 funtów.",
        "Typowa laska waży od 1 do 2,5 kilograma.",
    ),
    (
        "Kostur waży od 2 do 7 funtów i dobrze służy jako laska lub kij.",
        "Kostur waży od 1 do 3,5 kilograma i dobrze służy jako laska lub kij.",
    ),
    (
        "Tworzysz 45 funtów żywności i 30 galonów świeżej wody",
        "Tworzysz 22,5 kilograma żywności i 120 litrów świeżej wody",
    ),
    (
        "może pomieścić do 500 funtów",
        "może pomieścić do 250 kilogramów",
    ),
    (
        "Ręka nie może atakować, aktywować magicznych przedmiotów ani nosić więcej niż 10 funtów.",
        "Ręka nie może atakować, aktywować magicznych przedmiotów ani nosić więcej niż 5 kilogramów.",
    ),
    (
        "grubości 1 cala, która unosi się 3 stopy nad ziemią",
        "grubości 2,5 centymetra, która unosi się 0,9 metra nad ziemią",
    ),
    (
        "za każdy galon wody rozpryskanej na niego",
        "za każde 4 litry wody rozpryskane na niego",
    ),
    (
        "Sferze o promieniu 5 stóp",
        "Sferze o promieniu 1,5 metra",
    ),
    (
        "na odległość do 30 stóp",
        "na odległość do 9 metrów",
    ),
    (
        "na odległość do 60 stóp",
        "na odległość do 18 metrów",
    ),
    (
        "na odległość do 120 stóp",
        "na odległość do 36 metrów",
    ),
    (
        "A Szklana butelka holds up to 1½ pints.",
        "Szklana butelka mieści do 0,75 litra.",
    ),
    # Grubość barier (czary)
    (
        "Czar jest blokowane przez kamień, ziemię lub drewno o grubości 1 stopy; 2,5 centymetrów metalu; lub cienki arkusz ołowiu.",
        "Czar jest blokowane przez kamień, ziemię lub drewno o grubości 30 centymetrów; 2,5 centymetra metalu; lub cienki arkusz ołowiu.",
    ),
    (
        "Magiczna cisza; 1 stopa kamienia, metalu lub drewna; lub cienka warstwa ołowiu blokuje czar.",
        "Magiczna cisza; 30 centymetrów kamienia, metalu lub drewna; lub cienka warstwa ołowiu blokuje czar.",
    ),
    # Ruch — definicje
    (
        "Stworzenie ma Szybkość, czyli odległość w stopach, jaką stworzenie może pokonać, poruszając się w swojej turze.",
        "Stworzenie ma Szybkość, czyli odległość w metrach, jaką stworzenie może pokonać, poruszając się w swojej turze.",
    ),
    (
        "Podczas pływania każdy stopa ruchu kosztuje cię 1 dodatkową stopę (2 dodatkowe stopy w trudnym terenie).",
        "Podczas pływania każdy metr ruchu kosztuje cię 1 dodatkowy metr (2 dodatkowe metry w trudnym terenie).",
    ),
    (
        "poświęcić 4 stopy ruchu na każdą 1 stopę, którą poruszy",
        "poświęcić 4 metry ruchu na każdy 1 metr, który pokona",
    ),
    # Bibeloty
    (
        "Kostka o wadze jednej uncji z nieznanego materiału",
        "Kostka o wadze około 30 gramów z nieznanego materiału",
    ),
    (
        "Jajo o wadze jednego funta i jaskrawoczerwonej skorupce",
        "Jajo o wadze 0,5 kilograma i jaskrawoczerwonej skorupce",
    ),
    # Klej / rozpuszczalnik
    (
        "Jedna uncja kleju może pokryć powierzchnię kwadratu o boku 30 centymetrów.",
        "30 mililitrów kleju może pokryć powierzchnię kwadratu o boku 30 centymetrów.",
    ),
    (
        "Nałożenie jednej uncji _Kleju absolutnego_",
        "Nałożenie 30 mililitrów _Kleju absolutnego_",
    ),
    (
        "Akcją Wykorzystaj możesz wylać 1 albo więcej uncji rozpuszczalnika",
        "Akcją Wykorzystaj możesz wylać 30 mililitrów albo więcej rozpuszczalnika",
    ),
    (
        "Każda uncja natychmiast rozpuszcza",
        "Każde 30 mililitrów natychmiast rozpuszcza",
    ),
    # Psion (UA)
    (
        "na odległość w stopach równą pięciokrotności wyrzuconej wartości",
        "na odległość w metrach równą 1,5 × pięciokrotność wyrzuconej wartości",
    ),
    (
        "zasięg telepatii rośnie o liczbę stóp równą dziesięciokrotności wyrzuconej wartości",
        "zasięg telepatii rośnie o liczbę metrów równą trzykrotności wyrzuconej wartości",
    ),
    # Dzban alchemiczny
    (
        "Ten ceramiczny dzban wygląda na pojemnik na około 4 litry płynu i waży 5,5 kilograma, pełny albo pusty.",
        "Ten ceramiczny dzban wygląda na pojemnik na około 4 litry płynu i waży 6 kilogramów, pełny albo pusty.",
    ),
    (
        "wylać ten płyn z prędkością do około 7,5 litra na minutę",
        "wylać ten płyn z prędkością do około 8 litrów na minutę",
    ),
    ("| Olej | 1 1 litr |", "| Olej | 1 litr |"),
    ("o średnicy 1 stopy", "o średnicy 30 centymetrów"),
    ("o grubości 1 stopy", "o grubości 30 centymetrów"),
    ("o średnicy 0,3 metrów", "o średnicy 30 centymetrów"),
    (
        "każdy stopień ruchu kosztuje je o 0,3 metrów więcej",
        "każdy metr ruchu kosztuje je 1 dodatkowy metr",
    ),
    (
        "Kufer może zawierać do 0,3 metra sześciennego materii nieożywionej (90 x 60 x 60 centymetrów).",
        "Kufer może zawierać do 336 litrów materii nieożywionej (0,9 × 0,6 × 0,6 metra).",
    ),
]

# Regex replacements — longest / most specific first.
REGEX_REPLACEMENTS: list[tuple[re.Pattern[str], str | callable]] = [
    (
        re.compile(r"\b(\d+(?:[.,]\d+)?)-foot-(?:radius|cube|square|diameter)\b", re.I),
        lambda m: f"{_fmt_num(feet_to_meters_value(float(m.group(1).replace(',', '.'))))}-metrowy",
    ),
    (
        re.compile(r"\b(\d+(?:[.,]\d+)?)-Foot-(?:radius|cube|square|diameter)\b"),
        lambda m: f"{_fmt_num(feet_to_meters_value(float(m.group(1).replace(',', '.'))))}-metrowy",
    ),
    (
        re.compile(r"\b(\d+(?:[.,]\d+)?)\s*Feet\b"),
        _replace_feet_distance,
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:stóp|stopy|stop)\s+sześcienn(?:a|e|ych|y)\b",
            re.I,
        ),
        _replace_cubic_feet,
    ),
    (
        re.compile(
            r"\b(?:pół|1/2|½)\s+stopy\s+sześciennej\b",
            re.I,
        ),
        lambda m: "14 litrów",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:uncji|uncje|uncja)\b",
            re.I,
        ),
        lambda m: f"{int(round(float(m.group(1).replace(',', '.')) * 30))} mililitrów",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:funtów|funty|funta|funt)\b",
            re.I,
        ),
        _replace_lb,
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:galonów|galony|galonu|galon)\b",
            re.I,
        ),
        _replace_gallons,
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:pintów|pinty|pinta|pint)\b",
            re.I,
        ),
        _replace_pints,
    ),
    (
        re.compile(r"\b(\d+(?:[.,]\d+)?)\s*lb\.?\b", re.I),
        _replace_lb,
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:feet|foot|ft\.?)\b",
            re.I,
        ),
        _replace_feet_distance,
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:stopy|stopa|stopę|stopie)\b",
            re.I,
        ),
        _replace_feet_distance,
    ),
    (
        re.compile(r"\b1\s+kwart(?:a|y|ę)\b", re.I),
        lambda m: "1 litr",
    ),
    (
        re.compile(r"\bkwart(?:a|y|ę)\b", re.I),
        lambda m: "1 litr",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:cal|cali)\b",
            re.I,
        ),
        lambda m: f"{_fmt_num(float(m.group(1).replace(',', '.')) * INCH_TO_CM)} centymetrów",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:mil|miles|mile)\s+per\s+hour\b",
            re.I,
        ),
        lambda m: f"{_fmt_num(float(m.group(1).replace(',', '.')) * MILE_TO_KM)} km/h",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*(?:mil|miles|mile)\b",
            re.I,
        ),
        lambda m: f"{_fmt_num(float(m.group(1).replace(',', '.')) * MILE_TO_KM)} km",
    ),
    (
        re.compile(
            r"\b(\d+(?:[.,]\d+)?)\s*stóp\b",
            re.I,
        ),
        _replace_feet_distance,
    ),
]


# Values leaked from ×0.3048 conversion — normalize to PG (×0.3) rounding.
SI_METER_FIXES: list[tuple[str, str]] = [
    ("152,4 metr", "150 metr"),
    ("91,4 metr", "90 metr"),
    ("45,7 metr", "45 metr"),
    ("36,6 metr", "36 metr"),
    ("30,5 metr", "30 metr"),
    ("27,4 metr", "27 metr"),
    ("18,3 metr", "18 metr"),
    ("15,2 metr", "15 metr"),
    ("12,2 metr", "12 metr"),
    ("9,1 metr", "9 metr"),
    ("6,1 metr", "6 metr"),
    ("4,6 metr", "4,5 metr"),
    ("3716 metrów kwadratowych", "3600 metrów kwadratowych"),
]

# Movement mechanics: feet → meters (after numeric distances converted).
MOVEMENT_UNIT_REPLACEMENTS: list[tuple[str, str]] = [
    ("stopa ruchu", "metr ruchu"),
    ("stopę ruchu", "metr ruchu"),
    ("stopy ruchu", "metry ruchu"),
    ("dodatkową stopę", "dodatkowy metr"),
    ("dodatkowe stopy", "dodatkowe metry"),
]


def normalize_si_to_pg(text: str) -> str:
    for old, new in SI_METER_FIXES:
        text = text.replace(old, new)
    return text


def apply_metric_units(text: str) -> str:
    for old, new in PHRASE_REPLACEMENTS:
        text = text.replace(old, new)
    for old, new in MOVEMENT_UNIT_REPLACEMENTS:
        text = text.replace(old, new)
    for pattern, repl in REGEX_REPLACEMENTS:
        if callable(repl):
            text = pattern.sub(repl, text)
        else:
            text = pattern.sub(repl, text)
    text = normalize_si_to_pg(text)
    return text


def feet_to_meters(text: str) -> str:
    """Compatibility wrapper for translate_wikidot_pl.py."""
    return apply_metric_units(text)
