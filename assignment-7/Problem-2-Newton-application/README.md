# Problem2

**Task 1.** We can actually relieve the user of providing the derivative df in the Newton-Raphson method. **Write another Newton-Raphson method newton2()** that numerically calculates df, so that df does not need to be provided outside newton2(). Test your newton2() on the sine function again to find a root at pi, this time only providing the sine fucntion itself but not its derivative.

**Task 2.** With this new-found freedom, test your newton2() on our in-class projectile exercise: given that the projectile starts out at a speed of 30 m/s, an angle of 30 degrees above ground level, how far can it reach? g = 9.8 m/s^2 and air drag linear coefficient b = 1 s^-1. We already found out in class that the answer is near 23.29m. You may find that you can only get this solution if your initial guess is roughly between 21 and 25 m; otherwise the code crashes.  

To find out why this is the case, plot out the f(R) function against R. Sketch out the first few iterations of the Newton-Raphson method. **Based on this sketech, provide a comment on why the algorithm fails if you start from R>25**. An example sketch is provided.

**Task 3**. Repeat the same to **explain why the algorithm fails if you start from R<21.**

(The intention of this problem is to show that the function could be ill-behaved around your desired solution such that you need to start really close to make the Newton-Raphson method work.)
