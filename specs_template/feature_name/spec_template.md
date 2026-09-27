# Spec: [Feature name]

<!-- One file per feature: specs/<feature-name>/spec.md. Describe observable behaviour here; put technical implementation in design.md. Remove guidance comments when filled. -->

## Overview

[Who can do what when this feature is complete? What exists today, if anything?]

## Depends on

- [Existing feature, data, service, or prerequisite; write "None" if independent.]

## Scope

### Included

- [Capability delivered in this feature.]

### Excluded

- [Related work deliberately deferred.]

## User flow

1. [How a user or calling system starts.]
2. [What input or action it provides.]
3. [What it observes on success or failure.]

## Requirements

### R1 — [Short name]

[State one required, observable behaviour without prescribing its implementation.]

- Given [starting condition], when [action], then [observable result].
- Given [important edge or failure condition], when [action], then [observable result].

### R2 — [Short name]

[Add or remove requirement blocks as needed. Keep IDs stable when revising the spec.]

- Given [starting condition], when [action], then [observable result].

## Input and validation rules

- [Input]: [Required or optional; allowed values, format, and limits.]
- [Invalid input]: [Observable response and whether previous state is preserved or cleared.]
- [Output]: [Required format or guarantees, if relevant.]

## Access and failure behaviour

- [Who or what may use the feature; write "No access control" if applicable.]
- [Behaviour for denied access, missing data, external failure, or undefined operation.]
- [Recovery or retry behaviour, if relevant.]

## Constraints

- [Fixed language, platform, integration, compatibility, security, or performance constraint.]
- [Leave framework and algorithm choices to design.md unless already fixed by the project.]

## Definition of done

- [ ] [Observable success outcome tied to requirement IDs.]
- [ ] [Important validation or failure outcome.]
- [ ] [Existing behaviour that must still work, if applicable.]

## Open questions

- [Question that could change the required behaviour; write "None" when resolved.]
