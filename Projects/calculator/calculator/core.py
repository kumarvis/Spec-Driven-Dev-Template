"""Calculation logic for the calculator: validation, the five operations,
and result formatting. No UI imports (design.md: Existing code to reuse
or change)."""

from __future__ import annotations

import math
from enum import Enum


class Operation(Enum):
    ADD = "Add"
    SUBTRACT = "Subtract"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"
    POWER = "Power"


class CalculatorError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class InvalidInputError(CalculatorError):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class UndefinedOperationError(CalculatorError):
    pass


class UnsupportedResultError(CalculatorError):
    pass


class NonFiniteResultError(CalculatorError):
    pass


def parse_number(text: str) -> float:
    """R6: validate and convert one input field's raw text."""
    stripped = text.strip()
    if not stripped:
        raise InvalidInputError("Enter a number.")
    try:
        value = float(stripped)
    except ValueError as exc:
        raise InvalidInputError(f"'{text}' is not a valid number.") from exc
    if not math.isfinite(value):
        raise InvalidInputError("Enter a finite number (not infinity or NaN).")
    return value


def calculate(operation: Operation, a: float, b: float) -> float:
    """R1-R5: apply the selected operation. R6: guarantee a finite result
    or raise a specific CalculatorError subclass."""
    if operation is Operation.ADD:
        result = a + b
    elif operation is Operation.SUBTRACT:
        result = a - b
    elif operation is Operation.MULTIPLY:
        result = a * b
    elif operation is Operation.DIVIDE:
        result = _divide(a, b)
    elif operation is Operation.POWER:
        result = _power(a, b)

    if not math.isfinite(result):
        raise NonFiniteResultError("Result is too large to display.")
    return result


def _divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


def _power(base: float, exponent: float) -> float:
    if base == 0 and exponent == 0:
        raise UndefinedOperationError("This power is undefined.")
    if base == 0 and exponent < 0:
        raise UndefinedOperationError("This power is undefined.")
    if base < 0 and not float(exponent).is_integer():
        raise UnsupportedResultError("This calculation has no real result.")
    try:
        return base ** exponent
    except OverflowError as exc:
        # Python's ** raises OverflowError for extreme magnitudes instead of
        # returning inf (unlike +, -, *, / which return inf silently);
        # translate it so the caller sees the same NonFiniteResultError
        # as any other overflowing operation (R6).
        raise NonFiniteResultError("Result is too large to display.") from exc


def format_result(value: float) -> str:
    """Design.md display policy: no unnecessary trailing zeros."""
    if value.is_integer():
        return str(int(value))
    return f"{value:.10g}"
