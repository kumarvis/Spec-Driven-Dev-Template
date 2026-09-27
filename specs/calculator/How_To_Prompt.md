# design.md
## Create design.md Generic Prompt
Read specs/<feature-name>/spec.md. Inspect relevant existing code,
tests, and project documentation. If the project has no code yet,
treat it as a new project.

This is the design stage. Do not write implementation code, executable
tests, or tasks.

Before drafting, ask me about any unresolved choice that would materially
change the design. Otherwise, create:

1. specs/<feature-name>/design.md
   - Explain the approach, component responsibilities, interfaces,
     main flow, core algorithm, error handling, and significant decisions.
   - Map the design to requirement IDs in spec.md.
   - Include a Low level design section describing the important classes
     or modules and linking to the separate diagram file.
   - Do not embed Mermaid source in design.md.

2. A separate diagram Markdown file in the same feature folder.
   - If classes are meaningful, name it class-diagram.md and show key
     classes or interfaces, methods, and relationships.
   - If classes are not a useful model, choose an appropriate diagram
     and filename, then explain the choice in design.md.
   - Identify existing elements and proposed elements.
   - Do not invent classes merely to produce a class diagram.

Check that the diagram and design agree and that the design covers the
specification. Stop for my review.

## Specific design.md from spec.md
Read specs/<feature-name>/spec.md and inspect the relevant project code,
tests, and documentation. This is the design stage: do not write code,
tests, or tasks.

Create these two files:

1. specs/<feature-name>/design.md
   - Explain the technical approach, component responsibilities, interfaces,
     main flow, core algorithm, errors, and significant design decisions.
   - Map the design to the requirement IDs in spec.md.
   - Include a "Low level design" section that explains the classes or
     modules and links to the diagram file.
   - Do not embed Mermaid source in design.md.

2. specs/<feature-name>/class-diagram.md
   - Create a Mermaid class diagram showing the important classes or
     interfaces, key methods, and relationships.
   - Identify which elements already exist and which are proposed.
   - Keep the diagram focused on this feature; do not invent classes
     merely to fill out the diagram.
   - If a class diagram does not fit the feature, explain why in design.md
     and create an appropriate module or flow diagram in a separate file.

Ask about decisions that would materially change the design. After
creating the files, check that the diagram agrees with design.md and that
both cover the spec. Stop for my review.


## Creating tasks.md from design.md

Read specs/calculator/spec.md, specs/calculator/design.md, and the diagram
linked from design.md.

This is the planning stage. Do not write implementation code or executable
tests.

Identify unresolved design decisions that would change a task or an
expected test result. Ask me to resolve them before finalizing tasks.md.

Create specs/calculator/tasks.md with:

- Concrete planned test cases, each with setup or input, action, expected
  result, and a link to the relevant requirement ID.
- Cases for all five operations, input order, invalid inputs, division by
  zero, power edge cases, non-finite results, and recovery after an error.
- Small implementation tasks in dependency order, linked to requirements
  and relevant design sections.
- Separate verification tasks for automated tests and desktop UI checks.
- No tables and no repetition of the full spec or design.

Stop after drafting tasks.md for my review. Do not start building.


## Create Code and Test cases

Read the approved spec.md, design.md, tasks.md, and linked diagram in
specs/calculator/ before changing code.

This is the build stage. Write code, but do not run tests or launch the
application. Do not fix failures based on test results.

1. Inspect the repository and follow its Python conventions. If it is
   empty, create a minimal calculator package, tests/ directory, and
   configuration needed to run the application and tests. Create missing
   directories and files as needed.

2. Turn the planned test cases in tasks.md into executable automated
   tests. Then implement the calculator according to design.md, keeping
   desktop UI code separate from calculation logic.

3. Work through the implementation tasks in dependency order. Leave
   verification checkboxes unchecked. You may record which files were
   written, but do not mark any task as tested, passed, or verified.

4. Inspect the written files for consistency with spec.md and design.md.
   This is a static review only; do not claim that behaviour works.

If a material design change is needed, stop before implementing the
affected part, explain the issue, and propose the design change for review.
Do not silently change requirements or the approved algorithm.

At the end, report:
- Files created or changed
- How to start the application
- Command for the independent reviewer to run the tests
- Test and UI checks still pending
- Any unimplemented requirement or design deviation

Do not report test results, because tests were not run. Keep the project
small and avoid unnecessary dependencies.


## Create README.md 
Inspect the current Python project structure and the code that was
written for the calculator.

Create or update the project-root README.md. Preserve useful existing
content and document:

- Python version and setup steps
- Exact command to start the desktop application
- Exact command to run the automated tests
- Any prerequisites for opening the desktop UI

Derive the commands from the actual files and configuration. Do not
change application code or test code. Do not run the application or
tests. Label the commands "Not yet independently verified."