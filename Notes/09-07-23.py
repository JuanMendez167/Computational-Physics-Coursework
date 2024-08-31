# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:43:34 2023

@author: Juan
"""

def hello():
    print("Hello")
    
def sum_two(i,j,):
    print("Input = ", i, j)
    return i,j, i+j

# Tuples (immutable) and list (mutable)

def ULJ(r, epsilon=4e-4, sigma=6):
    V = 4*epsilon * ((sigma/r)**12 - (sigma/r)**6)
    return V

def finite_diff(f,r, dr):
    dfdr = (f(r+dr) - f(r)) / dr
    return dfdr
    
# Using DOC strings
    """
    Parameters
    _____________
    r:float
        r is the distance between 2 particles
    epsilon: float, optional
        energy scale. The default is 4e-4.
    sigma: float, optional
        length sccale. The dafult is 6.
        
    Returns
    ______________
    V: float
        LJ potential in AU
        
    """
    
# Integrating equations of motion




    


