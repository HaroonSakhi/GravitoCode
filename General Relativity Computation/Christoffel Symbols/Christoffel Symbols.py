# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project GR Computations.
# Any use or modification of this code should include proper
# attribution to the original author.

from sympy import *


t, r, theta, phi, M, G, c = symbols("t r theta phi M G c")


coordinates = [t, r, theta, phi]


def g(i,j):
    
    g00 = (1) - (2*G*M)/(r*(c**2))
    g01 = 0
    g02 = 0
    g03 = 0
    g10 = 0
    g11 = -(1/(1 - ((2*G*M)/(r*(c**2)))))
    g12 = 0
    g13 = 0
    g20 = 0
    g21 = 0
    g22 = -r**2
    g23 = 0
    g30 = 0
    g31 = 0
    g32 = 0
    g33 = -(r**2)*((sin(theta))**2)
    
    g = ([g00,g01,g02,g03],
         [g10,g11,g12,g13],
         [g20,g21,g22,g23],
         [g30,g31,g32,g33])

    
    return g[i][j]


def dydx(i,j,k):
    derivative = diff(g(i,j), coordinates[k])
    return simplify(derivative)

def Inverse_Metric(i,j):

    M = Matrix([[g(0,0),g(0,1),g(0,2),g(0,3)],
                [g(1,0),g(1,1),g(1,2),g(1,3)],
                [g(2,0),g(2,1),g(2,2),g(2,3)],
                [g(3,0),g(3,1),g(3,2),g(3,3)]])

    return M.inv(method = "LU")[i,j]

def Gamma(i,j,k):

    s = 0

    for l in range(4):
        s = s + ((0.500) * Inverse_Metric(i, l) * (dydx(k,l,j) + dydx(l,j,k) - dydx(j,k,l)))

    return simplify(s)

for i in range(4):
    for j in range(4):
        for k in range(4):
            if Gamma(i,j,k) == 0:
                pass
            else:
              print("[",coordinates[i],coordinates[j],coordinates[k],"]",Gamma(i,j,k))
              
