---
id: encoding-hybridization-imaging
name: Encoding- and readout-probe hybridization and imaging
version: 0.2
status: draft
inputs:
  well_count:
    type: integer
    minimum: 1
  probe_stock_concentration:
    type: number
    exclusive_minimum: 0
    description: Encoding-probe stock concentration recorded with explicit molar or mass-per-volume units.
  readout_probe_identity:
    type: string
    description: Readout-probe sequence/barcode, matched to the encoding probe(s) used in the run; defined per encoder, not fixed by this protocol.
  readout_probe_stock_concentration:
    type: number
    exclusive_minimum: 0
    required: false
    description: Readout-probe stock concentration, with explicit units. Left blank until supplied.
  readout_probe_final_concentration:
    type: number
    exclusive_minimum: 0
    required: false
    description: Readout-probe working concentration for hybridization. Left blank until supplied.
  master_mix_overage_percent:
    type: number
    minimum: 0
    required: false
parameters:
  hybridization_volume_per_well_ul:
    type: number
    fixed: 40
  probe_final_concentration_nm:
    type: number
    fixed: 1
  formamide_final_percent:
    type: number
    fixed: 20
  hybridization_temperature_c:
    type: number
    fixed: 37
  post_encoding_hybridization_wash_conditions:
    type: object
    description: Wash buffer, count, duration, and temperature selected for the run.
  readout_hybridization_temperature:
    type: string
    fixed: room temperature
  readout_formamide_final_percent:
    type: number
    fixed: 10
  readout_hybridization_duration:
    type: string
    description: Readout-probe hybridization duration. Left blank until supplied.
  readout_hybridization_volume_per_well_ul:
    type: number
    description: Readout-probe hybridization volume per well. Left blank until supplied.
  post_readout_hybridization_wash_conditions:
    type: object
    description: Wash buffer, count, duration, and temperature selected for the run.
  imaging_configuration:
    type: object
    description: Microscope and acquisition settings selected for the run.
outputs:
  - encoding-probe-hybridized samples and fluorescence images
dependencies:
  - protocol-id: pdl-coating-cell-plating-fixation
    path: ../pdl-coating-cell-plating-fixation/protocol.md
subprotocols: []
references:
  - protocol-id: phi29-rca
    path: ../phi29-rca/protocol.md
---

# Encoding- and readout-probe hybridization and imaging

## Purpose

Hybridize encoding probes to permeabilized cells under formamide-stringency conditions, wash away unbound probe, hybridize a matched fluorescent readout probe to the encoding probe under separate formamide-stringency conditions, wash away unbound readout probe, and acquire fluorescence images. This protocol contains no rolling circle amplification step; the encoding probe itself is not directly imaged — signal comes from the readout probe.

## Run inputs

Record these values when instantiating the protocol:

- Number of wells
- Encoding-probe identity
- Encoding-probe stock concentration, with explicit units
- Readout-probe identity, matched to the encoding probe(s) used
- Readout-probe stock and working concentration, with explicit units
- Readout-probe hybridization volume and duration
- Optional hybridization-mix overage percentage (applies to both hybridization steps)
- Post-encoding-hybridization wash conditions
- Post-readout-hybridization wash conditions
- Final imaging buffer
- Microscope and image-acquisition configuration

Assign sample conditions and physical wells in the experiment record rather than this protocol.

## Fixed hybridization conditions

| Parameter | Fixed value |
| --- | ---: |
| Pre-hybridization washes | 3 |
| Duration per pre-hybridization wash | 5 minutes |
| Pre-hybridization wash buffer | 20% formamide in TBST |
| Pre-hybridization wash temperature | 37°C |
| Hybridization volume | 40 µL per well |
| Final probe concentration | 1 nM |
| Final formamide concentration | 20% |
| Hybridization buffer | TBST |
| Hybridization temperature | 37°C |
| Hybridization duration | Overnight |

For the rRNA padlock-probe preparation represented by the source record, 1 nM is equivalent to 2 ng/µL. Do not use that mass concentration for a different probe unless its molecular weight supports the same conversion.

## Fixed readout-hybridization conditions

| Parameter | Fixed value |
| --- | ---: |
| Readout-hybridization temperature | Room temperature |
| Readout formamide concentration | 10% |
| Readout-hybridization buffer | TBST |

Readout-probe identity, concentration, hybridization volume, duration, and wash conditions are run-specific and are not fixed by this protocol; they must be supplied per run and are matched to the encoding probe(s) in use.

## Materials

- Permeabilized cells in a multiwell plate, produced by `pdl-coating-cell-plating-fixation` (dependency: complete plating and fixation before starting this protocol)
- TBST
- Formamide, 50%
- Encoding-probe stock
- Readout-probe stock, matched to the encoding probe(s) in use
- Run-specific post-encoding-hybridization wash buffer
- Run-specific post-readout-hybridization wash buffer
- Run-specific final imaging buffer

## Hybridization-mix preparation

Prepare 40 µL per well, plus any overage selected for the run.

### General 1 nM preparation

For a probe stock recorded in nM:

- Probe stock volume per well = `40 µL × 1 nM / probe stock concentration in nM`
- 50% formamide volume per well = 16 µL
- TBST volume per well = `40 µL − probe stock volume − 16 µL`

### rRNA padlock probe at 62 ng/µL

The source identifies 2 ng/µL as the 1 nM equivalent for this probe.

| Component | Stock concentration | Final concentration | Volume per 40 µL well |
| --- | ---: | ---: | ---: |
| rRNA padlock probe | 62 ng/µL | 2 ng/µL (1 nM) | 1.29 µL |
| Formamide | 50% | 20% | 16 µL |
| TBST | — | — | 22.71 µL |
| **Total** |  |  | **40 µL** |

Scale the applicable per-well formulation using the well count and any selected overage. The arithmetic is kept in the protocol because it is a direct dilution with no special rounding rule.

## Procedure

### 1. Pre-hybridization washes

1. Prepare 20% formamide in TBST.
2. Wash the permeabilized cells three times for 5 minutes per wash at 37°C.

### 2. Encoding-probe hybridization

1. Prepare the hybridization mixture containing 1 nM encoding probe and 20% formamide in TBST.
2. Add 40 µL of hybridization mixture to each well.
3. Incubate overnight at 37°C.

### 3. Post-encoding-hybridization washes

Record and perform the run-specific conditions:

- Wash buffer:
- Number of washes:
- Duration per wash:
- Temperature:

### 4. Readout-probe hybridization

1. Prepare the readout-hybridization mixture containing the readout probe matched to the encoding probe(s) in use, at its run-specific working concentration, in 10% formamide in TBST.
2. Add the run-specific hybridization volume to each well.
3. Incubate at room temperature for the run-specific duration.

### 5. Post-readout-hybridization washes

Record and perform the run-specific conditions:

- Wash buffer:
- Number of washes:
- Duration per wash:
- Temperature:
- Final imaging buffer:

### 6. Imaging

Record the microscope and acquisition settings in the experiment record.

#### Microscope

- Manufacturer and model:
- Acquisition software and version:
- Objective:
- Immersion medium:
- Camera or detector:
- Autofocus method:

#### Acquisition configuration

| Channel | Fluorophore/readout | Excitation | Emission | Exposure time | Illumination power |
| --- | --- | ---: | ---: | ---: | ---: |
|  |  |  |  |  |  |

- Imaging mode:
- Field or position selection:
- Number of fields per sample:
- Z-stack range:
- Z-step size:
- Binning:
- Pixel size:
- Image format:
- Output location or dataset ID:
- Additional acquisition settings:

## Safety

Handle formamide and all other reagents according to their safety data sheets and institutional laboratory procedures. Wear the required personal protective equipment and dispose of chemical and biological waste through the appropriate waste streams.

## Unresolved items

- Post-encoding-hybridization and post-readout-hybridization wash conditions and the final imaging buffer are run-specific and were not supplied in the source record.
- Microscope and acquisition settings were not supplied in the source record.
- The exact duration represented by "overnight" (encoding-probe hybridization) is not fixed.
- Readout-probe identity, stock/working concentration, hybridization volume, and hybridization duration are run-specific and were not supplied in the source record; readout probes are matched to the encoding probe(s) in use rather than fixed by this protocol.
- Resolved: the PFA-fixation/PBST-PVSA wash in `pdl-coating-cell-plating-fixation` is used as-is for permeabilization; no separate permeabilization step is inserted between the two protocols.
