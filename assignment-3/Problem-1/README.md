# Week 3 Assignment 1

Previously, we implemented the formula to compute the Lennard-Jones potential between two Argon atoms. Given the expression of the potential energy as a function of the distance between the atoms, it is possible to compute the magnitude of the force acting on atoms using the relation <a href="https://www.codecogs.com/eqnedit.php?latex=f(r)=-\frac{dU(r)}{dr}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(r)=-\frac{dU(r)}{dr}" title="f(r)=-\frac{dU(r)}{dr}" /></a>. 

TASK: Take the analytical derivative of the LJ potential energy to get the expression for the force. Write a program to compute the force between two Argon atoms, given their distance, using the parameters in the previous assignment.

EXPECTED OUTCOME: Test your results for three values of the distance. For large distances the force should be small and negative, for short distances the force should be large and positive. For one special distance (which we mentioned in class, expressing r in terms of sigma) the force should be equal to zero.  
