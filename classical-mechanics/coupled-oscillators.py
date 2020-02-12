import numpy as np
from matplotlib import pyplot as plt

# Defines some variables

initial_position_vector = np.array([2, -1]) # Initial positions of all the springs
evolution_matrix = np.array([[-1, 1], [1, -1]])
velocity_vector = np.array([0, 0])

time_int = 0.005
num = 0

# Calculates acceleration of the specific equation of motion

def update():

    global initial_position_vector
    global num
    global velocity_vector

    acceleration_vector = np.matmul(evolution_matrix, initial_position_vector)
    initial_position_vector = np.add(initial_position_vector, np.array([0.5*acceleration_vector[0]*(time_int**2), 0.5*acceleration_vector[1]*(time_int**2)]))
    initial_position_vector = np.add(initial_position_vector, np.array([velocity_vector[0]*time_int, velocity_vector[1]*time_int]))
    #print(acceleration_vector)

    velocity_vector = np.add(velocity_vector, np.array([acceleration_vector[0]*time_int, acceleration_vector[1]*time_int]))
    plt.quiver([0], [0], [initial_position_vector[0]], [initial_position_vector[1]], angles='xy', scale_units='xy', scale=1)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.savefig("./Pictures/"+str(num)+".png")
    plt.clf()

    num = num + 1
    print("Done: "+str(num))


for i in range(0, 2000):
    update()
