# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 10:36:12 2023

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

mass = 0.1 # in Kg

# Analytical expression for x
xa = [xvel * t for t in t_range]
za = [zvel * t - 0.5*g*t**2 for t in t_range]

def move(zpos, zvel, xpos, xvel):
    zpos += zvel * dt
    zvel -= g * dt
    xpos += xvel *dt
    return zpos, zvel, xpos, xvel

for t in t_range:
    zpos, zvel, xpos, xvel = move(zpos,zvel, xpos, xvel)
    if zpos < 0:
        zvel = -zvel
    zpos_list.append(zpos)
    xpos_list.append(xpos)

fig, ax = plt.subplots(1)
ax.



