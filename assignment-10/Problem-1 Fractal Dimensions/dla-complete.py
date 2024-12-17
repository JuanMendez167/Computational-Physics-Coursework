# In class we demonstrated two general methods to calculate the fractal dimension of a given 
# shape. In this Problem we will show that, for the typical fractal "dendritic-shaped" pattern 
# formed in diffusion limited aggregation in Exam 3, its fractal dimension is 1.7 - the finger-
# like structures may remind you of one-dimensional shapes, but there are so many fingers 
# trying to fill up a two-dimensional plane, so the intuitive to expect that the fractal 
# dimension is somewhere between 1 and 2.

# We will use the first method discussed in class to show this. Using the DLA code from the
# template provided, calculate the number of particles n within a given radius r, as a 
# function of r (see "sample radius.png"). If the shape is fully two dimensional 
# (e.g. a filled circular disk), then n should scale as pi*r^2. If the shape is one 
# dimensional (e.g. a bar or line shape), then n should scale as r. 
# We can therefore make a generalized statement that for an arbitrary shape, n scales as
# r^(the dimension of the shape D).

# Calculate n for a range of r values. Since n = Cr^D (where C is some constant), 
# log(n) = log(C) + Dlog(r). So if we plot log(n) versus log(r), the slope will be D. 
# Draw several lines with slopes ranging from 1.5 to 2 and show that D is around 1.7. 
# A quick example figure "sample log-log plot.png" is attached showing slopes of 1.6, 1.7 and 
# 1.8.

import numpy as np
import matplotlib.pyplot as plt

def rw2d(x0,y0,N):
    N = int(N)
    
    rng = np.random.default_rng()
    angles = np.array(np.arange(0,360,90))
    stepx = np.cos(angles/180 * np.pi)
    stepy = np.sin(angles/180 * np.pi)
    step = np.transpose([stepx,stepy])
    
    hop_list = rng.choice(step,N)
    x = np.cumsum(hop_list[:,0])
    y = np.cumsum(hop_list[:,1])
    return np.array([x0+x, y0+y]).T
    
def check_intersec(traj, cluster):
    """
    traj: a 2D array with dimensions Nsteps x 2. Needs to be all integers.
    cluster: a 2D array with dimensions Cluster Size x 2. Needs to be all integers.
    
    Description: This function searches for the first time traj intersects with cluster.
    
    Returns: the index of traj immediately before the intersection,
    i.e. the element in traj to be appended to the growing cluster.
    If there is no intersection, it returns -1.
    """
    traj = np.around(traj).astype(int)
    cluster = np.around(cluster).astype(int)
    traj = traj[:,0] + traj[:,1] * 1j
    cluster = cluster[:,0] + cluster [:,1] * 1j
    
    intersec = np.where(np.isin(traj,cluster))[0]
    idx = -1 # Default return value
    if len(intersec) > 0 :
        idx = intersec[0] -1
        # To prevent accidentally returning negative values
        if idx < 0:
            idx = -1
    return idx

def dla():
    rng = np.random.default_rng()
    cluster = np.array([[0,0], [0,1]])
    
    Ns = 10000
    rs = [] # Initializing rs
    ns = [] # Initializing ns
    
    for i in range(Ns):
        cluster_max_radius = np.sqrt(cluster[:,0]**2 + cluster[:,1]**2).max()
        spawn_radius = cluster_max_radius * 2
        if i % 100 == 0:
            print(int(i/Ns *100), '%')
        angle = rng.uniform(0,2 * np.pi)
        x0, y0 = int(spawn_radius * np.cos(angle)), int(spawn_radius * np.sin(angle))
        traj = rw2d(x0, y0, 1e4)
        
        idx = check_intersec(traj, cluster)
        if idx > 0:
            cluster = np.append(cluster, [traj[idx]], axis=0)
            
        # We need to calculate the radius and the number of particles
        r = np.sqrt(cluster[:,0]**2 + cluster[:,1]**2).max()
        n = len(cluster)

        rs.append(r)
        ns.append(n)
        
    # Next, we need to convert the lists into numpy arrays
    rs = np.array(rs)
    ns = np.array(ns)

    # Afterwards, lets calculate the log values
    log_r = np.log(rs)
    log_n = np.log(ns)
        
    # Finally, we can begin plotting
    plt.figure()
    plt.scatter(log_r, log_n, marker='.', label='Logging Data')
        
    # We can expect lines with different slopes
    for slope in np.arange(1.5, 2.1, 0.1):
        plt.plot(log_r, slope * log_r, label = f'Slope = {slope:.1f}')
        
    plt.xlabel('log(r)')
    plt.ylabel('log(n)')
    plt.legend()
    plt.show()
    
    # Need to include the original dla plot
    xplot = cluster[:,0]
    yplot = cluster[:,1]
    
    r = 100
    intervals = 8
    color = plt.cm.rainbow(np.linspace(0, 1,intervals))
    plt.rcParams["axes.prop_cycle"] = plt.cycler("color", color )
    plt.figure()
    plt.xlim(-r,r)
    plt.ylim(-r,r)
    
    size = int(len(xplot)/intervals)
    for i in range(intervals):
        plt.plot(  xplot[i*size:(i+1)*size],   yplot[i*size:(i+1)*size] ,\
                  marker='.', linestyle='')
    print(len(xplot))

    plt.show()
    return cluster

dla()



#Very nice log-log plot.
# ✔






