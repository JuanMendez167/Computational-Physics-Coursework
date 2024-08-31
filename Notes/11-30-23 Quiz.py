# import numpy as np
# import matplotlib.pyplot as plt

# class Line():
#     def __init__(self,c0, c1):
#         self.c0 = c0
#         self.c1 = c1
        
#     def __calc__(self, x):
#         return self.c0 + self.c1 * x
        
        
#     def table(self, LB=0, RB=20, n=100):
#         x = np.linspace(LB,RB,n)
#         y = self.__calc__(x)
#         return x,y
    
# class Parabola(Line):
#     def __init__(self, c0,c1,c2):
#         super().__init__(c0, c1)
#         self.c2=c2      
        
#     def __calc__(self, x):
#         return super().__calc__(x) + self.c2 * x**2
        
# class Cubic(Line):
#     def __init__(self, c0,c1,c2, c3):
#         super().__init__(c0, c1)
#         self.c2=c2
#         self.c3=c3
        
#     def __calc__(self,x):
#         return super().__calc__(x) + self.c2 * x **2 + self.c3 * x**3
        
        
# L1 = Line(c0=1, c1=2) # Intercept of 1 and slope of 2
# L2 = Line(c0=0.5, c1=2.5)
# P1 = Parabola(1,2,3)
# Cu1 = Cubic(1,2,3,4)
# print("The slope and intersecr of line 1 is", L1.c1, L1.c0)


# plt.figure()

# plt.plot(*L1.table(LB=0, RB=10, n =20), 'ro') # Unpacking returning x and y
# plt.plot(*L2.table(LB=0, RB=10, n =20), 'bo') # Unpacking
# plt.plot(*P1.table(LB=0, RB=10, n =20), 'ko') # Unpacking
# plt.plot(*Cu1.table(LB=0, RB=10, n =20), 'go') # Unpacking)

# plt.show()
# /////////////////////////////////////////////////////////////////////////////////////////////////////


# A more efficient method of achieving the same thing is to pass the parabola class directly since it defines
# more variables to begin witth

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
    
class Parabola(Line):
    def __init__(self, c0,c1,c2):
        super().__init__(c0, c1)
        self.c2=c2      
        
    def __calc__(self, x):
        return super().__calc__(x) + self.c2 * x**2
        
class Cubic(Parabola):
    def __init__(self, c0,c1,c2, c3):
        super().__init__(c0, c1, c2)
        self.c3=c3
        
    def __calc__(self,x):
        return super().__calc__(x) + self.c3 * x**3
        
        
L1 = Line(c0=1, c1=2) # Intercept of 1 and slope of 2
L2 = Line(c0=0.5, c1=2.5)
P1 = Parabola(1,2,3)
Cu1 = Cubic(1,2,3,4)
print("The slope and intersecr of line 1 is", L1.c1, L1.c0)


plt.figure()

plt.plot(*L1.table(LB=0, RB=10, n =20), 'ro') # Unpacking returning x and y
plt.plot(*L2.table(LB=0, RB=10, n =20), 'bo') # Unpacking
plt.plot(*P1.table(LB=0, RB=10, n =20), 'ko') # Unpacking
plt.plot(*Cu1.table(LB=0, RB=10, n =20), 'go') # Unpacking)

plt.show()



