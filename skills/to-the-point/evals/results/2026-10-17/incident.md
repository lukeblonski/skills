# Rozmowa

## Użytkownik

Pomóż mi uporządkować koncepcję autonomicznego narzędzia do naprawiania incydentów produkcyjnych. W ramach przyznanych uprawnień samo diagnozuje problem, przygotowuje i wdraża naprawę, obserwuje rezultat i informuje operatora. Ma polecenie stop i ścieżkę odzyskania działania, ale nie obiecuję, że cofnie każdy skutek zewnętrzny. Ma też poprawiać swoje instrukcje na podstawie wyników. Nie chcę każdorazowych akceptacji operatora. Wczoraj wygenerowało MR z naprawą, który czeka na review, oraz dopisało wnioski do pliku; ktoś nazwał to dowodem, że «naprawiło produkcję i nauczyło się unikać błędu». Ja nie wiem, czy to trafne. Chcę krótki koncept, bez architektury i implementacji.

## Asystent

:::writing{variant="standard" id="82461"}
Narzędzie pomaga operatorowi przywracać prawidłowe działanie produkcji bez ręcznego prowadzenia każdej naprawy. W ramach przyznanych uprawnień samodzielnie diagnozuje incydent, przygotowuje i wdraża naprawę, obserwuje jej rezultat oraz informuje operatora o wyniku. Przygotowanie zmiany jest etapem pracy; zakończeniem naprawy jest potwierdzone przywrócenie oczekiwanego działania.

Operator określa granice samodzielności narzędzia i może zatrzymać jego dalsze działania, ale nie akceptuje każdego kroku. Produkt zapewnia ścieżkę odzyskania działania po nieudanej interwencji, bez obietnicy cofnięcia wszystkich skutków zewnętrznych. Informuje też, gdy naprawa się nie powiodła lub jej wynik pozostaje niepewny.

Narzędzie wykorzystuje rzeczywiste wyniki do samodzielnego poprawiania swoich instrukcji. Zapisany wniosek jest kandydatem na ulepszenie; dopiero skuteczniejsze działanie w kolejnych przypadkach daje dowód poprawy. Kryteria oceny pozostają niezależne od zmienianych instrukcji, a nieskuteczne zasady można uprościć lub usunąć.
:::

Wczorajszy wynik potwierdza **przygotowanie MR do review i zapisanie wniosków**. Nie potwierdza wdrożenia skutecznej naprawy ani nauczenia się unikania błędu. Do doprecyzowania pozostaje, po czym i po jakim czasie obserwacji uznajecie produkcję za przywróconą do prawidłowego działania.
