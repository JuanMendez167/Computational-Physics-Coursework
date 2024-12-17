import numpy as np
import matplotlib.pyplot as plt

def rw2d_multi(Np, Nstep):
    '''
    A simulation for 2D random walk.
    Np = the number of particles simulated
    Nstep = the number of steps each particle takes
    '''
    
    Ntep = int(Nstep)
    Np = int(Np)
    
    rng = np.random.default_rng()
    
    # Individual steps in x and y
    angles = rng.uniform(0, 2*np.pi, size=(Np,Nstep)) # a 2D array of dimensions Np x Nstep
    x_list = np.cos(angles)  # a 2D array of dimensions Np x Nstep
    y_list = np.sin(angles)  # a 2D array of dimensions Np x Nstep
    
    # Final x,y positions of all particles
    # No need eto record their trajectories
    x_final = np.sum(x_list, axis = 1) # a 1D array of size Np using np.sum
    y_final = np.sum(y_list, axis = 1) # a 1D array of size Np using np.sum
    
    fig, ax1 = plt.subplots(1)
    ax1.plot(x_final, y_final, 'ro')
    ax1.set_aspect('equal', 'box')
    plt.show()
    
    # In order to caclulate the average x and y positions consider
    avg_x = np.mean(x_final)
    avg_y = np.mean(y_final)
    print(f"Avg x of all final positions {avg_x}")
    print(f"Avg y of all final positions {avg_y}")
    
    # Obtaining the average radius r measured from the origin
    radius = np.sqrt(x_final**2 + y_final**2)
    avg_radius = np.mean(radius)
    print(f"Average radius: {avg_radius}")
    
    #3D plotting section
    fig, ax = plt.subplots(1, subplot_kw=dict(projection="3d"))
    h, xbins, ybins = np.histogram2d(x_final,y_final, bins=10)
    
    # creating a mesh grid 
    xgrid, ygrid = np.meshgrid(xbins[:-1], ybins[:-1])
    bottom = 0*xgrid
    
    # width and depth of bar graph will be the bin size
    width = xbins[1]-xbins[0]
    depth = ybins[1]-ybins[0]
    
    # feed everything into bar3d!
    ax.bar3d(xgrid.flatten(), ygrid.flatten(), bottom.flatten(), width, depth, h.flatten(), shade=True)
    ax.set_title('2D Histogram for 2D Random Walk')
    
rw2d_multi(Np= 1000, Nstep = 10000)


# Plot works.
# Just missing the part to modify the thickness of the bars.
# -1 

