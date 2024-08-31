# In class we talked about using the generic bisection method to solve the special problem of 
# finding x where sin(x) = 0, near x=0 and near x=2pi. 


 # In this quiz, without changing the bisection() function definition part, 
 # try to find x where sin(x)=0.1 near x=2pi. 
 # Your solution of x should be approximately 0.1 larger than 2pi.

def bisection(f, a, b , dx=1e-5):
    while b-a > dx:
        midp = (a+b)/2
        if f(midp) * f(a) > 0 :
            a = midp
        else:
            b = midp          
    return (a+b)/2

# write your own function here   
def f(x):
    return np.sin(x) - 0.1

import numpy as np
res1 = bisection(np.sin, 5,7, dx=1e-6)
res2 = bisection(f,5,6,dx=1e-6)
print(res1)
print(res2)






