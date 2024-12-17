#Week 10 Task 2

import numpy as np
import matplotlib.pyplot as plt

#Every column is a country. 
#Total of 4 countries.

#Every row is one year. e.g. first row is the population in 2020
#Total of 18 rows, representing 1955-2020 in steps of 5 years.
popula = np.array([[3.31002651e+08, 1.28932753e+08, 3.77421540e+07, 2.12559417e+08],
       [3.29064917e+08, 1.27575529e+08, 3.74110470e+07, 2.11049527e+08],
       [3.27096265e+08, 1.26190788e+08, 3.70745620e+07, 2.09469323e+08],
       [3.25084756e+08, 1.24777324e+08, 3.67320950e+07, 2.07833823e+08],
       [3.23015995e+08, 1.23333376e+08, 3.63829440e+07, 2.06163053e+08],
       [3.20878310e+08, 1.21858258e+08, 3.60266760e+07, 2.04471769e+08],
       [3.09011475e+08, 1.14092963e+08, 3.41475640e+07, 1.95713635e+08],
       [2.94993511e+08, 1.06005203e+08, 3.21643090e+07, 1.86127103e+08],
       [2.81710909e+08, 9.88998450e+07, 3.05883830e+07, 1.74790340e+08],
       [2.65163745e+08, 9.16632850e+07, 2.91641520e+07, 1.62019896e+08],
       [2.52120309e+08, 8.39431320e+07, 2.75413190e+07, 1.49003223e+08],
       [2.40499825e+08, 7.59834850e+07, 2.57448100e+07, 1.35274080e+08],
       [2.29476354e+08, 6.77613720e+07, 2.44168860e+07, 1.20694009e+08],
       [2.19081251e+08, 5.96079530e+07, 2.30592650e+07, 1.07216205e+08],
       [2.09513341e+08, 5.14935650e+07, 2.13743260e+07, 9.51132650e+07],
       [1.99733676e+08, 4.41238530e+07, 1.96279800e+07, 8.33735300e+07],
       [1.86720571e+08, 3.77718590e+07, 1.78474050e+07, 7.21792260e+07],
       [1.71685336e+08, 3.23505960e+07, 1.56737630e+07, 6.25339190e+07]])

# Calculate the average population for every year across all countries considered here
# The result should be 18 numbers for the 18 years we consider.
average_population = np.mean(popula, axis=1)
print(average_population)

'''
This prints 
[1.77559244e+08 1.76275255e+08 1.74957734e+08 1.73607000e+08
 1.72223842e+08 1.70808753e+08 1.63241409e+08 1.54822532e+08
 1.46497369e+08 1.37002770e+08 1.28151996e+08 1.19375550e+08
 1.10587155e+08 1.02241168e+08 9.43736242e+07 8.67147598e+07
 7.86297652e+07 7.05609035e+07]
'''

# KEYPOINT WHEN REVIEWING THIS
# The dimensions of the years array and the data in popula list don't match, I noticed some 
# discrepancies in the total amount of data points an years we consider. Its confusing intially
# on github it says 1995 to 2020 and then 1955 to 2020 and so in order to avoid that lets shift 
# away from that and use the information we have available
 
years = np.arange(2020, 2020 - 5 * len(average_population), -5)

# Plot population against year for all 4 countries using array slicing, all on the same plot. 

for i in range(4):
    plt.plot(years, popula[:, i], label=f'Country {i + 1}')

# Plot the average population for the available years
plt.plot(years[:len(average_population)], average_population, label='Average Population', linestyle='--')

plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()



#✔
