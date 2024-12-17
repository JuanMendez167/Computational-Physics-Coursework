# #Problem 1

import numpy as np

def newton1(f, df, x, tol=1.e-5): 
    """
    Function to compute the zero of a function using Newton-Raphson method
    Input variables
      f: function of which we search the zero
      df: derivative of function f
      x: initial guess for the zero of the function
      tol: accuracy of the result
    """
    while np.abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x

# Demonstrate how to find a root at pi using your newton1()
x_init = 3  # Initial guess
result = newton1(np.sin, np.cos, x_init)
print("Approximate root:", result)
print("sin(result) =", np.sin(result))

#✔
#good confirmation too.
