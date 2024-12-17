# Week 2 Assignment 1
# Write a loop that computes pi using the Leibniz formula. 

#calculate a new term
#then add this new term to result, and repeat.
def Leibniz (n):
    result = 0
    for i in range(n):
        term = ((4.0 * (-1)**i) / (2*i +1))
        result = result + term
    return result

terms = int(input("Number of terms: " ))
pi = Leibniz(terms)

print("Then the value of pi is:", pi )

#✔
# good job making the term number a user input!