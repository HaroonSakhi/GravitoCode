from vpython import *
from math import sqrt, pi, cos, sin

g1 = graph(xtitle="r [m]",ytitle="E [J]",width=400, height=200)
fK = gcurve(color=color.red, dot=True)
fU = gcurve(color=color.blue, dot = True)
fE = gcurve(color=color.purple, dot = True)
G = 6.67e-11
ME = 5.97e24
R = 6.3e6
m = 100
v1 = sqrt(2*G*ME/R)
v = vector(v1*cos(pi/4),v1*sin(pi/4),0)
t = 0 
dt = 1

earth = sphere(pos=vector(0,0,0),radius=R, texture=textures.earth)
ball = sphere(pos=vector(R,0,0),radius=R/20, color=color.yellow, make_trail=True)

while t <8600:
  rate(1000)
  r = ball.pos
  F = -G*ME*m*norm(r)/mag(r)**2
  a = F/m
  v = v + a*dt
  ball.pos = ball.pos + v*dt
  K = .5*m*mag(v)**2
  U = - G*ME*m/mag(r)
  E = K + U
  fK.plot(mag(r),K)
  fU.plot(mag(r),U)
  fE.plot(mag(r),E)
  t = t + dt

r2 = G*ME/(-.5*v1**2+G*ME/R)
print("r2 = ",r2," m")