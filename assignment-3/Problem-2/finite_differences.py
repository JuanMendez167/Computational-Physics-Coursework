# Week 3 Problem 2
# Write a finite difference calculation of the Lennard-Jones force, plot it, and compare it with a plot from your previous analytical calculation.
#
#
# Variables: 
#   epsilon, sigma: parameters of the Lennard-Jones potential, in a.u.
#   dx: finite-difference parameter

import numpy as np
epsilon=4.e-4 # in a.u.
sigma=6 # in a.u.
rmin = 5.5
rmax = 10
dr = 0.0001

r_range = np.arange(rmin,rmax,dr)

def flj_analytical(r):
  #return the analytical result
  flj_ana_ans = (-48 * epsilon *(sigma)**12 / r**13) - (24 * epsilon * (sigma)**6 / (r)**7)
  return flj_ana_ans

def ulj(r):
    v = 4*epsilon*((sigma/r)**12-(sigma/r)**6)
    return v
    
def flj_numerical(r,dx):
    numerical = (ulj(r+dx) - ulj(r))/dx
    return numerical
 
flj_analytical_list = flj_analytical(r_range)
flj_numerical_list =  flj_numerical(r_range, 1.0e-6)

#plot two curves
import matplotlib.pyplot as plt
plt.figure(figsize=(7,4))

plt.plot(r_range, flj_analytical_list , 'k--')
plt.plot(r_range, flj_numerical_list , 'b-')

plt.xlabel("r [Bohr]")
plt.ylabel("ULJ(r) [Hartree]")


# Very close! Just missing a minus sign
# for both the analytical and numerical expressions.
#-0.5