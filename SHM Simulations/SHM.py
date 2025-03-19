import numpy as np

# Constants
k = 1.00  
mass = 1.00  
x0 = 5.00  
mu = 0.20  
dt = 0.001  
time = 30.00  

# Functions
def potential_energy(x):
    return 0.5 * k * x**2

def kinetic_energy(v):
    return 0.5 * mass * v**2

def force(x, v):
    return -k * x - mu * v

# Initialization
x = x0
v = 0.00
t = 0

# Open file to save data
with open("Data.txt", "w") as file:
    while t < time:
        pe = potential_energy(x)
        ke = kinetic_energy(v)
        te = pe + ke

        a = force(x, v) / mass
        x = x + (v * dt) + (a * (dt**2) / 2)
        v = v + (a * dt)

        file.write(f"{t} {x} {v} {pe} {ke} {te}\n")

        t += dt  # Increment time
