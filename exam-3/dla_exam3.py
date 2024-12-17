import numpy as np
import matplotlib.pyplot as plt

def rw2d(x0,y0,Nstep):
    # Task 1: Make a copy of the 2D Random Walk program that you wrote for Homework #9 as rw2d() in the template 
    # code. Modify it so that the particles trajectory starts from a coordinate x0,y0, instead of from the origin. The rw2d() function will return a 2D numpy array of dimensions Nstep x 2.

    Nstep = int(Nstep)
    rng = np.random.default_rng()
    
    # Individual steps in x and y components
    angles = rng.choice([0, 90, 180, 270], size=Nstep, replace=True) # generates an array of random angles
    x_list = np.cos(np.radians(angles)) # a 1D array of dimensions Nstep
    y_list = np.sin(np.radians(angles)) # a 1D array of dimensions Nstep
    
    #Generate the trajectories starting from x0 and y0
    x_traj_shifted = x0 + np.cumsum(x_list) # a 1D array of size Nstep using cumulative sum (shifted)
    y_traj_shifted = y0 + np.cumsum(y_list) # a 1D array of size Nstep using cumulative sum (shifted)
    
    # We will return a 2D array of dimensions Nstep x 2.
    # .T stands for taking the transpose
    return np.array([x_traj_shifted, y_traj_shifted]).T

def check_intersec(traj, cluster):
    """
    traj: a 2D array with dimensions Nsteps x 2. Needs to be all integers.
    cluster: a 2D array with dimensions Cluster Size x 2. Needs to be all integers.
    
    Description: This function searches for the first time traj intersects with cluster.
    
    Returns: the index of traj immediately before the intersection,
    i.e. the element in traj to be appended to the growing cluster.
    If there is no intersection, it returns -1.
    """
    traj    = np.around(traj).astype(int)
    cluster = np.around(cluster).astype(int)
    traj = traj[:,0]+traj[:,1]*1j
    cluster= cluster[:,0] + cluster[:,1]*1j
    
    intersec = np.where(np.isin(traj,  cluster ))[0]
    idx = -1 #default return value
    if len(intersec) > 0:
        idx = intersec[0] - 1
        #to prevent accidentally returning negative values
        if idx < 0 : 
            idx = -1
    return idx
            
def dla():
    rng = np.random.default_rng()
    
    #This is our starting cluster, two particles at [0,0] and [0,1]
    cluster = np.array([[0,0],[0,1]])
    
    #Number of steps. If wait times are long, start with fewer steps.
    Nparticle = 10000 
    for i in range(Nparticle):
        #A progress monitor
        if i%100==0: print(int(i/Nparticle*100),'%')
        
        # Task 2: Setup a starting radius "spawn_radius" from which mobile particles will spawn and perform 
        # random walk. It needs to be far enough from the growing cluster so that there's enough space for the 
        # particle to wander around before it sticks; but not too far so that it wastes too much simulation time 
        # to wait for the particle to be captured. To choose an appropriate spawn_radius, let's do the following.
        # Among all the anchored and immovable particles belonging to the existing cluster, find the one with 
        # the furthest distance cluster_max_radius from the origin. 
        
        # A good spawn_radius is around 2*cluster_max_radius. Note that this spawn_radius needs to grow as the 
        # cluster grows. 
        
        cluster_max_radius = np.max(np.linalg.norm(cluster, axis=1))
        spawn_radius = 2*cluster_max_radius
        
        # Task 3: We need to generate a random spawn coordinate x0, y0 for the particle somewhere on the 
        # spawn_radius one at a time. Then we need to convert those spawn coordinates to integers so that they 
        # belong to a square grid with step size 1 and also mainly because check_intersec() only works for 
        # integers. After this, we generare a trajectory for each spawned paeticle with 1e4 steps. 
        
        
        x0 = rng.uniform(-spawn_radius, spawn_radius)
        y0 = rng.uniform(-spawn_radius, spawn_radius)
        
        x0 = int(x0) # Converting spawn coordinates to ingegers
        y0 = int(y0) # Converting spawn coordinates to ingegers
        
        #Generate random walk trajector starting from x0,y0
        #We'll try 10000 steps.
        traj = rw2d(x0,y0,1e4)
        
        #This is a provided function that finds the correct coordinate where the particle sticks to the growing
        # cluster. Takes 2D arrays of dimensions Nstep x 2 and ClusterSize x 2 as input. No need to worry about 
        # how it works.
        idx = check_intersec(traj, cluster)
        if idx >0:
            cluster = np.append(cluster, [traj[idx]],axis=0)
    
    # Task 4: Plot the cluster you grew using points or circles. The shape should look fractal. 
    # Starting out, you can use fewer particles for quicker simulations and to debug your code. Then increase
    # your particle number to Nparticle=10000 to view larger clusters. You can use the provided 
    # print(int(i/Nparticle*100),'%') line to monitor simulation progress to make sure that the 
    # simulation will not take forever.
    
    # Task 5 : Divide the cluster data into five equal slices from the earliest to the latest arrivals. 
    # Plot each group of particles using a different color. You may either choose custom colors or 
    # simply run plt.plot() five times, which allows python to choose a different color every time by default. 
    
    r=100
    plt.figure()
    plt.xlim(-r,r)
    plt.ylim(-r,r)
    
    # Dividing the cluster data into 5 equal slices
    slice_size = len(cluster) // 5
    for i in range(5):
        start_idx = i * slice_size
        end_idx = (i+1) * slice_size
        plt.plot(cluster[start_idx:end_idx, 0], cluster[start_idx:end_idx, 1], marker='.', linestyle='', label = f'{i + 1}st Region')

    plt.legend(title='Order of Region Arrival')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Diffusion-Limited Aggregation (DLA) Simulation')
    plt.show()
    
    
dla()    

# %time dla()


#Task 1. Implement rw2d() starting from x0,y0.    
#20/20

#Task 2. cluster_max_radius and spawn_radius. 
#20/20

#Task 3. Spawn particles to perform RW.              
#10/20

#Task 4. Plotting.    
#20/20

#Task 5. Plotting with five slices.
#20/20

#Total 90/100


# Your rng.choice([-spawn_radius,spawn_radius]) line
# chooses initial positions from four discrete points,
# instead of from a random position on top of circle with radius = spawn_radius.
# Here we need a function that generates a random angle 
# with a uniform probability between 0 and 2pi;
# then combine the angle with spawn_radius to generate x0 and y0.


# Overall good job and nice way to set up plot legends! The minor bug in Task 3 doesn't seem to affect the result
# qualitatively but could create a bias if the simulation is run for longer times.