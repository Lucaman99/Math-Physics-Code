import math
import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

# Using a simulation to demonstrate central limit theorem

def distribute(prob, colors):

    x_data = range(0, 100000)

    y_data = []

    for r in range (0, 100000):
        random_sum = 0
        for i in range (0, 100):
            selector = random.randint(1, 10)
            if (selector < prob+1):
                random_sum = random_sum - 1
            else:
                random_sum = random_sum + 1
        random_sum = float(random_sum)/100
        y_data.append(random_sum)



    y_final = []
    x_final = []

    for t in y_data:
        if (t not in x_final):
            x_final.append(float(t))
            summation = 0
            for f in y_data:
                if (f == t):
                    summation = summation + 1
            summation = summation - 1
            y_final.append(float(summation))


    #def input_function(x, a, b):
    #    return float(a * math.exp(x + b))


    #params, params_covariance = optimize.curve_fit(input_function, x_final, y_final,
    #                                               p0=[2.0, 2.0])


    #print(params)


    print(y_final)
    print(x_final)
    print(len(x_final))
    print(len(y_final))

    plt.scatter(x_final, y_final, color=colors)

distribute(1, 'r')
distribute(2, 'b')
distribute(3, 'g')
distribute(4, 'y')
distribute(5, 'r')
distribute(6, 'b')
distribute(7, 'g')
distribute(8, 'y')
distribute(9, 'r')

plt.title("Central Limit Theorem Simulation")
#plt.plot(x_final, input_function(x_final, params[0], params[1]))
plt.show()
