# Problem 1

In this assignment we will implement a 1D "biased" random walk model.

Start from the single particle code we developed in class (rw1 or rw2 or rw3), but now let the particle take a step left (-1) with a probability of 25% and a step right (+1) with a probability of 75%.

1. You can consult numpy documentation for choice() to find out how to do this with an optional argument p=...
https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html

2. Can you implement another version still using np.random.choice() but we're not allowed to use the p=... argument?
