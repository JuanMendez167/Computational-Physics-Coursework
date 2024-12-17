import numpy as np
import matplotlib.pyplot as plt

# TASK 1 : a tentative choice of dt = 0.01 seconds is chosen here. Although it's not small 
# enough to eliminate all visible errors, it's a good initial choice. 
# If this dt were not given, how would you have come up with it by yourself? 
# Provide a comment. Hint: what is the characteristic timescale of this problem?

# Initialize the physical properties of the system
dt=0.01 
# The characteristic time scale can be obtained by selecting dt to be a fraction of 
# the period where dt = period / 100
k=1.0   #spring constant in SI units
xeq=0.0 #equilibrium position of the particle on a spring
mass=0.1 # in kg
omega = np.sqrt(k/mass)
period = 2* np.pi/omega 

# TASK 2 :  Using dt = 0.01, measure the error in xpos at t=8.8s (where a vertical bar 
# is provided) between the results from Euler's method and the analytical solution. Measure 
# the error again using dt = 0.005. How does the two errors compare and why?

# A less accurate results can be achieved by eyeballing the difference, but a more accurate
# result can be obtained with a little extra work.

# Then initialize time step (dt) for both cases
dt1= 0.01
dt2 = 0.005

t_total = period * 5  #we simulate for a total of 5 periods

# The following is the function responsible to compute the elastic force
def felastic(k,xeq,x):
    force = - k * (x - xeq)
    return force

# Advance time using Euler's rule
def move_Euler(xpos,xvel):
    xacc = felastic(k, xeq, xpos) / mass
    xpos = xpos + xvel * dt
    xvel = xvel + xacc * dt
    return xpos,xvel

#Euler's method
# Initialize position and velocities for both cases
xpos1 = 1
xvel1 = 0
xpos2 = 1
xvel2 = 0

# Initialize the arrays for both cases
xEuler1 = []
xEuler2 = []

t_range = np.arange(0,t_total, dt1) # Initializing the time range for dt1

for t in t_range:
    # Case 1: dt = 0.01
    force1 = felastic(k,xeq,xpos1)
    xpos1,xvel1 = move_Euler(xpos1,xvel1)
    xEuler1.append(xpos1)

t_range2 = np.arange(0, t_total, dt2)  # Initializing the time range for dt2

for t in t_range2:
    # Case 2: dt = 0.005
    force2 = felastic(k,xeq,xpos2)
    xpos2, xvel2 = move_Euler(xpos2,xvel2)
    xEuler2.append(xpos2)

# Analytical result for both cases (the time range is the same for both)
xa1 =  [np.cos(omega * t) for t in t_range]
xa2 =  [np.cos(omega * t) for t in t_range2]

# Calculate the errors at t = 8.8s for both cases
t_target = 8.8
index_target1 = int(t_target / dt1)
index_target2 = int(t_target / dt2)
error1 = abs(xa1[index_target1] - xEuler1[index_target1])
error2 = abs(xa2[index_target2] - xEuler2[index_target2])

print("Error with dt = 0.01 at t=8.8s:"  , error1)
print("Error with dt = 0.005 at t=8.8s:" , error2)

# Plot results for both cases
fig, ax = plt.subplots(1)
ax.plot(t_range, xEuler1 , 'b.', label='Euler (dt = 0.01)')
ax.axvline(8.8)

ax.plot(t_range, xa1 , 'r-', label='Analytical (dt = 0.01)')

ax.legend()
ax.set_ylim(-2,2)
ax.set_xlim(0,10)
ax.set_xlabel('time (s)')
ax.set_ylabel('x position (m)')

plt.title('Harmonic Motion: Numerical vs Analytic Solution (dt = 0.01)')
plt.show()

fig, ax = plt.subplots(1)
ax.plot(t_range2, xEuler2, 'g.', label='Euler (dt = 0.005)')
ax.axvline(8.8)

ax.plot(t_range2, xa2, 'r-', label='Analytical (dt = 0.005)')

ax.legend()
ax.set_ylim(-2, 2)
ax.set_xlim(0, 10)
ax.set_xlabel('time (s)')
ax.set_ylabel('x position (m)')
plt.title('Harmonic Motion: Numerical vs Analytical (dt = 0.005)')
plt.show()

# Interpreting the results
# The final results of this code will plot two different graphs involving two different time steps 
# ,moreover, it will also print the error associated with each time step. 

# Here is what is printed
# Error with dt = 0.01 at t=8.8s: 0.5135904611298849
# Error with dt = 0.005 at t=8.8s: 2.4391652632144414

# Do these results make sense however? Well they do, it makes sense that smaller time steps
# while more accurate would results in a higher error this is because while bigger time
# steps are less accurate they result in a better error. However, thats only by comparison, think
# about another example that would effcicently describe this. 














