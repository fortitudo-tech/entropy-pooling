# Copyright (c) 2021-2024, Fortitudo Technologies
# This work is licensed under BSD 3-Clause "New" or "Revised" License:
# https://github.com/fortitudo-tech/entropy-pooling/blob/main/LICENSE

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entropy_pooling import ep
from fortitudo.tech import load_pnl

R = load_pnl()
