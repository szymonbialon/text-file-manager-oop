from pathlib import Path


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
