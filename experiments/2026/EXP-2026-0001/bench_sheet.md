# EXP-2026-0001 — Testing Exo7

**Owner:** RJ  |  **Project:** ATLAS  |  **Prepared:** 2026-09-11  |  **Status:** READY_TO_RUN

Bench sheet generated from `experiments/2026/EXP-2026-0001/manifest.yaml`. The manifest
remains the authoritative record; this sheet is the working copy for the person running
the experiment.

---

## 1. What this experiment tests

Exo7 degrades single-stranded DNA from free ends but does not act on double-stranded DNA.
A correctly hybridized padlock (circular) encoding probe has its 5' and 3' ends held in
duplex, so it should be protected. A probe bound incorrectly leaves exposed ssDNA ends,
so it should be digested.

To test this without relying on genuinely non-specific binding, a **linear** rRNA probe is
used as a stand-in for the exposed-end case and a **circular** rRNA probe for the protected
case. Both bind rRNA specifically; they differ in end structure.

**Measurement:** cytoplasmic fluorescence intensity per cell.

**A positive result** is Exo7 substantially reducing linear-probe signal while circular-probe
signal stays largely intact.

#### Read this before you start

The linear probe is doing double duty — it is both the test arm and the only check that the
Exo7 enzyme worked at all. If the linear signal does **not** drop, you cannot tell whether
the enzyme was inactive or the hypothesis is wrong. If that happens, do not discard the run;
flag it, because distinguishing those two cases needs a separate enzyme-activity control.

---

## 2. Conditions and plate layout

Ten wells, one plate, one plating batch. The two wells per condition are **technical**
replicates.

| Cond | Wells | Encoding probe | Exo7 | Readout probe |
| --- | --- | --- | :---: | --- |
| C1 | A1, A2 | linear-to-rRNA | **+** | YEH1 |
| C2 | A3, A4 | linear-to-rRNA | − (mock) | YEH1 |
| C3 | A5, A6 | circular-to-rRNA | **+** | YEH2 |
| C4 | A7, A8 | circular-to-rRNA | − (mock) | YEH2 |
| C5 | A9 | none | − (mock) | YEH1 |
| C6 | A10 | none | − (mock) | none |

C5 is the background for YEH1 binding without a target-specific encoder. C6 is bare
cell/plate autofluorescence.

**The well assignment above is a proposal** — the manifest does not fix physical wells.
Use it or change it, but write down what you actually used.

---

## 3. Reagents and stocks

| Item | Stock | Used for |
| --- | --- | --- |
| Poly-D-lysine | 0.1 mg/mL | plate coating |
| 3T3 cells | T75 flask | plating |
| Trypsin-EDTA | 0.5% | harvest |
| PFA | 32% | fixation |
| PBS, PBST + PVSA | — | washes, storage |
| Linear rRNA encoding probe | 100 nM | C1, C2 |
| Circular rRNA encoding probe | 100 nM | C3, C4 |
| YEH1 readout probe | 100 nM | C1, C2, C5 |
| YEH2 readout probe | 100 nM | C3, C4 |
| Formamide | 50% | both hybridizations |
| TBST | — | hybridization + washes |
| Exo7 | *record U/µL from the tube* | C1, C3 |
| TBE | 1× standard | Exo7 + mock |

---

## 4. Day 1 — plate, fix, and start encoding hybridization

Protocol: `pdl-coating-cell-plating-fixation` v0.1. All volumes below include **10% overage**.

#### 4a. Coat the plate

| Component | Per well | Total (10 wells + 10%) |
| --- | ---: | ---: |
| PDL, 0.1 mg/mL | 25 µL | **275 µL** |

1. Add 25 µL PDL per well. Incubate **1 h at room temperature**.
2. Wash 3× with PBS, enough to cover the surface each time.
3. Dry uncovered in the biosafety cabinet, **1 h**.

#### 4b. Harvest, count, and plate

Target is **10,000 cells per well in 50 µL**, i.e. a plating suspension at **200 cells/µL**.

| Quantity | Value |
| --- | ---: |
| Total plating suspension needed | **550 µL** |
| Total cells needed | **110,000** |
| Required suspension concentration | **200 cells/µL** |

1. Trypsinize with 2.5 mL 0.5% trypsin-EDTA per T75; detach and collect per the usual 3T3
   procedure; resuspend in complete medium.
2. Count cells and record the concentration below. **This run uses a total cell count, not
   a viability-gated count** — a deliberate deviation from the protocol, which specifies
   viable cells.
3. Compute and record:

| Fill in | Value |
| --- | --- |
| Measured concentration (cells/µL) | ______________ |
| Cell suspension volume = 110,000 ÷ measured conc. | ______________ µL |
| Medium to add = 550 − suspension volume | ______________ µL |

If the measured suspension is below 200 cells/µL it cannot reach target by dilution —
concentrate, recount, recompute.

4. Mix gently and plate 50 µL per well into all 10 wells.

#### 4c. Attachment period

Culture the cells before fixation. **Duration is not specified in the manifest or the
protocol — confirm with RJ before starting.**

#### 4d. Fix

| Component | Per well | Total (10 wells + 10%) |
| --- | ---: | ---: |
| PFA, 32% | 7.14 µL | **78.5 µL** |

1. Add 7.14 µL of 32% PFA directly into the 50 µL of medium in each well → 4% PFA in
   ~57 µL. **Fume hood, PFA is toxic.**
2. Incubate **20 min at room temperature**.
3. Dispose of fixative as hazardous waste.
4. Wash **3 × 5 min** with PBST + PVSA.

No separate permeabilization step — this fixation and wash serves that purpose.

#### 4e. Pre-hybridization washes and encoding-probe hybridization

Protocol: `encoding-hybridization-imaging` v0.2, steps 1–2.

1. Wash **3 × 5 min at 37 °C** in 20% formamide / TBST.
2. Prepare the three encoding mixes below. Each well receives **40 µL**; final probe
   concentration is **1 nM**, final formamide **20%**.

| Mix | Wells | Probe stock (100 nM) | Formamide 50% | TBST | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| **Linear** | A1–A4 (4) | 1.76 µL | 70.4 µL | 103.8 µL | 176 µL |
| **Circular** | A5–A8 (4) | 1.76 µL | 70.4 µL | 103.8 µL | 176 µL |
| **No-probe** | A9, A10 (2) | — | 35.2 µL | 52.8 µL | 88 µL |

Per well that works out to 0.4 µL probe stock + 16 µL formamide + 23.6 µL TBST
(24 µL TBST in the no-probe mix).

3. Add 40 µL of the appropriate mix to each well.
4. Incubate **overnight at 37 °C**.

---

## 5. Day 2 — Exo7, readout, imaging

Total hands-on plus incubation is roughly **4.5 h before imaging**.

#### 5a. Post-hybridization wash

Wash **2 × 10 min**. Buffer and temperature are assumed TBST at room temperature —
**not explicitly confirmed; check with RJ.**

#### 5b. Exo7 / mock incubation

This is the experimental variable. It is a run-specific step, not a canonical protocol.
**50 µL per well, 10 U Exo7 per treated well, 1× TBE, 3 h at 37 °C.**

All ten wells are on one plate and **must be incubated together for the same 3 h** — the
mock wells get buffer without enzyme so that the incubation itself is not a confound.

| Mix | Wells | Exo7 | TBE | Total |
| --- | --- | ---: | ---: | ---: |
| **+Exo7** | A1, A2, A5, A6 (4) | **44 U total** | to 220 µL | 220 µL |
| **Mock** | A3, A4, A7, A8, A9, A10 (6) | none | 330 µL | 330 µL |

The Exo7 **volume** depends on the tube's activity, which is not recorded in the manifest:

| Fill in | Value |
| --- | --- |
| Exo7 stock activity (U/µL) | ______________ |
| Exo7 volume = 44 U ÷ stock activity | ______________ µL |
| TBE = 220 µL − Exo7 volume | ______________ µL |

1. Add 50 µL of the appropriate mix to each well.
2. Incubate **3 h at 37 °C**, all wells together.

#### 5c. Wash

Wash **2 × 10 min** (TBST, room temperature — same assumption as 5a).

#### 5d. Readout-probe hybridization

Protocol: `encoding-hybridization-imaging` v0.2, step 4. **50 µL per well, 5 nM final probe,
10% final formamide, 30 min at room temperature.**

| Mix | Wells | Probe stock (100 nM) | Formamide 50% | TBST | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| **YEH1** | A1–A4, A9 (5) | 13.75 µL | 55.0 µL | 206.3 µL | 275 µL |
| **YEH2** | A5–A8 (4) | 11.0 µL | 44.0 µL | 165.0 µL | 220 µL |

Per well: 2.5 µL probe stock + 10 µL formamide + 37.5 µL TBST.

**A10 (C6) gets no readout probe.** Whether it should still receive 50 µL of probe-free
buffer for the same 30 min — matching the handling as the Exo7 mock does — is not specified.
Confirm with RJ; see the checklist in section 7.

#### 5e. Final wash and imaging

1. Wash **2 × 10 min** (TBST, room temperature — same assumption as 5a).
2. Image. **Acquisition settings are deliberately left to you at the scope** — set exposure
   and channels after checking signal, then record what you used in the table below.

| Setting | Value used |
| --- | --- |
| Microscope / objective | ______________ |
| Channel(s) and fluorophore | ______________ |
| Exposure time | ______________ |
| Illumination power | ______________ |
| Fields per well | ______________ |
| Z-range / step | ______________ |
| Pixel size / binning | ______________ |
| Output dataset ID | ______________ |

Keep settings **identical across all ten wells** — the comparison is between wells, so any
per-well change in exposure or power invalidates it.

---

## 6. What gets measured

Primary measurement is **cytoplasmic intensity per cell**. The planned comparisons are
+Exo7 vs −Exo7 within each probe type (C1 vs C2, C3 vs C4), then the relative change
between probe types. C5 and C6 serve as background references, not part of the primary
comparison.

Segmentation, background subtraction, and QC exclusions are intentionally not fixed in
advance — they will be chosen at analysis time.

---

## 7. Confirm before you start

1. Attachment/growth period between plating and fixation — not specified anywhere.
2. Wash buffer and temperature for the three 2 × 10 min washes — assumed TBST at room
   temperature, never confirmed.
3. Exo7 stock activity in U/µL, to convert 44 U into a volume.
4. Whether A10 (C6) receives probe-free buffer during the readout step.
5. Physical well assignment — confirm or replace the proposed A1–A10 map.

## 8. Known limitations of this design

These are recorded in the manifest and are accepted, not oversights:

1. **n = 2 technical replicates from one plating batch.** No biological replication; this is
   a pilot, not a quantitative result.
2. **The linear probe is both the test arm and the only Exo7 activity control** — a null
   result will be ambiguous.
3. **Only YEH1 has a background well (C5).** If YEH1 and YEH2 differ in non-specific
   binding, C3/C4 have no matched background.
4. **C6 measures general autofluorescence,** not whether the encoding probe itself
   fluoresces without a readout probe attached. Nothing in this design tests the latter.
5. **Cell counts are total, not viability-gated,** deviating from the plating protocol.
