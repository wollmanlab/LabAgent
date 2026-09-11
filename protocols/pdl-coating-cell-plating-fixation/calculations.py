#!/usr/bin/env python3
"""Scale per-well quantities for the PDL coating and cell-fixation protocol."""

from __future__ import annotations

import argparse
import json


TARGET_CELLS_PER_WELL = 10_000
PLATING_VOLUME_PER_WELL_UL = 50.0
REQUIRED_PLATING_CONCENTRATION_CELLS_PER_UL = (
    TARGET_CELLS_PER_WELL / PLATING_VOLUME_PER_WELL_UL
)
PFA_STOCK_PERCENT = 32.0
PFA_FINAL_PERCENT = 4.0
PFA_VOLUME_PER_WELL_UL = (
    PFA_FINAL_PERCENT * PLATING_VOLUME_PER_WELL_UL
    / (PFA_STOCK_PERCENT - PFA_FINAL_PERCENT)
)


def calculate(
    well_count: int,
    measured_viable_cells_per_ul: float,
    pdl_volume_per_well_ul: float,
    overage_percent: float = 0.0,
) -> dict[str, float | int]:
    """Return scaled preparation quantities with explicit units."""
    if well_count < 1:
        raise ValueError("well_count must be at least 1")
    if measured_viable_cells_per_ul <= 0:
        raise ValueError("measured_viable_cells_per_ul must be greater than 0")
    if not 20.0 <= pdl_volume_per_well_ul <= 25.0:
        raise ValueError("pdl_volume_per_well_ul must be between 20 and 25")
    if overage_percent < 0:
        raise ValueError("overage_percent must be nonnegative")
    if measured_viable_cells_per_ul < REQUIRED_PLATING_CONCENTRATION_CELLS_PER_UL:
        raise ValueError(
            "measured cell suspension is below 200 viable cells/uL; "
            "concentrate and recount before preparing the plating suspension"
        )

    scale = well_count * (1.0 + overage_percent / 100.0)
    total_cells = TARGET_CELLS_PER_WELL * scale
    total_plating_volume_ul = PLATING_VOLUME_PER_WELL_UL * scale
    measured_cell_suspension_volume_ul = total_cells / measured_viable_cells_per_ul
    culture_medium_volume_ul = (
        total_plating_volume_ul - measured_cell_suspension_volume_ul
    )

    return {
        "well_count": well_count,
        "overage_percent": overage_percent,
        "target_cells_per_well": TARGET_CELLS_PER_WELL,
        "plating_volume_per_well_ul": PLATING_VOLUME_PER_WELL_UL,
        "required_plating_concentration_cells_per_ul": (
            REQUIRED_PLATING_CONCENTRATION_CELLS_PER_UL
        ),
        "total_cells_required": total_cells,
        "total_plating_volume_ul": total_plating_volume_ul,
        "measured_cell_suspension_volume_ul": measured_cell_suspension_volume_ul,
        "culture_medium_volume_ul": culture_medium_volume_ul,
        "total_pdl_volume_ul": pdl_volume_per_well_ul * scale,
        "pfa_stock_percent": PFA_STOCK_PERCENT,
        "pfa_final_percent": PFA_FINAL_PERCENT,
        "pfa_volume_per_well_ul": PFA_VOLUME_PER_WELL_UL,
        "total_pfa_volume_ul": PFA_VOLUME_PER_WELL_UL * scale,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--well-count", type=int, required=True)
    parser.add_argument(
        "--measured-viable-cells-per-ul", type=float, required=True
    )
    parser.add_argument("--pdl-volume-per-well-ul", type=float, required=True)
    parser.add_argument("--overage-percent", type=float, default=0.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = calculate(
        well_count=args.well_count,
        measured_viable_cells_per_ul=args.measured_viable_cells_per_ul,
        pdl_volume_per_well_ul=args.pdl_volume_per_well_ul,
        overage_percent=args.overage_percent,
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
