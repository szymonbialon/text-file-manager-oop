# Text File Manager OOP

Mini project for reading, modifying and analyzing text files using object-oriented design and Python protocols.

## Setup

```bash
uv sync
```

## Run

```bash
uv run main.py
```

## Tests

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=src --cov-report=term-missing --cov-report=html
```

The HTML coverage report is generated in `htmlcov/index.html`.

## Type Checking

```bash
uv run mypy src
uv run pyright
```

## Linting

```bash
uv run ruff check src tests main.py
```
