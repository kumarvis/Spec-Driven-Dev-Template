# How to Prompt: Feature Workflow

Replace `<feature-name>` with a short folder name, such as `search`. Run these prompts in order from the project root. Review and approve each document before moving to the next stage. Use the corresponding templates in this folder. A diagram is a separate optional artifact; its source does not belong in `design.md`.

## 1. Create `spec.md` from a feature request

```text
Feature request: [Describe the feature, users, intended outcome, and any fixed constraints.]

Read templates/spec_template.md and inspect relevant existing project
documentation and behaviour. Draft specs/<feature-name>/spec.md using the
template. Describe what the feature must do, not how to implement it.

Define scope, user flow, numbered requirements with observable acceptance
scenarios, input rules, failure behaviour, constraints, and definition of
done. Identify dependencies on existing features. Do not invent missing
requirements or choose an implementation framework without a reason.

Ask me about missing information that would materially change the feature.
If a nonblocking choice remains open, record it under Open questions.
Do not create design, tasks, tests, or implementation code. Stop for my
review after drafting the spec.
```

## 2. Create `design.md` from the approved spec

```text
Read specs/<feature-name>/spec.md and templates/design_template.md.
Inspect relevant existing code, tests, and project documentation. If the
project has no code, treat it as a new project.

This is the design stage. Do not write implementation code, executable
tests, or tasks. Ask me about unresolved choices that would materially
change the design before finalizing it.

Create specs/<feature-name>/design.md. Explain the technical approach,
component responsibilities, interfaces, main flow, core algorithm,
failure handling, and significant decisions. Map the design to the
requirement IDs in spec.md. Include a Low level design section that
explains the important classes or modules.

Create a separate diagram Markdown file in the same feature folder only
when a diagram clarifies the design. For meaningful class relationships,
use class-diagram.md with a Mermaid class diagram showing important
classes or interfaces, key methods, and relationships. Otherwise choose
an appropriate module, flow, sequence, or data diagram and filename.
Distinguish existing elements from proposed ones. Do not invent classes
just to produce a class diagram. Link the diagram from design.md; do not
embed Mermaid source in design.md.

Check the design and diagram against each other and against the spec.
Stop for my review.
```

## 3. Create `tasks.md` from the approved design

```text
Read specs/<feature-name>/spec.md, specs/<feature-name>/design.md,
templates/tasks_template.md, and any diagram linked from design.md.

This is the planning stage. Do not write implementation code or
executable tests. Identify unresolved choices that would change a task
or expected test result, and ask me to resolve them before finalizing.

Create specs/<feature-name>/tasks.md. List concrete planned test cases,
each with setup or input, action, expected result, and a requirement ID.
Cover the acceptance scenarios plus meaningful boundaries, failures,
security or access cases, and recovery where applicable. Break the
implementation into small tasks in dependency order, linked to the
requirements and design sections. Include independent verification
steps for automated and relevant manual checks.

Do not use tables or repeat the full spec or design. Stop for my review;
do not start building.
```

## 4. Write executable tests and application code

```text
Read the approved spec.md, design.md, and tasks.md in
specs/<feature-name>/, plus any diagram linked from design.md.

This is the build stage. Inspect the repository and follow its existing
language, package, and folder conventions. If it is empty, create a
small, appropriate source structure, a test directory, and only the
configuration required to build and test this project. Create missing
directories and files as needed.

Turn the planned test cases in tasks.md into executable test code, then
implement the feature according to design.md. Work through tasks in
dependency order. Keep module boundaries and the approved algorithm.
Inspect the written files for static consistency with the documents.

Do not run tests, launch the application, or fix failures based on test
results in this stage. Leave verification checkboxes unchecked. Record
what was written without claiming that any behaviour works or tests pass.

If a material design change is necessary, stop before implementing the
affected part, explain the issue, and propose the change for review.
Do not silently change requirements or the approved algorithm.

At the end, report the files created or changed, unimplemented
requirements, design deviations, and checks pending for an independent
reviewer. Do not report test results because no tests were run.
```

## 5. Create or update `README.md` (optional follow-up)

```text
Inspect the current project structure, application code, test code, and
configuration. Create or update the project-root README.md while
preserving useful existing content.

Document the language/runtime version and setup, the exact command to
start or use the application, the exact command to run automated tests,
and any platform or interface prerequisites. Derive commands from the
actual files and configuration.

Do not change application code or test code. Do not run the application
or tests. Label commands "Not yet independently verified." Do not create
an implementation log. Briefly summarize the README changes and any
uncertainty about the commands.
```
