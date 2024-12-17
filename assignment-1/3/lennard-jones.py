# Week 1 Assigment 3
# Code to compute the value of the Lennard-Jones (LJ) potential for a pair of Argon atoms
# as a function of the separation between the atoms
# 
# Variables: 
#   epsilon and sigma: LJ parmeters in atomic units
#   distance: distance between atoms in atomic units
#   ulj: LJ potential in atomic units
#   If you are not familiar with atomic units, that's okay - just treat it as some unit. Knowing atomic units is not required to finish this task.

epsilon = 4.0e-4 # These are atomic units. 
sigma = 6 # Also atomic units
distance = float(input('Specify the separation between the atoms (in a.u.): '))
ulj = 4*epsilon*((sigma/distance)**12-(sigma/distance)**6)
print("The potential energy of two Argon atoms at a distance of %f a.u. is %f a.u." % (distance,ulj))

# You found it!✔
