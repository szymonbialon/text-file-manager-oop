from src.contracts.text_protocols import TextProvider


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