#!/usr/bin/env python3
"""Translate UA fighter subclasses (batch 64)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"

FILES = {
    "subclass-fighter-cavalier.md": """# Kawaler (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-fighter-cavalier

---

Źródło: [UA10 — Aktualizacja podklas (30.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/subclasses-update)

*Broń sojuszników pieszo albo z konia*

Kawalerowie wyróżniają się walką konną i strzegą tych, którzy im powierzono — często chroniąc przełożonych i słabszych. Kawaler czuje się równie dobrze na czele szarży kawalerii, jak i wymieniając repartee podczas uroczystej kolacji.

### Poziom 3: Dodatkowa biegłość

Zyskujesz biegłość w jednej z następujących umiejętności według własnego wyboru: Opieka nad zwierzętami, Historia, Intuicja, Występy albo Perswazja. Alternatywnie uczysz się jednego języka według własnego wyboru.

### Poziom 3: Urodzony w siodle

Masz ułatwienie w rzutach obronnych wykonywanych, by uniknąć spadnięcia z wierzchowca. Jeśli spadniesz z wierzchowca i opadniesz nie więcej niż 3 metry, możesz wylądować na nogach, o ile nie masz stanu obezwładniony.

Ponadto wsiadanie na istotę albo zsiadanie z niej kosztuje cię tylko 1,5 metra ruchu, a nie połowę Szybkości.

### Poziom 3: Niezachwiana piętna

Możesz grozić wrogom, udaremniając ich ataki i karząc za krzywdzenie innych. Gdy trafisz istotę bronią do walki wręcz, możesz oznaczyć ją piętną do końca swojej następnej tury. Efekt kończy się wcześniej, jeśli masz stan obezwładniony, jeśli umrzesz albo jeśli ktoś inny oznaczy tę istotę.

Dopóki oznaczona przez ciebie istota znajduje się w promieniu 1,5 metra od ciebie, ma utrudnienie w testach ataku przeciwko istotom innym niż ty.

Ponadto, jeśli istota oznaczona przez ciebie trafi testem ataku istotę inną niż ty, masz ułatwienie w testach ataku przeciwko oznaczonej istocie do końca swojej następnej tury.

### Poziom 7: Manewr ochronny

Uczysz się odbijać ciosy skierowane w ciebie, twój wierzchowiec albo inne istoty w pobliżu. Jeśli ty albo istota, którą widzisz w promieniu 1,5 metra od siebie, zostaniecie trafieni testem ataku, możesz rzucić 1k8 reakcją, o ile dzierżysz broń do walki wręcz albo tarczę. Rzuć kością i dodaj wyrzuconą wartość do KP celu wobec wyzwalającego ataku. Jeśli atak i tak trafi, cel ma odporność na obrażenia z tego ataku.

Możesz użyć tej cechy liczbę razy równą twojemu modyfikatorowi Kondycji (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku.

### Poziom 10: Trzymaj linię

Istoty prowokują od ciebie atak okazji, gdy poruszają się o 1,5 metra lub więcej będąc w twoim zasięgu. Gdy trafisz istotę atakiem okazji, jej Szybkość spada do 0 do końca bieżącej tury.

### Poziom 15: Dziki szarżowicz

W pierwszej rundzie każdej walki twoja Szybkość i Szybkość twojego wierzchowca wzrastają o 3 metry, a twój ruch nie prowokuje ataków okazji przez tę rundę. Gdy w tej rundzie poruszasz się w promień 1,5 metra od istoty, ta istota musi odnieść sukces w rzucie obronnym na Siłę (ST 8 plus twój modyfikator Siły i premia z biegłości) albo albo odepchniesz ją o 1,5 metra, albo nadasz jej stan powalony. Istota wykonuje ten rzut tylko raz w turze.

### Poziom 18: Czujny obrońca

W walce zyskujesz specjalną reakcję, którą możesz wykorzystać raz w turze każdej istoty oprócz swojej. Możesz wykorzystać tę reakcję wyłącznie, by wykonać atak okazji, i nie możesz tego zrobić w tej samej turze, w której wykorzystujesz normalną reakcję.
""",
    "subclass-fighter-gladiator.md": """# Gladiator (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-fighter-gladiator

---

Źródło: [UA7 — Apokaliptyczne podklasy (21.08.2025)](https://www.dndbeyond.com/sources/dnd/ua/apocalyptic-subclasses)

*Opanuj brutalność i krwawy spektakl*

Gladiatorzy są równie mocno wykonawcami, co wojownikami. Niezależnie od tego, czy walczą w podziemnych ringach, czy o życie na skrwawionych arenach, łączą umiejętności bojowe z teatralnością, by olśniewać i zastraszać widownię.

### Poziom 3: Brutalność

Ukształtowany intensywnością areny, nauczyłeś się wykonywać brutalne zagrania bojowe. Raz na turę, gdy trafisz istotę testem ataku używając broni do walki wręcz, możesz dodać jeden z poniższych efektów Brutalności według własnego wyboru. Możesz to zrobić liczbę razy równą twojemu modyfikatorowi Charyzmy (minimum raz) i odzyskujesz wszystkie zużyte użycia po zakończeniu Krótkiego lub Długiego odpoczynku.

**Krwawienie.** Możesz aktywować właściwość mistrzowską Osłabienie oprócz innej właściwości mistrzowskiej używanej z tą bronią, a cel otrzymuje dodatkowe obrażenia równe twojemu modyfikatorowi Charyzmy (minimum 1 obrażenia). Typ dodatkowych obrażeń jest taki sam jak typ obrażeń broni.

**Blef.** Możesz aktywować właściwość mistrzowską Nękanie oprócz innej właściwości mistrzowskiej używanej z tą bronią, i masz ułatwienie w następnym rzucie obronnym, który wykonasz przed końcem swojej następnej tury.

**Potknięcie.** Możesz aktywować właściwość mistrzowską Obalenie oprócz innej właściwości mistrzowskiej używanej z tą bronią, a w swojej następnej turze cel może wykonać tylko akcję albo akcję dodatkową, nie obie.

### Poziom 3: Teatralność bojowa

Doskonaliłeś umiejętności bojowe pod kątem widowiska, niszcząc przeciwników i olśniewając widzów. Zyskujesz następujące korzyści.

**Atletyczna finezja.** Za każdym razem, gdy wykonujesz test Zręczności (Akrobatyka) albo Siły (Atletyka), zyskujesz premię do testu równą twojemu modyfikatorowi Charyzmy (minimum +1).

**Dodatkowa biegłość.** Zyskujesz biegłość w jednej z następujących umiejętności według własnego wyboru: Akrobatyka, Atletyka, Oszustwo, Zastraszanie albo Występy.

### Poziom 7: Parada z finezją

Nauczyłeś się stylowo parować ciosy przeciwników. Gdy wróg trafi cię testem ataku wręcz, możesz wykorzystać reakcję, by dodać swój modyfikator Charyzmy (minimum +1) do KP wobec tego ataku, co może sprawić, że atak chybi.

**Kontratak z finezją.** Jeśli ta reakcja sprawi, że atak chybi, możesz w ramach tej samej reakcji odpowiedzieć potężnym kontratakiem. Wykonaj test ataku bronią do walki wręcz przeciwko wyzwalającej istocie. Jeśli ten atak trafi, możesz użyć jednego efektu Brutalności na celu bez zużywania użycia tej cechy.

Gdy ten kontratak trafi, nie możesz użyć tej cechy do kolejnego kontrataku, dopóki nie zakończysz Długiego odpoczynku. Możesz też odzyskać użycie tego kontrataku, wydając użycie Drugiego oddechu (bez wymaganej akcji).

### Poziom 10: Odważniejsze brutalności

Twoja brutalna sprawność bojowa się poprawiła. Do opcji Brutalności dodano następujące efekty.

**Rozerwanie.** Możesz aktywować właściwość mistrzowską Szerokie cięcie oprócz innej właściwości mistrzowskiej używanej z tą bronią, i możesz dodać modyfikator z cechy do obrażeń dodatkowego ataku wykonanego w ramach aktywacji tej właściwości.

**Szarża.** Możesz aktywować właściwość mistrzowską Popchnięcie oprócz innej właściwości mistrzowskiej używanej z tą bronią, i możesz natychmiast przemieścić się o swoją Szybkość bez prowokowania ataków okazji.

**Zatoczenie.** Możesz aktywować właściwość mistrzowską Spowolnienie oprócz innej właściwości mistrzowskiej używanej z tą bronią, a cel ma utrudnienie w następnym rzucie obronnym, który wykona przed końcem twojej następnej tury.

### Poziom 15: Brutalne odrodzenie

Za każdym razem, gdy używasz Drugiego oddechu, by odzyskać PW, odzyskujesz też jedno zużyte użycie Brutalności. Odzyskujesz też jedno zużyte użycie Brutalności za każdym razem, gdy używasz Przypływu sił.

### Poziom 18: Okaleczenie

Gdy trafisz skrwawioną istotę testem ataku, możesz spróbować krytycznie ją okaleczyć. Cel wykonuje rzut obronny na Kondycję (ST 8 plus twój modyfikator Charyzmy i premia z biegłości). Przy nieudanym rzucie cel cierpi z następujących efektów:

**Okaleczony.** Jeśli cel podejmuje akcję Atak, może wykonać tylko jeden atak.

**Ospały.** Szybkość celu jest zmniejszona o połowę, a jego Klasa Pancerza ma karę −2.

Efekty trwają, dopóki cel nie odzyska PW. Gdy cel nie zda swojego rzutu obronnego przeciwko tej cesze, nie możesz użyć jej ponownie, dopóki nie zakończysz Długiego odpoczynku.
""",
}


def main():
    for name, content in FILES.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(FILES)} files (fighter batch 64 part 1)")


if __name__ == "__main__":
    main()
