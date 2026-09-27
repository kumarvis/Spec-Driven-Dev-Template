# Tasks: [Feature name]

<!-- One file per feature: specs/<feature-name>/tasks.md. Draft after spec.md and design.md are reviewed. Plan tests and implementation here; do not claim a checkbox is verified until an independent check has actually run. -->

## Approved inputs

- Specification: `specs/<feature-name>/spec.md`
- Design: `specs/<feature-name>/design.md`
- Diagram: [Relative link if one exists; otherwise "None".]

## Test cases to implement

<!-- Each case needs setup/input, action, expected result, and a requirement ID. Distinguish levels only where it changes the test approach. Do not use a table. -->

### Behaviour and integration

- [ ] T1 — R1: Given [setup and input], when [action], expect [observable outcome].
- [ ] T2 — R2: Given [invalid, denied, or failure condition], when [action], expect [error or safe outcome].

### Core algorithm or module

- [ ] T3 — R1: Given [input or boundary], when [function or module is used], expect [precise output or invariant].
- [ ] T4 — R2 / design section [name]: Given [edge case], expect [precise result or error].

## Implementation tasks

<!-- Order by dependency. Keep tasks small and link them to requirements and design sections. Add or remove tasks as needed. -->

- [ ] I1 — [Create or modify a component]. Covers: [R1]. Depends on: [None]. Design: [section].
- [ ] I2 — [Implement core behaviour]. Covers: [R1, R2]. Depends on: [I1]. Design: [section].
- [ ] I3 — [Connect entry point and handle errors]. Covers: [R1, R2]. Depends on: [I2]. Design: [section].

## Verification

<!-- For an independent validator. Planning and build agents leave these unchecked. -->

- [ ] Run the relevant automated tests and record the command and result.
- [ ] Check each acceptance scenario and the definition of done in `spec.md`.
- [ ] Review the implementation against `design.md` and the linked diagram, if any.
- [ ] Perform relevant manual or end-to-end checks that automation does not cover.
- [ ] Record failures, deviations, and unresolved issues below.

## Results and deviations

[Leave blank during planning. During implementation, record what was written without claiming unrun tests passed. The independent validator records actual test outcomes and remaining issues here.]
