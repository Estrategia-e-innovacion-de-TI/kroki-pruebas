# Kroki API Test Suite

This test suite verifies the functionality of the [Kroki.io](https://kroki.io) diagram rendering API using `pytest` and the Python `kroki` client.

## 🚀 Running Tests

From the project root, execute:

```bash
uv run pytest tests/
```

## 🧪 Test Coverage
- `test_connection.py`: Basic API availability
- `test_diagram_creation.py`: Generates diagrams in all formats
- `test_error_handling.py`: Checks for invalid inputs
- `test_full_coverage.py`: Ensures all supported diagram types/formats are working

## ✨ Diagram generation

```bash
uv run diagram_generator.py <input_file.txt> <diagram_type> [output_file.svg]
```

## ✅ Requirements
- Python 3.7+
- Internet connection (to access https://kroki.io)

## 📁 Structure
```
kroki_tests/
├── pyproject.toml
├── README.md
└── tests/
    ├── conftest.py
    ├── test_connection.py
    ├── test_diagram_creation.py
    ├── test_error_handling.py
    └── test_full_coverage.py
```
