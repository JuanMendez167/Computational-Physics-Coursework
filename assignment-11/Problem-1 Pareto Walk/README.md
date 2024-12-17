In this problem we will explore a special type of random walk – Pareto Walk in 2D – included as one of the classes defined in nd_rw.py. In Pareto Walk, a particle can take steps in any directions and random magnitudes. The particle will make small frequent small steps and occasional long steps. We will compare it with random walk on a 2D square lattice, which we are familiar with.

- Use the _get_steps() method to obtain the step magnitudes of the two types of random walk (Nstep numbers for lattice_2d and Nstep numbers for pareto_2d), and plot a histogram of step magnitudes of each type of random walk. The average step size of both types of random walk is 1. 

- Use the get_walk() method to obtain the trajectory of a particle doing lattice_2d walk and pareto_2d walk. Write a comment on how Pareto Walk looks different from good ol' 2D square lattice random walk.

- Use get_endpoints() method to obtain a scatter plot of the final positions of 1000  particles for each type of walk, to show that Pareto Walk has a larger coverage (even though its mean step size is the same).

A sample output figure of the result is attached.

Many animals adopt Pareto Walk as a strategy to search for food: when wandering around an area carefully in small steps is not helpful, it's more efficient to leave the area in long jumps toward somewhere else to continue careful exploring in small steps.

See more at https://en.wikipedia.org/wiki/L%C3%A9vy_flight
