# Week 1 Assignment 3

Debugging is one of the most important parts of computational thinking. Finding and fixing bugs (errors) is often a tedious task that requires to develop strategy and some good habits. 

The Lennard-Jones potential is a useful formula to describe the interaction between two atoms of a rare gas (like Argon). The potential energy of interaction of two atoms is expressed in terms of their distance as 

<img src="https://latex.codecogs.com/gif.latex?U^{LJ}(r)=4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}&space;\right&space;]" title="U^{LJ}(r)=4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6} \right ]" />

TASK: In this assignment you will need to fix a bug in the lennard-jones.py code provided, which calculates the energy of two atoms of Argon (for which <img src="https://latex.codecogs.com/gif.latex?\epsilon=4\cdot10^{-4}" title="\epsilon=4\cdot10^{-4}" /> atomic units and <img src="https://latex.codecogs.com/gif.latex?\sigma=6" title="\sigma=6" /> atomic units) as a function of a given distance.

EXPECTED OUTCOME: The code gives reasonable values of the Lennard-Jones potential (can you think of some distances for which you know the exact result?)
