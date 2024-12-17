# Here we'll generalize to 2D random walk for multiple particles and perform simple statistical analysis.
# A template using angles to generate x and y steps is provided. Similar to what we did in class for 1D 
# random walk, we'll generate all the Nparticles*Nsteps random steps we need all at once, so that no 
# for loop is needed.

# Next, instead of keeping track of all the trajectories using cumulative sums, let's perform a 
# simple sum (with appropriate axis arguments) for each particle to obtain their final positions.
# A plotting section to show all the final positions of the random walkers is provided. A sample image 
# is attached.

# Your code should simulate 1000 particles with 10000 steps. With proper vectorization, this should 
# take around one second.

# What is the average x and y position of all the final positions? Use np.mean() to find out. 
# Are they consistent with what you see in the final plot?

# Still looking at the final positions, what is the average radius r = sqrt(x^2 + y^2) measured from 
# the origin? Use np.mean() to find out. This measures the spread of the particles. 
# Confirm that this spread is around sqrt(Nstep) = sqrt(10000) = 100, same behavior as the 1D random 
# walk model.

import numpy as np
import matplotlib.pyplot as plt

def rw2d_multi(Np, Nstep):
    '''
    A simulation for 2D random walk.
    Np = the number of particles simulated
    Nstep = the number of steps each particle takes
    '''
    
    Ntep = int(Nstep)
    Np = int(Np)
    
    rng = np.random.default_rng()
    
    # Individual steps in x and y
    angles = rng.uniform(0, 2*np.pi, size=(Np,Nstep)) # a 2D array of dimensions Np x Nstep
    x_list = np.cos(angles)  # a 2D array of dimensions Np x Nstep
    y_list = np.sin(angles)  # a 2D array of dimensions Np x Nstep
    
    # Final x,y positions of all particles
    # No need eto record their trajectories
    x_final = np.sum(x_list, axis = 1) # a 1D array of size Np using np.sum
    y_final = np.sum(y_list, axis = 1) # a 1D array of size Np using np.sum
    
    fig, ax1 = plt.subplots(1)
    ax1.plot(x_final, y_final, 'ro')
    ax1.set_aspect('equal', 'box')
    plt.show()
    
    # In order to caclulate the average x and y positions consider
    avg_x = np.mean(x_final)
    avg_y = np.mean(y_final)
    print(f"Avg x of all final positions {avg_x}")
    print(f"Avg y of all final positions {avg_y}")
    
    # Obtaining the average radius r measured from the origin
    radius = np.sqrt(x_final**2 + y_final**2)
    avg_radius = np.mean(radius)
    print(f"Average radius: {avg_radius}")
    
rw2d_multi(Np= 1000, Nstep = 10000)

# All looking good here.
# ✔


    






