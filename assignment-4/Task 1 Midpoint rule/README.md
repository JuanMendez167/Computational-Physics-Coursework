# Week 5 Task 1

In this assignment we will try to estimate the definite integral of a function. One of the simplest method is the "midpoint rule", where the integration domain is split into a set of regular and small intervals, and the area below the function within each interval is estimated from a rectangle with a width of the interval and a height of the value of the function at the midpoint of the interval

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_a^bf(x)dx\approx&space;\frac{b-a}{n}\sum&space;_{i=0}^{n-1}f\left(a&plus;\left(i&plus;\frac{1}{2}\right)\frac{b-a}{n}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_a^bf(x)dx\approx&space;\frac{b-a}{n}\sum&space;_{i=0}^{n-1}f\left(a&plus;\left(i&plus;\frac{1}{2}\right)\frac{b-a}{n}&space;\right&space;)" title="\int_a^bf(x)dx\approx \frac{b-a}{n}\sum _{i=0}^{n-1}f\left(a+\left(i+\frac{1}{2}\right)\frac{b-a}{n} \right )" /></a>

The visual representation of the idea can be seen in following image

<img src="fmidpoint.png" alt="hi" class="inline"/>

TASK: In the midpoint.py program you can find the basic loop to perform midpoint integration of a generic function f from a to b, using a large number of small intervals. Modify the code to compute the integral of:
 
1. the sine function between 0 and pi, and
2. the cosine function between 0 and pi.

In each case, write out the error, i.e., the difference between the exact integral and the numerical result.
