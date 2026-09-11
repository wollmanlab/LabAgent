---
name: create-experiment
description: Initialize a new scientific or technical experiment through an adaptive Socratic dialogue, then create its minimal repository record. Use when a user wants to start or register an experiment; detailed experimental design belongs to prepare-experiment.
---

# Create Experiment

## Purpose

Turn a rough experimental intent into a clearly framed experiment and initialize its repository record. Establish what the experiment is for before creating files, while keeping detailed experimental design for the next stage.

## Socratic interaction

Start from the user's stated intent and conduct an adaptive dialogue:

- Ask one or two focused questions at a time.
- Choose each question in response to what the user has already said; do not work through a rigid questionnaire.
- Probe ambiguity, assumptions, and decision criteria without making the exchange needlessly long.
- Reflect the proposed framing back to the user when that will expose a misunderstanding.
- Stop asking questions once the completion criteria below are satisfied.

Clarify enough to determine:

- the scientific or technical objective;
- the decision the experiment should inform;
- what is being changed, compared, or evaluated;
- relevant project context or prior work;
- what outcome would be informative, including the metric or observation that matters.

Challenge vague goals. For example, if the user says "optimize X," ask what measurable criterion defines improvement and what decision an improved result would support.

Do not design detailed controls, choose exact conditions, calculate reagent quantities, or write a full protocol during this skill. Those tasks belong to `prepare-experiment`.

## Completion criteria

Before initializing the experiment, establish:

- a clear objective;
- an experiment name or concise title;
- an owner;
- project tags, when applicable.

Also capture the decision, comparison or change, project context, and informative-outcome criteria when known. If a field is not applicable, do not force the user to invent a value.

Summarize the intended experiment and resolve any material misunderstanding before writing files.

## Initialize the experiment

Follow the repository's existing conventions when they are present. Otherwise:

1. Assign the next available experiment ID in the form `EXP-<year>-<sequence>`, using a zero-padded sequence such as `EXP-2026-0042`. Determine the sequence from existing experiment records and never reuse an ID.
2. Create an experiment branch named `exp/<experiment_id>-<short-slug>`, using the repository's naming convention if it differs. Do not discard or overwrite unrelated working-tree changes; if branch creation would be unsafe, explain the conflict and stop before changing repository state.
3. Create `experiments/<year>/<experiment_id>/` containing:

   ```text
   manifest.yaml
   execution.md
   analysis.md
   summary.md
   figures/
   src/
   ```

4. Initialize `manifest.yaml` with known metadata only. Omit unknown optional fields rather than guessing or inserting fabricated values. Use the repository's established schema when available; otherwise use a minimal structure such as:

   ```yaml
   experiment_id: EXP-2026-0042
   date: 2026-09-11
   owner: Example Owner
   title: Concise experiment title
   projects:
     - example-project
   objective: >
     Clear scientific or technical objective.
   decision: >
     Decision this experiment is intended to inform.
   informative_outcome: >
     Metric or observation that would make the result informative.
   status: planning
   context:
     - projects/example-project/context.md
   ```

   Include `projects` and `context` only when applicable and known. Reference relevant project context rather than copying it into the experiment record.
5. Keep `execution.md`, `analysis.md`, and `summary.md` minimal. Add only established repository headings or a short purpose heading; do not pre-fill experimental details that have not been decided.

## Handoff

Report the experiment ID, branch, directory, and metadata created. Then invite the user to continue with `prepare-experiment` to design controls, conditions, calculations, and the execution plan.
