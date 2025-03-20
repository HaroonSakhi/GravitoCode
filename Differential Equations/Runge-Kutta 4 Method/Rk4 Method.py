# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project Numerical differentiation.
# Any use or modification of this code should include proper
# attribution to the original author.

from numpy import exp, linspace, arange
import matplotlib.pyplot as plt

def dydx(x, y):
    return -2 * x * y

def Solution(x):
    return 4 * exp(-x**2)

def RK4(start, end, stepSize, initialConditions=[0, 0]):
    X = [initialConditions[0]]
    Y = [initialConditions[1]]

    x = X[0] + stepSize
    y = Y[0]

    for x in arange(start + stepSize, end, stepSize):
        K1 = stepSize * dydx(x, y)
        K2 = stepSize * dydx(x + stepSize/2, y + K1/2)
        K3 = stepSize * dydx(x + stepSize/2, y + K2/2)
        K4 = stepSize * dydx(x + stepSize, y + K3)
        y += (1 / 6) * (K1 + 2*K2 + 2*K3 + K4)
        X.append(x)
        Y.append(y)

    return X, Y

xi = -2
xf = 2
dx = 1e-6
IC = [-2, 0.07326]

X, Y = RK4(xi, xf, dx, IC)

# Exact solution
x_sol = linspace(xi, xf, 10000)
y_sol = Solution(x_sol)

# Plot both the RK4 method approximation and the exact solution
plt.plot(X, Y, label="RK4 Approximation")
plt.plot(x_sol, y_sol, label="Exact Solution", linestyle="--")
plt.grid()
plt.legend()
plt.show()