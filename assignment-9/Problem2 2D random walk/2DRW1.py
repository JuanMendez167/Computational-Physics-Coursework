import numpy as np
import matplotlib.pyplot as plt

'''In this assignment we will implement a 2D random walk model on a square lattice for one particle with proper 
vectorization. 
For every step in 2D, you'll make a choice between up, down, left, and right = [1,0], [0,-1], [-1,0], [0,1]. 
You may be tempted to write: x_list = rng.choice([-1,1]) and y_list = rng.choice([-1,1])
and stitch them together to form your steps, but then you'll run into diagonal steps like [1,1] every once in a 
while, which is not a valid move, so we have to find another way. One way is to generate a random array of 
angles (0,80,180,270 degrees) all at once and then convert them into x and y components using array operations. 
A template following this approach is provided, but feel free to use any other time-efficient approach you prefer.

You can use for loops for prototyping and vectorize things later. The final code should not contain any for loop.
At the end, a plotting section is provided to show the trajectory of the particle and its starting / ending points in green / red. 
A sample image is attached.'''
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# cumsum example
# Original Array: [1 2 3 4 5]
# Cumulative Sum: [ 1  3  6 10 15]

# Most critical here is converting the steps in x and y components
# size=Nstep argument specifies the number of values to generate
# replace=True allows for replacement (sampling with replacement), meaning the same value can be
#  chosen more than once.

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def rw2d(Nstep):
    """
    A simulation for 2D random walk for a single particle.
    Nstep = the number of steps each particle takes
    """

    Nstep = int(Nstep)
    rng = np.random.default_rng()

    # Individual steps in x and y components
    angles = rng.choice([0, 90, 180, 270], size=Nstep, replace=True) # generates an array of random angles
    x_list = np.cos(np.radians(angles)) # a 1D array of dimensions Nstep
    y_list = np.sin(np.radians(angles)) # a 1D array of dimensions Nstep
    
    # x, y trajectories of the particle
    x_traj = np.cumsum(x_list) # a 1D array of size Nstep using cumulative sum
    y_traj = np.cumsum(y_list) # a 1D array of size Nstep using cumulative sum
    
    # plotting
    fig, ax1 = plt.subplots(1)
    ax1.plot(0, 0, 'go')  # highlight the initial position
    ax1.plot(x_traj[-1], y_traj[-1], 'ro')  # highlight the final position
    ax1.plot(x_traj, y_traj, 'k-')  # particle trajectory
    ax1.set_aspect('equal', 'box')
    plt.show()

rw2d(Nstep=1e4)

# Code works and fully vectorized. ✔

