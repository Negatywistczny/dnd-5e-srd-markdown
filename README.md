# D&D 5e SRD 5.2.1 Markdown (2024)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![D&D 5e 2024](https://img.shields.io/badge/D%26D%205e-2024%20(5.2.1)-red.svg)](https://www.dndbeyond.com/)
[![Format](https://img.shields.io/badge/format-markdown-blue.svg)](https://commonmark.org/)

Oficjalny **System Reference Document 5.2.1** D&D 5e (2024) w formacie Markdown — w wersji angielskiej i polskiej. Repozytorium zawiera też treści ze scrapowane z [dnd2024.wikidot.com](http://dnd2024.wikidot.com).

## Struktura repozytorium

```
├── srd-5.2.1/
│   ├── en/              # SRD 5.2.1 — angielski
│   └── pl/              # SRD 5.2.1 — polski
├── dnd2024-wikidot/     # Klasy, czary, przedmioty itd. z wikidot
├── docs/
│   └── czary-tlumaczenie.md   # Tabela tłumaczeń nazw czarów EN→PL
├── sources/             # Pliki źródłowe (PDF, starsze wersje)
└── scripts/             # Skrypty do scrapowania wikidot
```

## SRD 5.2.1

Główne pliki reguł w `srd-5.2.1/en/` i `srd-5.2.1/pl/`:

| Plik | Opis |
| --- | --- |
| [character-creation.md](srd-5.2.1/en/character-creation.md) | Tworzenie postaci |
| [character-origins.md](srd-5.2.1/en/character-origins.md) | Pochodzenie i gatunki |
| [classes.md](srd-5.2.1/en/classes.md) | 12 klas bazowych |
| [equipment.md](srd-5.2.1/en/equipment.md) | Wyposażenie |
| [feats.md](srd-5.2.1/en/feats.md) | Featy |
| [spells.md](srd-5.2.1/en/spells.md) | Lista czarów |
| [magic-items.md](srd-5.2.1/en/magic-items.md) | Przedmioty magiczne |
| [playing-the-game.md](srd-5.2.1/en/playing-the-game.md) | Zasady gry |
| [gameplay-toolbox.md](srd-5.2.1/en/gameplay-toolbox.md) | Zaawansowane zasady |
| [monsters.md](srd-5.2.1/en/monsters.md) | Przegląd potworów |
| [monsters-A-Z.md](srd-5.2.1/en/monsters-A-Z.md) | Bestiariusz A–Z |
| [animals.md](srd-5.2.1/en/animals.md) | Zwierzęta |
| [rules-glossary.md](srd-5.2.1/en/rules-glossary.md) | Słownik reguł |

Polskie tłumaczenia znajdują się w odpowiadających plikach w `srd-5.2.1/pl/`.

## D&D 2024 Wikidot

Folder `dnd2024-wikidot/` zawiera treści spoza SRD: podklasy, tła, gatunki, UA, rozszerzone listy czarów i przedmiotów magicznych.

Aby zaktualizować dane z wikidot:

```bash
python scripts/scrape_wikidot_wiki.py
python scripts/scrape_wikidot_subclasses.py
```

## Licencja

Treść SRD jest udostępniana na licencji [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Szczegóły w pliku [LICENSE](LICENSE).

Dungeons & Dragons, D&D, Wizards of the Coast oraz powiązane nazwy są znakami towarowymi Wizards of the Coast LLC.
