# Week 7 Problem 1 

In this problem we will simulate two particles connected by a spring, using an ODE solver of your choice to integrate the equation of motion. 

To calculate the force acting on each particle, we can start from the expression of the potential energy of the system

<a href="https://www.codecogs.com/eqnedit.php?latex=U^{el}=\frac{1}{2}k(r_{12}-r_{eq})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U=\frac{1}{2}k(r_{12}-r_{eq})^2" title="U=\frac{1}{2}k(r_{12}-r_{eq})^2" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=r_{12}=|r_1-r_2|=((x_1-x_2)^2+(z_1-z_2)^2)^\frac{1}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{12}=|r_1-r_2|=((x_1-x_2)^2+(z_1-z_2)^2)^\frac{1}{2}" title="" /></a>

is the distance between the two particles, <a href="https://www.codecogs.com/eqnedit.php?latex=r_{eq}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{eq}" title="r_{eq}" /></a> is the equilibrium position of the spring connecting particle 1 and 2, <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> is the force constant of that spring.

The force acting on particle i can be evaluated from the partial derivative of the expression above with respect to the position of particle i, namely

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i,x}=-\frac{\partial&space;U}{\partial&space;x_i}" title="f_{on\: i,x}=-\frac{\partial U}{\partial x_i}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i,z}=-\frac{\partial&space;U}{\partial&space;z_i}" title="f_{on\: i,z}=-\frac{\partial U}{\partial z_i}" /></a>

TASK 1: In the harmonic_motion.py program, choose a timestep dt based on the period of the two-particle oscillation. For example, dt = some number times period.

TASK 2: Finish the rest of the code. This includes the diffeq() function where you calculate all forces, choosing an ODE solver, and plotting the trajectories of the two particles. An example output using a the Runge-Kutta 2nd order solver is attached in "example trajectory.png".

TASK 3: On top of the existing plot, plot the trajectory of the center-of-mass of the two-particle system. Estimate the center-of-mass velocity and explain how it relates to the initial velocities and masses of the two particles provided in the simuation. If it's not clear to you why we're doing this or what motion are the two particles performing, proceed to Problem 2 and return back to this task later.



