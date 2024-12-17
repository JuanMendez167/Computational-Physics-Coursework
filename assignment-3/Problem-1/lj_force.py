# Week 3 Problem 1
# Code to compute the force between two Argon atoms, starting from the Lennard-Jones expression of the potential energy. 
# 
# Variables: 
#   epsilon and sigma: LJ parmeters in atomic units
#   distance: distance between atoms in atomic units
#   flj: magnitude of the force acting on the atoms, with flj = -dU/dr

epsilon = 4.0e-4 # these are a.u.
sigma = 6 # also a.u.
distance = float(input("Choose your input distance in  a.u. : ")) #choose your input distance
flj = (48 * epsilon *(sigma)**12 / distance**13) - (24 * epsilon * (sigma)**6 / (distance)**7)
print("The force acting on two Argon atoms at a distance of ", distance, " a.u. is equal to", flj, " a.u.")

# ✔
