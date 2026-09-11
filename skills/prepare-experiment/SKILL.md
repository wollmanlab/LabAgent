---
name: prepare-experiment
description: Collaboratively turn an initialized experiment into a complete, executable, preflight-checked run manifest. Use after create-experiment to design the experiment, instantiate canonical protocols, specify analysis and acquisition, resolve run-specific calculations, and determine whether the experiment is ready to run.
---

# Prepare Experiment

## Purpose

Turn an experiment initialized by `create-experiment` into a complete, executable run manifest through collaborative scientific reasoning. Do not merely fill fields: clarify what the experiment must teach, challenge the design, instantiate reusable protocols, specify analysis before execution, validate the complete run, and only then finalize the manifest.

Keep scientific judgment with the user. Make assumptions, tradeoffs, and unresolved risks visible; do not silently decide scientifically material questions.

## Load context before asking questions

Inspect the repository before beginning the design discussion. Read:

- the experiment's initial `manifest.yaml` and its linked files;
- relevant project context referenced by the experiment or discoverable through its project tags;
- protocols already referenced by the experiment;
- related canonical protocols in LabAgent, including their dependencies and subprotocols;
- relevant previous experiments and results, when available.

Follow repository links and established conventions. Search selectively using the experiment's objective, methods, samples, measurements, and project tags. Prefer the most relevant prior experiments rather than loading the entire history. Treat prior runs as evidence and context, not automatically as authoritative templates.

Do not ask the user to repeat information that is already recorded. Summarize material facts, contradictions, and gaps from the loaded context before asking the first question when that will help establish shared understanding. If sources conflict, surface the conflict and ask which is authoritative rather than silently reconciling it.

## Conduct a Socratic design discussion

Ask one or two focused questions at a time. Adapt each question to what is still uncertain rather than following a fixed questionnaire. Work with the user to establish:

- the question the experiment is trying to answer;
- why the answer matters and what decision it will inform;
- conditions, comparisons, controls, and replicate strategy;
- variables that must be held constant;
- plausible confounders, biases, and likely failure modes;
- what results would be positive, negative, ambiguous, or uninterpretable.

Probe whether the proposed comparison isolates the intended causal or descriptive question. Challenge missing controls, pseudoreplication, avoidable confounding, inadequate replication, underdetermined measurements, and designs too complex to interpret. Suggest a simpler or staged design when it would answer the question with less ambiguity, cost, or operational risk.

Explain the reasoning behind a challenge and present consequential tradeoffs clearly. The user decides scientifically material choices. Do not optimize solely for convenience, and do not expand the experiment beyond what is needed to inform its stated decision.

## Build the analysis plan before execution

Determine the analysis before finalizing the experimental procedure. Establish:

- the primary measurement that answers the question;
- secondary or diagnostic measurements, when justified;
- normalization and baseline definitions;
- planned comparisons and, when relevant, statistical units or models;
- exclusion rules, quality-control criteria, and handling of failed samples;
- expected raw data, processed outputs, figures, tables, or decision artifacts;
- analysis skills, scripts, or pipelines to use when available.

Define choices prospectively where possible so they are not selected after seeing the result. Confirm that the sample layout, instrumentation, acquisition settings, metadata capture, and file outputs will generate the data the analysis requires. If the planned acquisition cannot support the intended analysis, revise the acquisition, analysis, or design with the user before proceeding.

## Instantiate canonical protocols

Retrieve the canonical protocol templates needed for the run. Resolve and inspect their dependencies and subprotocols, preserving the distinction between:

- a dependency completed before the protocol;
- a subprotocol invoked during it;
- a reference that informs the work but is not executed.

Reference canonical protocols rather than copying their full procedures into the experiment. Preserve each protocol's identifier and version so the run is reproducible. Record any deliberate deviation or version override explicitly.

Convert template parameters into run-specific values. Derive sample, well, slide, reaction, field, and measurement counts from the agreed design and layout. Scale reagent quantities, dilutions, master mixes, consumables, and other per-unit amounts using the protocol's normalized definitions, including documented excess and rounding rules.

For a master mix serving multiple wells, reactions, or condition groups with the same composition, prepare 10% over the theoretical dispensing requirement to cover transfer loss: multiply the total required volume and every component by `1.10`. Calculate separate mixes for conditions with different compositions. Record both the theoretical requirement and the overage-adjusted preparation amount, including the 10% factor and any subsequent rounding. If the canonical protocol specifies a different excess or the user deliberately chooses one, use and document that value instead; do not apply both overages.

Use the protocol's deterministic calculation code when provided. Use deterministic code for nontrivial, repeated, safety-critical, or accuracy-critical calculations; verify its inputs, units, constraints, and outputs. Keep simple arithmetic transparent. Never invent missing concentrations, defaults, excess factors, or conversion rules: resolve them with the user or record them as blocking issues.

## Assemble the run manifest

Follow the repository's existing manifest schema and conventions. Extend the initialized manifest in place rather than creating a competing source of truth. The completed run manifest must capture, at minimum:

- **experiment metadata**: ID, title, owner, date, and project tags;
- **objective**: scientific question, rationale, and decision to be informed;
- **design**: conditions, comparisons, controls, replicates, variables held constant, and sample layout;
- **protocols**: canonical IDs, versions, relationships, and run-specific parameters or deviations;
- **inputs**: materials, reagents, samples, and relevant lot or stock information when required;
- **calculations**: counts, scaled quantities, dilutions, master mixes, excess or rounding rules, and calculation provenance;
- **execution**: an ordered plan with dependencies, handoffs, timing constraints, and relevant instrument or acquisition settings;
- **analysis**: primary measurement, normalization, comparisons, analysis skills or pipelines, expected outputs, exclusions, and QC criteria;
- **preflight**: check results, warnings, and unresolved issues, distinguishing critical blockers from noncritical warnings;
- **status**: `PLANNING`, `DESIGN_COMPLETE`, or `READY_TO_RUN`.

Use structured fields where they support validation and automation, while keeping the manifest understandable to a scientist. Link to detailed canonical procedures and analysis resources rather than duplicating them unnecessarily. Update companion experiment files such as `execution.md` or `analysis.md` only when repository conventions assign detail to them, and keep the manifest as the authoritative index of the run.

## Apply experiment states

Use only these states:

- `PLANNING`: scientifically or operationally material choices remain unresolved.
- `DESIGN_COMPLETE`: the scientific design and analysis approach are agreed, but operational instantiation or preflight still has unresolved blockers.
- `READY_TO_RUN`: every completion criterion below is satisfied; only explicit noncritical warnings may remain.

Do not advance status merely because the manifest is populated. If an issue is unresolved, record its owner or required decision when known and keep the state below `READY_TO_RUN` whenever the issue can affect validity, safety, feasibility, reproducibility, or analysis.

## Run integrated preflight

Validate the run as a connected system rather than checking sections independently. Confirm consistency across the question, decision, design, controls, protocols, sample layout, calculations, execution order, instruments, acquisition, and analysis.

Check at least for:

- sample, condition, replicate, well, slide, reaction, and measurement-count mismatches;
- missing or inappropriate controls and comparisons;
- insufficient reagent or consumable quantities after excess and dead-volume rules;
- unresolved protocol dependencies, subprotocols, versions, parameters, or deviations;
- infeasible execution order, timing, capacity, or instrument requirements;
- incompatible acquisition settings or missing metadata;
- analysis inputs or QC requirements not supported by the planned data;
- ambiguities or failure modes that would make likely outcomes uninterpretable.

Re-run affected calculations and consistency checks after material design changes. Report preflight results in the manifest with explicit pass, warning, or blocking status. Unresolved critical issues prevent `READY_TO_RUN`.

## Completion criteria

Mark the experiment `READY_TO_RUN` only when:

- the scientific question, rationale, and decision are clear;
- conditions, comparisons, controls, and replication are adequate for that question;
- canonical protocol IDs and versions are identified;
- dependencies, run-specific parameters, layouts, and calculations are resolved;
- materials and quantities are sufficient;
- execution and acquisition settings are executable and support the intended analysis;
- the analysis plan, primary measurement, normalization, comparisons, expected outputs, exclusions, and QC are specified;
- integrated preflight passes, with no unresolved critical issues and only explicit noncritical warnings remaining.

Before finishing, review the proposed manifest with the user when scientifically material decisions were made during preparation. Report the final state, the key design and analysis decisions, the canonical protocol versions instantiated, preflight findings, and any remaining warnings or unresolved issues.
