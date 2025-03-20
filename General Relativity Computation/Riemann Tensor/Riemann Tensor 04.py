# Author: Haroon Sakhi
# Description: This code was developed by Haroon Sakhi as part
# of the project GR Computations.
# Any use or modification of this code should include proper
# attribution to the original author.

from ChristoffelSymbols import *
from RiemannTensor13 import *
from sympy import *

t, r, theta, phi

non_zeros = []
coors = [t, r, theta, phi]

def Riemann_Tensor2(i,j,k,l):

    R = g(i,i) * Riemann_Tensor(i,j,k,l)

    return simplify(R)


#for i in range(4):
 #   for j in range(4):
  #      for k in range(4):
   #         for l in range(4):
    #            if Riemann_Tensor2(i,j,k,l) == 0 or Riemann_Tensor2(i,j,k,l) in non_zeros:
     #               pass
      #          else:
       #             print("[",coors[i],coors[j],coors[k],coors[l],"]", Riemann_Tensor2(i,j,k,l))
        #            non_zeros.append(Riemann_Tensor2(i,j,k,l))

print(Riemann_Tensor(0,1,0,1))

print(Riemann_Tensor2(0,1,0,1))
