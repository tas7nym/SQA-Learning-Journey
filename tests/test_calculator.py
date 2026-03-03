"""
test_calculator.py — Unit tests for the calculator module.

SQA concepts demonstrated here:
    - Arrange / Act / Assert (AAA) pattern
    - Testing the "happy path" (normal inputs)
    - Testing edge cases (boundary values, error conditions)
    - Parameterised tests to reduce duplication
    - Descriptive test names that act as living documentation
"""

import pytest

from src.calculator import add, divide, multiply, subtract


# ---------------------------------------------------------------------------
# add()
# ---------------------------------------------------------------------------

class TestAdd:
    def test_add_two_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_positive_and_negative(self):
        assert add(10, -4) == 6

    def test_add_two_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_with_zero(self):
        assert add(7, 0) == 7

    def test_add_floats(self):
        assert add(1.1, 2.2) == pytest.approx(3.3)

    @pytest.mark.parametrize("a, b, expected", [
        (0, 0, 0),
        (100, 200, 300),
        (-50, 50, 0),
    ])
    def test_add_parametrised(self, a, b, expected):
        assert add(a, b) == expected


# ---------------------------------------------------------------------------
# subtract()
# ---------------------------------------------------------------------------

class TestSubtract:
    def test_subtract_two_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_resulting_in_negative(self):
        assert subtract(3, 7) == -4

    def test_subtract_same_numbers(self):
        assert subtract(5, 5) == 0

    def test_subtract_with_zero(self):
        assert subtract(9, 0) == 9


# ---------------------------------------------------------------------------
# multiply()
# ---------------------------------------------------------------------------

class TestMultiply:
    def test_multiply_two_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(99, 0) == 0

    def test_multiply_by_negative(self):
        assert multiply(5, -3) == -15

    def test_multiply_two_negatives_gives_positive(self):
        assert multiply(-4, -4) == 16

    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 1),
        (2, 3, 6),
        (10, 10, 100),
    ])
    def test_multiply_parametrised(self, a, b, expected):
        assert multiply(a, b) == expected


# ---------------------------------------------------------------------------
# divide()
# ---------------------------------------------------------------------------

class TestDivide:
    def test_divide_two_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_resulting_in_float(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_negative_by_positive(self):
        assert divide(-6, 3) == -2

    def test_divide_by_negative(self):
        assert divide(8, -4) == -2

    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0

    def test_divide_by_zero_raises_value_error(self):
        """Edge case: dividing by zero must raise a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(10, 0)

    def test_divide_negative_by_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            divide(-5, 0)
