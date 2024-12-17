# Week 5 Task 2
# Apply trapezoid integration to the sine function within the [0,pi] interval. 
#
# Variables: 
#   a/b: left/right border of the interval
#   n: number of intervals used in the calculation
#   exact_result: analytic result of the definite integral
#   numerical_integral: numerical result of the definite integral using the trapezoid rule

import numpy as np
a = 0
b = np.pi
n = 100
exact_result = 2.0  # Exact integral of sin(x) from 0 to pi

dx = (b - a) / n

numerical_integral = 0.0
for i in range(n):
    x_i = a + i * dx  # Left endpoint of the current interval
    x_ip1 = a + (i + 1) * dx  # Right endpoint of the current interval
    numerical_integral += 0.5 * (np.sin(x_i) + np.sin(x_ip1)) * dx

# Calculate the error
error = exact_result - numerical_integral

# Print the results and error
print("Numerical Integral of sin(x) from 0 to pi (Trapezoid Rule):", numerical_integral)
print("Exact Integral of sin(x) from 0 to pi:", exact_result)
print("Error for sin(x):", error)

#✔
# Results for sine look good. Just missing the same for cosine 
# and also the comments part in the last step of this problem.
#-1 