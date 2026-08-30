# Pomysły na dalszy rozwój tego programu

## 1

## feature/analysis-and-result

Mogę rozszerzyć moduł z analizą o dodatkowe metody w text_analyzer, np.:

- `unique_word_count: int`
- `longest_word: str | None`
- `average_word_length: float`
- `most_common_words: list[tuple[str, int]]`

oczywiście z testami do każdej z metod.

## 2

- Dodać klasę `TextReport` w paczce analysis:
  - przechowanie podsumowania wszystkich statystyk w jednym obiekcie

`TextReport`:

- `word_count: int`
- `sentence_count: int`
- `unique_word_count: int`
- `longest_word: str | None`
- `average_word_length: float`
- `most_common_words: list[tuple[str, int]]`

- Klasa `TextAnalyzer`:
  - `analyze_all()` metoda zwróci gotowy obiekt `TextReport`

## 3

- Zapis danych z `TextReport` do pliku (najpewniej w jeszcze jednej paczce `report`).
