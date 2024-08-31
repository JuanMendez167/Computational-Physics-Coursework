# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:39:37 2023

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

fig, ax = plt.subplots(1)
ax.set_ylim(0,10)
ax.set_xlim(0,30)
plot1, = ax.plot([], [], 'go')

import matplotlib.animation as ani
def animate (i):
    plot1.set_data(xpos_list[i], zpos_list[i])
    
anim = ani.FuncAnimation(fig, animate, frames = len(t_range), interval=100, repeat = True)

# When at ground z = 0, add bounce? Then think about
# Write an analytical expression


# Local error and global error euler's rule
# ruge-katta method