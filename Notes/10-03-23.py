# This is another aproach that manages to plot the potential energy given np.arange
# except this does not use a for loop. Either section works as intended. 
import numpy as np
import matplotlib.pyplot as plt

sigma = 6.0
epsilon = 4e-4

rmin = 5.5
rmax = 10.0
dr = 0.01

def ULJ(r):
    V = 4*epsilon*((sigma/r)**12 - (sigma/r)**6)
    return V

r_array = np.arange(rmin, rmax, dr)
V_array = 4*epsilon*((sigma/r_array)**12 - (sigma/r_array)**6)

plt.plot(r_array, V_array, 'k-')

plt.xlabel("r [Bohr]")
plt.ylabel("VLJ(r) [Hartree]")
plt.show()