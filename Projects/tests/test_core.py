"""Unit tests for calculator.core: R1-R6 (tasks.md T5-T20)."""

import unittest

from calculator.core import (
    DivisionByZeroError,
    InvalidInputError,
    NonFiniteResultError,
    Operation,
    UndefinedOperationError,
    UnsupportedResultError,
    calculate,
    format_result,
    parse_number,
)


class AddSubtractMultiplyTests(unittest.TestCase):
    def test_add_r1(self) -> None:
        # T5
        self.assertEqual(calculate(Operation.ADD, 7, 3), 10)

    def test_subtract_r2(self) -> None:
        # T6
        self.assertEqual(calculate(Operation.SUBTRACT, 7, 3), 4)

    def test_subtract_input_order_r2(self) -> None:
        # T7
        self.assertEqual(calculate(Operation.SUBTRACT, 3, 7), -4)

    def test_multiply_r3(self) -> None:
        # T8
        self.assertEqual(calculate(Operation.MULTIPLY, 7, 3), 21)


class DivideTests(unittest.TestCase):
    def test_divide_r4(self) -> None:
        # T9
        self.assertEqual(calculate(Operation.DIVIDE, 7, 2), 3.5)

    def test_divide_by_zero_r4(self) -> None:
        # T10
        with self.assertRaises(DivisionByZeroError):
            calculate(Operation.DIVIDE, 7, 0)


class PowerTests(unittest.TestCase):
    def test_power_r5(self) -> None:
        # T11
        self.assertEqual(calculate(Operation.POWER, 2, 3), 8)

    def test_power_negative_exponent_r5(self) -> None:
        # T12
        self.assertEqual(calculate(Operation.POWER, 2, -2), 0.25)

    def test_power_zero_to_zero_r5(self) -> None:
        # T13
        with self.assertRaises(UndefinedOperationError):
            calculate(Operation.POWER, 0, 0)

    def test_power_negative_base_fractional_exponent_r5(self) -> None:
        # T14
        with self.assertRaises(UnsupportedResultError):
            calculate(Operation.POWER, -2, 0.5)

    def test_power_zero_base_negative_exponent_r5(self) -> None:
        # T15
        with self.assertRaises(UndefinedOperationError):
            calculate(Operation.POWER, 0, -3)

    def test_power_negative_base_near_integer_exponent_boundary(self) -> None:
        # T16 - design.md confirmed decision: float.is_integer() boundary.
        with self.assertRaises(UnsupportedResultError):
            calculate(Operation.POWER, -2, 2.0000001)

    def test_power_overflow_is_non_finite_result(self) -> None:
        # T17 - design.md confirmed decision: isfinite-only overflow policy.
        with self.assertRaises(NonFiniteResultError):
            calculate(Operation.POWER, 10.0, 400.0)


class ValidationTests(unittest.TestCase):
    def test_blank_input_r6(self) -> None:
        # T18
        with self.assertRaises(InvalidInputError):
            parse_number("")

    def test_non_numeric_input_r6(self) -> None:
        # T18
        with self.assertRaises(InvalidInputError):
            parse_number("abc")

    def test_infinite_input_rejected_r6(self) -> None:
        # T19
        with self.assertRaises(InvalidInputError):
            parse_number("inf")
        with self.assertRaises(InvalidInputError):
            parse_number("-inf")

    def test_nan_input_rejected_r6(self) -> None:
        # T19
        with self.assertRaises(InvalidInputError):
            parse_number("nan")


class FormatResultTests(unittest.TestCase):
    def test_integer_result_has_no_trailing_zero(self) -> None:
        # T20
        self.assertEqual(format_result(8.0), "8")

    def test_fractional_result(self) -> None:
        # T20
        self.assertEqual(format_result(3.5), "3.5")


if __name__ == "__main__":
    unittest.main()
