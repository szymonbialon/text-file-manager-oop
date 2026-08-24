# Pomysł na uogólnienie klasy

Obecnie `TextFileManager` robi kilka rzeczy naraz:
- zna ścieżkę do pliku,
- czyta plik,
- zapisuje plik,
- dopisuje tekst,
- liczy słowa,
- liczy zdania.


# 1 
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


# 2
Na dalszym etapie można też rozważyć typy generyczne w `TextFileManager`, ale raczej dopiero wtedy, 
gdy klasa miałaby obsługiwać nie tylko zwykły tekst, ale też inne formaty danych i zwracać różne typy wyników, 
np. `str` dla tekstu, `dict` dla JSON albo listę rekordów dla CSV.