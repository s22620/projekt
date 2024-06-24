# Data Analysis Project

## Opis Projektu
Ten projekt ma na celu demonstrację analizy danych przy użyciu bibliotek NumPy, Pandas, Matplotlib i Seaborn. Analizujemy dane dotyczące wynagrodzeń w różnych zawodach technologicznych.

## Struktura Projektu
- `data/`: Katalog zawierający dane wejściowe
- `src/`: Katalog zawierający kod źródłowy
- `src/tests/`: Katalog zawierający testy jednostkowe
- `requirements.txt`: Plik z wymaganymi bibliotekami
- `README.md`: Plik z dokumentacją projektu

## Jak Uruchomić Projekt
1. Sklonuj repozytorium.
2. Zainstaluj zależności:
    ```bash
    pip install -r requirements.txt
    ```
3. Uruchom główny plik:
    ```bash
    python src/main.py
    ```

## Uzasadnienie Metod

### Metody Analizy Danych
- `describe()`: Generuje podstawowe statystyki opisowe, takie jak średnia, mediana, odchylenie standardowe itp., które są przydatne do zrozumienia ogólnej charakterystyki danych.
- `factorize()`: Konwertuje dane kategoryczne na numeryczne, co jest przydatne do analizy ilościowej.

### Wizualizacje
- Histogram: Dobrze obrazuje rozkład danych. Używany do wizualizacji rozkładu wynagrodzeń.
- Scatter plot: Pokazuje zależności między dwiema zmiennymi. Używany do analizy zależności między doświadczeniem a wynagrodzeniem.

## Struktura Kodu
- `DataLoader`: Klasa do ładowania danych.
- `DataAnalysis`: Klasa do przeprowadzania analizy danych.
- `DataVisualization`: Klasa do wizualizacji danych.

### Testowanie
Testy jednostkowe znajdują się w `src/tests/test_data_analysis.py`.
