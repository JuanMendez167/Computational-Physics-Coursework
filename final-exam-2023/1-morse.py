import numpy as np
import matplotlib.pyplot as plt

epsilon= 4e-4 * 27.211 * 1.6e-19 # in J
bohr = 0.53e-10 
sigma=2.4 * bohr # in m


def flj(x):    
    return -4*epsilon*(-12*sigma**12/x**13 \
                       +6*sigma**6/x**7)
      
def ulj(x):    
    return 4*epsilon*(sigma**12/x**12 \
                       -sigma**6/x**6)
        
rrange = np.linspace(1,2,100)*sigma


fig,ax = plt.subplots(2, figsize=(6,6))
ax[0].plot(rrange, ulj(rrange), 'k--')
ax[1].plot(rrange, flj(rrange), 'k-' )

ax[0].axhline(-epsilon)
ax[1].axhline(0)

ax[0].set_ylabel('Potentials(r)')
ax[1].set_ylabel('Forces(r)')
ax[0].set_xlabel('r')
ax[1].set_xlabel('r')

fig.tight_layout()
# //////////////////////////////////////////////

# Would we need to defind ke as well

De = epsilon
re = 2**(1/6) * sigma
a = np.sqrt(ke/2De)


def umorse(x):
     return De*(e**(-2*a(r-r*e)) - 2*e**(-a(r-re)))

def fmorse(x):
    return -De*(1-e**(-a(r-re)))**2

fig,ax = plt.subplots(2, figsize=(6,6))
ax[0].plot(rrange, umorse(rrange), 'k--')
ax[1].plot(rrange, fmorse(rrange), 'k-' )

ax[0].axhline(-De)
ax[1].axhline(0)

ax[0].set_ylabel('Potentials(r)')
ax[1].set_ylabel('Forces(r)')
ax[0].set_xlabel('r')
ax[1].set_xlabel('r')

fig.tight_layout()


# Question 1:
# a). The minimum Leonard Jones potential can be found as such
# vmin = 4*epsilon*(sigma**12/x**12 -sigma**6/x**6)
# Then vmin = 4*epsilon*(sigma/sigma**6 * np.sqqrt(2)**12 - (sigma/simga**6*np.sqrt(2))**6)
# Then vmin = 4*epsilon((1/2**2 - 1/2))
# Then vmin = 4*epsilon(1/4-1/2)
# Then vimn = 4*epsilon(1-2 / 4) = -epsilon # I exclueded the negative till the final part

# b). We can find r0, expressed using sigma as such
# Consider taking the partial derivate with respect to u the leonard jines potential
# upon doing soo you will obtain the following quantity.
# r0 = du/dr = -4*epsilon*(12(sigma/r)**12 * 1/r - 6*(sigma/r)^^6 *1/r)
# We just need to solve for r, we can do so by settingi the square breacket inside to 0
# Then we find (sigma/r)**6 = 1/2
# and therefore, r0 = 2**(1/6) * sigma

# We need to find the effective spring constant
# The effective spring constant is much harder to calculate but it can be done
# the effective spring constat value is k = 2*epslion*(n/r0)**2
# Heres how to calculate

# If we know that the min occurs at r=r0
# Then we can perform a taylor expansion at the equilibrium point
# you will find U(r) = U(r0) + 1/2*U"(r0)(r-r0)^2
# Afterwards it can be compared to a harmonic oscillator
# k= U"(r0)! and the plugging in our known values we can get
# The equilibirum constant

# Question 2:
# a) Finding the minimum value of the Morese Potential
# Similar to part a of question 1 you need to take the
# derivative  and then isolate for De. We could do rigorous math
# or realize that the minimum value is -De.(Where De is the well-depth)

# b) The minimum value is achieved at r=r0. Find r0.
# We have to equate 2^1/6*simga = 

# c) Show that the effective spring constant for the Morse potential
# is k=2Da^2. Hint: We need to use another Taylor expansion, but this time for
# the exponential function.

# A way easier method is to just take the derivate of the morese potential twice with respect to r, 
# evaluated at r=re, gives k=2Dea^2




#Task 1. ULJ analysis.
#Umin and r0 correct. you can find k in 2-md.py 
#13/15

#Task 2. U_Morse analysis. 
# Umin and k are correct.
#12/15

#Task 3. Morse potential and force
#5/15

#Subtotal
#30/45

