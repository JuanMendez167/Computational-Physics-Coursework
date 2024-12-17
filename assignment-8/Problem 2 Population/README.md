# Problem 2 

In this assignment we will practice using the axis argument in numpy functions. 

A 18x4 table is given for the population of 4 countries from 1955 to 2015 in steps of 5 years, plus every year from 2016 to 2020 in step of 1 year. Every column is a country. Every row is a year, starting from 2020 in the first row and 1955 in the last row.

Calculate the average population for every year across all countries considered here using np.sum() and an appropriate axis as the optional argument. The result should be 18 numbers for the 18 years we consider.

Plot population against year for all 4 countries using array slicing, all on the same plot. The plot should start with the 1955 data on the left and 2020 data towards the right, so be sure to check the direction you slice your data.

Then plot the average population every year you just calculated on the same plot. Make sure it also starts from 1955 and ends with 2020.

