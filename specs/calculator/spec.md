# Spec: Calculator

## Overview

Create a small calculator with a Python desktop window. A user enters two numbers, chooses Add, Subtract, Multiply, Divide, or Power, and sees the result. This is a new feature; there is no existing calculator behaviour to preserve.

## Depends on

- None. This is the first feature of the demo project.

## Scope

### Included

- A desktop window with two number inputs, controls for the five operations, and a result or error display.
- Arithmetic on finite real numbers, subject to the power rules below.
- Clear feedback for invalid input and undefined results.

### Excluded

- Scientific functions, calculation history, memory, and saved results.
- Complex-number results and symbolic mathematics.
- A web interface or command-line interface.

## User flow

1. The user opens the calculator's desktop window.
2. The user enters two numbers and selects one of the five operations.
3. The window displays the result, or a clear error if the input or operation is invalid. The user can correct the input and try again without restarting.

## Requirements

### R1 — Add

The calculator adds the first number to the second.

- Given inputs `7` and `3`, when the user selects Add, then the result is `10`.

### R2 — Subtract

The calculator subtracts the second number from the first; input order matters.

- Given inputs `7` and `3`, when the user selects Subtract, then the result is `4`.
- Given inputs `3` and `7`, when the user selects Subtract, then the result is `-4`.

### R3 — Multiply

The calculator multiplies the two numbers.

- Given inputs `7` and `3`, when the user selects Multiply, then the result is `21`.

### R4 — Divide

The calculator divides the first number by the second; input order matters.

- Given inputs `7` and `2`, when the user selects Divide, then the result is `3.5`.
- Given inputs `7` and `0`, when the user selects Divide, then a division-by-zero error is shown and no numeric result is shown.

### R5 — Power

The calculator raises the first number (base) to the power of the second (exponent), returning a real-valued result when supported. Negative bases are supported only with integer exponents.

- Given inputs `2` and `3`, when the user selects Power, then the result is `8`.
- Given inputs `2` and `-2`, when the user selects Power, then the result is `0.25`.
- Given inputs `0` and `0`, when the user selects Power, then an undefined-operation error is shown.
- Given inputs `-2` and `0.5`, when the user selects Power, then an unsupported-real-result error is shown.
- Given base `0` and a negative exponent, when the user selects Power, then an undefined-operation error is shown.

### R6 — Validate input and recover

Every operation requires two valid, finite numbers. Invalid input produces an understandable message and does not close or freeze the window.

- Given a blank or non-numeric input, when the user selects any operation, then the window identifies the invalid input and shows no numeric result.
- Given an input that represents infinity or NaN, when the user selects any operation, then the input is rejected.
- Given a valid calculation after an error, when the user selects an operation, then the new result replaces the old error.
- Given a calculation whose result cannot be represented as a finite real number, then a clear error is shown rather than an invalid numeric result.

## Input and validation rules

- First number and second number: required; accept signed integers or decimals, including values entered with decimal notation. Reject blank, non-numeric, infinite, and NaN values.
- Operation: one of Add, Subtract, Multiply, Divide, or Power.
- Results: show a readable number without unnecessary trailing zeros; exact presentation and rounding are design decisions, but the displayed result must not imply greater precision than the calculation provides.
- Invalid input or undefined operation: show an error in the window without displaying a stale numeric result.

## Access and failure behaviour

- Anyone who opens the local calculator window can use it; accounts and authentication are out of scope.
- Missing or invalid input, division by zero, and undefined or non-real results must be handled in the interface without crashing the app.
- The user can revise either input and perform another calculation after any error.

## Constraints

- Use Python for both the desktop interface and calculation logic.
- The choice of Python UI toolkit belongs in `design.md`.
- Keep the application small and self-contained; no network service or external account is required.

## Definition of done

- [ ] A Python desktop window opens with two inputs, five operation controls, and an area for the result or error.
- [ ] Add, Subtract, Multiply, Divide, and Power produce the specified results for valid inputs.
- [ ] Input order is correct for Subtract, Divide, and Power.
- [ ] Invalid input, division by zero, and undefined or non-real power cases produce clear errors without crashing.
- [ ] The user can correct an error and complete another calculation in the same window.
- [ ] No result from a previous calculation remains visible as if it were the result of a failed calculation.

## Open questions

- None required before design. The design should select a Python desktop UI toolkit and a sensible numeric display policy while preserving the observable behaviour above.
