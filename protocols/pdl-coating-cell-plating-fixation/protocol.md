---
id: pdl-coating-cell-plating-fixation
name: Poly-D-lysine coating, adherent-cell plating, and fixation
version: 0.1
status: draft
inputs:
  well_count:
    type: integer
    minimum: 1
  measured_viable_cells_per_ul:
    type: number
    exclusive_minimum: 0
  master_mix_overage_percent:
    type: number
    minimum: 0
    required: false
parameters:
  target_cells_per_well:
    type: integer
    fixed: 10000
  plating_volume_per_well_ul:
    type: number
    fixed: 50
  pdl_volume_per_well_ul:
    type: number
    minimum: 20
    maximum: 25
  pdl_concentration_mg_per_ml:
    type: number
    fixed: 0.1
outputs:
  - fixed adherent cells in a PDL-coated plate
dependencies: []
subprotocols: []
references: []
---

# Poly-D-lysine coating, adherent-cell plating, and fixation

## Purpose

Coat a plate with poly-D-lysine (PDL), harvest and count adherent cells, plate 10,000 cells per well in 50 µL, fix with 4% paraformaldehyde (PFA), and prepare the plate for short- or long-term storage.

## Run inputs

Record the following when instantiating this protocol:

- Number of wells
- PDL coating volume per well, selected from 20–25 µL
- Measured viable-cell concentration in cells/µL
- Optional preparation overage percentage
- Selected storage condition

## Fixed values and scalable quantities

| Item | Stock concentration | Final concentration or target | Quantity per well |
| --- | ---: | ---: | ---: |
| PDL coating solution | 0.1 mg/mL | 0.1 mg/mL | 20–25 µL |
| Cells in culture medium | Measured for each run | 10,000 cells in 50 µL | 50 µL |
| PFA | 32% | 4% after addition to 50 µL cell medium | 7.14 µL |

The required plating suspension concentration is 200 viable cells/µL. Use `calculations.py` to calculate run-specific PDL, cell suspension, culture-medium, and PFA quantities.

## Materials

- Cell-culture plate
- Poly-D-lysine, 0.1 mg/mL
- PBS
- Adherent cells in a T75 flask
- Trypsin-EDTA, 0.5%
- Appropriate complete culture medium
- Cell-counting equipment and viability reagent, if used
- PFA, 32%
- PBST containing PVSA
- 70% ethanol, for long-term storage

## Procedure

### 1. Coat the plate with PDL

1. Add 20–25 µL of 0.1 mg/mL PDL to each well, using the volume selected for the run.
2. Incubate for 1 hour at room temperature.
3. Wash three times with PBS, using enough PBS to cover the coated surface during each wash.
4. Leave the plate uncovered in the biosafety cabinet for 1 hour to dry.

### 2. Harvest adherent cells

1. Add 2.5 mL of 0.5% trypsin-EDTA per T75 flask.
2. Detach and collect the cells using the cell line's established culture conditions.
3. Resuspend the collected cells in an appropriate volume of complete culture medium.

### 3. Count and dilute the cells

1. Measure the viable-cell concentration and record it in cells/µL.
2. Calculate the required total plating volume from the well count, 50 µL per well, and any selected overage.
3. Calculate the volume of measured cell suspension required to supply 10,000 viable cells per well.
4. Add culture medium to reach a final plating suspension concentration of 200 viable cells/µL.
5. Mix gently and thoroughly before and during plating to maintain a uniform cell suspension.

If the measured suspension contains fewer than 200 viable cells/µL, it cannot reach the target in 50 µL by dilution. Concentrate the cells, recount them, and repeat the calculation.

### 4. Plate the cells

1. Add 50 µL of the 200 viable cells/µL plating suspension to each PDL-coated well.
2. Each well receives 10,000 viable cells.
3. Culture the cells for the experiment-specific attachment or growth period before fixation.

### 5. Fix the cells

1. Add 7.14 µL of 32% PFA directly to each well containing 50 µL of cell medium. This produces 4% PFA in a final volume of approximately 57.14 µL per well.
2. Incubate for 20 minutes at room temperature.
3. Remove the fixative according to institutional hazardous-waste procedures.
4. Wash three times for 5 minutes per wash with PBST containing PVSA, using enough buffer to cover the cells.

### 6. Store the fixed plate

Choose one storage condition:

- **Short-term:** PBST containing PVSA at 4°C.
- **Long-term:** 70% ethanol at −20°C.

Record the storage start time and condition in the experiment record.

## Safety

PFA is toxic and should be handled in a certified chemical fume hood with institutionally required personal protective equipment. Dispose of PFA waste through the designated hazardous-waste stream. Handle cell cultures and biological waste using the applicable biosafety procedures.

## Unresolved items

- The source does not specify the PBS or PBST-with-PVSA wash volume per well.
- The source does not specify trypsinization duration, detachment criteria, neutralization volume, or centrifugation conditions; use the established procedure for the cell line.
- The attachment or growth period between plating and fixation is experiment-specific.
- The source does not define the intended duration of short-term or long-term storage.

