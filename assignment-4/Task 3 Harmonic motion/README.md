# Week 5 Task 3

In this project we will implement a code to simulate the motion of a particle subject to an elastic force. We will use the Euler method to integrate the equation of motion. 

The problem to solve is a second order differential equation in position and time. For a one-dimensional motion we have

<a href="https://www.codecogs.com/eqnedit.php?latex=f=-k(x-x_{eq})=ma=m\frac{d^2x}{dt^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f=-k(x-x_{eq})=ma=m\frac{d^2x}{dt^2}" title="f=-k(x-x_{eq})=ma=m\frac{d^2x}{dt^2}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=x_{eq}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{eq}" title="x_{eq}" /></a> is the equilibrium position of the spring, while <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> is the force constant.

For a linear restoring force we know the analytical solution of this problem

<a href="https://www.codecogs.com/eqnedit.php?latex=x(t)=x_0&plus;A\cos\left(\sqrt\frac{k}{m}&space;\:&space;t&space;&plus;\phi&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x(t)=x_{eq}&plus;A\cos\left(\sqrt\frac{k}{m}&space;\:&space;t&space;&plus;\phi&space;\right)" title="x(t)=x_{eq}+A\cos\left(\sqrt\frac{k}{m} \: t +\phi \right)" /></a>

where the amplitude <a href="https://www.codecogs.com/eqnedit.php?latex=A" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A" title="A" /></a> and the phase <a href="https://www.codecogs.com/eqnedit.php?latex=\phi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\phi" title="\phi" /></a> are quantities that depend on the initial conditions of the system.

TASK: Complete the missing pieces in the code to propagate the particle's motion in time using Euler's method. Visualize the trajectory of the particle undergoing simple harmonic motion, plotting its position x as against time t, both in physical units like meters and seconds. Compare the numerical trajectory with the exact solution for the motion. 

EXPECTED OUTCOME: For small enough timesteps (<=0.001), the numerical trajectory should be very close to the analytical result. An example figure is attached where the timestep is too large such that numerical errors are obvious.
