"""
calculator.py — A simple calculator module used to demonstrate SQA practices.

Learning objectives:
    - Understand what a "unit under test" is
    - See how clear, focused functions are easier to test
    - Observe how edge cases (e.g. division by zero) are handled explicitly
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
