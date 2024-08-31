# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:10:00 2023

@author: Juan
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t_range = np.arange(0,10,dt)
g = 9.8 # in m/s^2

zpos = 0
zvel = 10
xpos = 0
xvel = 3
zpos_list = []
xpos_list = []
ke_list = []
pe_list = []
te_list = []

mass = 0.1 # in Kg

# Analytical expression for x
xa = [xvel * t for t in t_range]
za = [zvel * t - 0.5*g*t**2 for t in t_range]

def move(zpos, zvel, xpos, xvel):
    zpos += zvel * dt
    zvel -= g * dt
    xpos += xvel *dt
    return zpos, zvel, xpos, xvel

def fke(vx, vz):
    return 0.5 * mass  * (vx**2 + vz**2)

def fpe(z):
    return mass * z * g

for t in t_range:
    zpos, zvel, xpos, xvel = move(zpos,zvel, xpos, xvel)
    if zpos < 0:
        zvel = -zvel
    ke = fke(xvel, zvel)
    pe = fpe(zpos)
    te =  ke + pe
    zpos_list.append(zpos)
    xpos_list.append(xpos)
    ke_list.append(ke)
    pe_list.append(pe)
    te_list.append(te)
    
plt.figure(figsize=(6,4))
plt.plot(xpos_list, zpos_list, 'k.')
plt.plot(xa, za, 'r-')
plt.ylim(0,10)

plt.xlabel('x position [m]')
plt.ylabel('z position [m]')

# plt.savefig("save.pdf")

# For subplots
fig, ax = plt.subplots(2)
ax[0].plot(xpos_list, zpos_list)
ax[0].set_ylim(0,10)
ax[0].set_ylabel('z position [m]')
ax[0].set_xlabel('x position [m]')

ax[1].plot(t_range, ke_list,'r-')
ax[1].plot(t_range, pe_list,'b-')
ax[1].plot(t_range, te_list,'k-')
ax[1].set_xlabel("Time [S]")
ax[1].set_ylabel("Energy [J]")

plt.tight_layout()
plt.show()

# When at ground z = 0, add bounce? Then think about
# Write an analytical expression


# Local error and global error euler's rule
# ruge-katta method
