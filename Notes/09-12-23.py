# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:28:47 2023

@author: Juan
"""
# ODE with 1 variable/particle
import numpy as np
import matplotlib.pyplot as plt

# dt = 0.1
# t_range = np.arange(0,10,dt)
# g = 9.8 # in m/s^2

# zpos = 1
# zvel = 1
# zpos_list = []

# def move(zpos, zvel):
#     zpos += zvel * dt
#     zvel -= g * dt
#     return zpos, zvel

# for t in t_range:
#     zpos, zvel = move(zpos,zvel)
#     zpos_list.append(zpos)
    
# plt.figure(figsize=(4,2))
# plt.plot(t_range, zpos_list, 'k.')
# plt.xlabel('t [s]')
# plt.ylabel('x position [m]')


# ///////////////////////////////////////////////
# use ctrl + f to use replace

# Given boundary conditions, how to make use of numerical method
# x = x+a,  x+ = a, y = y * b, y *= b
# x(0) = 0, z = (0)

# Need to replace t_range -- xpos_list
# This is z vs x

dt = 0.01
t_range = np.arange(0,10,dt)
g = 9.8 # in m/s^2

zpos = 0
zvel = 10
xpos = 0
xvel = 3
zpos_list = []
xpos_list = []

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
    
    
plt.figure(figsize=(6,4))
plt.plot(xpos_list, zpos_list, 'k.')
plt.plot(xa, za, 'r-')
plt.ylim(0,10)


plt.xlabel('x position [m]')
plt.ylabel('z position [m]')

plt.savefig("save.pdf")
# When at ground z = 0, add bounce? Then think about
# Write an analytical expression




