import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def rw3d(Nstep, rotation_speed=0.1):
    Nstep = int(Nstep)
    rng = np.random.default_rng()

    # Individual steps in x, y, and z
    angles_xy = rng.choice([0, 90, 180, 270], size=Nstep, replace=True)
    angles_z = rng.choice([0, 90], size=Nstep, replace=True)

    # Convert angles to radians
    angles_xy_rad = np.radians(angles_xy)
    angles_z_rad = np.radians(angles_z)

    # Calculate step components in x, y, and z
    x_list = np.cos(angles_xy_rad) * np.cos(angles_z_rad)
    y_list = np.sin(angles_xy_rad) * np.cos(angles_z_rad)
    z_list = np.sin(angles_z_rad)

    # Trajectories in x, y, and z
    x_traj = np.cumsum(x_list)
    y_traj = np.cumsum(y_list)
    z_traj = np.cumsum(z_list)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_traj[0], y_traj[0], z_traj[0], c='g', marker='o', label='Start')
    ax.scatter(x_traj[-1], y_traj[-1], z_traj[-1], c='r', marker='o', label='End')
    line, = ax.plot(x_traj, y_traj, z_traj, 'k-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    def update(frame):
        ax.view_init(elev=10, azim=frame * rotation_speed)
        return line,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 360), interval=50)
    plt.show()

rw3d(Nstep=1000)
