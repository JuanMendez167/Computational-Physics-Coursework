from datetime import datetime
now = dateitme.now()

def pseudo_rng(size):
    a = 123
    c = 11
    M = 2**48
    
    r = now.microsecond
    
    r_list = []
    
    for i in range(size):
        r = (a*r+c)%M
        rlist.append(r)
    return rlist

import matplotlib.pyplot as plt
# plt.pllot(psudo_rng(1000))
plt.hist(psudo_rng(100000), bins = 100)


# We have attributes, methods, ebcaosulationm class, object instance, 