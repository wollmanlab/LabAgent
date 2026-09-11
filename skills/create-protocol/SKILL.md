---
name: create-protocol
description: Convert messy protocol source material or records of past runs into canonical, reusable LabAgent protocol templates. Use when a user wants to create or standardize a protocol; instantiating a protocol for a specific experiment belongs to prepare-experiment.
---

# Create Protocol

## Purpose

Turn pasted text, old Notion content, notes, SOPs, manuals, or records of specific past runs into a canonical protocol template that scientists can read and edit and agents can later instantiate.

Experiments contain instantiated values; protocols contain the rules and templates used to generate those values. Preserve enough procedural and quantitative detail to reproduce the method without retaining the accidental details of one historical run.

## Inspect existing protocols first

Before drafting, inspect the repository's protocols and related references. Search for:

- protocols that perform the same or a related operation;
- reusable dependencies that must be completed first;
- subprotocols invoked within the procedure;
- reference protocols that provide useful background without being required;
- established metadata, naming, linking, unit, and directory conventions.

Reuse and link existing protocols rather than copying their procedures. Avoid creating a second source of truth. Distinguish the relationships explicitly:

- **dependency**: another protocol must be completed before this protocol;
- **subprotocol**: another protocol is invoked as part of this protocol;
- **reference**: another protocol informs or supports this one but is not executed as a required step.

If no repository convention exists, place the protocol at `protocols/<protocol-id>/protocol.md`, with optional supporting files in the same directory.

## Socratic clarification

Start from the supplied material and ask one or two focused questions at a time. Adapt each question to the remaining ambiguity rather than using a fixed questionnaire. Ask especially when:

- a value may be either fixed or specific to one run;
- the natural scaling unit is unclear;
- a parameter lacks a justified default or allowed range;
- source materials conflict;
- a dependency or subprotocol relationship is uncertain;
- chemically meaningful context is incomplete.

When sources conflict, identify the contradiction and ask which source or version is authoritative. Do not silently reconcile conflicting instructions. Stop asking once the protocol can be generalized safely; record any intentionally unresolved issue explicitly.

## Abstract the source

Perform an explicit abstraction pass before writing the canonical protocol. Classify source details as:

- **run-specific**: sample IDs, well names, dates, filenames, batch names, operator notes, and the exact number of wells or samples used in one run; remove these or replace them with parameters;
- **invariant**: procedural order, technique, required materials, fixed settings, acceptance criteria, and other rules that define the method; preserve these;
- **scalable**: quantities that vary with work performed; normalize them per natural unit such as per well, sample, slide, reaction, measurement, or cm²;
- **parameterized**: values users may select for a future run; define their type or units, constraints when known, and a source-supported default when appropriate;
- **fixed**: values that genuinely define the method; keep them fixed rather than turning every number into a variable;
- **related**: dependencies, subprotocols, and references already represented elsewhere; link them with the correct relationship.

Do not infer a general rule from a one-off historical value. If the source does not establish whether a value is fixed, variable, or merely observed in that run, ask the user instead of guessing.

Preserve chemically and operationally meaningful information, including stock concentrations, final concentrations, dilution ratios, incubation times and temperatures, and volume per natural unit. Keep stock concentration, final concentration, and volume per unit conceptually distinct; do not collapse them into one ambiguous field.

Before drafting, briefly summarize the proposed abstraction when doing so would expose a mistaken assumption.

## Write the protocol package

Follow established repository conventions when present. Otherwise create:

```text
protocols/<protocol-id>/
  protocol.md
  calculations.py        # only when justified
```

Write `protocol.md` as human-readable Markdown with YAML front matter. Use only fields that are applicable and known; do not invent values. A suitable fallback shape is:

```yaml
---
id: example-protocol
name: Example protocol
version: 1.0
status: draft
owners:
  - Example Owner
inputs:
  well_count:
    type: integer
parameters:
  volume_per_well_ul:
    type: number
    default: 100
controls:
  recommended:
    - untreated
outputs:
  - prepared plate
dependencies:
  - protocol-id: cell-plating-96well
    path: ../cell-plating-96well/protocol.md
subprotocols: []
references: []
---
```

Adapt the metadata to the repository schema and the protocol rather than forcing every example field. Preserve units in field names or explicit unit properties. Use repository-relative links where possible.

Organize the body around the method's needs, typically prerequisites, materials or inputs, procedure, controls, outputs or acceptance criteria, safety notes, and unresolved items. Keep the procedure readable to scientists and avoid encoding all meaning only in YAML.

## Deterministic calculations

Use deterministic code such as `calculations.py` when calculations are nontrivial, repeated, or safety- or accuracy-critical. The code should accept normalized protocol parameters and produce run-specific quantities with explicit units, validation, and any documented excess or rounding rules. Keep simple transparent arithmetic in the protocol; do not create code merely because quantities are present.

Do not embed values from a particular run in calculation code. Future `prepare-experiment` agents should supply values such as well count or sample count and use the protocol's per-unit quantities to calculate totals.

## Completion criteria

Complete the protocol only when:

- it is reusable rather than a record of one run;
- it remains human-readable and suitable for scientists to edit;
- its metadata and parameters are structured enough for later agent instantiation;
- scalable quantities are normalized to appropriate natural units;
- fixed values, defaults, and user-selectable parameters are distinguished;
- stock concentrations, final concentrations, ratios, incubation conditions, and per-unit volumes retain their meaning;
- dependencies, subprotocols, and references are linked without duplicated procedures;
- conflicts and ambiguities are resolved or explicitly marked;
- any necessary deterministic calculations are included and any code is verified;
- a future `prepare-experiment` agent can calculate run-specific quantities from the template.

Report the protocol ID, files created, relationships to existing protocols, key abstraction decisions, and any explicitly unresolved items.
