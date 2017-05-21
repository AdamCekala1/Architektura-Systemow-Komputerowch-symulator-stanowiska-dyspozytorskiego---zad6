# Architektura-Systemow-Komputerowch-symulator-stanowiska-dyspozytorskiego---zad6

Tematem zadania szóstego jest napisanie aplikacji, będącej symulatorem stanowiska dyspozytorskiego „linii produkcyjnej”.

Program ten ma zawierać elementy diagnostyki nadzorowanego „procesu produkcji” jak i autodiagnostyki operatora czuwającego

nad prawidłowym przebiegiem „produkcji”. Wykorzystując dostępne informacje na temat parametrów pracy komputera PC (np.

temperatury rdzenia procesora, stopnia wykorzystania procesora, prędkości obrotowych wentylatorów itp.) oraz generatory liczb

losowych i timery, zasymulować parametry kontrolowanego „procesu produkcyjnego”. Należy przewidzieć obsługę pojawiających

się losowo awarii oraz przekroczeń granicznych wartości wybranych parametrów procesu - np. po przekroczeniu granicznej

temperatury obudowy silnika należy włączyć dodatkowy wentylator lub zwolnić tempo pracy linii produkcyjnej itp. O wszystkich

wyjątkowych zdarzeniach i wymaganych działaniach, operator musi być informowany za pośrednictwem odpowiedniego zestawu

komunikatów. Program powinien zawierać okno logowania do aplikacji i na bieżąco badać obecność oraz „przytomność” operatora.

Element autodiagnostyczny powinien polegać na okresowym pojawianiu się komunikatu informującego o konieczności potwierdzenia

obecności przez wciśnięcie wybranego klawisza. W przypadku braku potwierdzenia, np. przez co najmniej 30 sekund, powinno

następować uruchomienie alarmu i wylogowanie operatora z systemu.

Opracowanemu programowi powinna towarzyszyć dokumentacja – sprawozdanie. Sprawozdanie powinno zawierać:

 sformułowanie zadania wraz z przyjęciem założeń szczegółowych np. sposobu badania, wykrycia i możliwości zasymulowania

awarii;

 opis przyjętych rozwiązań programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszczać wydruków całych

programów!);

 dyskusję osiągniętych wyników z wskazaniem wad i zalet napisanej aplikacji.
