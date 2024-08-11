#!/usr/bin/env python3

# This generates the same codeplug as generate.sh
# using python code.

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
    source_seattledmr=True,
    source_default_k7abd=False,
    source_k7abd=[(cp_dir / "k7abd")],
    source_repeaterbook_proximity=cp_dir / "prox.csv",
    repeaterbook_states=["washington", "oregon"],
    repeaterbook_name_format='{Nearest City}/{Landmark}/{Callsign}',
    exclude=cp_dir / "exclude.csv",
    order=cp_dir / "order.csv",
    replacements=cp_dir / "replacements.csv",
    output_opengd77=True
).generate(output / cp_dir.name)
