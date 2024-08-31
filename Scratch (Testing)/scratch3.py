# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as ani

# # Initialization
# dt = 0.1
# t_range = np.arange(0, 10, dt)
# xpos = 0
# xvel = 3
# zpos = 0
# zvel = 10
# zpos_list = []
# zvel_list = []
# xpos_list = []
# g = 9.8
# mass = 0.1

# # Energy Calculation Functions
# def KineticE(v):
#     return 0.5 * mass * v**2

# def PotentialE(zpos):
#     return mass * g * zpos

# # Lists for Energy Storage
# KEn = []
# PEn = []
# TEn = []

# # Physics Simulation
# def move(zpos, zvel, xpos, xvel):
#     zpos += zvel * dt
#     zvel -= g * dt
#     xpos += xvel * dt
#     return zpos, zvel, xpos, xvel

# xa = [xvel * t for t in t_range]
# za = [zvel * t - 0.5 * g * t**2 for t in t_range]

# # Simulation Loop
# for t in t_range:
#     zpos, zvel, xpos, xvel = move(zpos, zvel, xpos, xvel)
#     if zpos < 0:
#         zvel = -zvel
#     zvel_list.append(zvel)
#     xpos_list.append(xpos)
#     zpos_list.append(zpos)
#     KE = KineticE(np.sqrt(xvel**2 + zvel**2))
#     PE = PotentialE(zpos)
#     KEn.append(KE)
#     PEn.append(PE)
#     TEn.append(KE + PE)

# # Plotting
# fig, ax = plt.subplots(2)
# ax[0].set_ylim(0, 10)
# ax[0].set_xlim(0, 30)
# ax[0].set_ylabel('z position')
# ax[0].set_xlabel('x position')

# ax[1].set_ylabel('energies [J]')
# ax[1].set_xlabel('t [s]')
# ax[1].set_xlim(0, 10)
# ax[1].set_ylim(0, 10)
# plot1, = ax[0].plot([], [], 'go')
# plot2, = ax[1].plot([], [], 'r.')
# plot3, = ax[1].plot([], [], 'b.')
# plot4, = ax[1].plot([], [], 'k.')

# def animate(i):
#     plot1.set_data(xpos_list[i], zpos_list[i])
#     plot2.set_data(t_range[:i], KEn[:i])
#     plot3.set_data(t_range[:i], PEn[:i])
#     plot4.set_data(t_range[:i], TEn[:i])

# # Animation
# anim = ani.FuncAnimation(fig, animate, frames=len(t_range), interval=50)
# plt.show()


# trajectory_matrix = np.column_stack((xpos_list, zpos_list))
# energy_matrix = np.column_stack((t_range, KEn, PEn, TEn))

# # Print or visualize the matrices
# print("Trajectory Matrix:")
# print(trajectory_matrix)

# print("\nEnergy Matrix:")
# print(energy_matrix)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import numpy as np
# import matplotlib.pyplot as plt

# def bisection(f, a, b, dx=1.e-10):
#     while b - a > dx:
#         tmp = (a + b) / 2
#         if f(tmp) * f(a) > 0:
#             a = tmp
#         else:
#             b = tmp
#     return (a + b) / 2

# # Function to visualize
# f = np.sin

# # Interval for bisection
# a_initial, b_initial = -1, 1

# # Perform bisection
# result = bisection(f, a_initial, b_initial)

# # Visualization
# x_values = np.linspace(a_initial, b_initial, 1000)
# y_values = f(x_values)

# plt.plot(x_values, y_values, label='sin(x)')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.8, label='y=0')

# # Highlight the interval
# plt.axvline(a_initial, color='red', linestyle='--', label='Interval')
# plt.axvline(b_initial, color='red', linestyle='--')

# # Mark the result
# plt.scatter(result, f(result), color='green', label='Root')

# plt.title('Bisection Method Visualization')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.legend()
# plt.show()
# # ///////////////////////////////////////////////////////////////////////////////

# def correlation(rlist):
#     res = 0
#     k = 1
#     for i in range(len(rlist)-k):
#         res = res + rlist[i] * rlist[i+k]
#     return res / (len(rlist) - 1)

# print(correlation([0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]))

# '''
# rlist: This is the input list for which we want to calculate the correlation.

# res: This variable is initialized to zero and represents the running sum of the product of corresponding 
#      elements in rlist and the shifted version of rlist.
# k: This is the lag or shift, and in this case, it is set to 1. It represents the time delay between the 
#    elements being compared.

# The for loop iterates over the elements of rlist up to the second-to-last element (length - 1). Inside the loop,
# it calculates the product of the current element (rlist[i]) and the element at the next position (rlist[i+k]),
# and adds this product to the running sum res. After the loop, the function returns the normalized correlation 
# by dividing the sum (res) by (len(rlist) - 1), which is the length of the list minus 1. This normalization 
# factor ensures that the correlation value is divided by the correct number of pairs.

# The print statement calls the function with a specific example list 
# [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1] and prints the result.
# The provided list has a repeating pattern of 0's and 1's, and the correlation function calculates 
# the correlation between consecutive elements in this pattern with a lag of 1.'''

# /////////////////////////////////////////////////////////////////////////////////////////
# import matplotlib.pyplot as plt
# import numpy as np
# import myode  # Assuming this module contains the move_RK2 function

# epsilon = 4e-4 * 27.211 * 1.6e-19  # in J
# bohr = 0.53e-10
# sigma = 2.4 * bohr  # in m
# mass = 40 * 1e-3 / 6.02e23  # in kg
# gridsize = 5
# nparticles = gridsize ** 2
# R = 10 * bohr  # Our simulation box is a square that spans -R to +R in
# k = 4 * epsilon * 18 / 2 ** (1 / 3) / sigma ** 2
# omega = np.sqrt(k / mass)
# period = 2 * np.pi / omega
# dt = 0.01 * period


# def flj(x):
#     return -4 * epsilon * (-12 * sigma ** 12 / x ** 13 + 6 * sigma ** 6 / x ** 7)


# def calc_forces(position):
#     forces = np.zeros((nparticles, 2))
#     for i in range(nparticles):
#         for j in range(i + 1, nparticles):
#             x1, z1 = position[i, 0], position[i, 1]
#             x2, z2 = position[j, 0], position[j, 1]
#             r12 = np.sqrt((x1 - x2) ** 2 + (z1 - z2) ** 2)
#             f = flj(r12)
#             forces[i, 0] += f * (x1 - x2) / r12
#             forces[i, 1] += f * (z1 - z2) / r12
#             forces[j, 0] -= forces[i, 0]
#             forces[j, 1] -= forces[i, 1]
#     return forces


# def diffeq(y):
#     position = y[0:nparticles * 2].reshape(nparticles, 2).copy()
#     a = calc_forces(position) / mass
#     ydot = y.copy()
#     ydot[:2 * nparticles] = y[2 * nparticles:]
#     ydot[2 * nparticles:] = a.flatten()
#     return ydot


# # Set up initial positions for visualization
# initial_positions = np.array([[i, j] for i in range(gridsize) for j in range(gridsize)])

# # Calculate initial forces
# initial_forces = calc_forces(initial_positions)

# # Create a quiver plot
# fig, ax = plt.subplots()
# ax.quiver(initial_positions[:, 0], initial_positions[:, 1], initial_forces[:, 0], initial_forces[:, 1], scale=50)

# # Set axis limits and labels
# ax.set_xlim(0, gridsize - 1)
# ax.set_ylim(0, gridsize - 1)
# ax.set_xlabel('X Position')
# ax.set_ylabel('Z Position')

# # Show the plot
# plt.show()
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import numpy as np

# def rw2d(x0, y0, Nstep):
#     Nstep = int(Nstep)
#     rng = np.random.default_rng()

#     # Individual steps in x and y components
#     angles = rng.choice([0, 90, 180, 270], size=Nstep, replace=True)
#     x_list = np.cos(np.radians(angles))
#     y_list = np.sin(np.radians(angles))

#     # Generate the trajectories starting from x0 and y0
#     x_traj_shifted = x0 + np.cumsum(x_list)
#     y_traj_shifted = y0 + np.cumsum(y_list)

#     # We will return a 2D array of dimensions Nstep x 2.
#     # .T stands for taking the transpose
#     result_array = np.array([x_traj_shifted, y_traj_shifted]).T
    
#     return result_array

# # Example usage:
# x0 = 0
# y0 = 0
# Nstep = 10
# result = rw2d(x0, y0, Nstep)

# # Print the arrays
# print("Before Transposition:")
# print(result)

# print("\nAfter Transposition:")
# print(result.T)
# ///////////////////////////////////////////////////////////////////////////////
