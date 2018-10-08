import math
import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

# Using a simulation to demonstrate central limit theorem

x_data = range(0, 100000)

y_data = []

for r in range (0, 100000):
    random_sum = 0
    for i in range (0, 100):
        selector = random.randint(0, 1)
        if (selector == 0):
            random_sum = random_sum - 1
        if (selector == 1):
            random_sum = random_sum + 1
    random_sum = float(random_sum)/100
    y_data.append(random_sum)

def input_function(x, a, b):
    return a * np.exp(-1 * ((b + x) ** 2))

#params, params_covariance = optimize.curve_fit(input_function, x_data, y_data,
#                                               p0=[2, 2])



y_final = []
x_final = []

for t in y_data:
    if (t not in x_final):
        x_final.append(t)
        summation = 0
        for f in y_data:
            if (f == t):
                summation = summation + 1
        summation = summation - 1
        y_final.append(summation)

print(y_final)
print(x_final)
print(len(x_final))
print(len(y_final))

plt.title("Central Limit Theorem Simulation")
plt.scatter(x_final, y_final)
plt.show()
