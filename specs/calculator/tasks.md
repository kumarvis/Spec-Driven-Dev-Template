# Tasks: Calculator

## Approved inputs

- Specification: `specs/calculator/spec.md`
- Design: `specs/calculator/design.md` (and `specs/calculator/class-diagram.md`)

## Test cases to implement

### Behaviour and integration (through `CalculatorWindow`)

- [ ] T1 — R6: Given an invalid field (blank text) and an operation selected, when a valid calculation is then performed with corrected input, expect the window to show the new numeric result and no trace of the prior error.
- [ ] T2 — R6 / DoD: Given a valid result is currently displayed, when the user then triggers an error (e.g., divide by zero), expect the error message to fully replace the prior numeric result — nothing stale left visible.
- [ ] T3 — R4: Given `7` and `0` with Divide selected, expect the window to show a division-by-zero error and no numeric result.
- [ ] T4 — R6 / Access and failure behaviour: Given any invalid-input or undefined-operation case, when triggered through the window, expect the window to remain open and responsive (no crash, no freeze) and both fields remain editable.

### Core algorithm or module (`core.py`, no UI)

- [ ] T5 — R1: `calculate(ADD, 7, 3)` → `10`.
- [ ] T6 — R2: `calculate(SUBTRACT, 7, 3)` → `4`.
- [ ] T7 — R2: `calculate(SUBTRACT, 3, 7)` → `-4` (confirms input order).
- [ ] T8 — R3: `calculate(MULTIPLY, 7, 3)` → `21`.
- [ ] T9 — R4: `calculate(DIVIDE, 7, 2)` → `3.5`.
- [ ] T10 — R4: `calculate(DIVIDE, 7, 0)` → raises `DivisionByZeroError`.
- [ ] T11 — R5: `calculate(POWER, 2, 3)` → `8`.
- [ ] T12 — R5: `calculate(POWER, 2, -2)` → `0.25`.
- [ ] T13 — R5: `calculate(POWER, 0, 0)` → raises `UndefinedOperationError`.
- [ ] T14 — R5: `calculate(POWER, -2, 0.5)` → raises `UnsupportedResultError`.
- [ ] T15 — R5: `calculate(POWER, 0, -3)` → raises `UndefinedOperationError` (zero base, negative exponent).
- [ ] T16 — design.md Core algorithm (confirmed decision): `calculate(POWER, -2, 2.0000001)` → raises `UnsupportedResultError`, pinning the `b.is_integer()` boundary (near-integer but non-integer exponent on a negative base is still rejected).
- [ ] T17 — design.md Core algorithm (confirmed decision): `calculate(POWER, 10, 400)` → raises `NonFiniteResultError`, confirming the isfinite-only overflow policy (no explicit magnitude cap).
- [ ] T18 — R6: `parse_number("")` and `parse_number("abc")` → both raise `InvalidInputError`.
- [ ] T19 — R6: `parse_number("inf")`, `parse_number("-inf")`, `parse_number("nan")` → all raise `InvalidInputError` (rejected despite `float()` accepting them).
- [ ] T20 — Input and validation rules (spec.md): `format_result(8.0)` → `"8"` (no trailing `.0`); `format_result(3.5)` → `"3.5"`.

## Implementation tasks

- [ ] I1 — Create the `calculator` package skeleton: `__init__.py`, empty `core.py`, `ui.py`, `main.py`.
      Covers: scaffolding for R1–R6. Depends on: None.
- [ ] I2 — Implement the `Operation` enum and `CalculatorError` hierarchy (`InvalidInputError`, `DivisionByZeroError`, `UndefinedOperationError`, `UnsupportedResultError`, `NonFiniteResultError`) in `core.py`.
      Covers: foundation for R1–R6. Depends on: I1. Design: Components — `core.Operation`, exception hierarchy.
- [ ] I3 — Implement `core.parse_number`.
      Covers: R6. Depends on: I2. Design: Components — `core.parse_number`.
- [ ] I4 — Implement `core.calculate` for Add, Subtract, Multiply, Divide.
      Covers: R1, R2, R3, R4. Depends on: I2. Design: Core algorithm.
- [ ] I5 — Implement Power's edge-case rules in `core.calculate` (zero base/exponent, negative base with non-integer exponent).
      Covers: R5. Depends on: I4. Design: Core algorithm.
- [ ] I6 — Add the `math.isfinite` check across all operations in `core.calculate`.
      Covers: R6 (non-finite-result rule). Depends on: I4, I5. Design: Core algorithm.
- [ ] I7 — Implement `core.format_result`.
      Covers: Input and validation rules (numeric display) in spec.md. Depends on: I2.
- [ ] I8 — Build `ui.CalculatorWindow`: two `Entry` widgets, five operation `Button`s, one result/error `Label`, laid out per the user flow in spec.md.
      Covers: R1–R6 user flow, DoD "window opens". Depends on: I1. Design: Components — `ui.CalculatorWindow`.
- [ ] I9 — Wire `on_operation_selected` to call `core.parse_number` → `core.calculate` → `core.format_result`, catching `CalculatorError` subclasses; implement `show_result`/`show_error` so the label is always fully overwritten.
      Covers: R6 recovery, DoD stale-display rule. Depends on: I3, I4, I5, I6, I7, I8. Design: Main execution flow, Failure handling.
- [ ] I10 — Implement `main.py` entry point (`CalculatorWindow` + `mainloop()`).
      Covers: DoD "window opens". Depends on: I9.

## Verification

- [ ] Run the relevant tests; record the command and result.
- [ ] Check every acceptance scenario in `spec.md` (R1–R6 examples, Definition of done checklist).
- [ ] Review the implementation against `design.md` and `class-diagram.md`, including module boundaries (`core.py` has no Tkinter imports; `ui.py` has no arithmetic).
- [ ] Review changed code for security, errors, and unintended changes.
- [ ] Manually exercise the desktop UI: all five operations with valid input, an invalid-input case, divide by zero, each Power edge case, and recovery after an error — confirm the window never crashes or freezes.
- [ ] Record any unresolved issue or approved design change below.

## Results and deviations

Build stage complete (code written; nothing run or verified — see report below).

Files written per task, for the independent reviewer's reference:

- I1: `calculator/__init__.py`, `calculator/core.py` (skeleton), `calculator/ui.py` (skeleton), `calculator/main.py` (skeleton)
- I2: `calculator/core.py` — `Operation`, `CalculatorError` hierarchy
- I3: `calculator/core.py` — `parse_number`
- I4: `calculator/core.py` — `calculate` (Add/Subtract/Multiply), `_divide`
- I5: `calculator/core.py` — `_power`
- I6: `calculator/core.py` — `calculate`'s `math.isfinite` check; `_power`'s `OverflowError` handling
- I7: `calculator/core.py` — `format_result`
- I8: `calculator/ui.py` — `CalculatorWindow` widgets/layout
- I9: `calculator/ui.py` — `on_operation_selected`, `show_result`, `show_error`
- I10: `calculator/main.py` — entry point

Test cases T1–T20 were written in `tests/test_core.py` (T5–T20) and `tests/test_ui.py` (T1–T4), matched 1:1 to the list above. None have been run; no checkbox above has been checked, per the build-stage instructions not to mark tasks as tested, passed, or verified.
