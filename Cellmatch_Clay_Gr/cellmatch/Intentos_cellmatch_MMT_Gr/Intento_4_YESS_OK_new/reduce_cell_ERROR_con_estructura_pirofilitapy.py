import numpy as np
import spglib
from ase.io import read, write
from ase import Atoms

# Archivo de entrada y salida
input_file = 'CONTCAR_PIROFILITAPY.vasp'  # Cambia esto por tu archivo de entrada
output_file = 'output_unitcell.vasp'  # Cambia esto por tu archivo de salida

# Leer la estructura desde el archivo de entrada
structure = read(input_file)

# Obtener la celda, posiciones y números atómicos
cell = structure.get_cell()
positions = structure.get_positions()
numbers = structure.get_atomic_numbers()

# Convertir coordenadas cartesianas a coordenadas fraccionarias
scaled_positions = np.dot(positions, np.linalg.inv(cell))

# Estructura cristalina
celltot = (cell, scaled_positions, numbers)

# Encontrar la celda primitiva utilizando spglib - PROBLEMA
primitive_cell = spglib.find_primitive(celltot,symprec=1e-5)

if primitive_cell is None:
    raise ValueError('No se pudo encontrar una celda unitaria primitiva.')

# Desempaquetar la celda primitiva
lattice, scaled_positions, atomic_numbers = primitive_cell

# Convertir coordenadas fraccionarias de vuelta a cartesianas
reduced_positions = np.dot(scaled_positions, lattice)

# Crear una nueva estructura ASE con la celda primitiva
reduced_structure = Atoms(
    numbers=atomic_numbers,
    positions=reduced_positions,
    cell=lattice,
    pbc=True
)

# Guardar la nueva estructura en el archivo de salida
write(output_file, reduced_structure, format='vasp')
print(f'Estructura reducida guardada en: {output_file}')
