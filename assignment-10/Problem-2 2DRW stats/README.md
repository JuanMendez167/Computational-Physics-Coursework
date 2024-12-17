# Problem 2

Here we'll generalize to 2D random walk for multiple particles and perform simple statistical analysis. 

1. A template using angles to generate x and y steps is provided. Similar to what we did in class for 1D random walk, we'll generate all the Nparticles*Nsteps random steps we need all at once, so that no for loop is needed. 

Next, instead of keeping track of all the trajectories using cumulative sums, let's perform a simple sum (with appropriate axis arguments) for each particle to obtain their final positions.

A plotting section to show all the final positions of the random walkers is provided. A sample image is attached. 

Your code should simulate 1000 particles with 10000 steps. With proper vectorization, this should take around one second.

2. What is the average x and y position of all the final positions? Use np.mean() to find out. Are they consistent with what you see in the final plot?

3. Still looking at the final positions, what is the average radius r = sqrt(x^2 + y^2) measured from the origin? Use np.mean() to find out. This measures the spread of the particles. Confirm that this spread is around sqrt(Nstep) = sqrt(10000) = 100, same behavior as the 1D random walk model.
