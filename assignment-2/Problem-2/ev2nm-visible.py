# Week 2 Assignment 2
#
# Code to convert energy (in eV) to wavelength (in nm) and determines if the energy of a photon is in the visible spectrum.

'''Loop the electron energy from 1.0 ev to 3,0 eV
in increments of 0.1 eV
report which case is red (620nm < 750nm))'''

h = 6.626e-34
c = 3e8
ev2J= 1.6e-19
m2nm = 1e-9

import numpy as np
    
for energy in np.arange(1.0, 3.1, 0.1):
    L= h * c / (energy * ev2J) / m2nm
    print("A photon with energy," ,  np.around(energy,1), "ev has a wavelength of", np.around (L,1), "nm")
    if 350 < L < 750:
        print("This photon is in the visible spectrum")
    
# This works.
# Just missing the part to detect the wavelength closest to 520nm.
# Also the problem is asking to use np.linspace() instead of np.arange()

#-0.5
