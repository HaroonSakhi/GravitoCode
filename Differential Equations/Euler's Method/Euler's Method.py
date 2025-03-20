# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project Numerical differentiation.
# Any use or modification of this code should include proper
# attribution to the original author.

from numpy import sin, cos, linspace, arange
import matplotlib.pyplot as plt

def dydx(x):
    return 2 * cos(x) + 2

def Solution(x):
    return 2 * sin(x) + 2*x

def EulerMethod(start, end, stepSize, initialCondition=[0, 0]):
    X = [initialCondition[0]]
    Y = [initialCondition[1]]

    x = X[0] + stepSize
    y = Y[0]
    for x in arange(start + stepSize, end, stepSize):
        y += dydx(x) * stepSize
        X.append(x)
        Y.append(y)
    
    return X, Y

xi = -6
xf = 6
dx = 0.1

# Euler method approximation
X, Y = EulerMethod(xi, xf, dx, [-6, -11.44])

# Exact solution
x_sol = linspace(xi, xf, 10000)
y_sol = Solution(x_sol)

# Plot both the Euler method approximation and the exact solution
plt.plot(X, Y, label="Euler Approximation")
plt.plot(x_sol, y_sol, label="Exact Solution", linestyle="--")
plt.grid()
plt.legend()
plt.show()