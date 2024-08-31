import numpy as np
import matplotlib.pyplot as plt

# # Version 1
# def rw1(N):
#     N = int(N) # Generating N random steps
#     r=0 # will be modified
#     r_list = [r] # Initializing
#     rng = np.random.default_rng()
#     hop_list = rng.choice([-1,1], N)
    
#     for i in range(N):
#         r += hop_list[i]
#         r_list.append(r)
#     return r_list

# plt.figure()
# plt.plot(rw1(1e4))

# # Version 2
# def rw2(N):
#     N = int(N) # Generating N random steps
#     r=0 # will be modified
#     r_list = [r] # Initializing
#     rng = np.random.default_rng()
#     hop_list = rng.choice([-1,1], N)
    
#     for i in range(N):
#         r += hop_list[i]
#         r_list.append(r)
#     return r_list

# plt.figure()
# plt.plot(rw2(1e4))

# Version 3
def rw3(N):
    N = int(N) # Generating N random steps
    r=0 # will be modified
    r_list = [r] # Initializing
    rng = np.random.default_rng()
    hop_list = rng.choice([-1,1], N)
    
    r_list = np.cumsum(hop_list)
    return r_list

plt.figure()
plt.plot(rw3(1e5))




