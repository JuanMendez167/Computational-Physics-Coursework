# Week 5 Task 1
# Apply midpoint integration to the sine and cosine functions within the [0,pi] interval. Fill in the missing pieces below.
# 
# Variables: 
#   a/b: left/right limit of the interval
#   n: number of intervals used in the calculation
#   exact_value: analytic result of the definite integral
#   numerical_integral: numerical result of the definite integral using midpoint rule

import numpy as np

a = 0
b = np.pi
n = 100 
exact_value_sin = 2  # Exact integral of sin(x) from 0 to pi
exact_value_cos = 0  # Exact integral of cos(x) from 0 to pi

dx = (b - a) / n

numerical_integral_sin = 0.0  # Numerical integral for sin(x)
numerical_integral_cos = 0.0  # Numerical integral for cos(x)

# The for loop acts as a summation/integral
for i in range(n):
    x_i = a + (i + 0.5) * dx  # Midpoint of the current interval
    numerical_integral_sin += np.sin(x_i) * dx
    numerical_integral_cos += np.cos(x_i) * dx

# Calculate errors
error_sin = exact_value_sin - numerical_integral_sin
error_cos = exact_value_cos - numerical_integral_cos

print("Numerical Integral of sin(x) from 0 to pi:", numerical_integral_sin)
print("Exact Integral of sin(x) from 0 to pi:", exact_value_sin)
print("Error for sin(x):", error_sin)

print("Numerical Integral of cos(x) from 0 to pi:", numerical_integral_cos)
print("Exact Integral of cos(x) from 0 to pi:", exact_value_cos)
print("Error for cos(x):", error_cos)

#✔