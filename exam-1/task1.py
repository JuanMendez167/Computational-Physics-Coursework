"""

TASK 1 (35 pts):  Consider a single particle moving in two dimensions. 
        The 2D box limits the movement of the particle between 0 and 1 in both the x and y directions, 
        with hard reflecting walls on all sides. 
        1. Complete the following code to simulated motion in 2D.
           Careful of the number of variables entering as arguments and the variables returned, 
           as well as their ordering! 
           Use the move() function call in the for loop as your hint.
           
        2. Implement the reflecting walls: if the particle hits any of the four walls, it should bounce back.
        
        3. Add xlabel "x position [m]" and ylabel "y position [m]"
        
        4. Comment on the trajectory of the particle you see. Where did it start and end?
            How many times did it hit the walls?
 
EXPECTED OUTCOME:   Here we will plot xpos against ypos, 
                    so that we can show a trajectory of a particle moving and bouncing inside a 2D box.
                    You should see the particle hit the walls of the 2D box many times, 
                    similar to the attached "1-sample.png" file.
 
Parameters and variables

    dt: length of the timestep (in seconds)
    xbox: size of box along the x axis (in meters)
    xpos: x component of particles positions (in meters)
    xvel: x component of particles velocities (in meters/second)
    ybox: size of box along the y axis (in meters)
    ypos: y component of particles positions (in meters)
    yvel: y component of particles velocities (in meters/second)
"""
import matplotlib.pyplot as plt
import numpy as np

# Setup simulation parameters
dt = 0.02 
t_range = np.arange(0,5,dt)

xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos=0.0 # initial x position
xvel=1.0 # initial x velocity
ypos=0.0 # initial y position
yvel=0.3 # initial y velocity

# creating the lists
xpos_list = []
ypos_list = []

def move(xpos, xvel, ypos, yvel): 
    xpos = xpos + xvel * dt
    ypos += yvel * dt
    return xpos, xvel, ypos, yvel

for t in t_range:
    xpos, xvel, ypos, yvel = move(xpos, xvel, ypos, yvel)
    # Implementing the reflecting walls through if statements
    if xpos < 0:
        xvel = -xvel
    if xpos > 1:
        xvel = -xvel
    if ypos < 0:
        yvel = -yvel
    if ypos > 1:
        yvel = -yvel
    xpos_list.append(xpos)
    ypos_list.append(ypos)
    
plt.plot(xpos_list, ypos_list, 'k--')

plt.ylim(0,1)
plt.xlim(0,1)
plt.xlabel("x position [m]")
plt.ylabel("y position [m]")
plt.savefig("Exam1_Task1.pdf")

# /////////////////////////////////////////////////////////////////////////////

# Commentary on the trajectory of the particle
# The initial coordinates of the particle are at (0,0) as the xpos_list and 
# ypos_list append and follows the flow of the if statements implementing the move 
# function in the for loop the ball bounces 6 times off the walls. Ending somewhere 
# along the coordinates (1,0.5). 

# /////////////////////////////////////////////////////////////////////////////

# Questions
# Why does the ball only bounce 6 times instead of infitely?
# A possible reason is due to t_range

# /////////////////////////////////////////////////////////////////////////////

# Mistakes
# My first mistake was considering an xvel_list as we are simply plotting the 
# xpos_list against the ypos_list. Furthermore my first approach towards the definition was
# incorrect as it is diffucult to explain consider the following example

# def move(xpos, xvel, ypos, yvel): 
#     xpos += xvel * dt                                                1st case
#     xpos = xpos + xvel * dt                                          2nd case
#     xpos += xpos + xvel * dt                                         3rd case

# The first two cases are correct and are allowed, the third one on the otherhand
# is not. Why is this the case? Well in the third case we pass xpos twice. How so? And why
# does that matter? First we need to understand the following operation += which in this
# case is the samething as updating the previous xpos case. So when we pass another xpos
# we get unexpected results.

# My final mistake was the structuring of the conditional blocks as I was using
# elif and else statements while passing my arguments instead of just using if in every case.
# the else statement would have never ran under the previous conditions.



# Everything works here. ✔
# Great effort on documenting your questions.
# You're right - it bounces 6 times because of the finite t_range. 
# If you extend t_range you'll see more motion.

# x += a means the same thing as x = x+a
# so if you write xpos += xpos +xvel*dt
# it's the same as saying xpos = xpos + (xpos+xvel*dt)
# which isn't what we want here.
