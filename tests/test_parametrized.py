"""Parametrized test examples."""

import pytest

from src.calculator import add, multiply, is_palindrome


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (-1, -1, -2),
        (0, 0, 0),
        (100, -50, 50),
        (0.5, 0.25, 0.75),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 4, -8),
        (10, 0.5, 5.0),
    ],
)
def test_multiply_parametrized(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("Madam", True),
        ("A Santa at NASA", True),
        ("", True),
        ("12321", True),
        ("12345", False),
    ],
)
def test_palindrome_parametrized(text, expected):
    assert is_palindrome(text) == expected
