"""Desktop window: Tkinter UI wired to calculator.core. No arithmetic here
(design.md: ui.CalculatorWindow depends on core, never the reverse)."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from calculator.core import (
    CalculatorError,
    Operation,
    calculate,
    format_result,
    parse_number,
)


class CalculatorWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        self.entry_a = self._build_input_row("First number", row=0)
        self.entry_b = self._build_input_row("Second number", row=1)

        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, pady=8)
        for column, operation in enumerate(Operation):
            ttk.Button(
                button_frame,
                text=operation.value,
                command=lambda op=operation: self.on_operation_selected(op),
            ).grid(row=0, column=column, padx=4)

        self.result_label = ttk.Label(self, text="", anchor="center")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=8, sticky="ew")

    def _build_input_row(self, label_text: str, row: int) -> ttk.Entry:
        ttk.Label(self, text=label_text).grid(row=row, column=0, padx=4, pady=4, sticky="e")
        entry = ttk.Entry(self)
        entry.grid(row=row, column=1, padx=4, pady=4, sticky="w")
        return entry

    def on_operation_selected(self, operation: Operation) -> None:
        try:
            a = parse_number(self.entry_a.get())
            b = parse_number(self.entry_b.get())
            result = calculate(operation, a, b)
        except CalculatorError as error:
            self.show_error(error.message)
            return
        self.show_result(format_result(result))

    def show_result(self, text: str) -> None:
        self.result_label.configure(text=text, foreground="black")

    def show_error(self, message: str) -> None:
        self.result_label.configure(text=message, foreground="red")
