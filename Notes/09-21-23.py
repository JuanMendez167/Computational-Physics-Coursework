import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t_range = np.arange(0,10,dt)
g = 9.8 # in m/s^2
zpos = 0
zvel = 10
xpos = 0
xvel = 3
zEuler_list = []
xEuler_list = []
zRK2_list = []
xRK2_list = []

mass = 0.1 # in Kg
b = 1 # in units of 1/s

def move_RK2(zpos, zvel, xpos, xvel):
    zacc = -g - b*zvel 
    xacc = -b * xvel
    
    zvel_half = zvel + 1/2 * zacc * dt
    zacc_half = -g - b*zvel_half
    
    xvel_half = xvel + 1/2 * zacc * dt
    xacc_half =- b*zvel_half 
    
    zpos += zvel_half * dt
    zvel += zacc_half * dt
    
    xpos += xvel + xvel_half *dt
    xvel += xacc_half * dt
    return zpos, zvel, xpos, xvel

def move_Euler(zpos, zvel, xpos, xvel):
    zacc = -g - b*zvel 
    xacc = -b * xvel
    
    zpos += zvel_half * dt # fix
    zvel += zacc_half * dt # fix
    
    zvel_half = zvel + 1/2 * zacc * dt
    zacc_half = -g - b*zvel_half
    
    xvel_half = xvel + 1/2 * zacc * dt
    xacc_half =- b*zvel_half 
    
    
    xpos += xvel + xvel_half *dt
    xvel += xacc_half * dt
    return zpos, zvel, xpos, xvel

# Euler
dt = 0.0001
t_range = np.arange(0,20,dt)

for t in t_range:
    zpos, zvel, xpos, xvel = move_Euler(zpos,zvel, xpos, xvel)
    if zpos < 0:
        zvel = -zvel
    zEuler_list.append(zpos)
    xEuler_list.append(xpos)

# RK2 (Need to reinitialize particle)
dt = 0.1/2
t_range = np.arange(0,20,dt)

zpos = 0
zvel = 10
xpos = 0
xvel = 3

for t in t_range:
    zpos, zvel, xpos, xvel = move_RK2(zpos,zvel, xpos, xvel)
    if zpos < 0:
        zvel = -zvel
    zRK2_list.append(zpos)
    xRK2_list.append(xpos)
    
fig, ax = plt.subplots(1)
ax.plot(xEuler, zEuler, 'b')
ax.plot(xRK2, zRK2, 'r.')

ax.set_ylim(0,10)
ax.set_xlabel('x position (m)')
ax.set_ylabel('z position (m) (Joules)')



