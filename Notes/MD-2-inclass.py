import matplotlib.pyplot as plt
import numpy as np
import my_ode  # this is the ode.py module we wrote in class, containing move_Euler() and move_RK2()

epsilon= 4e-4 * 27.211 * 1.6e-19 # in J
bohr = 0.53e-10 
sigma=2.4 * bohr # in m
mass= 40 * 1e-3/6.02e23 # in kg

nparticles = 2 # Total of 2 particles
R = 10 * bohr # Our simulation box is a square that spans -R to +R in both the x and y directions.

k = 4*epsilon * 18/2**(1/3)/sigma**2
omega = np.sqrt(k/mass)

period = 2*np.pi/omega
dt = 0.01 * period


def flj(x):    
    return -4*epsilon*(-12*sigma**12/x**13 \
                       +6*sigma**6/x**7)

def calc_forces(position):
    
    x1 = position[0,0]
    z1 = position[0,1]
    x2 = position[1,0]
    z2 = position[1,1]
    
    r12 =  np.sqrt((x1-x2)**2 + (z1-z2)**2)
    fx1 = flj(r12) * (x1-x2)/r12
    fz1 = flj(r12) * (z1-z2)/r12
    fx2 = flj(r12) * (x2-x1)/r12
    fz2 = flj(r12) * (z2-z1)/r12
    forces = np.array([[fx1,fz1],[fx2,fz2]])
    return forces
    
def diffeq(y):
    x1,z1, x2,z2, vx1,vz1, vx2, vz2 = y
    position = y[0:4].reshape(2,2).copy()
    a = calc_forces( position) / mass
    ydot = [vx1, vz1, vx2, vz2, a[0,0], a[0,1], a[1,0], a[1,1] ]
    ydot = np.array(ydot)
    return ydot

y = np.zeros(8)
y[0:4] = np.array([-1,0,1,1]) * bohr

t_total = 1000*dt
t_range = np.arange(0, t_total, dt)
y_list = []
    
for t in t_range:
    y = my_ode.move_RK2( diffeq, y, dt)
    # some boundary conditions here too
    for i in range(2*nparticles):
        if abs(y[i])>R:
            y[i+4] = -y[i+4]
            
    y_list.append(y)
    
y_list = np.array(y_list)    
    

fig, ax = plt.subplots(1)
ax.set_aspect('equal', 'box')
ax.set_xlim(-R,R)
ax.set_ylim(-R,R)
a, =  ax.plot([],[], 'go')

import matplotlib.animation as anim
def animate(i):
    a.set_data( [y_list[i,0], y_list[i,2]  ],\
               [y_list[i,1], y_list[i,3] ] )
    return a,

anim = anim.FuncAnimation(fig, animate, \
                frames=len(t_range),\
                interval=0.1, repeat=True,\
                    blit=True)






    
    