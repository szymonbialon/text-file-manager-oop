from pathlib import Path

from src.storage.text_file_manager import TextFileManager


def test_get_text_reads_file(tmp_path: Path):
    file_path = tmp_path / 'example.txt'
    file_path.write_text('hello world', encoding='utf-8')

    manager = TextFileManager(file_path)

    assert manager.get_text() == 'hello world'


def test_append_text(tmp_path: Path):
    file_path = tmp_path / 'example.txt'
    file_path.write_text('First line', encoding='utf-8')

    manager = TextFileManager(file_path)
    manager.append_text('Second line')

    assert manager.get_text() == 'First line\nSecond line'


def test_replace_text(tmp_path: Path):
    file_path = tmp_path / 'example.txt'
    file_path.write_text('First line', encoding='utf-8')

    manager = TextFileManager(file_path)
    manager.replace_text('Second line')

    assert manager.get_text() == 'Second line'
