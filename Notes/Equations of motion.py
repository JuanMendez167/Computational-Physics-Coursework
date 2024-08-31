# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:19:01 2023

@author: Juan
"""

# Integrating EOM
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
xpos= 1
xvel = 1
t_range = np.arange(0,2,dt)

xpos_list = []
xvel_list = []

def move(xpos, xvel):
    xpos = xpos + xvel * dt
    return xpos, xvel

for t in t_range:
    # xpos = xpos + xvel * dt
    xpos , xvel = move(xpos, xvel)
    xpos_list.append(xpos)
    xvel_list.append(xvel)
        
plt.plot(t_range, xpos_list, 'b-')
plt.plot(t_range, xvel_list, 'r-')
plt.xlabel("t [s]")
plt.ylabel;("x [m]")




