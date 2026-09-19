#!/usr/bin/env python3
"""Generate New Gold's pre-National-Dex Bug-Catching Contest encounter table.

The vanilla contest reads data/mushi/mushi_encount.bin directly instead of the
normal wild encounter NARC. Each BUGMON record is 8 bytes:

    u16 species, u8 min_level, u8 max_level, u8 rate, u8 score, u16 padding

This script replaces table 0 (the first 10 records) and preserves the three
post-National-Dex vanilla tables already present in the base ROM.
"""

from pathlib import Path
import struct

RECORD = struct.Struct("<HBBBBH")
TABLE_SIZE = 10 * RECORD.size

# Species IDs from include/constants/species.h
BUTTERFREE = 12
BEEDRILL = 15
SCYTHER = 123
PINSIR = 127
LEDIAN = 166
ARIADOS = 168
SHUCKLE = 213
HERACROSS = 214
ESCAVALIER = 639
GALVANTULA = 646

# Keep vanilla encounter probabilities: 20/20/10/10/10/10/5/5/5/5.
# "rate" is a descending threshold, not the slot's percentage.
# Levels are capped at 30: the contest is intended to be high-risk/high-reward
# around the Whitney level cap (30).
NEW_GOLD_TABLE_0 = [
    # species       min max rate score
    (BUTTERFREE,     20, 24, 80,  60),
    (BEEDRILL,       20, 24, 60,  60),
    (ARIADOS,        22, 26, 50,  60),
    (LEDIAN,         22, 26, 40,  60),
    (SHUCKLE,        23, 27, 30,  80),
    (SCYTHER,        23, 27, 20,  80),
    (PINSIR,         25, 28, 15,  80),
    (HERACROSS,      25, 28, 10,  80),
    (GALVANTULA,     27, 30,  5, 100),
    (ESCAVALIER,     27, 30,  0, 100),
]


def build_table() -> bytes:
    return b"".join(
        RECORD.pack(species, min_level, max_level, rate, score, 0)
        for species, min_level, max_level, rate, score in NEW_GOLD_TABLE_0
    )


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    target = root / "base/root/data/mushi/mushi_encount.bin"

    if not target.exists():
        raise SystemExit(
            f"{target} does not exist. Run make once so the base ROM filesystem "
            "is extracted before running this script."
        )

    original = target.read_bytes()
    if len(original) != 320:
        raise SystemExit(
            f"Unexpected mushi_encount.bin size: {len(original)} bytes (expected 320)."
        )

    table = build_table()
    assert len(table) == TABLE_SIZE == 80

    # Replace only the story/pre-National-Dex table. Preserve tables 1-3.
    target.write_bytes(table + original[TABLE_SIZE:])

    print(f"Patched {target}")
    print("Bug-Catching Contest table 0:")
    for species, lo, hi, rate, score in NEW_GOLD_TABLE_0:
        print(
            f"  species {species:3d}: Lv{lo}-{hi}, "
            f"threshold {rate:2d}, score {score}"
        )


if __name__ == "__main__":
    main()
