#!/usr/bin/env python3
"""Translate UA monk + paladin subclasses (batch 65)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"

FILES = {
    "subclass-monk-tattooed-warrior.md": """# Wojownik z tatuażami (UA6 — 26.06.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-monk-tattooed-warrior

---

Źródło: [UA6 — Podklasy arkaniczne (26.06.2025)](https://www.dndbeyond.com/sources/dnd/ua/arcane-subclasses)

*Wzmacniaj sztuki walki magicznymi tatuażami*

Czerpiąc z różnorodnych tradycji znaków ciała z całego multiwersum, Wojownicy z tatuażami korzystają z mocy arkanicznej tkwiącej w magicznych tatuażach. Ci mnisi zdobywają tatuaże w miarę rozwoju sprawności bojowej i wglądu. Wojownicy z tatuażami mogą zmieniać kształt tatuaży, by uzyskać dostęp do wszechstronnego zestawu efektów fizycznych i magicznych do pokonywania wrogów.

### Poziom 3: Magiczne tatuaże

Zyskujesz magiczne tatuaże opisane w innych cechach tej podklasy. Tatuaże pojawiają się na ciele tam, gdzie chcesz. Obrażenia i urazy nie zakłócają działania magicznych tatuaży. Magiczny tatuaż może wyglądać jak piętno, skarifikacja, znamię, wzór łusek albo inna kosmetyczna zmiana.

Jeśli efekt tatuażu wymaga rzutu obronnego, ST równa się 8 plus twój modyfikator Mądrości plus premia z biegłości. Mądrość jest twoją cechą rzucania czarów nadanych przez tatuaż.

Za każdym razem, gdy kończysz Długi odpoczynek, możesz przemodelować jeden ze swoich magicznych tatuaży, zamieniając wybraną opcję z jednej listy na inną opcję z tej samej listy.

### Poziom 3: Tatuaże zwierząt

Zyskujesz dwa tatuaże zwierząt. Wybierz dwa tatuaże z poniższych opcji.

**Nietoperz.** Znasz sztuczkę [Tańczące światła](../spells/dancing-lights.md). Gdy wydajesz 1 punkt skupienia, by użyć Cierpliwej obrony albo Kroku w powietrzu, zyskujesz ślepowidzenie w promieniu 3 metrów na 1 minutę.

**Motyl.** Znasz sztuczkę [Światło](../spells/light.md). Możesz wydać 1 punkt skupienia, by rzucić [Milczący obraz](../spells/silent-image.md) bez komponentów materialnych.

**Kameleon.** Znasz sztuczkę [Pomniejsza iluzja](../spells/minor-illusion.md). Możesz wydać 1 punkt skupienia, by rzucić [Przebranie siebie](../spells/disguise-self.md).

**Żuraw.** Znasz sztuczkę [Wskazówki](../spells/guidance.md). Gdy chybisz istotę atakiem z Gradu ciosów, masz ułatwienie w testach ataku dla pozostałych uderzeń bez broni z tego użycia Gradu ciosów.

**Koń.** Znasz sztuczkę [Wiadomość](../spells/message.md). Możesz wydać 1 punkt skupienia, by rzucić [Szybkonogi](../spells/longstrider.md) bez komponentów materialnych.

**Pająk.** Znasz sztuczkę [Naprawa](../spells/mending.md). Gdy trafisz istotę atakiem z Gradu ciosów, ma ona utrudnienie w następnym teście ataku przed początkiem twojej następnej tury.

**Żółw.** Znasz sztuczkę [Powstrzymanie śmierci](../spells/spare-the-dying.md). Możesz wydać 1 punkt skupienia, by rzucić [Fałszywe życie](../spells/false-life.md) bez komponentów materialnych.

### Poziom 6: Tatuaż niebiański

Zyskujesz dodatkowy magiczny tatuaż przedstawiający zjawisko niebiańskie. Wybierz tatuaż z poniższych opcji.

**Kometa.** Możesz wydać 2 punkty skupienia, by rzucić [Wykrycie pułapek](../spells/find-traps.md).

**Sierp księżyca.** Możesz wydać 2 punkty skupienia, by rzucić [Krok przez mgłę](../spells/misty-step.md).

**Zaćmienie.** Możesz wydać 2 punkty skupienia, by rzucić [Niewidzialność](../spells/invisibility.md) bez komponentów materialnych.

**Rozbłysk słońca.** Możesz wydać 2 punkty skupienia, by rzucić [Mniejsze przywrócenie](../spells/lesser-restoration.md).

### Poziom 11: Tatuaż natury

Zyskujesz dodatkowy magiczny tatuaż przedstawiający element natury. Wybierz tatuaż z poniższych opcji.

**Góra.** Akcją magiczną możesz wydać 3 punkty skupienia, by zyskać odporność na obrażenia od kwasu i ułatwienie w rzutach obronnych na Kondycję na 1 minutę.

**Burza.** Akcją magiczną możesz wydać 3 punkty skupienia, by zyskać odporność na obrażenia od błyskawic i ułatwienie w rzutach obronnych na Zręczność na 1 minutę.

**Wulkan.** Akcją magiczną możesz wydać 3 punkty skupienia, by zyskać odporność na obrażenia od ognia i ułatwienie w rzutach obronnych na Siłę na 1 minutę.

**Fala.** Akcją magiczną możesz wydać 3 punkty skupienia, by zyskać odporność na obrażenia od zimna i ułatwienie w rzutach obronnych na Mądrość na 1 minutę.

### Poziom 17: Tatuaż potwora

Zyskujesz magiczny tatuaż przedstawiający nadnaturalne stworzenie. Wybierz tatuaż z poniższych opcji.

**Obserwator.** Masz prędkość lotu 3 metry i możesz unosić się. Ponadto możesz wydać 3 punkty skupienia, by rzucić [Przeciwzaklęcie](../spells/counterspell.md).

**Pies mignięcia.** Gdy wydajesz punkt skupienia, by użyć Cierpliwej obrony, możesz wydać 3 punkty skupienia, by rzucić [Mignięcie](../spells/blink.md) natychmiast po tej akcji dodatkowej.

**Bestia przesuwacza.** Gdy wydajesz punkt skupienia, by użyć Gradu ciosów albo Kroku w powietrzu, możesz wydać 2 punkty skupienia, by rzucić [Lustrzane odbicia](../spells/mirror-image.md) natychmiast po tej akcji dodatkowej.

**Naga strażniczka.** Gdy miałbyś spaść do 0 PW, ale nie zostajesz zabity natychmiast, twoje PW zamiast tego zmieniają się na liczbę równą podwojeniu twojego poziomu mnicha. Gdy skorzystasz z tej korzyści, nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",
    "subclass-monk-tattooed-warrior2.md": """# Wojownik z tatuażami (UA8 — 18.09.2025)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-monk-tattooed-warrior2

---

Źródło: [UA8 — Aktualizacja podklas arkanicznych (18.09.2025)](https://www.dndbeyond.com/sources/dnd/ua/arcane-subclasses-update)

*Wzmacniaj sztuki walki magicznymi tatuażami*

Czerpiąc z tradycji znaków ciała z całego multiwersum, Wojownicy z tatuażami korzystają z mocy arkanicznej tkwiącej w magicznych tatuażach. Ci mnisi zdobywają tatuaże w miarę rozwoju sprawności bojowej i wglądu. Wojownicy z tatuażami mogą przemodelowywać tatuaże, by uzyskać dostęp do zestawu efektów fizycznych i magicznych.

### Poziom 3: Magiczne tatuaże

Zyskujesz magiczne tatuaże opisane w innych cechach tej podklasy. Tatuaże pojawiają się na ciele tam, gdzie chcesz. Obrażenia i urazy nie zakłócają działania magicznych tatuaży. Magiczny tatuaż może wyglądać jak piętno, skarifikacja, znamię, wzór łusek albo inna kosmetyczna zmiana.

Jeśli efekt tatuażu wymaga rzutu obronnego, ST równa się 8 plus twój modyfikator Mądrości plus premia z biegłości. Mądrość jest twoją cechą rzucania czarów nadanych przez tatuaż.

Za każdym razem, gdy kończysz Długi odpoczynek, możesz przemodelować jeden ze swoich magicznych tatuaży, zamieniając wybraną opcję z jednej listy na inną opcję z tej samej listy.

### Poziom 3: Tatuaż zwierzęcia

Zyskujesz dwa tatuaże zwierząt. Wybierz dwa tatuaże z poniższych opcji.

**Nietoperz.** Znasz sztuczkę [Tańczące światła](../spells/dancing-lights.md). Zyskujesz też ślepowidzenie w promieniu 3 metrów.

**Motyl.** Znasz sztuczkę [Światło](../spells/light.md). Gdy wykonujesz Skok wzwyż, możesz użyć modyfikatora Zręczności zamiast modyfikatora Siły, by określić, jak wysoko możesz skoczyć.

**Żuraw.** Znasz sztuczkę [Wskazówki](../spells/guidance.md). Gdy chybisz istotę atakiem z Gradu ciosów, masz ułatwienie w następnym teście ataku przeciwko temu celowi przed końcem swojej następnej tury.

**Koń.** Znasz sztuczkę [Wiadomość](../spells/message.md). Gdy wydajesz 1 punkt skupienia, by użyć Kroku w powietrzu, twoja Szybkość wzrasta o 3 metry do początku twojej następnej tury.

**Żółw.** Znasz sztuczkę [Powstrzymanie śmierci](../spells/spare-the-dying.md). Gdy wydajesz 1 punkt skupienia, by użyć Cierpliwej obrony, masz premię +1 do KP do początku swojej następnej tury.

### Poziom 6: Tatuaż niebiański

Zyskujesz dodatkowy magiczny tatuaż przedstawiający zjawisko niebiańskie. Wybierz tatuaż z poniższych opcji.

**Kometa.** Gdy wykonujesz akcję Szukaj, możesz wydać 1 punkt skupienia, by rzucić swoją kością sztuk walki i dodać wyrzuconą wartość do testu Mądrości.

**Zaćmienie.** Gdy wykonujesz akcję Ukryj się, możesz wydać 1 punkt skupienia, by rzucić swoją kością sztuk walki i dodać wyrzuconą wartość do testu Zręczności (Skradanie się).

**Rozbłysk słońca.** Gdy wykonujesz akcję Badaj, możesz wydać 1 punkt skupienia, by rzucić swoją kością sztuk walki i dodać wyrzuconą wartość do testu Inteligencji.

### Poziom 11: Tatuaż natury

Zyskujesz dodatkowy magiczny tatuaż przedstawiający element natury. Wybierz tatuaż z poniższych opcji.

**Burza morska.** Zyskujesz odporność na jeden z następujących typów obrażeń według własnego wyboru: zimno, błyskawice albo grzmot. Za każdym razem, gdy kończysz Krótki lub Długi odpoczynek albo używasz cechy Niesamowity metabolizm, możesz zmienić ten wybór.

**Wulkan.** Zyskujesz odporność na jeden z następujących typów obrażeń według własnego wyboru: kwas, ogień albo trucizna. Za każdym razem, gdy kończysz Krótki lub Długi odpoczynek albo używasz cechy Niesamowity metabolizm, możesz zmienić ten wybór.

### Poziom 17: Tatuaż potwora

Zyskujesz magiczny tatuaż przedstawiający potężne stworzenie. Wybierz tatuaż z poniższych opcji.

**Obserwator.** Na początku swojej tury możesz wydać 1 punkt skupienia, by zyskać prędkość lotu równą swojej Szybkości na 10 minut. Dopóki masz tę prędkość lotu, możesz unosić się.

Ponadto akcją magiczną możesz wydać 1 punkt skupienia, by wystrzelić cztery promienie ze swoich oczu. Możesz wystrzelić je w jeden cel, który widzisz w promieniu 36 metrów, albo w kilka celów. Wykonaj test ataku czarem dystansowego dla każdego promienia, używając Mądrości jako cechy rzucania czarów. Przy trafieniu atak zadaje obrażenia od mocy równe jednemu rzutowi twojej kości sztuk walki plus twój modyfikator Mądrości.

**Smok chromatyczny.** Gdy w swojej turze podejmujesz akcję Atak, możesz wydać 1 punkt skupienia, by zastąpić jeden ze swoich ataków wydechem magicznej energii w stożku o długości 9 metrów. Wybierz typ obrażeń: kwas, zimno, ogień, błyskawice albo trucizna. Każda istota w tym obszarze wykonuje rzut obronny na Zręczność. Przy nieudanym rzucie istota otrzymuje obrażenia wybranego typu równe dwóm rzutom twojej kości sztuk walki plus twój modyfikator Mądrości. Przy udanym rzucie istota otrzymuje połowę tyle obrażeń.

**Bestia przesuwacza.** Gdy wydajesz punkt skupienia, by użyć Gradu ciosów albo Kroku w powietrzu, możesz wydać 1 punkt skupienia, by rzucić czar [Lustrzane odbicia](../spells/mirror-image.md) w ramach tej akcji dodatkowej.

**Troll.** Na początku każdej swojej tury odzyskujesz PW równe 5 plus twój modyfikator Mądrości, jeśli jesteś skrwawiony i masz co najmniej 1 PW. Każda odcięta część ciała odrasta po zakończeniu Krótkiego lub Długiego odpoczynku.
""",
}


def main():
    for name, content in FILES.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(FILES)} files (monk tattooed batch 65 part 1)")


if __name__ == "__main__":
    main()
