# Code for the generation of electromagnetic field lines

import numpy as np
from matplotlib import pyplot as plt

class FixedCharge:

    def __init__(self, magnitude, coordinate):
        self.magnitude = magnitude
        self.coordinate = np.array(coordinate)

class MovingCharge:

    def __init__(self, magnitude, mass, init_coordinate, init_velocity):
        self.magnitude = magnitude
        self.mass = mass
        self.coordinate = np.array(init_coordinate)
        self.velocity = np.array(init_velocity)

# Takes one step forward in time

def simulation_step(fixed_charges, moving_charge, time_step):

    net_force = np.array([0.0, 0.0])

    for i in fixed_charges:
        
        vector = moving_charge.coordinate - i.coordinate
        distance = np.linalg.norm(vector)

        vector = vector / distance

        magnitude = (i.magnitude * moving_charge.magnitude) / distance**2

        net_force += magnitude * vector
    
    acceleration = (1 / moving_charge.mass) * net_force

    new_position = moving_charge.coordinate + moving_charge.velocity * time_step + 0.5 * acceleration * time_step**2

    moving_charge.coordinate =  new_position

    new_velocity = moving_charge.velocity + acceleration * time_step
    moving_charge.velocity = new_velocity

    return [new_position, new_velocity]

# Simulates the motion of the particle, assuming k = 1

def simulate_motion(fixed_charges, moving_charge, time_step, N):

    positions = []
    for j in range(0, N):
        res = simulation_step(fixed_charges, moving_charge, time_step)
        positions.append(res[0])

    return [[i[0] for i in positions], [i[1] for i in positions]]

# Creates the fixed and moving charges

# Runs the simulation

time = 0.0001
fixed = [FixedCharge(1, [1, 0]), FixedCharge(-1, [-1, 0])] 

init_p = [[0, 0.1], [0, 0.075], [0, 0.05], [0, 0.025], [0, 0], [1.1, 0.1], [1.5, 0], [1.5, 0.075]]
init_v = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, -1], [0, 0], [0, -0.04]]
N = [8870, 8820, 8770, 8740, 8720, 475, 3950, 4000]

positions = []

for i in range(0, len(init_p)):
    
    moving = MovingCharge(-1, 1, init_p[i], init_v[i])
    positions.append(simulate_motion(fixed, moving, time, N[i]))

# Plots all of the positions 

x_fixed = []
y_fixed = []

for k in fixed:
    x_fixed.append(k.coordinate[0])
    y_fixed.append(k.coordinate[1])

plt.scatter(x_fixed, y_fixed)

for i in positions:

    x = i[0]
    y = i[1]

    plt.plot(x, y, c="blue")
    plt.plot([-1*i for i in x], y, c="blue")
    plt.plot(x, [-1*i for i in y], c="blue")
    plt.plot([-1*i for i in x], [-1*i for i in y], c="blue")

plt.show()




