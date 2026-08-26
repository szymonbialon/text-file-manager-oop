# Pomysł na uogólnienie klasy

Obecnie `TextFileManager` robi kilka rzeczy naraz:
- zna ścieżkę do pliku,
- czyta plik,
- zapisuje plik,
- dopisuje tekst,
- liczy słowa,
- liczy zdania.


# 1  Done
Pierwszy pomysł na uogólnienie to **oddzielenie operacji na pliku od analizy tekstu**.

Analiza tekstu nie musi być na stałe związana z plikiem, bo ten sam tekst może 
pochodzić z różnych źródeł, na przykład:
- z pliku,
- z tekstu wpisanego ręcznie,
- z bazy danych,

Dlatego można rozważyć podział na dwie role:

- `TextFileManager` - odpowiada za odczyt i zapis tekstu w pliku,
- `TextAnalyzer` - odpowiada za analizę dowolnego tekstu.

W takim podejściu `TextFileManager` mógłby korzystać z `TextAnalyzer`, 
ale sama analiza tekstu nie byłaby przywiązana do pliku.


# 2 Done
Na dalszym etapie można też rozważyć typy generyczne w `TextFileManager`, ale raczej dopiero wtedy, 
gdy klasa miałaby obsługiwać nie tylko zwykły tekst, ale też inne formaty danych i zwracać różne typy wyników, 
np. `str` dla tekstu, `dict` dla JSON albo listę rekordów dla CSV.

# Kolejne pomysły na rozwój skryptu 

# 3
## feature/text-cleaning
- Klasa `TextCleaner` lub metody w `TextAnalyzer`:
  - `_clean_words()`
  - `remove_extra_whitespace()`

# 4
## feature/text-statistics
- Klasa `TextAnalyzer`:
  - `count_unique_words()`
  - `get_longest_word()`
  - `get_average_word_length()`
  - `get_most_common_words()`

# 5
## feature/analysis-result
- Klasa `TextReport`:
  - przechowanie podsumowania wszystkich statystyk w jednym obiekcie i zapis do pliku
- Klasa `TextAnalyzer`:
  - `analyze_all()` (zwraca gotowy obiekt `TextReport`)