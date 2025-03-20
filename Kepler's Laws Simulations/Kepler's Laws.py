import math

G = 6.6743e-11
M = 1.9891e30
Au = 1.496e+11
dt = 30

time = 31536000  

class Planet:
    def __init__(self, mass, vel, pos):
        self.mass = mass
        self.vel = vel  # [vx, vy]
        self.pos = pos  # [x, y]

def force(r, mass):
    F = (G * M * mass) * (1 / r**2)
    return -F

def radius(x, y):
    return math.sqrt(x**2 + y**2)

def area(r, theta):
    return 0.5 * (r**2) * theta

# Initialize planets
earth = Planet(5.97219e24, [0, 30e3], [Au, 0])
mars = Planet(6.39e23, [0, 24e3], [1.5 * Au, 0])

earth_data = []
mars_data = []

for t in range(0, time, dt):
    theta0 = math.atan2(earth.pos[1], earth.pos[0])
    
    r = radius(earth.pos[0], earth.pos[1])
    rm = radius(mars.pos[0], mars.pos[1])
    
    a = force(r, earth.mass) / earth.mass
    am = force(r, mars.mass) / mars.mass
    
    ax = a * (earth.pos[0] / r)
    ay = a * (earth.pos[1] / r)
    axm = am * (mars.pos[0] / r)
    aym = am * (mars.pos[1] / r)
    
    earth.vel[0] += ax * dt
    earth.vel[1] += ay * dt
    
    mars.vel[0] += axm * dt
    mars.vel[1] += aym * dt
    
    earth.pos[0] += (earth.vel[0] * dt) + 0.5 * (ax * dt**2)
    earth.pos[1] += (earth.vel[1] * dt) + 0.5 * (ay * dt**2)
    
    mars.pos[0] += (mars.vel[0] * dt) + 0.5 * (axm * dt**2)
    mars.pos[1] += (mars.vel[1] * dt) + 0.5 * (aym * dt**2)
    
    theta = math.atan2(earth.pos[1], earth.pos[0])
    theta = theta - theta0
    area_value = area(r, theta)
    
    earth_data.append(f"{t} {earth.pos[0]} {earth.pos[1]} {area_value}\n")
    mars_data.append(f"{t} {mars.pos[0]} {mars.pos[1]} {area_value}\n")

with open("earth.txt", "w") as earth_file:
    earth_file.writelines(earth_data)

with open("mars.txt", "w") as mars_file:
    mars_file.writelines(mars_data)
