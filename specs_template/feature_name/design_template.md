# Design: [Feature name]

<!-- One file per feature: specs/<feature-name>/design.md. Read the approved spec and relevant existing code first. Explain consequential technical choices without repeating the full spec. Keep diagram source in a separate file. -->

## Source

- Specification: `specs/<feature-name>/spec.md`
- Requirements addressed: [R1, R2, ...]

## Approach

[Summarize how the feature fits the system, the main technical approach, and why it was chosen.]

## Existing code to reuse or change

- [Path or component]: [Current responsibility and intended change or reuse.]
- [For a new project, state that no code exists and name the proposed boundaries.]

## Components and responsibilities

### [Class, module, or service name]

- Responsibility: [One clear purpose and boundary.]
- Public methods or functions: [Names and signatures only where useful.]
- Inputs and outputs: [Contract with callers.]
- Dependencies: [Other components or systems used.]
- State owned: [State or data it owns; write "None" if stateless.]

<!-- Repeat for important components only. Do not invent classes for stateless functions. -->

## Low level design

[Explain the key relationships and why the proposed structure fits this feature. Distinguish existing elements from proposed elements.]

- Diagram: [Link to a separate feature-specific diagram file, if a diagram adds value.]
- Existing elements: [List or "None".]
- Proposed elements: [List or "None".]
- Key dependency direction: [Which component calls or owns which, if important.]

<!-- For class-oriented features, the separate file may be class-diagram.md. For other features, choose a module, flow, sequence, or data diagram. Do not embed Mermaid source here. -->

## Main execution flow

1. [Entry point and input handling.]
2. [Calls and data movement between components.]
3. [Core processing and result.]
4. [Failure path or recovery, if relevant.]

## Interfaces and data

- Entry points: [API, event, command, UI action, etc.]
- Input contract: [Important fields, types, and validation boundary.]
- Output contract: [Success result and error form.]
- Data or schema changes: [Changes or "None".]
- External dependencies: [Systems or libraries and why needed; "None" if absent.]

## Core algorithm

<!-- Omit this section only when there is no nontrivial logic to decide. -->

- Purpose: [What it computes or decides.]
- Inputs and assumptions: [Preconditions.]
- Outputs and guarantees: [Postconditions and invariants.]
- Steps or pseudocode: [Enough detail to remove consequential ambiguity.]
- Edge cases: [Boundaries and undefined cases.]
- Complexity or resource limits: [Only if relevant.]
- Decisions reserved for review: [Choices requiring the feature owner's input; "None" if resolved.]

## Failure handling

- [Failure or invalid condition] → [Error, response, or recovery.]
- [Boundary case] → [Expected handling.]

## Design decisions and open questions

- Decision: [Choice, reason, and meaningful alternative if one exists.]
- Open question: [Question that must be resolved before tasks.md; write "None" when resolved.]
