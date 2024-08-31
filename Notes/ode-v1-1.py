import numpy as np
import matplotlib.pyplot as plt
g = 9.8 # in m/s2
zpos = 0
zvel = 10
xpos = 0
xvel = 3
zEuler = []
xEuler = []
zRK2 = []
xRK2 = []

mass = 0.1 # in kg
b = 1 # in units of 1/s

def move_RK2(zpos,zvel, xpos, xvel):
    zacc = -g - b*zvel  
    xacc = -b * xvel
    
    zvel_half = zvel + 1/2* zacc * dt 
    zacc_half = -g - b*zvel_half
    
    xvel_half = xvel + 1/2* xacc * dt 
    xacc_half = - b*xvel_half
    
    zpos = zpos + zvel_half* dt
    zvel = zvel + zacc_half * dt
    
    xpos = xpos + xvel_half * dt
    xvel = xvel + xacc_half * dt
    return zpos, zvel, xpos, xvel

def move_Euler(zpos,zvel, xpos, xvel):
    zacc = -g - b*zvel  
    xacc = -b * xvel
    zpos = zpos + zvel* dt
    zvel = zvel + zacc * dt
    xpos = xpos + xvel * dt
    xvel = xvel + xacc * dt
    return zpos, zvel, xpos, xvel

#Euler
dt = 0.0001
t_range = np.arange(0,20,dt)

for t in t_range:
    zpos, zvel, xpos, xvel = move_Euler(zpos, zvel, xpos, xvel)
    zEuler.append(zpos)
    xEuler.append(xpos)

#RK2
# reinitialize positions and velocities for the second solution
dt = 0.1/2
t_range = np.arange(0,20,dt)

zpos = 0
zvel = 10
xpos = 0
xvel = 3

for t in t_range:
    zpos, zvel, xpos, xvel = move_RK2(zpos, zvel, xpos, xvel)
    zRK2.append(zpos)
    xRK2.append(xpos)

fig, ax = plt.subplots(1)
ax.plot(xEuler, zEuler, 'b.')
ax.plot(xRK2, zRK2 , 'r.')

ax.set_ylim(0, 10)
ax.set_ylabel('z position [m]')
ax.set_xlabel('x position [m]')
plt.tight_layout()
plt.show()