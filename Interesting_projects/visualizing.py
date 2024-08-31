# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Function to calculate the projection of a vector onto another
# def project_onto(v, onto):
#     return np.dot(v, onto) / np.linalg.norm(onto) * onto / np.linalg.norm(onto)

# # Define the polarization vector
# P = np.array([1, 2, 3])  # Replace with your specific values

# # Define the normal vector at the interface
# normal_vector = np.array([0, 0, 1])  # Assuming interface is in the z-direction

# # Calculate the projection of polarization onto the normal direction
# sigma_b = project_onto(P, normal_vector)

# # Visualization
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the polarization vector
# ax.quiver(0, 0, 0, P[0], P[1], P[2], color='r', label='Polarization Vector')

# # Plot the normal vector
# ax.quiver(0, 0, 0, normal_vector[0], normal_vector[1], normal_vector[2], color='b', label='Normal Vector')

# # Plot the projection of polarization onto the normal direction
# ax.quiver(0, 0, 0, sigma_b[0], sigma_b[1], sigma_b[2], color='g', label='Projection onto Normal')

# ax.set_xlim([0, 2])
# ax.set_ylim([0, 4])
# ax.set_zlim([0, 6])
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.legend()

# plt.show()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

