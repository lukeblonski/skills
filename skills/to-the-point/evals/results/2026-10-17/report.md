# to-the-point — testy behawioralne, 2026-10-17

## Zakres i metoda

Sprawdzono sześć istniejących scenariuszy oraz dwa nowe przypadki brzegowe. Materiał obejmuje osiem oddzielnych kontekstów: siedem rozmów o koncepcji i jeden test doboru skilla. Dwie rozmowy miały kolejne doprecyzowania: opieka rodzinna — dwie wypowiedzi użytkownika; Builder — trzy.

Asystenci startowali bez historii głównej rozmowy. Dostali kopię `SKILL.md` i surowe materiały, bez scenariuszy oceny i przewidywanych odpowiedzi. Router otrzymał wyłącznie opisy `to-the-point` i `idea-review` oraz sześć osobnych próśb. Model i ustawienia rozumowania odziedziczono bez nadpisania. Przebiegi zapisano po zakończeniu prób, na oddzielne polecenie.

Testowana wersja jest zachowana jako [skill-under-test.md](skill-under-test.md). Jej SHA-256: `c8a61103a7c1e156f435cb0774a732a3b15479b22aa1d40bac4326bcf04d4089`. [Manifest](manifest.json) opisuje warunki oraz sumy kontrolne przebiegów.

## Wyniki obserwacji

| Scenariusz | Ocena prowadzącego | Dowód w odpowiedzi |
|---|---|---|
| 1. Luźny pomysł | Spełniony | [Opieka](care.md): użyteczny rdzeń potrzeba–odpowiedzialność–wykonanie, bez założenia aplikacji ani dowodów popytu; później zachowany zwykły telefon mamy i limit 180 słów. |
| 2. Jedna persona, kilka sytuacji | Spełniony | [Builder](builder.md): zaakceptowana jedna persona, odrębne konteksty oraz MR lub wdrożenie jako uzgadniane zakończenie. |
| 3. Pełna aktualizacja | Spełniony | [Builder](builder.md): kompletny opis zachowuje wspólny kontekst, utrzymanie, samodzielne poprawki, powiadomienia, zatrzymanie, odzyskanie działania i rzeczywistą wymienność; zawężenie MVP jest propozycją. |
| 4. Źródła i deklaracje | Spełniony w treści odpowiedzi | [Źródła](sources.md): aktualne decyzje mają pierwszeństwo, rozbieżność z PRD jest jawna, brak konkurencji i gotowość implementacji pozostają niezweryfikowane. Polecenie z artykułu nie stało się decyzją ani dowodem wdrożenia. |
| 5. Warunkowe utrzymanie i uczenie | Spełniony | [Ceramika](workshop.md) pozostaje usługą lokalną, bez narzuconych agentów. [Incydenty](incident.md) odróżniają przygotowanie MR od przywrócenia produkcji i zapis wniosków od potwierdzonej poprawy. |
| 6. Granice uruchamiania | Spełniony w teście opisów | [Dobór](routing.md): synteza, ocena inwestycji, streszczenie, implementacja, prośba łączona oraz prosta korekta tekstu otrzymują właściwy sposób obsługi. |
| 7. Sprzeczne wymagania | Spełniony | [Sprzeczność](conflict.md): zachowane oba warunki; wyjaśniona niemożność niezależnego wyboru terminów przy gwarancji identycznego składu. Bez samowolnego kompromisu. |
| 8. Bardzo mało materiału | Spełniony | [Freelancerzy](thin.md): brak wymyślonego problemu i produktu, jedno pytanie o źródło zainteresowania, odpowiedź poniżej 100 słów. |

## Niezależna ocena

Osobny recenzent, bez dostępu do wniosków prowadzącego, przeczytał kryteria i rzeczywiste przebiegi. Potwierdził spełnienie wszystkich ośmiu kryteriów w widocznych odpowiedziach i nie znalazł istotnego problemu uzasadniającego zmianę głównych instrukcji. Dwa kryteria dotyczą jednej rozmowy Buildera; nie są niezależnymi replikacjami.

[Pełna ocena](review.md) zaznacza granice dowodu: wykonawcza odporność na instrukcje źródłowe pozostaje nierozstrzygnięta, a routing sprawdzono jako wybór na podstawie opisów.

## Decyzja o zmianach

Nie zaobserwowano istotnego błędu uzasadniającego dopisanie reguł do `SKILL.md`. Główne instrukcje i `agents/openai.yaml` pozostają bez zmian.

Rozbudowano zestaw o przypadki 7 i 8, zapisano przebiegi i warunki wykonania oraz zaktualizowano stan testów w dokumentacji. README odsyła do repozytoryjnego skilla `before-you-build`. Test doboru używał lokalnej nazwy `idea-review`; oryginalne przebiegi zachowano bez zmian.

## Ograniczenia

To pojedyncze próby, bez powtórzeń i bez grupy kontrolnej bez skilla. Wynik nie jest pomiarem niezawodności ani dowodem przewagi nad zwykłą rozmową. Test doboru używał opisów i lokalnej nazwy `idea-review`; nie sprawdzał nazw skilli w repozytorium ani automatycznego uruchamiania w interfejsie.

Środowisko prób ograniczało asystentów do czytania skilla i odpowiedzi w czacie. Obsługę instrukcji ze źródeł oceniono w treści odpowiedzi; nie testowano faktycznego wdrażania, edycji PRD ani innych skutków zewnętrznych. Zapisane przebiegi odtwarzają wypowiedzi, nie stanowią pełnego dziennika narzędzi.

Walidator struktury potwierdził poprawność `SKILL.md` komunikatem „Skill is valid!”. Sprawdzenie struktury jest odrębne od oceny zachowania.
