# import numpy as np

# def bisection(f, a, b, dx = 1.e-6):
#     while b-a > dx:
#         tmp = (a+b)/2
#         if f(tmp)*f(a) > 0:
#             a = tmp
#         else: 
#             b=tmp
#     return (a+b)/2

# # Example 1
# bisection(np.sin, -1, 1)

# vx0 = 0.2 # In m/s
# vz0 = 4 # In m/s 
# b = 1 # In 1/s
# g = 9.8 # In m/s^2

# bisection(np.sin, -1, 1)

# def f(R):
#     res = R/ vx0 * (vz0+ g/b) + g/b**2 * np.log(1-b*R/vx0)
    
#     return res

# # Example 2
# bisection(f,0.01,0.2, dx=1e-6)
# ////////////////////////////////////////////////////////////////////////////
import numpy as np

# def bisection(f, a, b, dx = 1.e-6):
#     while b-a > dx:
#         tmp =(a+b)/2
#         if f(tmp)*f(a) > 0:
#             a = tmp
#         else: 
#             b=tmp
#     return (a+b)/2

# # Example 1
# bisection(np.sin, -1, 1)

# b = 1 # In 1/s
# g = 9.8 # In m/s^2

# bisection(np.sin, -1, 1)

# def f(thetha):
#     vx0 = 30 * np.cos(theta)
#     vz0 = 30 * np.sin(theta) 
#     R = 20
#     res = R/ vx0 * (vz0+ g/b) + g/b**2 * np.log(1-b*R/vx0)
#     return res

# # Example 2
# bisection(f, 0/180 * np.pi, 90/180 * np.pi, 1.e-6)
# print(t/np.pi * 180)
# # .............................................................................

import numpy as np

def bisection(f, a, b, dx=1.e-6):
    while b - a > dx:
        tmp = (a + b) / 2
        if f(tmp) * f(a) > 0:
            a = tmp
        else:
            b = tmp
    return (a + b) / 2

# Example 1
result1 = bisection(np.sin, -1, 1)
print("Example 1 Result:", result1)

b = 1  # In 1/s
g = 9.8  # In m/s^2

# Example 2
def f(theta):
    vx0 = 30 * np.cos(theta)
    vz0 = 30 * np.sin(theta)
    R = 20
    res = R / vx0 * (vz0 + g / b) + g / b ** 2 * np.log(1 - b * R / vx0)
    return res

result2 = bisection(f, 0 / 180 * np.pi, 90 / 180 * np.pi, 1.e-6)
print("Example 2 Result (in degrees):", result2 / np.pi * 180)




