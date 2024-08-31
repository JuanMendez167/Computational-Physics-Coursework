import numpy as np
import matplotlib.pyplot as plt

class Line():
    def __init__(self,c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __calc__(self, x):
        return self.c0 + self.c1 * x
        
        
    def table(self, LB=0, RB=20, n=100):
        x = np.linspace(LB,RB,n)
        y = self.__calc__(x)
        return x,y
        
L1 = Line(c0=1, c1=2) # Intercept of 1 and slope of 2
L2 = Line(c0=0.5, c1=2.5)
print("The slope and intersecr of line 1 is", L1.c1, L1.c0)


plt.figure()

plt.plot(*L1.table(LB=0, RB=10, n =20), 'ro') # Unpacking returning x and y
plt.plot(*L2.table(LB=0, RB=10, n =20), 'bo') # Unpacking
plt.show()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////







