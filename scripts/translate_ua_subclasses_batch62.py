#!/usr/bin/env python3
"""Translate UA barbarian + bard subclasses (batch 62)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = ROOT / "dnd2024-wikidot-pl/ua"

FILES = {
    "subclass-barbarian-path-of-the-ancestral-guardian.md": """# Ścieżka Strażnika Przodków (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-barbarian-path-of-the-ancestral-guardian

---

Źródło: [UA10 — Aktualizacja podklas (30.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/subclasses-update)

*Wzywaj duchy na pomoc w walce*

Barbarzyńcy idący Ścieżką Strażnika Duchów wzywają duchy — bestialskie duchy natury, duchy zmarłych przodków albo duchy surowej mocy żywiołów — by ich prowadziły i chroniły. Gdy wpadają w Szał, kontaktują się z krainą duchów i proszą o pomoc.

### Poziom 3: Duchowi obrońcy

Twój Szał przywołuje widmowych wojowników na pomoc. Dopóki twój Szał jest aktywny, gdy trafisz istotę bronią lub uderzeniem bez broni, staje się celem duchów, które wywołują jeden z poniższych efektów według twojego wyboru.

**Rozproszenie.** Do początku twojej następnej tury cel ma utrudnienie do testów ataku przeciwko celom innym niż ty albo inny barbarzyńca z tą cechą.

**Ochrona.** Do końca następnej tury celu, gdy następnym razem trafi istotę inną niż ty testem ataku, ta istota ma odporność na obrażenia zadane tym atakiem.

**Uderzenie.** Cel otrzymuje dodatkowe 1k6 obrażeń — od kwasu, zimna, ognia, mocy, błyskawic lub grzmotu (według twojego wyboru).

### Poziom 6: Tarcza duchów

Twoje duchy obrończe mogą zapewniać nadnaturalną ochronę tym, których bronisz. Dopóki twój Szał jest aktywny, gdy inna istota, którą widzisz w promieniu 9 metrów od siebie, otrzymuje obrażenia, możesz wykorzystać reakcję, by je zmniejszyć. Aby określić, o ile zmniejszasz obrażenia, rzuć liczbą k6 równą twojej premii do obrażeń z Szału i dodaj wyniki.

### Poziom 10: Radzenie się z duchami

Zyskujesz zdolność konsultowania się ze swoimi duchami obrończymi. Gdy to robisz, rzucasz czar [Wróżba](../spells/augury.md) lub [Jasnowidzenie](../spells/clairvoyance.md) bez zużywania komórki czaru i bez komponentów materialnych.

Zamiast tworzyć kuliste czujniki, to użycie [Jasnowidzenia](../spells/clairvoyance.md) niewidocznie przywołuje jednego z twoich duchów obrończych w wybrane miejsce. Mądrość jest twoją cechą bazową rzucania czarów dla tych czarów.

Po rzuceniu któregoś z tych czarów w ten sposób nie możesz ponownie skorzystać z tej cechy, dopóki nie zakończysz Krótkiego lub Długiego odpoczynku.

### Poziom 14: Mściwe duchy

Gdy wykonujesz test ataku bronią do walki wręcz w ramach akcji Ataku i wyrzucisz 18–20 na K20, możesz wykonać jeden dodatkowy test ataku tą samą bronią w ramach tej akcji. Po użyciu tej cechy nie możesz zrobić tego ponownie do początku swojej następnej tury.
""",
    "subclass-barbarian-path-of-lament.md": """# Ścieżka Żałoby (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-barbarian-path-of-lament

---

Źródło: [UA13 — Złoczyńcze opcje 2 (23.04.2026)](https://www.dndbeyond.com/sources/dnd/ua/villainous-options-2)

*Przekształcaj gorzką rozpacz w nadnaturalny Szał*

Barbarzyńcy idący Ścieżką Żałoby ostrzą swoje żale w śmiertelne bronie i kierują najgłębszy smutek w szałowne działanie. Napędzani nadnaturalnym żalem, ich furia obdarza ich darami zza grobu.

Barbarzyńca może wybrać Ścieżkę Żałoby, lecz częściej droga ta zostaje mu wymuszona nieszczęsnym zbiegiem okoliczności. W sercu Szału barbarzyńcy tkwią wielka trauma i nierozwiązany żal — bolesne emocje podsycane przez prześladujące wspomnienia, które wypływają na powierzchnię w chwilach pełnych adrenaliny. Możesz rzucić lub wybrać wynik z tabeli Pochodzenie Ścieżki Żałoby, by zainspirować incydent będący korzeniem twojej rozpaczy.

### Pochodzenie Ścieżki Żałoby

| 1k6 | Twój Szał wypływa z czasu, gdy… |
| --- | --- |
| 1 | Utracona ukochana osoba powstała jako nieumarły potwór. |
| 2 | Wrogowie zabili twojego zwierzęcego towarzysza. |
| 3 | Uciekłeś (jako jedyny) od brutalnych oprawców. |
| 4 | Znalazłeś zwęglone szczątki swojej rodziny. |
| 5 | Twoja decyzja doprowadziła do katastrofalnego rozbicia statku. |
| 6 | Starsi wygnał cię z domu. |

### Poziom 3: Zawód banshee

Gdy aktywujesz Szał albo akcją dodatkową, dopóki Szał jest aktywny, możesz wydać żałosny zawód. Każda istota według twojego wyboru w promieniu 9 metrów wychodzącym od ciebie wykonuje rzut obronny na Kondycję (ST 8 plus twój modyfikator Kondycji i premia z biegłości). Przy nieudanym rzucie istota otrzymuje obrażenia psychiczne i ma stan ogłuszony przez 1 minutę. Przy udanym rzucie istota otrzymuje tylko połowę tyle obrażeń. Aby określić obrażenia psychiczne, rzuć liczbą k12 równą twojej premii do obrażeń z Szału i dodaj wyniki.

Możesz użyć tej cechy liczbę razy równą twojemu modyfikatorowi Kondycji (minimum raz). Odzyskujesz wszystkie zużyte użycia po zakończeniu Długiego odpoczynku. Możesz też odzyskać wszystkie użycia, wydając jedno użycie Szału (nie wymaga akcji).

### Poziom 6: Komunia z umarłymi

Możesz rzucić czar [Rozmawianie z umarłymi](../spells/speak-with-dead.md), ale tylko jako rytuał. Mądrość jest twoją cechą bazową rzucania czarów dla tego czaru.

### Poziom 6: Przerażające uderzenie

Raz na turę, gdy trafisz istotę testem ataku opartym na Sile, dopóki twój Szał jest aktywny, możesz spróbować przestraszyć cel. Cel musi odnieść sukces w rzucie obronnym na Mądrość (ST 8 plus twój modyfikator Kondycji i premia z biegłości), inaczej ma stan przerażony do początku twojej następnej tury.

### Poziom 10: Inświatowa udręka

Czerpiesz moc ze smutku tak głębokiego, że sięga poza granice krainy żywych. Zyskujesz następujące korzyści.

**Zawód śmierci.** Jeśli cel nie zda rzutu obronnego przeciwko twojemu Zawodowi banshee i ma PW równe co najwyżej podwójnemu twojemu poziomowi barbarzyńcy, spada do 0 PW zamiast otrzymywać obrażenia.

**Nieprzenikniony smutek.** Nie możesz zostać opętany.

**Odporność.** Dopóki twój Szał jest aktywny, masz odporność na obrażenia od zimna i nekrotyczne.

### Poziom 14: Forma żałoby

Gdy aktywujesz Szał, możesz wzmocnić siebie nieumarłością. Zyskujesz poniższe korzyści na 1 minutę albo dopóki nie spadniesz do 0 PW. Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku.

**Niewrażliwości.** Masz niewrażliwość na stany zauroczony i przerażony. Jeśli masz stan zauroczony lub przerażony w chwili wzmocnienia, stan kończy się na tobie. Ponadto nie możesz zyskiwać poziomów wyczerpania.

**Uderzenie wysysające życie.** Gdy istota nie zda rzutu obronnego przeciwko twojemu Przerażającemu uderzeniu, otrzymuje 2k10 obrażeń nekrotycznych. Odzyskujesz PW równe zadanym obrażeniom nekrotycznym.

**Nieumarły.** Twój typ istoty to nieumarły.
""",
    "subclass-barbarian-path-of-the-storm-herald.md": """# Ścieżka Herolda Burzy (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-barbarian-path-of-the-storm-herald

---

Źródło: [UA10 — Aktualizacja podklas (30.10.2025)](https://www.dndbeyond.com/sources/dnd/ua/subclasses-update)

*Władaj wściekłością burzy*

Barbarzyńcy idący Ścieżką Herolda Burzy uczą się kierować Szałem w płaszcz pierwotnej magii wirowej wokół nich jak burza. W Szałzie czerpią z żywiołowych sił natury, by tworzyć potężne efekty magiczne.

### Poziom 3: Aura burzy

Za każdym razem, gdy aktywujesz Szał, wybierz Pustynię, Morze albo Tundrę. Rozciągasz aurę w promieniu 3 metrów wychodzącym od siebie na czas trwania Szału.

Twoja aura ma efekt uruchamiany, gdy wchodzisz w Szał, i możesz aktywować efekt ponownie w każdej swojej turze akcją dodatkową. Efekt aury zależy od wybranego środowiska, jak opisano poniżej.

Jeśli efekt aury wymaga rzutu obronnego, ST wynosi 8 plus twoja premia z biegłości plus twój modyfikator Kondycji.

**Pustynia.** Gdy efekt się aktywuje, rzuć liczbą k4 równą twojej premii do obrażeń z Szału i dodaj wyniki. Każda istota w aurze musi odnieść sukces w rzucie obronnym na Zręczność albo otrzyma obrażenia od ognia równe wyrzuconej liczbie. Możesz wybrać jedną istotę, którą widzisz w aurze, by automatycznie zdała ten rzut obronny.

**Morze.** Gdy efekt się aktywuje, rzuć liczbą k6 równą twojej premii do obrażeń z Szału i dodaj wyniki. Następnie możesz miotnąć błyskawicę w inną istotę, którą widzisz w aurze. Cel wykonuje rzut obronny na Zręczność, otrzymując obrażenia od błyskawic równe wyrzuconej liczbie przy nieudanym rzucie albo połowę tyle przy udanym.

**Tundra.** Gdy efekt się aktywuje, rzuć liczbą k4 równą twojej premii do obrażeń z Szału i dodaj wyniki. Możesz wybrać inną istotę, którą widzisz w aurze, by nękały ją lodowe duchy. Cel musi odnieść sukces w rzucie obronnym na Siłę, inaczej odejmuje wyrzuconą liczbę od następnego rzutu obrażeń, który wykona przed początkiem twojej następnej tury.

### Poziom 6: Dusza burzy

Burza obdarza cię korzyściami nawet wtedy, gdy aura nie jest aktywna. Korzyści zależą od środowiska wybranego dla Aury burzy przy ostatnim wejściu w Szał.

**Pustynia.** Zyskujesz odporność na obrażenia od ognia. Akcją magiczną możesz dotknąć palnego przedmiotu, którego nikt nie nosi ani nie trzyma, i sprawić, że zacznie płonąć.

**Morze.** Zyskujesz odporność na obrażenia od błyskawic i możesz oddychać pod wodą. Zyskujesz też prędkość pływania równą swojej prędkości.

**Tundra.** Zyskujesz odporność na obrażenia od zimna. Akcją magiczną możesz dotknąć wody i zamienić sześcian o boku 1,5 metra w lód, który topi się po 1 minucie. Akcja kończy się niepowodzeniem, jeśli istota znajduje się w sześcianie.

### Poziom 10: Osłaniająca burza

Możesz używać mistrzostwa nad burzą, by chronić innych. Każda istota według twojego wyboru w twojej Aurze burzy ma odporność na obrażenia, którą zyskujesz z cechy Dusza burzy.

### Poziom 14: Szalejąca burza

Moc burzy, którą kierujesz, rośnie w siłę i biczuje wrogów. Efekt zależy od środowiska wybranego dla Aury burzy.

**Pustynia.** Raz na turę, gdy istota, którą widzisz, nie zda rzutu obronnego przeciwko efektowi Aury burzy, możesz sprawić, że zacznie płonąć przez 1 minutę albo dopóki twój Szał się nie skończy. Płonąca istota otrzymuje dodatkowe 1k4 obrażeń od ognia (łącznie 2k4 obrażeń od ognia) na początku każdej swojej tury.

**Morze.** Niezależnie od tego, czy cel zda, czy nie zda rzutu obronnego przeciwko efektowi Aury burzy, błyskawica skacze z celu do innego celu według twojego wyboru, który musi być w promieniu 9 metrów od pierwszego. Nowy cel wykonuje ten sam rzut obronny na Zręczność co pierwszy.

**Tundra.** Raz na turę, gdy istota, którą widzisz, nie zda rzutu obronnego przeciwko efektowi Aury burzy, możesz sprawić, że otrzyma 2k4 obrażeń od zimna, a jej prędkość jest zmniejszona o połowę do końca następnej tury.
""",
    "subclass-bard-college-of-spirits.md": """# Kolegium Duchów (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-bard-college-of-spirits

---

Źródło: [UA4 — Podklasy grozy (06.05.2025)](https://www.dndbeyond.com/sources/dnd/ua/horror-subclasses)

*Przywołuj duchy zza grobu*

Za pomocą okultystycznych rekwizytów bardzi Kolegium Duchów przywołują legendarne i dawno zmarłe duchy, by zmieniać świat. Takie istoty są jednak kapryśne, a to, co bard przywołuje, nie zawsze w pełni podlega jego kontroli.

### Poziom 3: Kanał

Uczysz się kontaktować z duchami zza grobu, pozwalając, by ich moc i wiedza przepływały przez ciebie. Zyskujesz następujące korzyści.

**Prowadzące szepty.** Znasz sztuczkę [Wskazówki](../spells/guidance.md). Gdy ją rzucasz, ma zasięg 18 metrów.

**Duchowe skupienie.** Używasz narzędzi, które pomagają ci kanałować duchy. Zyskujesz zestaw do gier (karty do gry). Masz w nim biegłość i możesz używać kart albo jednego z następujących przedmiotów jako magicznego fokusu do czarów barda: skupienie arkaniczne (kryształ lub kula), świeca lub pióro.

### Poziom 3: Duchy zza grobu

Trzymając magiczny fokus, możesz wykonać akcję dodatkową, by wydać jedno użycie kości Bardowskiej inspiracji i wezwać moc ducha.

Rzuć kością Bardowskiej inspiracji i sprawdź tabelę Duchy zza grobu, by określić skanalizowany duch. Następnie wybierz jedną istotę, którą widzisz w promieniu 9 metrów od siebie, jako cel ducha.

Efekt ducha występuje natychmiast. Jeśli efekt ducha wymaga rzutu obronnego, ST wynosi ST twoich czarów.

### Duchy zza grobu

| Kość BI | Duch |
| --- | --- |
| 1 | **Ukochany.** Cel odzyskuje PW równe jednemu wyrzuceniu kości Bardowskiej inspiracji plus twój modyfikator Charyzmy. |
| 2 | **Strzelec wyborowy.** Cel otrzymuje obrażenia od mocy równe wyrzuceniu kości Bardowskiej inspiracji plus twój modyfikator Charyzmy. |
| 3 | **Mściciel.** Do końca twojej następnej tury każda istota, która trafi cel testem ataku w walce wręcz, otrzymuje obrażenia od mocy równe wyrzuceniu kości Bardowskiej inspiracji. |
| 4 | **Renegat.** Cel może natychmiast wykorzystać reakcję, by teleportować się na odległość do 9 metrów do niezajętej przestrzeni, którą widzi. |
| 5 | **Wróżbita.** Cel ma ułatwienie do testów K20 do początku twojej następnej tury. |
| 6 | **Wędrowiec.** Cel zyskuje tymczasowe PW równe wyrzuceniu kości Bardowskiej inspiracji plus twój poziom barda. Dopóki ma te tymczasowe PW, jego prędkość wzrasta o 3 metry. |
| 7 | **Sztukmistrz.** Cel wykonuje rzut obronny na Mądrość. Przy nieudanym rzucie cel otrzymuje obrażenia psychiczne równe dwóm wyrzuceniom kości Bardowskiej inspiracji i ma stan zauroczony do początku twojej następnej tury. Przy udanym rzucie cel otrzymuje tylko połowę tych obrażeń. |
| 8 | **Cień.** Cel uzyskuje stan niewidzialny do końca swojej następnej tury albo do momentu, gdy wykona test ataku, zada obrażenia lub rzuci czar. Gdy niewidzialność się kończy, każda istota w promieniu 1,5 metra wychodzącym od celu musi odnieść sukces w rzucie obronnym na Kondycję albo otrzyma obrażenia nekrotyczne równe dwóm wyrzuceniom kości Bardowskiej inspiracji. |
| 9 | **Podpalacz.** Cel wykonuje rzut obronny na Zręczność, otrzymując obrażenia od ognia równe czterem wyrzuceniom kości Bardowskiej inspiracji przy nieudanym rzucie albo połowę tyle przy udanym. |
| 10 | **Tchórz.** Cel i każda istota według twojego wyboru w promieniu 9 metrów wychodzącym od celu muszą odnieść sukces w rzucie obronnym na Mądrość albo mają stan przerażony do początku twojej następnej tury. Dopóki istota ma stan przerażony, jej prędkość jest zmniejszona o połowę i może wykonać albo akcję, albo akcję dodatkową, nie obie. |
| 11 | **Brutal.** Każda istota według twojego wyboru w promieniu 9 metrów wychodzącym od celu wykonuje rzut obronny na Siłę. Przy nieudanym rzucie istota otrzymuje obrażenia od grzmotu równe trzem wyrzuceniom kości Bardowskiej inspiracji i ma stan powalony. Przy udanym rzucie istota otrzymuje tylko połowę tych obrażeń. |
| 12 | **Kontrolowane kanałowanie.** Określasz efekt ducha, wybierając jeden z pozostałych wierszy tej tabeli. |

### Poziom 6: Wzmocnione kanałowanie

Twoja zdolność kanałowania duchów się poprawia. Zyskujesz następujące korzyści.

**Moc zza grobu.** Raz na turę, gdy rzucasz czar barda, który zadaje obrażenia albo przywraca PW, rzuć 1k6. Zyskujesz premię równą wyrzuconej liczbie do jednego z rzutów obrażeń czaru albo do łącznej liczby PW przywracanych przez czar.

**Duchowa manifestacja.** Zawsze masz przygotowany czar [Duchowi strażnicy](../spells/spirit-guardians.md). Możesz rzucić ten czar raz bez komórki czaru i odzyskujesz możliwość takiego rzucenia po zakończeniu Długiego odpoczynku.

Za każdym razem, gdy rzucasz ten czar, możesz go zmodyfikować tak, by duchy strzegły również przed zagrożeniami ze świata materialnego. Gdy rzucasz czar w ten sposób, ty i sojusznicy w emanacji czaru macie połowę osłony. Po zmodyfikowaniu czaru w ten sposób nie możesz zrobić tego ponownie, dopóki nie zakończysz Krótkiego lub Długiego odpoczynku.

### Poziom 14: Mistyczne połączenie

Zyskujesz mistrzostwo nad duchami, które przywołujesz. Za każdym razem, gdy rzucasz na tabeli Duchy zza grobu, możesz rzucić kością Bardowskiej inspiracji dwa razy i wybrać jeden z dwóch efektów.
""",
    "subclass-bard-college-of-the-moon.md": """# Kolegium Księżyca (UA)

**URL źródła:** http://dnd2024.wikidot.com/ua:subclass-bard-college-of-the-moon

---

Źródło: [UA — Podklasy Zapomnianych Krain (28.01.2025)](https://www.dndbeyond.com/sources/dnd/ua/forgotten-realms-subclasses)

*Inspiruj sojuszników pierwotnymi opowieściami*

Kolegium Księżyca wywodzi swoje początki od starożytnych kręgów druidów Wysp Księżyca, którzy powierzyli pierwszym bardom tej tradycji spisywanie opowieści o wyspach i ich mieszkańcach. Bardzi tego kolegium czerpią z magii feów wysp i pierwotnej mocy księżycowych studni, by wzmacniać sojuszników, chronić świat natury i inspirować swoje dzieła.

Takie dzieła opierają się zwykle na znanych mitach Wysp Księżyca — np. o kaprysach feowych psotników, okrucieństwie Bestii i tajemnicach księżycowych studni.

### Poziom 3: Bajki Wysp Księżyca

Akcją magiczną możesz wezwać moc baśni, napełniając siebie pierwotną magią, dopóki nie użyjesz tej cechy ponownie. Gdy korzystasz z tej cechy, wybierz jedną z poniższych baśni; wybór daje określone korzyści, dopóki magia trwa.

**Baśń o życiu.**

Wzywasz opowieść o witalności i kwitnącej ziemi. Gdy przywracasz PW istocie czarem, możesz wydać kość Bardowskiej inspiracji i zwiększyć liczbę przywróconych PW o wartość równą wyrzuceniu kości Bardowskiej inspiracji. Możesz to zrobić tylko raz na turę.

**Baśń o zmierzchu.**

Wzywasz opowieść o tajemnicy i sekretach. Gdy wykonujesz akcję dodatkową, by dać istocie kość Bardowskiej inspiracji, możesz w ramach tej akcji dodatkowej wykonać akcję Odwrót albo Ukrycie.

**Baśń o weselu.**

Wzywasz opowieść o radości i feowej przebiegłości. Gdy wróg, którego widzisz w promieniu 18 metrów od siebie, odniesie sukces w rzucie obronnym, możesz wykorzystać reakcję, by wydać kość Bardowskiej inspiracji i odjąć wyrzuconą liczbę od wyniku rzutu, co może sprawić, że rzut się nie powiedzie.

### Poziom 3: Pierwotna wiedza

Uczysz się języka druidzkiego i jednej sztuczki z listy czarów druida. Liczy się ona jako czar barda, ale nie wlicza się do liczby znanych ci sztuczek.

Dodatkowo wybierz jedną z następujących umiejętności: Obsługa zwierząt, Intuicja, Medycyna, Natura, Percepcja lub Sztuka przetrwania. Masz w niej biegłość.

### Poziom 6: Błogosławieństwo księżycowych studni

Zawsze masz przygotowany czar [Księżycowy promień](../spells/moonbeam.md).

Akcją dodatkową możesz rzucić [Księżycowy promień](../spells/moonbeam.md) bez zużywania komórki czaru. Gdy rzucasz go tą cechą, słabo świeć, dopóki utrzymujesz koncentrację na czarze. Dopóki świeć, emitujesz przyćmione światło w promieniu 1,5 metra, a za każdym razem, gdy istota nie zda rzutu obronnego przeciwko efektom tego Księżycowego promienia, inna istota według twojego wyboru, którą widzisz w promieniu 18 metrów od siebie, odzyskuje 2k4 PW.

Po użyciu tej cechy nie możesz zrobić tego ponownie, dopóki nie zakończysz Długiego odpoczynku. Możesz też odzyskać użycie, wydając komórkę czaru 3. kręgu lub wyższego (nie wymaga akcji).

### Poziom 14: Wzmocnione bajki

Moc twoich Bajek Wysp Księżyca rośnie. Gdy używasz Baśni o życiu albo Baśni o weselu, możesz rzucić 1k6 i użyć wyrzuconej liczby zamiast wydawania kości Bardowskiej inspiracji. Gdy używasz Baśni o zmierzchu, możesz też teleportować się na odległość do 9 metrów do niezajętej przestrzeni, którą widzisz, w ramach tej samej akcji dodatkowej.
""",
}


def main():
    for name, content in FILES.items():
        (UA / name).write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {len(FILES)} UA subclass files")


if __name__ == "__main__":
    main()
