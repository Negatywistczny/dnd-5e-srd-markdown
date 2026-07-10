# Słownik terminologii mechanicznej (EN → PL)

Oficjalne polskie nazwy pojęć zasad D&D 5e dla `dnd2024-wikidot-pl/`.

Powiązane słowniki:
- [Podklasy](podklasy-tlumaczenie.md) — nazwy podklas
- [Czary](czary-tlumaczenie.md) — nazwy czarów

## Źródła (w kolejności wiarygodności)

| Skrót | Źródło | Rola |
| --- | --- | --- |
| **PG** | [`sources/5e-SRD_v1.0.md`](../sources/5e-SRD_v1.0.md) — oficjalne PL SRD 5.1 (Rebel / Galaktyka) | **Jedyne oficjalne źródło terminologii 5.1** |
| **proj.** | Ustalenia kuracji tego repozytorium | **Terminologia 2024** — brak polskiego PHB 2024; to jest właśnie cel projektu |
| **Foundry** | `lang-pl-dnd5` — kompendium Foundry VTT | Uzupełnienie (np. typy istot, nazwy podklas) |
| **srd** | `srd-5.2.1/pl/` — SRD 5.2.1 PL | Materiał wejściowy do korekty; **nie źródło** — błędy poprawiamy wg PG + **proj.** |
| **EN** | `dnd2024-wikidot/`, SRD 5.2.1 EN | Treść i sens; nie tłumaczenie gotowe |

### Zasada pracy

1. **PG** tam, gdzie pojęcie istnieje w 5.1 PL.
2. **proj.** dla mechanik i terminów z edycji 2024 — ustalane ręcznie w tym repo (patrz tabele poniżej).
3. Gdy `srd-5.2.1/pl` odstaje — poprawiamy skryptem `scripts/fix_srd_pl_terminology.py` i kuratorujemy `dnd2024-wikidot-pl`.
4. Nie wprowadzamy konwencji sprzecznych z PG ani już ustalonymi wpisami **proj.**

Korekty w `srd-5.2.1/pl` i `dnd2024-wikidot-pl`: `scripts/fix_srd_pl_terminology.py` (domyślnie oba katalogi).

---

## Zmysły specjalne

| EN | PL | Źródło |
| --- | --- | --- |
| Blindsight | Ślepowidzenie | PG |
| Truesight | Prawdziwe widzenie | PG |
| True Seeing (czar) | Prawdziwe widzenie | PG, [czary](czary-tlumaczenie.md) |
| Darkvision | Widzenie w ciemności | PG |
| Tremorsense | **Wyczucie drgań** | proj. |
| Passive Perception (wartość w zasadach) | **Pasywna Mądrość (Percepcja)** | PG |
| Passive Perception (skrót w stat bloku) | **Pasywna Percepcja** | proj. |

---

## Stany (Conditions)

| EN | PL | Źródło | Uwagi |
| --- | --- | --- | --- |
| Blinded | Oślepiony | PG | |
| Charmed | Zauroczony | PG | |
| Deafened | Ogłuchony | PG | ≠ Ogłuszony |
| Frightened | Przerażony | PG | |
| Grappled | Pochwycony | PG | |
| Incapacitated | Obezwładniony | PG | |
| Invisible | Niewidzialny | PG | |
| Paralyzed | Sparaliżowany | PG | |
| Petrified | Skamieniały | PG | |
| Poisoned | Zatruty | PG | |
| Prone | Powalony | PG | |
| Restrained | Unieruchomiony | PG | |
| Stunned | Ogłuszony | PG | ≠ Ogłuchony |
| Unconscious | Nieprzytomny | PG | |
| Exhaustion | Wyczerpanie | PG | Poziomy wyczerpania |

---

## Rzuty i testy

| EN | PL | Źródło |
| --- | --- | --- |
| Ability check | Test cechy | PG |
| Attack roll | Test ataku | PG |
| Saving throw | Rzut obronny | PG |
| Death saving throw | Rzut przeciw śmierci | PG |
| Damage roll | Rzut na obrażenia | PG |
| Critical hit | Trafienie krytyczne | PG |
| Advantage | Ułatwienie | PG |
| Disadvantage | Utrudnienie | PG |
| Proficiency bonus | **Premia z biegłości** | PG |
| Expertise | **Znawstwo** | PG |
| Passive check | Test pasywny | PG |
| Initiative | Inicjatywa | PG |
| Armor Class (AC) | Klasa Pancerza (KP) | PG |
| Difficulty Class (DC) | Stopień Trudności (ST) | PG |
| D20 Test | **Test K20** | proj. |

---

## Ochrona przed obrażeniami

| EN | PL | Źródło |
| --- | --- | --- |
| Resistance | Odporność | PG |
| Immunity | **Niepodatność** | PG |
| Vulnerability | **Podatność** | PG |

### Typy obrażeń (PG — pełne nazwy)

| EN | PL (oficjalnie) |
| --- | --- |
| Acid | obrażenia od kwasu |
| Bludgeoning | obrażenia obuchowe |
| Cold | obrażenia od zimna |
| Fire | obrażenia od ognia |
| Force | obrażenia od mocy |
| Lightning | obrażenia od elektryczności |
| Necrotic | obrażenia nekrotyczne |
| Piercing | obrażenia kłute |
| Poison | obrażenia od trucizn |
| Psychic | obrażenia psychiczne |
| Radiant | obrażenia od światłości |
| Slashing | obrażenia cięte |
| Thunder | obrażenia od dźwięku |

W skróconych listach (tabele, tagi) dopuszczalne są formy jednosłowne (np. obuchowe, kłute), jeśli kontekst jest jasny.

---

## Akcje w walce

### PG 5.1

| EN | PL | Źródło |
| --- | --- | --- |
| Action | Akcja | PG |
| Bonus Action | Akcja dodatkowa | PG |
| Reaction | Reakcja | PG |
| Attack | Atak | PG |
| Dash | Sprint | PG |
| Disengage | Odstąpienie | PG |
| Dodge | Unik | PG |
| Help | Pomoc | PG |
| Hide | **Ukrycie się** | PG |
| Ready | Przygotowanie | PG |
| Search | Przeszukiwanie | PG |
| Cast a Spell | **Rzucenie czaru** | PG |
| Use an Object | Użycie obiektu | PG |
| Opportunity attack | Atak okazji | PG |

### Tylko edycja 2024 (proj.)

| EN | PL | Źródło |
| --- | --- | --- |
| Influence | **Wpływ** | proj. |
| Study | **Nauka** | proj. |
| Magic | **Akcja magiczna** | proj. |

---

## Eksploracja i walka

| EN | PL | Źródło |
| --- | --- | --- |
| Speed | Szybkość | PG |
| Difficult terrain | Trudny teren | PG |
| Cover (half) | Osłona **połowiczna** / połowicznie | PG |
| Cover (three-quarters) | Osłona **w trzech czwartych** | PG |
| Cover (total) | Osłona **całkowita** / w całości | PG |
| Bright light | Jasne światło | PG |
| Dim light | **Słabe światło** | PG |
| Darkness | Ciemność | PG |
| Heavily obscured | **Silnie przesłonięty** (obszar) | proj. |
| Lightly obscured | **Lekko przesłonięty** (obszar) | proj. |
| Short rest | Krótki odpoczynek | PG |
| Long rest | Długi odpoczynek | PG |
| Hit Points (HP) | Punkty wytrzymałości (PW) | PG |
| Hit Point Dice | Kości Wytrzymałości | PG |
| Temporary Hit Points | Tymczasowe punkty wytrzymałości | PG |
| Inspiration | **Inspiracja** | PG |
| Heroic Inspiration | **Heroiczna inspiracja** | proj. |
| Attunement | **Zestrojenie** | proj. |
| Reach (melee) | Strefa ataku | PG |
| Dungeon Master (DM) | **MP** — Mistrz Podziemi | PG |

Unikać **MG** (Mistrz Gry) — to tłumaczenie ang. *Game Master*, nie *Dungeon Master*.

---

## Obszary działania

| EN | PL | Źródło |
| --- | --- | --- |
| Area of Effect | **Obszar działania** | proj. |
| Cone | Stożek | proj. |
| Cube | Sześcian | proj. |
| Cylinder | Walec | proj. |
| Emanation | Emanacja | proj. |
| Line | Prosta | proj. |
| Sphere | Sfera | proj. |

---

## Rzucanie czarów

| EN | PL | Źródło |
| --- | --- | --- |
| Spell / spell | **Zaklęcie** (preferowane) / czar | PG (obie formy); w opisach zasad preferujemy *zaklęcie* |
| Cantrip | Sztuczka | PG |
| Spell slot | Komórka czaru | PG |
| Spell level (slot) | Krąg czaru | PG |
| Spellcasting | Rzucanie czarów | PG |
| Spell attack | Atak czarem | PG |
| Spell save DC | ST rzutu obronnego (przeciw czarowi) | PG |
| Concentration | Koncentracja | PG |
| Ritual | Rytuał | PG |
| Spellcasting ability | Cecha bazowa | PG |
| Arcane focus | **Magiczny fokus** / **Fokus magii wtajemniczeń** | PG |
| Druidic focus | **Druidyczny fetysz** | PG |
| Holy symbol | **Święty symbol** | PG |
| Pact Magic | **Magia paktu** | proj. |
| Sorcery Points | **Punkty zaklinania** | proj. |
| Metamagic | **Metamagia** | proj. |
| Eldritch Invocations | **Mistyczne inwokacje** | proj. |

---

## Cechy i umiejętności

### Cechy (Ability Scores)

| EN | PL | Skrót |
| --- | --- | --- |
| Strength | Siła | — |
| Dexterity | Zręczność | — |
| Constitution | Kondycja | — |
| Intelligence | Inteligencja | — |
| Wisdom | Mądrość | — |
| Charisma | Charyzma | — |

### Umiejętności (Skills) — PG

| EN | PL | Cecha |
| --- | --- | --- |
| Acrobatics | Akrobatyka | Zręczność |
| Animal Handling | Opieka nad zwierzętami | Mądrość |
| Arcana | Wiedza tajemna | Inteligencja |
| Athletics | Atletyka | Siła |
| Deception | Oszustwo | Charyzma |
| History | Historia | Inteligencja |
| Insight | Intuicja | Mądrość |
| Intimidation | Zastraszanie | Charyzma |
| Investigation | Śledztwo | Inteligencja |
| Medicine | Medycyna | Mądrość |
| Nature | Przyroda | Inteligencja |
| Perception | Percepcja | Mądrość |
| Performance | Występy | Charyzma |
| Persuasion | **Perswazja** | Charyzma |
| Religion | Religia | Inteligencja |
| Sleight of Hand | Zwinne dłonie | Zręczność |
| Stealth | Skradanie się | Zręczność |
| Survival | Sztuka przetrwania | Mądrość |

---

## Nazwy klas (PG)

| EN | PL |
| --- | --- |
| Barbarian | Barbarzyńca |
| Bard | Bard |
| Cleric | Kleryk |
| Druid | Druid |
| Fighter | Wojownik |
| Monk | Mnich |
| Paladin | Paladyn |
| Ranger | Łowca |
| Rogue | Łotr |
| Sorcerer | **Zaklinacz** |
| Warlock | Czarownik |
| Wizard | Mag |

---

## Typy istot (Creature Types)

| EN | PL | Źródło |
| --- | --- | --- |
| Aberration | Wynaturzenie | Foundry |
| Beast | Bestia | Foundry |
| Celestial | Niebiański | Foundry |
| Construct | Konstrukt | Foundry |
| Dragon | Smok | Foundry |
| Elemental | Żywiołak | Foundry |
| Fey | **Fey** | 2024 — bez polskiego odpowiednika |
| Fiend | Czart | Foundry |
| Giant | Gigant | Foundry |
| Humanoid | Humanoid | Foundry |
| Monstrosity | Potworność | Foundry |
| Ooze | Szlam | Foundry |
| Plant | Roślina | Foundry |
| Undead | Nieumarły | Foundry |

---

## Zdolności klasowe (wybrane)

| EN | PL | Źródło |
| --- | --- | --- |
| Second Wind | **Drugi oddech** | proj. |
| Action Surge | **Przypływ sił** | proj. |
| Sneak Attack | Chytre uderzenie | PG |
| Divine Sense | **Boski zmysł** | proj. |
| Lay on Hands | **Nakładanie rąk** | proj. |
| Wild Shape | **Dzika postać** | proj. |
| Evasion | **Odskok** | proj. |
| Ability Score Improvement | **Zwiększenie cechy** | proj. |

---

## Konwencje wyłącznie projektu `dnd2024-wikidot-pl`

Te ustalenia **nie zastępują** terminologii — dotyczą tylko formatu repozytorium:

| Temat | Zasada |
| --- | --- |
| Metadane plików | `**Klasa:**`, `**URL źródła:**`, `**Źródło:** Podręcznik Gracza` |
| Odległość | ft → m (×0,3): 5→1,5; 10→3; 15→4,5; 30→9; 60→18; 120→36 |
| Waga | lb → kg (×0,5): 1 lb → 0,5 kg; 2 lb → 1 kg |
| Pojemność płynów | 1 pinta → 0,5 l; 1 galon → 4 l |
| Objętość sucha | 1 stopa sześcienna → 28 l (0,5 ft³ → 14 l) |
| Podróż | 1 mila → 1,5 km |
| Długość | 1 cal → 2,5 cm |
| Skoki | PG: skok w dal = Siła × 30 cm; skok wzwyż = 90 cm + 30 cm × mod. Siły |
| Udźwig | tabela SRD: współczynniki lb × 0,5 → kg (Śr.: Si. × 7,5 kg) |
| Linki | Względne ścieżki w obrębie `dnd2024-wikidot-pl/` |

---

## Częste błędy

| ❌ Unikać | ✅ Używać |
| --- | --- |
| Czarnoksiężnik | Zaklinacz |
| premia do biegłości | premia z biegłości |
| skupienie rzucania czarów | magiczny fokus |
| Persuazja | Perswazja |
| ślepozmysł / ślepy wzrok | Ślepowidzenie |
| Niewrażliwość (na typ obrażeń) | niepodatność |
| Połowa osłony | osłona połowiczna |
| Ukrycie (akcja) | Ukrycie się |
| pasywna percepcja (w tekście zasad) | pasywna Mądrość (Percepcja) |
| Ekspertyza | Znawstwo |
| Inspiracja (w materiale 2024) | Heroiczna inspiracja |
| mocno / lekko zasłonięty | silnie / lekko **przesłonięty** |
| przyciemnione światło | słabe światło |
| Magia (akcja) | Akcja magiczna |
| Nieziemskie inwokacje | Mistyczne inwokacje |
| Drugie tchnienie | Drugi oddech |
| Przypływ działania | Przypływ sił |
| MG | MP |
| Okładka (Cover) | Osłona |

---

## Status weryfikacji

- **Oficjalne (PG 5.1):** zmysły, stany, akcje 5.1, testy, premia z biegłości, osłony, typy obrażeń, umiejętności, klasy, fokusy, komórki czarów, MP
- **Ustalone w projekcie (brak PL PHB 2024):** Heroiczna inspiracja, Test K20, Wpływ, Nauka, Akcja magiczna, przesłonięcie, Punkty zaklinania, Metamagia, Mistyczne inwokacje, zdolności klasowe, Obszary działania, Zestrojenie, Wyczucie drgań, Pasywna Percepcja (stat bloki), Fey
- **Skorygowane skryptem:** `srd-5.2.1/pl` i `dnd2024-wikidot-pl` — `scripts/fix_srd_pl_terminology.py`
- **Do kuracji:** nazwy podklas nowe w 2024 — patrz [podklasy-tlumaczenie.md](podklasy-tlumaczenie.md)
