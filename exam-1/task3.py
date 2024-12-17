"""
Task 3 (30 pts): We will extend the previous program to an arbitrary number of particles. 
                
    1. Copy everything in task 2 here, and replace the initial setup block with the block of code below. 
    Here you'll encounter a new function, np.random.uniform(a,b), which creates a random number between a an b.
    You'll won't need to modify this block.
                
    2. Comment on what this block is trying to achieve physically.
                
    3. Modify your code to extend the simulation to 10 particles, using a for loop over particles like in task 2. 
    (Duplicating the same simulation code 10 times for the 10 particles without using a for loop is not allowed.)
    
    Your trajectory plot will probably gets quite messy. Decrease the total simluation time from 5s to 0.5s
    to visualize just a short time after the simulation started.
                
    4. Add proper xlabels and ylabel as usual.
                
EXPECTED OUTCOME: A trajectory plot of 10 particles.

"""

import numpy as np
import matplotlib.pyplot as plt

# Setup simulation parameters
dt = 0.02
t_range = np.arange(0, 0.5,dt)

xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# creating the lists
xpos_list = []
ypos_list = []

# Setup starting configuration of the system
nparticles = 10 
xpos_all =[np.random.uniform(0, xbox)  for i in range(nparticles)  ] 
xvel_all= [np.random.uniform(-1,1   )  for i in range(nparticles)  ] 
ypos_all =[np.random.uniform(0, ybox)  for i in range(nparticles)  ]
yvel_all =[np.random.uniform(-1,1   )  for i in range(nparticles)  ] 

# The starting configuration of the system defines the numer of particles
# and randomizes the trajactory of the particle by randomizing the xpos, ypos, xvel, yvel
# where xbox and  ybox define the bounds of the particle.


########################################################################
def move(xpos, xvel, ypos, yvel): 
    xpos += xvel * dt
    ypos += yvel * dt
    if xpos < 0:
        xvel = -xvel
    if xpos > 1:
        xvel = -xvel
    if ypos < 0:
        yvel = -yvel
    if ypos > 1:
        yvel = -yvel
    return xpos, xvel, ypos, yvel
####################################################

for i in range(nparticles):
    for t in t_range:
        xpos_all[i], xvel_all[i], ypos_all[i], yvel_all[i] = move( xpos_all[i], xvel_all[i], ypos_all[i], yvel_all[i])
        xpos_list.append(xpos_all)
        ypos_list.append(ypos_all)
        plt.plot(xpos_list, ypos_list, 'b.') # Why do only dots work?

plt.ylim(0,1)
plt.xlim(0,1)
plt.xlabel("x position [m]")
plt.ylabel("y position [m]")
plt.show()

# Everything works here. ✔
# 100/100



