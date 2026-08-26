from pathlib import Path
from typing import Protocol

"""Twoim zadaniem jest zaprojektowanie i implementacja klasy obiektowej TextFileManager,
która ułatwi podstawowe operacje na plikach tekstowych. Klasa ma pełnić rolę narzędzia do odczytu,
modyfikacji oraz analizy statystycznej treści, zachowując zasady hermetyzacji i czystego kodu.

Wymagania projektowe

1. Konstruktor
Klasa powinna przyjmować podczas tworzenia instancji jeden argument: ścieżkę do pliku tekstowego.
Jeśli plik nie istnieje, konstruktor nie powinien rzucać błędu – plik ma zostać utworzony dopiero
przy pierwszej próbie zapisu.


2. Metody zarządzania zawartością (I/O)
Klasa musi realizować następujące zachowania związane z edycją treści:
Odczyt: Pobranie i zwrócenie całej zawartości pliku. Jeżeli plik nie istnieje, metoda powinna rzucić odpowiedni
wyjątek (np. FileNotFoundError).
Dopisywanie: Dodanie przekazanego tekstu na samym końcu istniejącego pliku
(bez usuwania jego dotychczasowej zawartości).
Zastępowanie: Całkowite nadpisanie pliku nowym, przekazanym jako argument tekstem
(stara zawartość jest trwale usuwana).


3. Metody statystyczne i analityczne
Klasa powinna umożliwiać analizę tekstu znajdującego się obecnie w pliku:
Liczenie słów: Metoda zwracająca całkowitą liczbę słów. Załóż, że słowa oddzielone są spacjami,
tabulacjami lub znakami nowej linii.
Liczenie zdań: Metoda zwracająca całkowitą liczbę zdań. Załóż, że zdanie kończy się jednym ze znaków
interpunkcyjnych: kropką ., znakiem zapytania ? lub wykrzyknikiem !."""


class TextProvider(Protocol):
    def get_text(self) -> str:
        ...


class TextFileManager:
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def get_text(self) -> str:
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()

    def append_text(self, text: str) -> None:
        with self.file_path.open("a", encoding="utf-8") as file:
            if self.file_path.exists() and self.file_path.stat().st_size > 0:
                file.write("\n")
            file.write(text)

    def replace_text(self, text: str) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(text)


class TextAnalyzer:
    def __init__(self, text_provider: TextProvider) -> None:
        self.text_provider = text_provider

    def count_words(self) -> int:
        text = self.text_provider.get_text()
        if not text:
            return 0
        words = text.split()
        return len(words)

    def count_sentences(self) -> int:
        text = self.text_provider.get_text()
        if not text:
            return 0
        sentences = text.count('.') + text.count('!') + text.count('?')
        return sentences


def main() -> None:
    manager = TextFileManager(Path('example.txt'))
    analyzer = TextAnalyzer(manager)

    print(manager.get_text())
    print('--------------------------------------')
    # manager.replace_text('Lorem ipsum.')
    # print(manager.get_text())
    # print('--------------------------------------')
    print(analyzer.cnt_words())
    print('--------------------------------------')
    print(analyzer.cnt_sentences())



if __name__ == "__main__":
    main()
