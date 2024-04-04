#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
from ase.io import read

atoms = read('POSCAR')
atomic_positions_fractional = atoms.get_scaled_positions()
c = atoms.cell.cellpar()[2]
lattice_vectors = atoms.cell

# Split atomic positions into two groups based on z-coordinate
z_coordinates = atomic_positions_fractional[:, 2]
less_than_0_5 = z_coordinates < 0.5
larger_than_0_5 = z_coordinates >= 0.5

z_coordinates_less_than_0_5 = z_coordinates[less_than_0_5]
z_coordinates_larger_than_0_5 = z_coordinates[larger_than_0_5]

# Calculate thickness
max_z_less_than_0_5 = np.max(z_coordinates_less_than_0_5)
min_z_larger_than_0_5 = np.min(z_coordinates_larger_than_0_5)
thickness = (min_z_larger_than_0_5 - max_z_less_than_0_5 ) *c
#thickness[ii, jj] = (max_z_less_than_0_5 - min_z_larger_than_0_5) * c
print(thickness)
