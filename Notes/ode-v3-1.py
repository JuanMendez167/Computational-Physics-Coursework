import numpy as np
import matplotlib.pyplot as plt
import my_ode as myode


g = 9.8 # in m/s2
# zpos = 0
# zvel = 10
# xpos = 0
# xvel = 3
# y is xpos, xvel, zpos, zvel
y = np.array([0, 3, 0 ,10 ])
zEuler = []
xEuler = []
zRK2 = []
xRK2 = []

mass = 0.1 # in kg
b = 1 # in units of 1/s

def diffeq(y):
    xpos, xvel, zpos, zvel = y
    zacc = -g - b*zvel  
    xacc = -b * xvel
    ydot = np.array( [xvel, xacc , zvel, zacc])
    return ydot

def move_RK2(diffeq,y):
    ydot = diffeq( y )
    y_half = y + 1/2 * ydot * dt
    
    ydot_half  =  diffeq( y_half)
    y = y + ydot_half * dt
    return y

def move_Euler(diffeq, y, dt):
    ydot = diffeq( y )
    y = y + ydot * dt
    return y

#Euler
dt = 0.0001
t_range = np.arange(0, 20, dt)

for t in t_range:
    y = myode.move_Euler(diffeq, y, dt)  # Include dt argument
    zEuler.append(y[2])
    xEuler.append(y[0])

#RK2
# reinitialize positions and velocities for the second solution
dt = 0.05
t_range = np.arange(0, 20, dt)
y = np.array([0, 3, 0, 10])

for t in t_range:
    y = myode.move_RK2(diffeq, y, dt)  # Include dt argument
    zRK2.append(y[2])
    xRK2.append(y[0])

fig, ax = plt.subplots(1)
ax.plot(xEuler, zEuler, 'b.')
ax.plot(xRK2, zRK2 , 'r.')

ax.set_ylim(0, 10)
ax.set_ylabel('z position [m]')
ax.set_xlabel('x position [m]')
plt.tight_layout()
plt.show()