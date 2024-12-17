"""
Task 2 (35 pts): 
        We will extend the previous program to *two* particles. 
        Here, instead of initializing xpos = some value for one particle, 
        we initialize a list of x positions for two particles,  xpos_all= [xpos of particle 1, xpos of particle 2].
        Same with xvel, ypos, and yvel.

        1. Copy the entire block of the move() function from the previous task. This block will stay the same.
        
        2. Complete the rest of the code to implement refective walls. Inspect your plot to make sure the code works.
        
        3. Reconstruct the two t_range loops to simplify them, by adding another layer of loop over the particles.
        
        Hint: One way to do this is (note the indentation)
            
        for i in range(2):
            #initialize empty lists to contain positions
            for t in t_range:
                # update positions and velocities of particle i
                # append xpos to a list and ypos to a list
            # make plots using these lists
           
        4. Add xlabel "x position [m]" and ylabel "y position [m]"
        
        
EXPECTED OUTCOME:   You should see the trajectories of two particles in a 2D box,
                    similar to the attached "2-sample.png" file.

"""

import matplotlib.pyplot as plt
import numpy as np

# Setup simulation parameters
dt = 0.02
t_range = np.arange(0,5,dt)


xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos_all =[0.0, 1.0]  #initial x position of particle 1 and 2; same below
xvel_all= [1.0, -0.07] 
ypos_all =[0.0, 0.0]
yvel_all =[0.3, 0.09]

# creating the lists
xpos_list = []
ypos_list = []

########################################################################
def move(xpos, xvel, ypos, yvel): 
    xpos += xvel * dt
    ypos += yvel * dt
    # credit goes to Jeffrey here as he recommended moving the if statements into
    # the move definion so that the code looks much cleaner and it wont have to be
    # repeated multiple times.
    if xpos < 0:
        xvel = -xvel
    if xpos > 1:
        xvel = -xvel
    if ypos < 0:
        yvel = -yvel
    if ypos > 1:
        yvel = -yvel
    return xpos, xvel, ypos, yvel
########################################################################

# Give credit to Abimelic he suggested nesting for loops, and thanks to the hint that you
# gave for condensing the lists.
for i in range(2):
    for t in t_range:
        xpos_all[i], xvel_all[i], ypos_all[i], yvel_all[i] = move( xpos_all[i], xvel_all[i], ypos_all[i], yvel_all[i])
        xpos_list.append(xpos_all)
        ypos_list.append(ypos_all)
        plt.plot(xpos_list, ypos_list, 'b.') # Why do only dots work?

plt.ylim(0,1)
plt.xlim(0,1)
plt.xlabel("x position [m]")
plt.ylabel("y position [m]")
# plt.savefig("Exam1_Task2.pdf")

###########################################################################

# Questions
# Why does plt.plot() only work if I use 'b.' for blue dotted lines? It drove me
# a little bit insane looking at the code trying to realize why it doesn't work if I use
# solid lines 'k-' to plot the trajectory as the lines no longer appear.




# This works ✔
# Good to acknowledge which line(s) you received help.

# The plotting issue is due to appending xpos_all instead of xpos_all[i].
# If you print out xpos_list you'll find that it's actually a list of lists.
# So when you're plotting xpos_list and ypos_list you see that unexpected behavior.
# Plotting with - will only show line segments between data points.
# Since all your xpos and ypos are isolated data points,
# there will be no line segments drawn.
# Instead, if you plot using dots, every point will show.

# In short, to avoid issues like this in the future, 
# it's safer to use one dimensional lists for each of the two arguments of plot()

