import numpy as np
import matplotlib.pyplot as plt
g = 9.8 # in m/s^2
# y is xpos, svel, zpos, zvel
y = np.array([0,3,0,10])
zEuler_list = []
xEuler_list = []
zRK2_list = []
xRK2_list = []

mass = 0.1 # in Kg
b = 1 # in units of 1/s

def diffeq(y):
    xpos, xvel, zpos, zvel = y
    
    zacc = -g - b*zvel
    xacc = -b * xvel
    
    y = np.array([xvel, xacc, zvel, zacc])
    
    return y

def move_RK2(y):
    
    ydot = diffeq(y)
    y_half = y + 1/2 * ydot * dt
    
    ydot_half = diffeq(y_half)
    y = y + ydot_half * dt
    
    return y

def move_Euler(y):
    ydot = diffeq(y)
    y = y + ydot * dt

    return y

# Euler
dt = 0.0001
t_range = np.arange(0,20,dt)

for t in t_range:
    y = move_Euler(y)
    zEuler_list.append(y[2])
    xEuler_list.append(y[0])

# RK2 (Need to reinitialize particle)
dt = 0.1/2
t_range = np.arange(0,20,dt)
y = np.array([0,3,0,10])

for t in t_range:
    y = move_RK2(y)
    zRK2_list.append(y[2])
    xRK2_list.append(y[0])
    
fig, ax = plt.subplots(1)
ax.plot(xEuler_list, zEuler_list, 'b')
ax.plot(xRK2_list, zRK2_list, 'r.')

ax.set_ylim(0,10)
ax.set_xlabel('x position (m)')
ax.set_ylabel('z position (m)')

