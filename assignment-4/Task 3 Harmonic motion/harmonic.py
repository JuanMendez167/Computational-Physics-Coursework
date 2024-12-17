# # Week 5 Task 3

import numpy as np
import matplotlib.pyplot as plt

# Initialize the physical properties of the system
dt = 0.001  # Time step in seconds.
k = 1.0  # Spring constant in SI units
xeq = 0.0  # Equilibrium position of the particle on a spring
mass = 0.1  # Mass in kg

# The following is the function responsible to compute the elastic force
def felastic(k, xeq, x):
    """
    This function computes the value of the elastic force
    Input arguments:
        k: force constant of the spring;
        xeq: equilibrium position of the spring;
        x: position of the spring;
    Output results:
        elastic force
    """
    return -k * (x - xeq)

# The following is the function responsible to describe the motion of a single particle during a short timestep
def move(xpos, xvel, xforce, mass):
    """
    This function describes the motion of a single particle subject to a constant force.
    The particle's coordinates are updated according to the Euler algorithm.
    Input arguments:
        xpos: particle's coordinate along x;
        xvel: x-component of particle's velocity;
        xforce: x-component of particle's force;
        mass: mass of particle.
    Output results:
        update x components of particle's position and velocity
    """
    xpos = xpos + dt * xvel
    xacceleration = xforce / mass
    xvel = xvel + dt * xacceleration
    return xpos, xvel

# Initialize the configuration of the system
# We drag the particle 1m away from its equilibrium position
# and let go with zero velocity
xpos = 1.0
xvel = 0.0
t_range = np.arange(0, 10, dt)

# Numerical result
xn = []
for t in t_range:
    force = felastic(k, xeq, xpos)
    xpos, xvel = move(xpos, xvel, force, mass)
    xn.append(xpos)

# Analytical result
xa = []
for t in t_range:
    xa.append(xeq + np.cos(np.sqrt(k / mass) * t))

fig, ax = plt.subplots(1)
ax.plot(t_range, xn, 'b.', label= 'Numerical')
ax.plot(t_range, xa, 'r-', label= 'Analytical')

ax.set_ylim(-2, 2) # Ask yourself why these limits?
ax.set_xlim(0, 10)
ax.set_xlabel('Time [s]')
ax.set_ylabel('X Position [m]')
plt.title('Harmonic Motion: Numerical vs Analytic Solution')
plt.legend()
plt.savefig("Harmonic.pdf")

# Everything works here. ✔

# Problem 4 is missing
# -1.5
