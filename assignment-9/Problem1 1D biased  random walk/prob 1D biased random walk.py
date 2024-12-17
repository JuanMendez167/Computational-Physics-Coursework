import numpy as np
import matplotlib.pyplot as plt
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Initially I had a hard time undestanding the graph when I first did it for version 1 and thats because I was
# observing what appeared to be a linear trend that I did not expect so I spent a while wondering what went wrong. 
# Then I realized the number of steps we were taking into consideration, my graph extends beyong 10,000 steps. What
#  if it was a 100 would be able to see a different type of behavior? The answer is yes, so I changed 
# r = rw1_biased() to accept a 100 rather and it made sense, but I realized you can just zoom in the graph and it
# its the same thing. 

# What does size=N do? Well it indicates the number of random samples we will generate.
# We average to observe the overall trend and the historam is included to add spice

# Essentially, what we are observing is the cumulative effect of the bias which is why rw1 biased appears linear. 
# I did it for all 3 because I wanted to confirm this effect. Is it unnecessary complex? Very much so, but we roll.
# The code will run much faser with version 3, but eh why not.

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# #version 1
def rw1_biased(N):
    N = int(N)
    r = 0
    r_list = [r]
    rng = np.random.default_rng()

    for i in range(N):
        hop = rng.choice([-1, 1], p=[0.25, 0.75]) # 25% left, 75% right
        r += hop
        r_list.append(r)
    return r_list

# biased random walk with 1e4 steps
r = rw1_biased(1e4)

# average position for each step
average_positions = [np.mean(r[:i+1]) for i in range(len(r))]

# Plotting random walk and average position
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(r, label='Random Walk')
plt.plot(average_positions, label='Average Position', linestyle='--')
plt.xlabel('Step')
plt.ylabel('Position')
plt.legend()
plt.title('Biased Random Walk - Version 1 (1e4 steps)')

plt.subplot(1, 2, 2)
plt.hist(r, bins=20, density=True, alpha=0.7)
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Histogram of Final Positions')

plt.tight_layout()
plt.show()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Version 2
def rw2_biased(N):
    N = int(N)
    r = 0
    r_list = [r]
    rng = np.random.default_rng()
    hop_list = rng.choice([-1, 1], p=[0.25, 0.75], size=N)  # 25% left, 75% right
    
    for i in range(N):
        r += hop_list[i]
        r_list.append(r)
    return r_list

# biased random walk with 1e4 steps
r = rw2_biased(1e4)

# average position for each step
average_positions = [np.mean(r[:i+1]) for i in range(len(r))]

# Plotting random walk and average position
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(r, label='Random Walk')
plt.plot(average_positions, label='Average Position', linestyle='--')
plt.xlabel('Step')
plt.ylabel('Position')
plt.legend()
plt.title('Biased Random Walk - Version 2 (1e4 steps)')

plt.subplot(1, 2, 2)
plt.hist(r, bins=20, density=True, alpha=0.7)
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Histogram of Final Positions')

plt.tight_layout()
plt.show()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#version 3 fully vectorized
def rw3_biased(N):
    N = int(N)
    rng = np.random.default_rng()
    hop_list = rng.choice([-1, 1], p=[0.25, 0.75], size=N) # 25% left, 75% right
    r_list = np.cumsum(hop_list)
    return r_list

# biased random walk with 1e4 steps
r = rw3_biased(1e4)

# average position for each step
average_positions = np.cumsum(r) / np.arange(1, len(r) + 1)

# Plotting random walk and average position
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(r, label='Random Walk')
plt.plot(average_positions, label='Average Position', linestyle='--')
plt.xlabel('Step')
plt.ylabel('Position')
plt.legend()
plt.title('Biased Random Walk - Version 3 (1e4 steps)')

plt.subplot(1, 2, 2)
plt.hist(r, bins=20, density=True, alpha=0.7)
plt.xlabel('Position')
plt.ylabel('Probability')
plt.title('Histogram of Final Positions')

plt.tight_layout()
plt.show()



# Part 1 using "p=": ✔
# Also great effort implementing this on all three versions of rw()! 
# Your observations in the comments are correct and useful too. 

# Part 2 without using "p=": missing
# -1.5
