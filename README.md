# Konwerter Liczb: Dec na Hex (Rozwiązanie PP0504D)

## Opis
Projekt jest propozycją rozwiązania problemu algorytmicznego [SPOJ PP0504D](https://pl.spoj.com/problems/PP0504D/).
Program nie korzysta z wbudowanych funkcji formatowania (jak `hex()`), lecz implementuje **własny algorytm matematyczny** konwersji liczb zmiennoprzecinkowych z systemu dziesiętnego na szesnastkowy.

## Jak to działa?
Algorytm dzieli liczbę na część całkowitą i ułamkową:

1.  **Część całkowita:**
    * Jest iteracyjnie dzielona przez 16 (`// 16`).
    * Reszta z dzielenia (`% 16`) jest mapowana na cyfry szesnastkowe (0-9, A-F).
2.  **Część ułamkowa:**
    * Jest mnożona przez 16.
    * Część całkowita wyniku staje się kolejną cyfrą po przecinku.

## uruchomienie
Wymagany jest Python 3.

```bash
python main.py
