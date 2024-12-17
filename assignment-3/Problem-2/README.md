# Week 3 Assignment 2

Now that you've implemented an analytical formula for the forces between two Argon atoms interacting through an LJ potential, in this assignment, you will implement an approximate estimate of the force using finite differences. The derivative of a function can be written as the limit of the difference quotient:

<a href="https://www.codecogs.com/eqnedit.php?latex=f'(x)=\lim_{dx\rightarrow0}\frac{f(x&plus;dx)-f(x)}{dx}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f'(x)=\lim_{dx\rightarrow0}\frac{f(x&plus;dx)-f(x)}{dx}" title="f'(x)=\lim_{dx\rightarrow0}\frac{f(x+dx)-f(x)}{dx}" /></a>

Using this formula, we can compute the LJ force at a given separation between the atoms as 

<a href="https://www.codecogs.com/eqnedit.php?latex=F^{LJ}(r)=-\lim_{dx\rightarrow0}\frac{U^{LJ}(r&plus;dx)-U^{LJ}(r)}{dx}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F^{LJ}(r)=-\lim_{dx\rightarrow0}\frac{U^{LJ}(r&plus;dx)-U^{LJ}(r)}{dx}" title="F^{LJ}(r)=-\lim_{dx\rightarrow0}\frac{U^{LJ}(r+dx)-U^{LJ}(r)}{dx}" /></a>

TASK: Given the expression for the Lennard-Jones potential energy, compute the associated magnitude of the force between two atoms using the numerical approach sketched above and using a small *dx*: as this value becomes smaller, we approach the result of the analytical result. Write both this numerical expression and your previous analytical expression of LJ forces into functions, so that you can create lists of forces within a range of r. Finally, similar to what we did in class, using these two lists, plot the force calculated analytically and calculated numerically by finite differences.

EXPECTED OUTCOME: Two curves that should agree with each other within a small numerical error. Tip: To avoid two curves overlapping each other so that one curve becomes blocked by the other, plot one using a solid line and the other using dots.
