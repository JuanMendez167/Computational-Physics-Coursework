# Week 2 Assignment 3
#
#
# This code computes the natural logarithm of an input number,
# and prints a clear message if the input is smaller or equal to zero

import numpy as np
print("Input a number in the folowing line to use for the log func:")
x = int(input())
a = np.log(x)
if x <=0:
    print("The value you entered is not a valid input for the log() function, choose a number greater than 0")
elif x > 0:
    print(a)
    
#✔
