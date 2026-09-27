# Design: Calculator

## Source

- Specification: `specs/calculator/spec.md`
- Requirements addressed: R1, R2, R3, R4, R5, R6

## Approach

This is a new project with no existing code. The design splits the feature into two independent modules: a UI-free calculation module (`core.py`) that owns validation, the five operations, the Power edge-case rules, and result formatting, and a thin Tkinter window (`ui.py`) that only reads widget input, calls `core`, and renders success or error text. The toolkit choice is Tkinter — it ships with the Python standard library, needs no extra install or license review, and its widget set (Entry, Button, Label, grid layout) is sufficient for two inputs, five operation buttons, and one result/error area. Heavier toolkits (PyQt6/PySide6, wxPython, Kivy) would add a dependency and, in PyQt6's case, a licensing question, for no benefit at this scope.

## Existing code to reuse or change

No existing code; this is the project's first feature. Proposed module boundaries:

- `calculator/core.py`: input parsing/validation, the five operations, Power's edge-case rules, and result formatting. No Tkinter or UI imports — pure functions over floats and strings.
- `calculator/ui.py`: `CalculatorWindow`, a `tk.Tk` subclass that owns the widgets, wires button clicks to `core` calls, and renders the outcome. No arithmetic — only calls into `core` and formats what to show.
- `calculator/main.py`: entry point (`if __name__ == "__main__"`) that constructs `CalculatorWindow` and calls `mainloop()`.
- `calculator/__init__.py`: empty package marker.

## Components and responsibilities

### `core.Operation` (enum)

- Responsibility: enumerate the five supported operations (R1–R5).
- Public: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `POWER`.
- Inputs and outputs: none.
- Dependencies: none.
- State owned: none.

### `core.parse_number(text: str) -> float`

- Responsibility: validate and convert one input field's raw text (R6).
- Public methods or functions: `parse_number(text) -> float`; raises `InvalidInputError` for blank, non-numeric, infinite, or NaN text.
- Inputs and outputs: raw `Entry` text in; a finite `float` out, or a raised error.
- Dependencies: `math.isfinite`.
- State owned: none.

### `core.calculate(operation, a, b) -> float`

- Responsibility: apply R1–R5, including all Power edge cases, and guarantee a finite result or a specific raised error (R6, last bullet).
- Public methods or functions: `calculate(operation: Operation, a: float, b: float) -> float`.
- Inputs and outputs: two already-validated finite floats and an `Operation` in; a finite `float` out, or one of `DivisionByZeroError`, `UndefinedOperationError`, `UnsupportedResultError`, `NonFiniteResultError`.
- Dependencies: `math`.
- State owned: none.

### `core.format_result(value: float) -> str`

- Responsibility: render a float "without unnecessary trailing zeros" per the spec's display rule (a design decision, flagged below).
- Dependencies: none.

### `core` exception hierarchy

- `CalculatorError(Exception)`: base class carrying a human-readable `message`.
- `InvalidInputError`, `DivisionByZeroError`, `UndefinedOperationError`, `UnsupportedResultError`, `NonFiniteResultError`: subclasses so the UI can branch on error *type*, not on parsing message strings.

### `ui.CalculatorWindow(tk.Tk)`

- Responsibility: own the two number `Entry` widgets, the five operation `Button`s, and one result/error `Label`; translate a button click into a `core` call; render exactly one outcome at a time.
- Public methods or functions: `on_operation_selected(operation)`, `show_result(text)`, `show_error(message)`.
- Inputs and outputs: widget events in; label text/style updates out.
- Dependencies: `core` only — no dependency in the other direction.
- State owned: the four widgets above. No calculation state is kept between clicks.

## Low level design

Calculation logic is a set of stateless, UI-independent transformations (numbers in, a number or an error out) — there's no meaningful identity, lifecycle, or polymorphism to model, so wrapping it in a `Calculator` class would only add ceremony. The one place classes genuinely fit is the error hierarchy (a real "is-a" relationship the UI relies on) and the Tkinter window (which must hold widget state across callbacks). `core`'s functions are therefore modeled as a module, not a class.

The full class diagram is in [`class-diagram.md`](class-diagram.md). Summary of what it shows, all proposed (this is a new project; nothing exists yet):

- `CalculatorWindow` (class) — the Tkinter window; holds `entry_a`, `entry_b`, `result_label` as instance state and exposes `on_operation_selected`, `show_result`, `show_error`.
- `core` (module, `<<module>>` stereotype) — `parse_number`, `calculate`, `format_result` as plain functions.
- `Operation` (enum) — `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `POWER`.
- `CalculatorError` hierarchy (classes) — base `CalculatorError` with subclasses `InvalidInputError`, `DivisionByZeroError`, `UndefinedOperationError`, `UnsupportedResultError`, `NonFiniteResultError`, so `CalculatorWindow` can catch broadly (never crash) while still branching on subclass to pick a message (R6).

`CalculatorWindow` depends on `core`, never the reverse, so calculation logic stays testable and displayable without a window.

## Main execution flow

1. `main.py` constructs a `CalculatorWindow` and calls `mainloop()`.
2. The user types into both `Entry` widgets and clicks an operation button.
3. `on_operation_selected(operation)` reads both `Entry` texts and calls `core.parse_number()` on each.
4. If either is invalid, it catches `InvalidInputError` and calls `show_error(...)`; both inputs remain editable (R6).
5. On successful parsing, it calls `core.calculate(operation, a, b)`.
6. On success, it formats the result via `core.format_result` and calls `show_result(text)`.
7. On any `CalculatorError` raised by `calculate`, it calls `show_error(message)` instead.
8. Either way, the single result/error `Label` is fully overwritten, so no prior result or error can linger (R6, Definition of done).

## Interfaces and data

- Entry points: two `Entry` widgets (first number, second number) and five `Button` widgets (Add, Subtract, Multiply, Divide, Power), each bound to `on_operation_selected`.
- Input contract: raw `Entry` text for both numbers; must pass `parse_number` (finite, numeric, non-blank) or the calculation does not proceed.
- Output contract: the result label shows either the formatted numeric result or a single error message — never both, never a value left over from a previous click.
- Data changes: none — no persistence, history, or memory (explicitly excluded in the spec).
- External dependencies: none beyond the Python standard library (`tkinter`, `math`).

## Core algorithm

- Purpose: `core.calculate` — apply R1–R5, with Power's edge cases enforced before Python's own numeric semantics can produce a misleading result.
- Inputs and assumptions: `a` and `b` are already finite floats (validated by `parse_number` before `calculate` is ever called).
- Outputs and guarantees: returns a finite `float`, or raises one specific `CalculatorError` subclass. Never returns `inf` or `nan`.
- Steps or pseudocode:
  ```
  ADD:      return a + b
  SUBTRACT: return a - b
  MULTIPLY: return a * b
  DIVIDE:
      if b == 0: raise DivisionByZeroError
      return a / b
  POWER:
      if a == 0 and b == 0: raise UndefinedOperationError        # R5, 0**0
      if a == 0 and b < 0:  raise UndefinedOperationError        # R5, 0 to a negative power
      if a < 0 and not b.is_integer(): raise UnsupportedResultError  # R5, non-real result
      return a ** b
  (all operations) result = <above>
  if not math.isfinite(result): raise NonFiniteResultError       # R6, last bullet
  return result
  ```
- Edge cases and invariants covered: `2 ** 3 = 8`; `2 ** -2 = 0.25`; `0 ** 0` and `0 ** (negative)` are rejected by explicit checks *before* Python evaluates them, since Python's own behaviour there (returning `1` for `0 ** 0`, raising `ZeroDivisionError` for `0 ** -2`) doesn't match the spec's required error type or message; `(-2) ** 0.5` is rejected before Python would otherwise silently return a complex number.
- Time and memory: O(1) per calculation; not a concern at this scale.
- Confirmed decisions:
  - The "integer exponent" check uses `b.is_integer()`: a typed exponent like `-2.0` is integer (allowed), `-2.0000001` is non-integer (rejected). Confirmed; covered by a boundary test in `tasks.md`.
  - Overflow (e.g., a negative base raised to a very large integer exponent) is caught after the fact via `math.isfinite`, with no explicit magnitude cap on inputs. Confirmed; covered by an overflow test in `tasks.md`.

## Failure handling

- Blank or non-numeric field → `InvalidInputError` → `show_error`; both fields stay editable.
- Field text is `"inf"`, `"-inf"`, or `"nan"` (all of which `float()` accepts) → `InvalidInputError`, since `parse_number` checks `math.isfinite` after conversion.
- Second number is `0` on Divide → `DivisionByZeroError` → `show_error("Cannot divide by zero.")`.
- `0 ** 0` or `0 ** negative` → `UndefinedOperationError` → `show_error("This power is undefined.")`.
- Negative base with a non-integer exponent → `UnsupportedResultError` → `show_error("This calculation has no real result.")`.
- Any operation whose numeric result overflows to non-finite → `NonFiniteResultError` → `show_error("Result is too large to display.")`.
- Any `CalculatorError`: caught in `on_operation_selected`, window stays open and responsive — computation is synchronous and O(1), so no background thread or freeze risk exists.

## Design decisions and open questions

- Decision: Tkinter for the UI toolkit — standard-library, zero extra install/licensing, and sufficient widget set for this scope. See Approach for rejected alternatives.
- Decision: `core.py` has no Tkinter imports and `ui.py` has no arithmetic, so the calculation rules can be exercised and verified independently of any window.
- Decision: a single result/error `Label`, always fully overwritten (never appended to or partially updated) — this is what guarantees "no stale numeric result remains after an error" and vice versa.
- Decision: `format_result` shows whole numbers without a trailing `.0` (e.g., `"8"` not `"8.0"`) and otherwise formats to a bounded number of significant digits with trailing zeros stripped (e.g., `7/2 → "3.5"`). Flag if you want a different precision or rounding policy — the spec leaves this open by design.
- Decision: overflow (e.g., very large intermediate results) is treated as a distinct `NonFiniteResultError`, separate from `UnsupportedResultError` (which is specifically the negative-base/non-integer-exponent, non-real case), so their messages can differ meaningfully.
- Decision: the `is_integer()` boundary for Power's negative-base rule and the isfinite-only overflow policy (no explicit magnitude cap) are both confirmed — see Core algorithm.
