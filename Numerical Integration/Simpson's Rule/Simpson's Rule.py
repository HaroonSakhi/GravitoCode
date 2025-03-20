# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project Numerical Integration.
# Any use or modification of this code should include proper
# attribution to the original author.

from numpy import sin


def Function(x):
    return 0.4 * sin(0.8 * (x*x)) + 2

def SimpsonsRule(start, end, numberOfIntervals):
    h = (end - start) / numberOfIntervals
    x = start + h


    y0 = Function(start)
    yn = Function(end)
    K = 0

    for i in range(1, numberOfIntervals):
        if i%2 == 0:
            K += 2 * Function(x)
        else:
            K += 4 * Function(x)
        x += h

    Area = (h/3.00) * (y0 + K + yn)
    return Area



xi = 0
xf = 5
N = 10000

if N%2 != 0:
    print("number of intervals must be even, adding 1 to number of intervals")
    N += 1

error = abs((SimpsonsRule(xi, xf, N) - 10.2588)/ 10.2588 )* 100
print(f"Area: {SimpsonsRule(xi, xf, N):.4f}")
print(f"Error: {error:.4f}")