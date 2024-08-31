# In this quiz we start from the random walk class definitions provided in the Canvas module.
# In class we saved this as nd_rw.py in our working directory and worked on the following 
# script to create random walk objects in 1D, 2D, and 3D. At the end we plotted histograms of 
# the final distances of multiple particles (from the origin) for each case.

# Here, we will replace the final plotting section with two new plots - one showing the 
# trajectory of a single random walk particle on a 2D lattice, the other showing a scatter plot 
# of all the final positions of multiple 2D random walk particles.
# A sample output is given below. Each plot will only require one line of plt.plot(), using a 
# method already defined in the RandomWalk() superclass and LatticeWalk() subclass.

import nd_random_walks as rw
import numpy as np
import matplotlib.pyplot as plt

# Creating 1D, 2D, 3D LatticeWalk random objects
lattice1d = rw.LatticeWalk(1)
lattice2d = rw.LatticeWalk(2)
lattice3d = rw.LatticeWalk(3)

# Number of steps and particles
Nsteps = 100
Nparticles = 5

# Plotting the trajectory of a single walk particle on a 2D lattice
plt.figure()
single_walk_2d = lattice2d.get_walk(Nsteps)
plt.plot(*single_walk_2d, 'b-')
plt.title('Trajectory')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()

# Scatter plot of all the final positions of multiple 2D random walk particles.
plt.figure()
final_positions_2d = lattice2d.get_endpoints(Nparticles, Nsteps)
plt.scatter(final_positions_2d[0], final_positions_2d[1], c='m') # X and Y Coord
plt.title('Scatter Plot')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()


