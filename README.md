# Spec-Driven Dev Template

A template for **spec-driven software development with Claude**: instead of prompting an AI straight into code, you move through reviewable stages — spec → design → tasks → build → README — each stage producing a Markdown artifact you approve before the next one starts. This repo holds the reusable templates and prompts for that workflow, plus a small working proof of concept (a calculator app) that shows the workflow end to end.

## Why spec-driven development

Jumping straight to "build me X" tends to produce code that satisfies the letter of a vague ask but not the actual requirements, with no artifact to check it against later. This workflow instead produces, per feature:

1. **`spec.md`** — observable behaviour: requirements, user flow, validation rules, failure behaviour, definition of done. No implementation detail.
2. **`design.md`** (+ an optional diagram file) — the technical approach: components, interfaces, algorithms, failure handling, mapped back to the spec's requirement IDs.
3. **`tasks.md`** — planned test cases and small implementation tasks in dependency order, mapped to the design.
4. **Build stage** — the actual code and tests, written to match the approved spec/design/tasks, with verification left for an independent reviewer to run.
5. **`README.md`** — setup and run instructions derived from what was actually built.

You review and approve each stage before moving to the next, so a wrong assumption gets caught in a one-page spec instead of after a thousand lines of code.

## Repository structure

```
specs_template/feature_name/   Reusable templates: spec, design, tasks, and the prompt playbook
specs/<feature-name>/          Filled-in spec/design/tasks (+ diagrams) for each feature actually built
Projects/<poc-name>/           Self-contained code + tests for each proof of concept described under specs/
```

Each proof of concept under `Projects/` is self-contained: its own package folder and its own `tests/` folder, so a new POC never collides with an existing one's test filenames or test discovery.

### `specs_template/feature_name/`

- `spec_template.md`, `design_template.md`, `tasks_template.md` — the blank templates for each stage.
- `How_To_Prompt_Template.md` — copy-paste prompts (one per stage) for driving Claude through the workflow for a new feature. Replace `<feature-name>` and fill in the feature request, then run the prompts in order, reviewing each generated document before continuing.

To start a new feature, create `specs/<feature-name>/` and follow the five prompts in `How_To_Prompt_Template.md` in order.

### `specs/calculator/`

The filled-in spec-driven artifacts for the calculator proof of concept: `spec.md`, `design.md`, `class-diagram.md`, `tasks.md`, and `How_To_Prompt.md` (the actual prompts used for this feature, including a generic and a feature-specific design prompt). Read these in order to see how the workflow's output looks for a real feature — including the "Results and deviations" section in `tasks.md`, which records what the build stage wrote without claiming any of it was verified.

### `Projects/`

Application code, organized one self-contained folder per proof of concept:

```
Projects/calculator/
  calculator/     the calculator package (core.py, ui.py, main.py, __init__.py)
  tests/          its automated tests (test_core.py, test_ui.py)
```

A future POC would follow the same pattern as a sibling folder, e.g. `Projects/todo_app/todo_app/` + `Projects/todo_app/tests/`, with its own package name and its own test discovery — no shared `tests/` folder to collide with.

## Proof of concept: Calculator

A small Tkinter desktop calculator (Add, Subtract, Multiply, Divide, Power) built entirely from `specs/calculator/`. See that folder for the full requirements and design rationale — in short:

- `Projects/calculator/calculator/core.py` — validation, the five operations (including Power's edge cases: `0**0`, negative base with a non-integer exponent, overflow), and result formatting. Pure functions, no UI imports.
- `Projects/calculator/calculator/ui.py` — `CalculatorWindow`, a `tkinter` window that reads the two input fields, calls `core`, and renders exactly one result or error at a time.
- `Projects/calculator/calculator/main.py` — entry point.
- `Projects/calculator/tests/test_core.py`, `Projects/calculator/tests/test_ui.py` — automated tests for the above (`unittest`).

### Requirements

- Python 3.9+ (uses only the standard library: `tkinter`, `math`, `enum`, `unittest` — no `requirements.txt` or extra install needed).
- `tkinter` must be available in your Python installation (bundled with most desktop Python installs; on some Linux distributions install it separately, e.g. `apt install python3-tk`).
- A graphical display, to open the desktop window and to run `test_ui.py` (which instantiates a real `Tk` window).

### Run the application

From the `Projects/calculator/` directory:

```
cd Projects/calculator
python -m calculator.main
```

*Not yet independently verified.*

### Run the automated tests

From the `Projects/calculator/` directory:

```
cd Projects/calculator
python -m unittest discover -s tests -t .
```

`-t .` puts `Projects/calculator/` on `sys.path` so the tests' `import calculator...` resolves. `test_core.py` needs no display; `test_ui.py` opens real `Tk` windows and needs a graphical environment.

*Not yet independently verified.*

## Using this template for a new feature

1. Copy the pattern in `specs_template/feature_name/`: create `specs/<feature-name>/` and work through `spec.md` → `design.md` → `tasks.md` → build, using the prompts in `How_To_Prompt_Template.md`.
2. Create a new self-contained folder under `Projects/<poc-name>/`, mirroring `Projects/calculator/`: its own package (`Projects/<poc-name>/<poc-name>/`) and its own `tests/` folder. Don't add files to another POC's folder or to a shared top-level `tests/` — that's what keeps POCs from colliding on test filenames or test discovery.
3. If the new POC needs dependencies beyond the standard library, give it its own manifest (e.g. `Projects/<poc-name>/requirements.txt`) rather than one shared across all POCs.
4. Update this README's Proof of concept section (or add a new one) once the feature is built.
