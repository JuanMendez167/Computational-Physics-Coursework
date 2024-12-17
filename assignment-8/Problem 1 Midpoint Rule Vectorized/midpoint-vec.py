# # Week 10 Task 1
import numpy as np

def midpoint(n):
    # n is the number of increments between a and b
    n = int(n)
    a = 0
    b = np.pi
    dx = (b - a) / n
    
    # a simple for loop that performs the integration
    integral = 0
    for i in range(n):
        integral = integral + np.sin((i+0.5)*dx)*dx
    
    print(integral)
    # Timing this function using n=1e6 takes about 1 second.
    
 
def midpoint_vec(n):
    n = int(n)
    a = 0
    b = np.pi
    dx = (b - a) / n

    # Create an array of sample points
    x = np.linspace(a + dx / 2, b - dx / 2, n)

    # Calculate the values of the function at the sample points
    fx = np.sin(x)

    # Use np.sum() to compute the integral
    integral = np.sum(fx) * dx

    print(integral)
    # Timing this function using n=1e6 should take about 100 ms.


# Testing the midpoint and midpoint_vec functions with n=1e6
print("Midpoint:")
%time midpoint(1e6)

print("Midpoint_vec:")
%time midpoint_vec(1e6)
    
# This prints
'''Midpoint:
2.0000000000008424
CPU times: total: 656 ms
Wall time: 1.76 s
Midpoint_vec:
2.000000000000823
CPU times: total: 0 ns
Wall time: 40.1 ms'''


# Both integration methods works. Timing performed. ✔






