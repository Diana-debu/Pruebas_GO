# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:13:32 2024

@author: USER2300
"""

from ase.io import read, write

# Leer el archivo .data de LAMMPS
atoms = read('C:/Users/Public/nuevacarpeta/Tesis/lammps_mmt/Curva_swelling/Intento_without_h2o/Estructura_python/finallmp', format='lammps-data')

# Escribir el archivo en formato .xyz
write('p_test_1.xyz', atoms)
