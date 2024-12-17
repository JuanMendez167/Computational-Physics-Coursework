import matplotlib.pyplot as plt
import numpy as np

# Task 1: We assume that the Sun is fixed at the origin (0,0) and that we know the perihelion 
# and aphelion (Earth-’s nearest and farthest point from the Sun respectively) to be 
# 147.1 million km and 152.1 million km. Make an analytical calculation of what the Earth’s 
# velocities are at these two points, v1 and v2.

# These are the constants to our problem
G = 6.67430e-11  # Gravitational constant in m^3/ (kg * s^2)
Msun = 1.989e30  # Solar mass in Kg
Me = 5.972e24  # Earth's mass in kg
R1 = 147.1e9  # Perihelion in m
R2 = 152.1e9  # Aphelion in m


from scipy.constants import G # Its the gravitaional constant

# Calculate Earth's velocities at perihelion and aphelion
v1_positive = np.sqrt(2 * G * Msun * (1 / R1 - 1 / (R1 + R2)))
v2_positive = np.sqrt(2 * G * Msun * (1 / R2 - 1 / (R1 + R2)))

v1_negative = -v1_positive
v2_negative = -v2_positive

# Display both sets of velocities
print("Velocities at Perihelion (Positive):", (v1_positive, v2_positive))
print("Velocities at Aphelion (Positive):", (v2_positive, v2_positive))
print("Velocities at Perihelion (Negative):", (v1_negative, v2_negative))
print("Velocities at Aphelion (Negative):", (v2_negative, v2_negative))

# Things get confusing as we have to take into account wether the velocity is positive or
# negative since a negative velocity indicates clockwise motion and a positive velocity counter
# clockwise motion. Things can get very easily complicated at this step if you think about it 
# too much. 

# //////////////////////////////////////////////////////////////////////////

# Task 2 
# Characteristic timescale
tau = np.sqrt((R1 ** 3) / (G * Msun)) # Notice we don't include aphelion here that because the
# perihelion is the distance of closest approach where the graviational forcest will be strongest.
# More simply, we are just taking into account the orbital period of an object in circular orbit.


# Choose a time step (smaller for improved accuracy)
dt = tau / 1000  # Because why not

# Total simulation time (one year)
t_total = 365 * 24 * 3600  # One year in seconds, its just easier because of SI units
t_range = np.arange(0, t_total, dt)

# ////////////////////////////////////////////////////////////////////////////

# Task 3
# Initial conditions
x0 = -R1  # Initial x-position in m, starting on the left side
y0 = [x0, 0, 0, v1_negative]  # Initial conditions using negative velocities

# Lists to store results
x_sol = []
z_sol = []
xvel_sol = []
zvel_sol = []

# Lists to store energy values
potential_energy = []
kinetic_energy = []
total_energy = []

# ///////////////////////////////////////////////////////////////////////////////////

# Task 4
# Define the differential equation
def diffeq(y):
    [xpos, xvel, zpos, zvel] = y
    r = np.sqrt(xpos**2 + zpos**2)
    xacc = -G * Msun * xpos / r**3
    zacc = -G * Msun * zpos / r**3
    ydot = np.array([xvel, xacc, zvel, zacc])
    return ydot

# Simulate the Earth's trajectory using the Runge-Kutta 2nd order method
for t in t_range:
    x_sol.append(y0[0])
    z_sol.append(y0[2])
    xvel_sol.append(y0[1])
    zvel_sol.append(y0[3])

    k1 = np.multiply(diffeq(y0), dt)
    k2 = np.multiply(diffeq(np.add(y0, k1)), dt)

    y0 = np.add(y0, (k1 + k2) / 2)

    # Calculate potential energy (including both Earth and Sun masses)
    r = np.sqrt(y0[0] ** 2 + y0[2] ** 2)
    potential_energy.append(-G * Msun * Me / r)

    # Calculate kinetic energy (using Earth's mass)
    kinetic_energy.append(0.5 * Me * (y0[1] ** 2 + y0[3] ** 2))

    # Calculate total energy
    total_energy.append(potential_energy[-1] + kinetic_energy[-1])
    
# Plotting section
fig, ax = plt.subplots()
ax.plot(0, 0, 'ro')
ax.text(0, 0, 'Sun', horizontalalignment='left', verticalalignment='bottom', color='red')

ax.plot(-R1, 0, 'k.')
ax.text(-R1, 0, 'Perihelion', horizontalalignment='left', verticalalignment='bottom')

ax.plot(R2, 0, 'k.')
ax.text(R2, 0, 'Aphelion', horizontalalignment='right', verticalalignment='bottom')

ax.plot(x_sol, z_sol, 'b-')

ax.set_ylabel('z position (m)')
ax.set_xlabel('x position (m)')
ax.set_title("Earth's Elliptical Orbit (Runge-Kutta 2nd Order)")
ax.set_aspect('equal', 'box')

# ////////////////////////////////////////////////////////

# Create a separate figure for energy plots
fig_energy, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 6))
plt.subplots_adjust(hspace=0.5)

# Plot potential energy
ax1.plot(t_range, potential_energy, label='Potential Energy')
ax1.set_ylabel('Energy (Joules)')
ax1.set_title('Potential Energy vs. Time')

# Plot kinetic energy
ax2.plot(t_range, kinetic_energy, label='Kinetic Energy', color='orange')
ax2.set_ylabel('Energy (Joules)')
ax2.set_title('Kinetic Energy vs. Time')

# Plot total energy
ax3.plot(t_range, total_energy, label='Total Energy', color='green')
ax3.set_xlabel('Time (seconds)')
ax3.set_ylabel('Energy (Joules)')
ax3.set_title('Total Energy vs. Time')

plt.show()

# /////////////////////////////////////////////////////////////////////////////
# Task 6
import matplotlib.pyplot as plt
import numpy as np

# The constants to our problem
G = 6.67430e-11  # Gravitational constant in m^3/ (kg * s^2)
Msun = 1.989e30  # Solar mass in kg
Me = 5.972e24  # Earth's mass in kg
R1 = 147.1e9  # Perihelion in m
R2 = 152.1e9  # Aphelion in m

# Calculate Earth's velocities at perihelion and aphelion
v1_positive = np.sqrt(2 * G * Msun * (1 / R1 - 1 / (R1 + R2)))
v2_positive = np.sqrt(2 * G * Msun * (1 / R2 - 1 / (R1 + R2)))

v1_negative = -v1_positive
v2_negative = -v2_positive

tau = np.sqrt((R1 ** 3) / (G * Msun))

dt = tau / 1000

# Total simulation time (200 years)
t_total = 200 * 365 * 24 * 3600  # 200 years in seconds

t_range = np.arange(0, t_total, dt)


x0 = -R1  # Initial x-position in m, starting on the left side
y0 = [x0, 0, 0, v1_negative]  # Initial conditions using negative velocities

# Lists to store results
x_sol = []
z_sol = []

# Simulate Earth's trajectory with the modified law of gravitation (exponent -3.02)
for t in t_range:
    x_sol.append(y0[0])
    z_sol.append(y0[2])

    # Calculate acceleration with the modified law
    r = np.sqrt(y0[0] ** 2 + y0[2] ** 2)
    xacc = -G * Msun * y0[0] / r ** 3.02
    zacc = -G * Msun * y0[2] / r ** 3.02

    y0[1] += xacc * dt
    y0[3] += zacc * dt
    y0[0] += y0[1] * dt
    y0[2] += y0[3] * dt

# Plotting section
fig, ax = plt.subplots()
ax.plot(0, 0, 'ro')
ax.text(0, 0, 'Sun', horizontalalignment='left', verticalalignment='bottom', color='red')

ax.plot(-R1, 0, 'k.')
ax.text(-R1, 0, 'Perihelion', horizontalalignment='left', verticalalignment='bottom')

ax.plot(R2, 0, 'k.')
ax.text(R2, 0, 'Aphelion', horizontalalignment='right', verticalalignment='bottom')

ax.plot(x_sol, z_sol, 'b-')

ax.set_ylabel('z position (m)')
ax.set_xlabel('x position (m)')
ax.set_title("Earth's Modified Trajectory (Runge-Kutta 2nd Order)")

plt.show()


#Task 1 on zvel1.       20/20pts
#Task 2 on dt.          10/10pts
#Task 3 on diffeq().    10/10pts
#Task 4 on move_RK2().  20/20pts
    # It would be a lot easier to use the myode.py module, but this is fine too.
#Task 5 on energies.    20/20pts
#Task 6 on r^-3.02.     10/20pts
    # missing description for task6.

#Total. 90/100
# Great effort writing detailed comments in your code!

