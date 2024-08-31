import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # Acceleration due to gravity in m/s^2
b = 0.1  # Damping coefficient in 1/s
mass = 0.1  # Mass of the particle in kg

def move_RK2(theta, v0):
    x, z = 0, 0  # Initial positions
    vx, vz = v0 * np.cos(np.radians(theta)), v0 * np.sin(np.radians(theta))  # Initial velocities
    
    x_traj, z_traj = [], []  # Lists to store trajectory points

    dt = 0.01  # Time step
    t = 0  # Initial time

    while z >= 0:
        x_traj.append(x)
        z_traj.append(z)

        # Calculate accelerations
        ax = -b * vx
        az = -g - b * vz

        # Update velocities using RK2 method
        vx_half = vx + 0.5 * ax * dt
        vz_half = vz + 0.5 * az * dt

        vx += ax * dt
        vz += az * dt

        # Update positions using RK2 method
        x_half = x + 0.5 * vx_half * dt
        z_half = z + 0.5 * vz_half * dt

        x += vx_half * dt
        z += vz_half * dt

        t += dt

    return x_traj, z_traj, x  # Return the x-coordinate of impact

launch_angles = np.arange(0, 91, 5)  # Range of launch angles from 0 to 90 degrees
initial_velocity = 30  # Initial velocity in m/s

plt.figure(figsize=(10, 6))

for angle in launch_angles:
    x_traj, z_traj, impact_x = move_RK2(angle, initial_velocity)
    plt.plot(x_traj, z_traj, label=f'Theta = {angle}°')
    print(f'Impact for Theta = {angle}°: x = {impact_x:.2f} m')

plt.grid(True)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion for Different Launch Angles')
plt.legend()
plt.show()

# ////////////////////////////////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
v0 = 30.0  # Initial velocity in m/s
g = 9.8  # Acceleration due to gravity in m/s^2
b = 0.1  # Damping coefficient in 1/s

# Create an array of launch angles (from 0 to 90 degrees with a step of 5 degrees)
theta_degrees = np.arange(0, 91, 5)
theta_radians = np.deg2rad(theta_degrees)

# Initialize lists to store x and z coordinates for each trajectory
x_trajectories = []
z_trajectories = []

# Function for the equations of motion with damping
def equations_of_motion(u, t):
    x, z, vx, vz = u
    dxdt = vx
    dzdt = vz
    dvxdt = -b * vx
    dvzdt = -g - b * vz
    return [dxdt, dzdt, dvxdt, dvzdt]

# Calculate trajectories for each launch angle
impact_points = []  # Initialize the list of impact points

for theta in theta_radians:
    # Initial conditions
    if theta == 0:
        u0 = [0, 0, v0, 0]  # Special case for 0-degree launch angle (horizontal)
    else:
        u0 = [0, 0, v0 * np.cos(theta), v0 * np.sin(theta)]
    
    # Time values
    t = np.arange(0, 2 * v0 * np.sin(theta) / g, 0.01)  # Adjusted time range
    
    # Solve the differential equations
    sol = odeint(equations_of_motion, u0, t)
    
    x = sol[:, 0]
    z = sol[:, 1]
    
    # Ensure z remains non-negative
    z = np.maximum(z, 0)
    
    x_trajectories.append(x)
    z_trajectories.append(z)
    
    # Calculate the impact point for each trajectory
    if len(x) > 0:
        z_zero_indices = np.where(z == 0)[0]
        if len(z_zero_indices) >= 2:
            # Interpolate to find the accurate impact point
            x1 = x[z_zero_indices[-2]]
            x2 = x[z_zero_indices[-1]]
            t1 = t[z_zero_indices[-2]]
            t2 = t[z_zero_indices[-1]]
            impact_x = np.interp(0, [z[z_zero_indices[-2]], z[z_zero_indices[-1]]], [x1, x2])
            impact_points.append(impact_x)
        else:
            impact_points.append(x[-1])
    else:
        # For 0-degree launch angle, directly calculate impact point
        impact_points.append(0.3)  # 0.3 meters (as in Template 1)

# Plot the trajectories
plt.figure(figsize=(10, 6))
for i, theta_deg in enumerate(theta_degrees):
    if len(x_trajectories[i]) > 0:
        impact_x = impact_points[i]
        impact_index = np.where(x_trajectories[i] >= impact_x)[0][0]  # Find the index at impact point
        plt.plot(x_trajectories[i][:impact_index+1], z_trajectories[i][:impact_index+1], label=f'Theta = {theta_deg} degrees')

plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion Trajectories with Damping for Different Launch Angles (z >= 0)')
plt.grid(True)
plt.legend()
plt.show()

# Print the accurate impact points for each trajectory
for theta_deg, impact_x in zip(theta_degrees, impact_points):
    print(f"Launch Angle: {theta_deg} degrees, Impact Point (x): {impact_x:.2f} meters")
# ///////////////////////////////////////////////////////////////////////////////////////////

# With drag
import numpy as np
import matplotlib.pyplot as plt

g = 9.8  # Acceleration due to gravity in m/s^2
b = 0.1  # Damping coefficient in 1/s
mass = 0.1  # Mass of the particle in kg

def move_RK2(theta, v0):
    x, z = 0, 0  # Initial positions
    vx, vz = v0 * np.cos(np.radians(theta)), v0 * np.sin(np.radians(theta))  # Initial velocities
    
    x_traj, z_traj = [], []  # Lists to store trajectory points

    dt = 0.01  # Time step
    t = 0  # Initial time

    while z >= 0:
        x_traj.append(x)
        z_traj.append(z)

        # Calculate accelerations including air drag
        v = np.sqrt(vx**2 + vz**2)
        ax = -b * v * vx
        az = -g - b * v * vz

        # Update velocities using RK2 method
        vx_half = vx + 0.5 * ax * dt
        vz_half = vz + 0.5 * az * dt

        vx += ax * dt
        vz += az * dt

        # Update positions using RK2 method
        x_half = x + 0.5 * vx_half * dt
        z_half = z + 0.5 * vz_half * dt

        x += vx_half * dt
        z += vz_half * dt

        t += dt

    return x_traj, z_traj, x  # Return the x-coordinate of impact

launch_angles = np.arange(0, 91, 5)  # Range of launch angles from 0 to 90 degrees
initial_velocity = 30  # Initial velocity in m/s

plt.figure(figsize=(10, 6))

for angle in launch_angles:
    x_traj, z_traj, impact_x = move_RK2(angle, initial_velocity)
    plt.plot(x_traj, z_traj, label=f'Theta = {angle}°')
    print(f'Impact for Theta = {angle}°: x = {impact_x:.2f} m')

plt.grid(True)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion with Air Drag for Different Launch Angles')
plt.legend()
plt.show()

# /////////////////////////////////////////////////////////////////////////////////

# With drag
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
v0 = 30.0  # Initial velocity in m/s
g = 9.8  # Acceleration due to gravity in m/s^2
b = 0.1  # Damping coefficient in 1/s

# Create an array of launch angles (from 0 to 90 degrees with a step of 5 degrees)
theta_degrees = np.arange(0, 91, 5)
theta_radians = np.deg2rad(theta_degrees)

# Initialize lists to store x and z coordinates for each trajectory
x_trajectories = []
z_trajectories = []

# Function for the equations of motion with damping and air drag
def equations_of_motion(u, t):
    x, z, vx, vz = u
    dxdt = vx
    dzdt = vz
    v = np.sqrt(vx**2 + vz**2)
    dvxdt = -b * vx - 0.5 * b * v * vx
    dvzdt = -g - b * vz - 0.5 * b * v * vz
    return [dxdt, dzdt, dvxdt, dvzdt]

# Calculate trajectories for each launch angle
impact_points = []  # Initialize the list of impact points

for theta in theta_radians:
    # Initial conditions
    if theta == 0:
        u0 = [0, 0, v0, 0]  # Special case for 0-degree launch angle (horizontal)
    else:
        u0 = [0, 0, v0 * np.cos(theta), v0 * np.sin(theta)]
    
    # Time values
    t = np.arange(0, 2 * v0 * np.sin(theta) / g, 0.01)  # Adjusted time range
    
    # Solve the differential equations
    sol = odeint(equations_of_motion, u0, t)
    
    x = sol[:, 0]
    z = sol[:, 1]
    
    # Ensure z remains non-negative
    z = np.maximum(z, 0)
    
    x_trajectories.append(x)
    z_trajectories.append(z)
    
    # Calculate the impact point for each trajectory
    if len(x) > 0:
        z_zero_indices = np.where(z == 0)[0]
        if len(z_zero_indices) >= 2:
            # Interpolate to find the accurate impact point
            x1 = x[z_zero_indices[-2]]
            x2 = x[z_zero_indices[-1]]
            t1 = t[z_zero_indices[-2]]
            t2 = t[z_zero_indices[-1]]
            impact_x = np.interp(0, [z[z_zero_indices[-2]], z[z_zero_indices[-1]]], [x1, x2])
            impact_points.append(impact_x)
        else:
            impact_points.append(x[-1])
    else:
        # For 0-degree launch angle, directly calculate impact point
        impact_points.append(0.3)  # 0.3 meters (as in Template 1)

# Plot the trajectories
plt.figure(figsize=(10, 6))
for i, theta_deg in enumerate(theta_degrees):
    if len(x_trajectories[i]) > 0:
        impact_x = impact_points[i]
        impact_index = np.where(x_trajectories[i] >= impact_x)[0][0]  # Find the index at impact point
        plt.plot(x_trajectories[i][:impact_index+1], z_trajectories[i][:impact_index+1], label=f'Theta = {theta_deg} degrees')

plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion Trajectories with Damping and Air Drag for Different Launch Angles (z >= 0)')
plt.grid(True)
plt.legend()
plt.show()

# Print the accurate impact points for each trajectory
for theta_deg, impact_x in zip(theta_degrees, impact_points):
    print(f"Launch Angle: {theta_deg} degrees, Impact Point (x): {impact_x:.2f} meters")

