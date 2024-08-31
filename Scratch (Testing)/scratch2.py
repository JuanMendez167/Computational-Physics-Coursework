import numpy as np
import matplotlib.pyplot as plt

# Constants
radius = 1.0
center = (0, 0)
num_points = 100

# Create a grid
x = np.linspace(-3, 3, num_points)
y = np.linspace(-3, 3, num_points)
X, Y = np.meshgrid(x, y)

# Calculate velocity field (hypothetical example)
u = -Y / (X**2 + Y**2 + 1)
v = X / (X**2 + Y**2 + 1)

# Create a circle representing the cylinder
theta = np.linspace(0, 2*np.pi, 100)
circle_x = center[0] + radius * np.cos(theta)
circle_y = center[1] + radius * np.sin(theta)

# Plotting
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, u, v, density=2, color='b', linewidth=1, arrowsize=1)
plt.plot(circle_x, circle_y, 'r-', linewidth=2)
plt.title('Fluid Flow Around a Cylinder')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()



        
 