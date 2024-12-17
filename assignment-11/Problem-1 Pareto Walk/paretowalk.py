import numpy as np
import nd_rw as RW
import matplotlib.pyplot as plt

# Its important to realize that we are creating instances here, meaning we can work with methods from that class
lattice_2d = RW.LatticeWalk(2) # Creating instance
pareto_2d = RW.ParetoWalk(2) # Creating instance

Nstep = 1000
Nparticle = 1000

fig, ax = plt.subplots(3, figsize=(10, 15)) # Needed thhe figsize to scale the graphs dont look nice without it
ax[1].set_aspect('equal', 'box')
ax[2].set_aspect('equal', 'box')

# Use the _get_steps() method to obtain the step magnitudes of the two types of random walk
# (Nstep numbers for lattice_2d and Nstep numbers for pareto_2d),
# and plot a histogram of step magnitudes of each type.
bins = 100 # For the histogram

# Need to cconvert 2D arrays to 1D arrays, thereby, effectively treating all steps as a a single sequence
steps1 = lattice_2d._get_steps(Nstep).flatten()
steps2 = pareto_2d._get_steps(Nstep).flatten()

# Creating the histogram involving both types of walks
# Note: Alpha helps keep the bars transparent in histogram in order to be able to see both despite overlap 
ax[0].hist(steps1, bins=bins, range=(0, 10), alpha=0.5, label='Lattice Walk')
ax[0].hist(steps2, bins=bins, range=(0, 10), alpha=0.5, label='Pareto Walk')
ax[0].set_xlabel('X-Coordinate')
ax[0].set_ylabel('Y-Coordinate')
ax[0].legend()
ax[0].legend(loc='upper right') # For adjusting the legend position, it can get annoying

# Use the get_walk() method to obtain the trajectory of a particle doing
# lattice_2d walk and pareto_2d walk.
lattice_traj = lattice_2d.get_walk(Nstep)
pareto_traj = pareto_2d.get_walk(Nstep)

ax[1].plot(lattice_traj[0], lattice_traj[1], 'r-', label='Lattice Walk')
ax[1].plot(pareto_traj[0], pareto_traj[1], 'k-', label='Pareto Walk')
ax[1].set_xlabel('X-coordinate')
ax[1].set_ylabel('Y-coordinate')
ax[1].legend()
ax[1].legend(loc='upper right') # For adjusting the legend position, it can get annoying

# Use get_endpoints() method to obtain a scatter plot of 
# the final positions of 1000 particles
lattice_endpoints = lattice_2d.get_endpoints(Nparticle, Nstep)
pareto_endpoints = pareto_2d.get_endpoints(Nparticle, Nstep)

ax[2].scatter(lattice_endpoints[0], lattice_endpoints[1], c='r', marker='.', label='Lattice Walk')
ax[2].scatter(pareto_endpoints[0], pareto_endpoints[1], c='k', marker='.', label='Pareto Walk')
ax[2].set_xlabel('X-coordinate')
ax[2].set_ylabel('Y-coordinate')
ax[2].legend()
ax[2].legend(loc='upper right') # For adjusting the legend position, it can get annoying

plt.show()

# Graph 1 represents the step magnitudes
# Graph 2 represent the trajectories of particles in both walks
# Graph 3 represents the final position of the particles albeit in a scatter plot form

# My bad for being a little late, I was studying for another exam



# Plots 2 and 3 works.
# For Plot 1, _get_steps() returns 2D arrays that cannot go directly into hist.
# Need to convert to a 1D array of step magnitudes first. 
# You've flattened the step vectors, which gave you x and y components.
# That's why you see 0s and 1s in your first plot.

#-1


