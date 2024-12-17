import matplotlib.pyplot as plt
import numpy as np
import myode # this is the myode.py module we wrote in class, containing move_Euler() and move_RK2()

mass = 1    # Mass of each particle, kg
k = 1       # Spring constant connecting two particles, N/m
r_eq = 1.2   # Equilibrium spring length, m

def diffeq(y):
    # We fist unpack y
    x1, vx1, z1, vz1, x2, vx2, z2, vz2 = y  
    r12 = np.sqrt((x2 - x1)**2 + (z2 - z1)**2)
    
    # Calculate forces on particle 1
    ax1 = k * (r12 - r_eq) * (x2 - x1) / (mass * r12) # Acceleration along x for particle 1
    az1 = k * (r12 - r_eq) * (z2 - z1) / (mass * r12) # Acceleration along z for particle 1
    
    # Calculate forces on particle 2
    ax2 = -ax1 # Acceleration along x for particle 2
    az2 = -az1 # Acceleration along z for particle 2
    
    # Finally we return the time derivative of every argument, in the same order
    ydot = np.array([vx1, ax1, vz1, az1, vx2, ax2, vz2, az2])
    return ydot

omega = np.sqrt(2 * k / mass)  # Angular frequency of the oscillation
period = 2 * np.pi / omega    # Period of the oscillation
dt = period / 100  # dt chosen based on the timescale of the system, in seconds

t_total = 20 * period  # Total simulation time
t_range = np.arange(0, t_total, dt)

# Initialize positions and velocities for two particles
x1 = -0.5
z1 = -0.5
x2 = 0.5
z2 = 0.5
vx1 = vx2 = vz1 = 0
vz2 = 0.1

y = [x1, vx1, z1, vz1, x2, vx2, z2, vz2]
xr1 = []
zr1 = []
xr2 = []
zr2 = []
com_x = []  # Center of mass x position
com_z = []  # Center of mass z position

# Solve ODE using Runge-Kutta 2nd order and plot the position of the COM
for t in t_range:
    y = myode.move_RK2(diffeq, y, dt)
    xr1.append(y[0])  # x1
    zr1.append(y[2])  # z1
    xr2.append(y[4])  # x2
    zr2.append(y[6])  # z2
    
    # Calculate COM position
    com_x.append(0.5 * (y[0] + y[4]))
    com_z.append(0.5 * (y[2] + y[6]))

# Calculate and print the COM velocity (average velocity of both particles)
com_velocity_x = (com_x[-1] - com_x[0]) / t_total # final - initial
com_velocity_z = (com_z[-1] - com_z[0]) / t_total

print(f"Center of Mass Velocity (x): {com_velocity_x} m/s")
print(f"Center of Mass Velocity (z): {com_velocity_z} m/s")

# Plot the trajectories of particles and the COM
fig, ax = plt.subplots(1)
ax.plot(xr1, zr1, 'b.')
ax.plot(xr2, zr2, 'r.')
ax.plot(com_x, com_z, 'g-', label='Center of Mass')

ax.set_ylabel('y position')
ax.set_xlabel('x position')
ax.set_aspect('equal', 'box')
ax.legend()
plt.show()



