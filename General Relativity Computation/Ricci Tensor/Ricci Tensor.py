# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project GR Computations.
# Any use or modification of this code should include proper
# attribution to the original author.

from ChristoffelSymbols import *

from sympy import *

t,r,theta,phi = symbols("t r theta phi")

coors = [t,r,theta,phi]


def Ricci_Tensor(i,j):
    T1 = 0
    T2 = 0
    T3 = 0
    T4 = 0

    for k in range(4):
        for m in range(4):

            T1 = T1 + diff(Gamma(k,i,j),coors[k])
            T2 = T2 + diff(Gamma(k,i,k),coors[j])
            T3 = T3 + (Gamma(k,i,j) * Gamma(m,k,m))
            T4 = T4 + (Gamma(k,i,m) * Gamma(m,j,k))

    Rij = T1 - T2 + T3 - T4

    return simplify(Rij)


for i in range(4):
    for j in range(4):
        if Ricci_Tensor(i,j) == 0:
            pass
        else:
            print("[",coors[i],coors[j],"]", "=", Ricci_Tensor(i,j))
