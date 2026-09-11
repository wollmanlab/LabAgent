---
id: phi29-rca
name: phi29 rolling circle amplification (RCA)
version: 0.1
status: draft
inputs:
  reaction_count:
    type: integer
    minimum: 1
  master_mix_overage_percent:
    type: number
    minimum: 0
    required: false
parameters:
  reaction_volume_ul:
    type: number
    fixed: 50
  sample_conditions:
    type: list
    description: Per-condition formamide wash, RCA primer, and priming settings.
  readout_probe_conditions:
    type: list
    description: Per-condition readout probe, fluorophore, concentration, and hybridization buffer.
  imaging_configuration:
    type: object
    description: Microscope and acquisition settings for the run.
outputs:
  - phi29-amplified rolling circle products ready for readout-probe detection and imaging
dependencies: []
subprotocols: []
references:
  - RAEFISH paper (full citation not supplied)
---

# phi29 rolling circle amplification (RCA)

## Purpose

Amplify primed, circularized padlock probes with phi29 DNA polymerase, hybridize readout probes to the resulting rolling circle products, and image the fluorescent signal.

## Run inputs

Record these values when instantiating the protocol for an experiment:

- Number of 50 µL reactions
- Optional master-mix overage percentage
- Sample-condition labels
- Formamide concentration for each pre-priming wash condition
- RCA primer identity and length for each sample condition
- Formamide concentration for each priming condition
- Readout-probe identities, fluorophores, concentrations, and hybridization buffers
- Readout-probe wash and hybridization conditions
- Microscope and image-acquisition configuration

Do not encode well identifiers in this protocol. Assign sample conditions to wells in the experiment record.

## Materials

- TBST
- Formamide
- RCA primer or primers
- Nuclease-free water
- dNTP mix, 10 mM
- DTT, 100 mM
- Recombinant albumin, 20 mg/mL
- Murine RNase inhibitor, 40 U/µL
- phi29 buffer, 10×
- phi29 DNA polymerase, 10 U/µL
- Readout probe or probes
- Run-specific readout hybridization and wash buffers
- Run-specific final imaging buffer

## Condition tables

Complete these tables in the experiment record before starting.

### RCA primer and formamide conditions

| Sample condition | Formamide wash concentration | RCA primer | Primer length | Primer concentration | Priming formamide concentration |
| --- | ---: | --- | ---: | ---: | ---: |
|  |  |  |  | 10 nM |  |

Different primer lengths may require different formamide wash conditions. The source run does not establish a general concentration rule; specify the concentration for each condition.

### Readout-probe conditions

| Sample condition | Readout probe | Fluorophore/channel | Probe concentration | Hybridization buffer |
| --- | --- | --- | ---: | --- |
|  |  |  |  |  |

## Procedure

### 1. Formamide washes

Wash three times for 5 minutes per wash at room temperature using the formamide concentration in TBST specified for each sample condition.

### 2. RCA primer hybridization

Prime for 30 minutes at room temperature with 10 nM of the assigned RCA primer in the run-specified concentration of formamide in TBST.

### 3. Post-priming washes and pre-RCA imaging

1. Wash three times for 10 minutes per wash with TBST at room temperature.
2. Image the orange and far-red channels using the run's imaging configuration.

### 4. Prepare the phi29 RCA reaction

Prepare one 50 µL reaction per well. The table contains the fixed per-well values required to scale a master mix for a future experiment.

| Component | Stock concentration | Final concentration or amount | Volume per 50 µL well |
| --- | ---: | ---: | ---: |
| Nuclease-free water | — | — | 36 µL |
| dNTP mix | 10 mM | 0.5 mM | 2.5 µL |
| DTT | 100 mM | 1 mM | 0.5 µL |
| Recombinant albumin | 20 mg/mL | 0.2 mg/mL | 0.5 µL |
| Murine RNase inhibitor | 40 U/µL | 20 U | 0.5 µL |
| phi29 buffer | 10× | 1× | 5 µL |
| phi29 DNA polymerase | 10 U/µL | 50 U | 5 µL |
| **Total** |  |  | **50 µL** |

Scale these per-well volumes using the reaction count and any chosen master-mix overage recorded for the experiment. This protocol does not prescribe a rounding rule or perform the calculation.

### 5. RCA incubation

Incubate at 30°C overnight.

### 6. Readout-probe washing and hybridization

Record and perform the run-specific conditions below.

#### Pre-hybridization wash

- Wash buffer:
- Number of washes:
- Duration per wash:
- Temperature:

#### Readout-probe hybridization

Hybridize each sample condition with its assigned readout probe.

- Hybridization volume per well:
- Hybridization duration:
- Hybridization temperature:

#### Post-hybridization wash

- Wash buffer:
- Number of washes:
- Duration per wash:
- Temperature:
- Final imaging buffer:

### 7. Final imaging

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

- The allowed or recommended formamide wash concentrations are intentionally run-specific; the source contained inconsistent values and did not establish a general selection rule.
- The source did not provide readout-probe wash, hybridization, or final imaging-buffer conditions.
- The source did not provide microscope or acquisition settings.
- The full citation for the RAEFISH paper remains to be added.
