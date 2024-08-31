# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:15:29 2023

@author: Juan
"""

def move_RK2(diffeq, y, dt):
    ydot = diffeq(y)
    y_half = y + 0.5 * ydot * dt
    ydot_half = diffeq(y_half)
    y = y + ydot_half * dt
    # For a numpy array avoid doing the following
    # y += ydot * dt, shorthand only works for a scalar
    return y

def move_Euler(diffeq, y, dt):
    ydot = diffeq(y)
    y = y + ydot * dt
    return y

