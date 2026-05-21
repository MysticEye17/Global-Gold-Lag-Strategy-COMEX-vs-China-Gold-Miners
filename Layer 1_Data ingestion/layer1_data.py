# Compatibility wrapper for legacy imports expecting `layer1_data`.
# Imports the main implementation in `layer1_data_1.py` and re-exports `load_all`.
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from layer1_data_1 import load_all, get_reserves_table  # type: ignore

__all__ = ["load_all", "get_reserves_table"]
