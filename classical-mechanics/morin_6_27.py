import numpy as np
from matplotlib import pyplot as plt

# Defines some variables

radius = 1
angle = 0
angular_velocity = 0
radial_velocity = 0
alpha = 0.1
time_int = 0.0005
grav_constant = 9.81

r_list = [radius]
a_list = [angle]
v_list = [radial_velocity]
ac_list = []

def update():

    global radius
    global angle
    global angular_velocity
    global radial_velocity

    angular_acceleration = ((1*grav_constant*np.cos(angle)) / radius) - (2 * angular_velocity * radial_velocity / radius)
    radial_acceleration = (1 / (1 + alpha)) * (alpha*radius*(angular_velocity**2) + alpha*grav_constant*np.sin(angle) - grav_constant)

    new_angular_velocity = angular_velocity + angular_acceleration*time_int
    new_radial_velocity = radial_velocity + radial_acceleration*time_int

    angle += angular_velocity*time_int
    radius += radial_velocity*time_int

    angular_velocity = new_angular_velocity
    radial_velocity = new_radial_velocity

    if (len(r_list) > 2):
        if (radius > r_list[len(r_list)-2] and r_list[len(r_list)-3] > r_list[len(r_list)-2]):
            print(r_list[len(r_list)-2])

    r_list.append(radius)
    v_list.append(radial_velocity)
    ac_list.append(angular_acceleration)
    a_list.append(angle)

    #print(angular_velocity)
    #print(angular_velocity*time_int + (1/2)*angular_acceleration*(time_int**2))

sum = 0
while(radius > 0):
    sum += 1
    update()

plt.plot([i for i in range(0, sum+1)], r_list)
plt.show()
