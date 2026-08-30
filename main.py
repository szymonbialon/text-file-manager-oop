from pathlib import Path

from src.analysis.text_analyzer import TextAnalyzer
from src.storage.text_file_manager import TextFileManager


def main():
    manager = TextFileManager(Path('data/example.txt'))
    analyzer = TextAnalyzer(manager)

    print(manager.get_text())
    print('\nStatystyki tekstu:')
    print(f"Liczba słów: {analyzer.count_words()}")
    print(f"Liczba zdań: {analyzer.count_sentences()}")


if __name__ == "__main__":
    main()
