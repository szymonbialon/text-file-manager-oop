from src.analysis.text_analyzer import TextAnalyzer


class FakeTextProvider:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text


def test_count_words():
    analyzer = TextAnalyzer(FakeTextProvider("Ala ma kota"))

    assert analyzer.count_words() == 3


def test_count_words_returns_zero_for_empty_text():
    analyzer = TextAnalyzer(FakeTextProvider(""))

    assert analyzer.count_words() == 0


def test_count_sentences():
    analyzer = TextAnalyzer(FakeTextProvider("Pierwsze zdanie. Drugie? Trzecie!"))

    assert analyzer.count_sentences() == 3


def test_count_sentences_returns_zero_for_empty_text():
    analyzer = TextAnalyzer(FakeTextProvider(""))

    assert analyzer.count_sentences() == 0
