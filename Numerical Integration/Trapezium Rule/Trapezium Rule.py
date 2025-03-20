# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project Numerical Integration.
# Any use or modification of this code should include proper
# attribution to the original author.

from numpy import exp

#Our function
def Function(x):
    return exp(-2* x)

def TrapezoidalRule(start, end, numberOfCuts):

    stepSize = (end - start) / numberOfCuts #Calculates the step size

    #Temporary variables,
    #K is just the sum (y1 + y2 + y3 + ... + y(n-1)) 
    K = 0
    x = start + stepSize

    for i in range(1, numberOfCuts - 1):
        K += Function(x)
        x += stepSize
    
    Area = stepSize/2 * (Function(start) + Function(end)) + stepSize * K
    return Area

x_start = 0
x_end = 2
N = 1000

#Outputs the area with a precision of 5 decimal places.
print(f'Area: {TrapezoidalRule(x_start, x_end, N):.5f}')