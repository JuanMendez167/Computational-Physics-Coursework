# Week 2 Assignment 4
# Write a code that computes the hyperbolic sine using three different formulas and numpy functions/constants. 
# Expected outcome: when testing for x = 2 \pi the results 
# should be 267.74489404101644, 267.74489404101644, and 267.7448940410163

import numpy as np
#method 1 using sinh() func of numpy
z = np.sinh(2*np.pi)
print(z)

# method 2 using the exp() func of numpy
y = 1/2 * (np.exp(2*np.pi) - np.exp(-2*np.pi))
print(y)


# method 3 using the value of Euler constant (e) from numpy and the builtin ** operator of Python
x = 2*np.pi
a = 1/2 *  (np.e ** x - np.e ** - x)
print(a)

#✔
