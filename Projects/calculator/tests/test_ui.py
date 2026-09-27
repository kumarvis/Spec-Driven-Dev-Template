"""Integration tests for calculator.ui.CalculatorWindow: R4, R6, and the
Definition of done's no-stale-display rule (tasks.md T1-T4).

These instantiate a real Tk window and require a graphical environment.
"""

import unittest

from calculator.core import Operation
from calculator.ui import CalculatorWindow


class CalculatorWindowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.window = CalculatorWindow()

    def tearDown(self) -> None:
        self.window.destroy()

    def _set_inputs(self, a_text: str, b_text: str) -> None:
        self.window.entry_a.delete(0, "end")
        self.window.entry_a.insert(0, a_text)
        self.window.entry_b.delete(0, "end")
        self.window.entry_b.insert(0, b_text)

    def test_error_then_valid_calculation_replaces_error_r6(self) -> None:
        # T1
        self._set_inputs("", "3")
        self.window.on_operation_selected(Operation.ADD)
        self.assertEqual(self.window.result_label.cget("text"), "Enter a number.")

        self._set_inputs("7", "3")
        self.window.on_operation_selected(Operation.ADD)
        self.assertEqual(self.window.result_label.cget("text"), "10")

    def test_valid_result_then_error_leaves_no_stale_result(self) -> None:
        # T2
        self._set_inputs("7", "2")
        self.window.on_operation_selected(Operation.DIVIDE)
        self.assertEqual(self.window.result_label.cget("text"), "3.5")

        self._set_inputs("7", "0")
        self.window.on_operation_selected(Operation.DIVIDE)
        text = self.window.result_label.cget("text")
        self.assertNotEqual(text, "3.5")
        self.assertIn("divide", text.lower())

    def test_divide_by_zero_shows_error_not_crash_r4(self) -> None:
        # T3
        self._set_inputs("7", "0")
        self.window.on_operation_selected(Operation.DIVIDE)
        self.assertNotEqual(self.window.result_label.cget("text"), "")
        self.assertTrue(self.window.winfo_exists())

    def test_window_stays_open_and_editable_after_invalid_input(self) -> None:
        # T4
        self._set_inputs("not-a-number", "3")
        self.window.on_operation_selected(Operation.MULTIPLY)
        self.assertTrue(self.window.winfo_exists())
        self.assertEqual(str(self.window.entry_a["state"]), "normal")
        self.assertEqual(str(self.window.entry_b["state"]), "normal")


if __name__ == "__main__":
    unittest.main()
