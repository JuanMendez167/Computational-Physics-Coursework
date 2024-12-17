# Week 1 Assignment 4

As with many problems in science, there is often more than one way to program a math calculation. 
Although in analytical terms, these ways should be equivalent, in a numerical world we may get different results.
The hyperbolic sine function is defined as 

<img src="https://latex.codecogs.com/gif.latex?\sinh(x)=\frac{1}{2}\left(e^{x}-e^{-x}&space;\right&space;)" title="\sinh(x)=\frac{1}{2}\left(e^{x}-e^{-x} \right )" />. 

This operation can be computed in (at least) three different ways using python:

1. using the sinh() function of numpy
2. using the exp() function of numpy
3. using the value of Euler constant (e) from numpy and the builtin ** operator of Python 

TASK: Write a program that, when given a generic input value of x, computes the hyperbolic sine using the three approaches above

EXPECTED OUTCOME: for a value of <img src="https://latex.codecogs.com/gif.latex?x=2\pi" title="x=2\pi" /> the results should be 267.74489404101644 (approach 1 and 2) and 267.7448940410163 (approach 3).
