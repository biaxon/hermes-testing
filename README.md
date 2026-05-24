# Hermes Testing

A collection of testing examples and patterns using Python's pytest framework.

## Structure

```
hermes-testing/
├── src/
│   └── calculator.py     # Simple calculator module to test
├── tests/
│   ├── test_calculator.py   # Unit tests
│   ├── test_parametrized.py # Parametrized test examples
│   └── test_fixtures.py     # Fixture-based test examples
├── pyproject.toml           # Project config
├── README.md
└── requirements.txt
```

## Running Tests

```bash
pip install -r requirements.txt
pytest -v
pytest -v --cov=src   # with coverage
```
