# # Week 9 Task 2

import numpy as np
import matplotlib.pyplot as plt

def newton2(f, x, tol=1.e-5): 
    h = 1.e-5  # tol
    df = (f(x + h) - f(x)) / h
    
    # Newton-Raphson method
    while np.abs(f(x)) > tol:
        x = x - f(x) / df
        df = (f(x + h) - f(x)) / h  # Update df
    return x

x_init_task1 = 3.0  # Initial guess
result_task1 = newton2(np.sin, x_init_task1)

print("Task 1: Approximate root for sin func:", result_task1)
print("sin result =", np.sin(result_task1))

def f(R):
    g = 9.8  # In m/s^2
    b = 1  # In 1/s
    angle = 30  # In degrees
    v0x = 30 * np.cos(angle/180 * np.pi)
    v0z = 30 * np.sin(angle/180 * np.pi)
    res = R / v0x * (v0z + g / b) + g / b**2 * np.log(1 - b * R / v0x) # In class, also something happens here
    
    return res

# An initial guess of 24 works. But the algorithm is quite fragile and breaks for initial guess smaller than 21 or larger than 25.
R_init_task2 = 24
result_task2 = newton2(f, R_init_task2)
print("Task 2: Approximate impact:", result_task2, "m") # In m

# plot out f(R) to finish the discussions on why the root search fails if R_init<21 or >25
R_values = np.linspace(0, 50, 500)
f_values = [f(R) for R in R_values]

plt.figure(figsize=(8, 6))
plt.plot(R_values, f_values, label='f(R)')
plt.axhline(0, color='red', linestyle='--', label='y = 0')
plt.axvline(result_task2, color='green', linestyle='--', label='Approximate root')
plt.xlabel('R (m)')
plt.ylabel('f(R)')
plt.legend()
plt.title("f(R) vs. R")
plt.show()


# Task 1 on implementing Newton2(): ✔

# Task 2 on why R>25 fails: 
# Code works here but missing comment.
# The reason is that for R>25 the log function would 
# take a negative argument, thereby breaking the search.
# -1

# Task 3 on why R<21 fails: 
# If R<21, you can show that the first tangent line overshoots R=25, 
# rendering the log function invalid again.
# -1