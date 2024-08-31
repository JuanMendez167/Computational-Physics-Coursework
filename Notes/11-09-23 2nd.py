import numpy as np
import matplotlib.pyplot as plt

# # Version 1
# def rw_multi1(N, Np):
#     N = int(N) # Generating N random steps
#     Np = int(Np)
#     r_list = [] # Initializing
#     rng = np.random.default_rng()
   
#     for i in range(Np):
#         hop_list = rng.choice([-1,1], N)
#         r_list.append(np.cumsum(hop_list))
#     return r_list

# res = rw_multi1(1e5,5)

# plt.figure()
# for i in range(5):
#     plt.plot(res[i])
    
# Version 2
def rw_multi2(N, Np):
    N = int(N) # Generating N random steps
    Np = int(Np)
    r_list = [] # Initializing
    rng = np.random.default_rng()
    hop_list = rng.choice([-1,1], [Np,N])
   
    r_list = np.cumsum(hop_list, axis = 1)
    
    return r_list

res = rw_multi2(1e5,100)

plt.figure()
for i in range(100):
    plt.plot(res[i])
    
plt.figure()
plt.hist(res[:,-1], bin = 20, density = True)