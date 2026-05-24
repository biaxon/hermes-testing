"""Fixture-based test examples."""

import pytest
from pathlib import Path
import tempfile
import json


@pytest.fixture
def numbers_dataset():
    """Fixture providing a set of test numbers."""
    return {
        "integers": [1, 2, 3, 4, 5],
        "negatives": [-1, -5, -10],
        "floats": [0.5, 1.5, 3.14],
    }


@pytest.fixture
def temp_json_file():
    """Fixture creating a temporary JSON file, cleaned up after the test."""
    data = {"name": "test", "values": [1, 2, 3]}
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump(data, tmp)
    tmp.close()
    yield Path(tmp.name)
    Path(tmp.name).unlink()


class TestWithFixtures:

    def test_numbers_dataset_has_required_keys(self, numbers_dataset):
        assert "integers" in numbers_dataset
        assert "negatives" in numbers_dataset
        assert "floats" in numbers_dataset

    def test_all_positive_integers(self, numbers_dataset):
        assert all(n > 0 for n in numbers_dataset["integers"])

    def test_all_negative_in_negatives(self, numbers_dataset):
        assert all(n < 0 for n in numbers_dataset["negatives"])

    def test_temp_json_file_exists(self, temp_json_file):
        assert temp_json_file.exists()
        assert temp_json_file.suffix == ".json"

    def test_temp_json_content(self, temp_json_file):
        data = json.loads(temp_json_file.read_text())
        assert data["name"] == "test"
        assert data["values"] == [1, 2, 3]


@pytest.fixture
def mock_response(mocker):
    """Fixture using pytest-mock to mock external dependencies."""
    mock = mocker.patch("src.calculator.is_palindrome")
    mock.return_value = True
    return mock


def test_with_mock(mock_response):
    """Test using mocked function."""
    from src.calculator import is_palindrome
    assert is_palindrome("anything") is True
    mock_response.assert_called_once_with("anything")
