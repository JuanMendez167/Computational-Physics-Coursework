# Problem 1

In this assignment we will revisit integration using the midpoint rule. This time around, instead of using a for loop to accumulate the integrand, we will vectorize the process using numpy arrays and np.sum().

The original midpoint() function integrating a sine wave is provided as a reference. Time it in the console with %time using n=1e6 increments and report the Wall time it takes. 

Then finish the midpoint_vec() function, without using for loops or list comprehension. Construct and operate on numpy arrays and use np.sum() for summation. Time it using n=1e6 increments and report the Wall time it takes. 


EXPECTED OUTCOME: On my laptop midpoint() takes ~1 s and midpoint_vec() takes ~100 ms : a 10x speedup
