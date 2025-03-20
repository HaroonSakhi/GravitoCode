# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project GR Computations.
# Any use or modification of this code should include proper
# attribution to the original author.

from ChristoffelSymbols import *
from sympy import *


t, r, theta, phi = symbols("t r theta phi")

coordinate = [t,r,theta,phi]




def Riemann_Tensor(i,j,k,l):
    T3 = 0
    T4 = 0
    T1 = diff(Gamma(i,l,j),coordinate[k])
    T2 = diff(Gamma(i,k,j),coordinate[l])
    
    for m in range(4):
        
        T3 = T3 + (Gamma(i,k,m) * Gamma(m,l,j))
        T4 = T4 + (Gamma(i,l,m) * Gamma(m,k,j))

    R = T1 - T2 + T3 - T4

    return simplify(R)

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if Riemann_Tensor(i,j,k,l) == 0:
                    pass
                else:
                 print("[", coordinate[i], coordinate[j], coordinate[k], coordinate[l],"]",Riemann_Tensor(i,j,k,l))