"""Unit tests for the calculator module."""

import pytest

from src.calculator import add, subtract, multiply, divide, factorial, is_palindrome


class TestCalculator:
    """Basic operation tests."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, 1) == 0

    def test_add_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        assert subtract(3, 10) == -7

    def test_multiply(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(7, 0) == 0

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_palindrome_simple(self):
        assert is_palindrome("racecar") is True

    def test_palindrome_phrase(self):
        assert is_palindrome("A man a plan a canal panama") is True

    def test_palindrome_not(self):
        assert is_palindrome("hello") is False

    def test_palindrome_empty(self):
        assert is_palindrome("") is True
