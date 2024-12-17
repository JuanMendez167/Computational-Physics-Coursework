
##### Animation section ######

import matplotlib.animation as ani
# The following command setup the visualization of plot, where the particle is represented by a green filled circle
fig, axes = plt.subplots(1)
axes.set_aspect('equal', 'box')
axes.set_ylabel('y position')
axes.set_xlabel('x position')

axes.set_xlim(-2, 2)
axes.set_ylim(-2, 10)
plota,=axes.plot([],[],'bo') # a placeholder plot for particle 1
plotb,=axes.plot([],[],'ro') # a placeholder plot for particle 2

# Define the function that performs a single step of the animation
def animate(i):
    plota.set_data(?, ?)
    plotb.set_data(?, ?)
    return plota, plotb

# This function requires as an argument the user-defined animate() function above
anim = ani.FuncAnimation(fig, animate, frames=len(t_range), interval=0, blit=True, repeat=True)

# No updates found here
# -3
