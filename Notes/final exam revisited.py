import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
import myode

epsilon = 4e-4 * 27.211 * 1.6e-19  # in J
bohr = 0.53e-10
sigma = 2.4 * bohr  # in m
mass = 40 * 1e-3 / 6.02e23  # in kg

gridsize = 4
nparticles = gridsize**2
R = 10 * bohr  # Our simulation box is a square that spans -R to +R in both the x and y directions.

# Parameters for Morse potential
De = epsilon
re = 2**(1/6) * sigma
a = np.sqrt(18 / (2**(1/3) * De / sigma**2))  # Adjusted based on Task 1 question

# For question 5 we probably need np.random.default_rng, but where to adjust velocities?
# Question 7, need numpy.std() and numpy.mean()

# Replace LJ potential-related functions with Morse potential-related functions
def fmorse(x):
    return -De * (1 - np.exp(-a * (x - re)))**2

def calc_forces(position):
    forces = np.zeros((nparticles, 2))
    
    for i in range(nparticles):
        for j in range(i+1, nparticles):
            x1, z1 = position[i]
            x2, z2 = position[j]
            r12 = np.sqrt((x1 - x2)**2 + (z1 - z2)**2)
            f = fmorse(r12)

            forces[i, 0] += f * (x1 - x2) / r12
            forces[i, 1] += f * (z1 - z2) / r12
            forces[j, 0] -= forces[i, 0]
            forces[j, 1] -= forces[i, 1]

    return forces

# initial positions
xpos = np.linspace(-0.9 * R, 0.9 * R, gridsize)
zpos = np.linspace(-0.9 * R, 0.9 * R, gridsize)
xgrid, zgrid = np.meshgrid(xpos, zpos)
y = np.zeros(4 * nparticles)
y[0:2 * nparticles:2] = xgrid.flatten()
y[1:2 * nparticles:2] = zgrid.flatten()

# initial velocities
rng = np.random.default_rng()
v = rng.uniform(-1, 1, size=nparticles * 2) * 1e2
y[2 * nparticles:] = v

t_total = 500  # Adjusted for the animation to be reasonable
dt = 0.1
t_range = np.arange(0, t_total, dt)
y_list = []

for t in t_range:
    y = myode.move_RK2(myode.diffeq, y, dt)
    
    # Task 6: Implement Periodic Boundary Conditions
    for i in range(2 * nparticles):
        if abs(y[i]) > R:
            y[i] = np.sign(y[i]) * R  # Set the position back to the boundary
            y[i + 2 * nparticles] = -y[i + 2 * nparticles]  # Invert the velocity

    y_list.append(y)

y_list = np.array(y_list)

# Task 7: Calculate Statistics at the Last Timestep
average_kinetic_energy = np.mean(0.5 * mass * y_list[-1, 2 * nparticles:]**2)
std_deviation_kinetic_energy = np.std(0.5 * mass * y_list[-1, 2 * nparticles:]**2)
print("Average Kinetic Energy:", average_kinetic_energy, "J")
print("Standard Deviation of Kinetic Energy:", std_deviation_kinetic_energy, "J")

fig, ax = plt.subplots(1)
ax.set_aspect('equal', 'box')
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
a, = ax.plot([], [], 'go')

def animate(i):
    a.set_data(y_list[i, 0:2 * nparticles:2], y_list[i, 1:2 * nparticles:2])
    return a,

animation = anim.FuncAnimation(fig, animate, frames=len(t_range), interval=50, repeat=True, blit=True)
plt.show()