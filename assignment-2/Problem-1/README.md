# Week 2 Assignment 1

Loops can be useful to compute a series expansion of a function. The Taylor series of the inverse tangent function is given by

<img src="https://latex.codecogs.com/gif.image?\dpi{120}\arctan(x)=1-\frac{1}{3}x^3&plus;\frac{1}{5}x^5-\frac{1}{7}x^7&plus;\frac{1}{9}x^9&plus;\cdots" title="https://latex.codecogs.com/gif.image?\dpi{120}\arctan(x)=1-\frac{1}{3}x^3+\frac{1}{5}x^5-\frac{1}{7}x^7+\frac{1}{9}x^9+\cdots" />

We can use the above expression to compute the value of pi, using the fact that

<img src="https://latex.codecogs.com/gif.image?\dpi{120}\frac{\pi}{4}=\arctan(1)=1-\frac{1}{3}&plus;\frac{1}{5}-\frac{1}{7}&plus;\frac{1}{9}&plus;\cdots" title="https://latex.codecogs.com/gif.image?\dpi{120}\frac{\pi}{4}=\arctan(1)=1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}+\cdots" />

TASK: Write a loop to compute the value of pi using the first 1000 terms of the above series. This called the Leibniz formula.


EXPECTED OUTCOME: a value close to pi.
