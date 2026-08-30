from typing import Protocol


class TextProvider(Protocol):
    def get_text(self) -> str:
        ...


class TextAppender(Protocol):
    def append_text(self, text: str) -> None:
        ...


class TextReplacer(Protocol):
    def replace_text(self, text: str) -> None:
        ...
