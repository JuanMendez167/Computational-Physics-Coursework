# Task 1: Without removing results from Euler's method, finish the 2nd order Runge-Kutta method
# and plot the results from Euler's method, RK2 method, and the analytical solution on the 
# same plot. An example plot using dt = 0.01 seconds is attached.

import numpy as np
import matplotlib.pyplot as plt

# Initialize the physical properties of the system
k = 1.0   # spring constant in SI units
xeq = 0.0  # equilibrium position of the particle on a spring
mass = 0.1  # Mass in kg
omega = np.sqrt(k / mass)

# Define the time step sizes
dt_values = [0.01, 0.005]

# Initialize lists to store errors for both methods and time step sizes
errors_rk2 = []
errors_euler = []

for dt in dt_values:
    period = 2 * np.pi / omega
    t_total = period * 5  # We simulate for a total of 5 periods
    t_range = np.arange(0, t_total, dt)

    # The following is the function responsible to compute the elastic force
    def felastic(k, xeq, x):
        force = -k * (x - xeq)
        return force

    # Advance time using Euler's rule
    def move_Euler(xpos, xvel):
        xacc = felastic(k, xeq, xpos) / mass
        xpos = xpos + xvel * dt
        xvel = xvel + xacc * dt
        return xpos, xvel

    # Advance time using the Runge-Kutta rule at 2nd order
    def move_RK2(xpos, xvel):
        # at time t+dt
        xacc = felastic(k, xeq, xpos) / mass
        xpos = xpos + xvel * dt
        xvel = xvel + xacc * dt
        
        # at time t+dt/2
        xpos_half = xpos + 0.5 * xvel * dt
        xacc_half = felastic(k, xeq, xpos_half) / mass
        xvel_half = xvel + 0.5 * xacc * dt
        return xpos, xvel

    # Analytical result
    xa = [np.cos(omega * t) for t in t_range]

    # Initialize positions and velocities
    xpos = 1
    xvel = 0
    xEuler = []
    xRK2 = []

    for t in t_range:
        force = felastic(k, xeq, xpos)
        xpos, xvel = move_Euler(xpos, xvel)
        xEuler.append(xpos)

        force_rk2 = felastic(k, xeq, xpos)
        xpos, xvel = move_RK2(xpos, xvel)
        xRK2.append(xpos)

    # TASK2 : Similar with we we did in Problem 1, Using dt = 0.01, measure the error in xpos at 
    # t=8.8s  between the results from RK2 and the analytical solution. Measure the error again 
    # using dt = 0.005s. How do the two errors compare and why?
    
    # Its rather easy to do so by taking the absolute value of the difference in xpos  at t=8.8s
    # between the results from RK2 and the analytical soln as stated. 
    
    # To demonstrate, for RK2 with dt = 0.01 at t=8.8s
    # Error = |1.5-(-0.9))| 2.49
    # Upon closer inspection its a pain, so lets get the actual values
    
    # Find the index corresponding to the target time (t = 8.8s)
    t_target = 8.8
    index_target = int(t_target / dt)

    # Calculate errors for RK2 and Euler's method at the target time
    error_rk2 = abs(xa[index_target] - xRK2[index_target])
    error_euler = abs(xa[index_target] - xEuler[index_target])

    errors_rk2.append(error_rk2)
    errors_euler.append(error_euler)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(t_range, xEuler, 'b-', label='Euler')
    plt.plot(t_range, xRK2, 'g-', label='RK2')
    plt.plot(t_range, xa, 'r-', label='Analytical')
    plt.axvline(t_target, color='k', linestyle='--', label= 't = 8.8s')
    plt.xlabel('Time (s)')
    plt.ylabel('X Position (m)')
    plt.ylim(-2, 2)
    plt.xlim(0, 10)
    plt.title(f'Harmonic Motion: Numerical (Euler and RK2) vs Analytical (dt = {dt})')
    plt.legend()
    plt.grid(True)
    plt.show()

# Print the errors for different time step sizes at t = 8.8s
for i, dt in enumerate(dt_values):
    print(f"Error with RK2 and dt={dt} at t=8.8s: {errors_rk2[i]}")
    print(f"Error with Euler and dt={dt} at t=8.8s: {errors_euler[i]}")
    
# The final results
# Two plots and the following lines of code
# Error with RK2 and dt=0.01 at t=8.8s: 2.4979055874128893
# Error with Euler and dt=0.01 at t=8.8s: 2.4391652632144414
# Error with RK2 and dt=0.005 at t=8.8s: 1.908691854564129
# Error with Euler and dt=0.005 at t=8.8s: 1.889746528469644
