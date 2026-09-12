---
name: create-bench-sheet
description: Render a prepared experiment's run manifest into a standalone human-readable bench sheet (markdown plus PDF) for the person who will execute it. Use as the final step of prepare-experiment, or to regenerate the sheet after the manifest changes.
---

# Create Bench Sheet

## Purpose

Turn a run manifest into a document someone can work from at the bench. The manifest is structured for validation and automation; the bench sheet is organized for execution, in the order the work happens, with every quantity already instantiated.

The bench sheet is a derived working document, not a second source of truth. The manifest remains authoritative; state that on the sheet.

This is not `execution.md`. `execution.md` records what actually happened during the run and is written afterward from the operator's feedback. The bench sheet is written before the run and describes what to do.

## When to use

Generate the sheet when the experiment reaches `READY_TO_RUN`, as the closing step of `prepare-experiment`. Regenerate it after any material change to the manifest.

If the sheet is requested while blockers remain, produce it, but mark every unresolved item visibly in place. Do not omit a blocked step or silently fill a missing value to make the document look complete.

## Load the run record first

Read the experiment's `manifest.yaml` and every protocol it instantiates, including their versions, dependencies, and subprotocols. Take quantities from the manifest's resolved calculations rather than recomputing them from memory, and verify the numbers you print against the manifest before writing them.

If the manifest and a protocol disagree, surface the conflict on the sheet rather than choosing silently.

## Contents

Organize for someone standing at the bench, not for validation. Include:

- what the experiment tests, in plain terms, and what a positive result looks like;
- conditions and the sample, well, slide, or reaction layout, with physical assignments;
- materials and stock concentrations;
- the ordered procedure grouped by session or day, with each step's quantities inline;
- the primary measurement and planned comparisons, briefly;
- known limitations.

Reference canonical protocols by ID and version rather than reproducing their full procedures, but inline the quantities and conditions the operator needs so the sheet is usable without opening every protocol. Carry forward safety-critical handling instructions rather than leaving them only in the protocol.

Present assumptions as assumptions and deviations as deviations. Never render an unconfirmed value as an established one.

## Quantities

Give each step's amounts as both per-unit and scaled totals, including any overage, so the operator can prepare a master mix without doing arithmetic. State the unit the scaling is per.

Use the protocol's own calculation code when it provides one. Never invent a concentration, excess factor, or conversion rule to complete a table.

## Fill-in fields

Any value that can only be obtained during execution becomes a labeled blank field rather than a guess. This includes day-of measurements, reagent lot activity or concentration, instrument and acquisition settings, and any quantity derived from them.

Where a blank feeds a calculation, print the formula beside it so the operator can finish the arithmetic at the bench. Where a setting must be held constant across samples, say so explicitly.

## Layout

Include the physical sample, well, or slide assignment. If the manifest does not fix it, propose one and mark it clearly as a proposal to confirm or replace, and tell the operator to record what they actually used.

Choose labels that do not collide with the manifest's condition identifiers; if condition IDs and plate coordinates would read ambiguously together, pick a layout or naming that keeps them distinct.

## Confirm before you start

Include a short checklist of everything that must be resolved before work begins: unconfirmed assumptions, values still missing, proposed layouts awaiting approval, and handling questions the manifest does not settle.

Writing the sheet frequently exposes gaps that section-by-section preflight did not, because it forces every step into an executable sequence. When it does:

- record the gap in the manifest's preflight findings as well;
- reconsider whether the experiment's state is still justified, and lower it if the gap can affect validity, safety, feasibility, reproducibility, or analysis;
- tell the user which gaps the sheet exposed that the manifest had not recorded.

Do not let the bench sheet become the only place a gap is documented.

## Render and place the output

Write the markdown source and a rendered PDF into the experiment directory, keeping the source so the sheet can be regenerated and diffed:

```text
experiments/<year>/<experiment_id>/
  bench_sheet.md
  <experiment_id>_bench_sheet.pdf
```

Render with the `md-to-pdf` skill when it is available; otherwise use `reportlab` directly. Do not spend time on pandoc, LaTeX, or WeasyPrint.

Verify the rendered PDF rather than trusting that it built: check the page count, confirm no missing glyphs, and look at a rendered page. Tables and lists inside blockquotes fail silently in this rendering path, so keep them in ordinary sections.

## Presenting it

Show the user the rendered sheet and summarize its sections. Call out explicitly any gap the sheet exposed that the manifest did not already record, and name the fill-in fields the operator will have to complete.

## Completion criteria

Complete the sheet only when:

- every step of the run appears in executable order;
- quantities are instantiated per unit and scaled, with overage stated;
- values obtainable only at the bench are blanks with formulas, not guesses;
- protocol IDs and versions are cited;
- assumptions, deviations, and limitations are visible rather than smoothed over;
- the confirm-before-you-start checklist is present, and anything new in it has been written back into the manifest;
- the PDF has been rendered and visually verified.
