import matplotlib.pyplot as plt
import numpy as np
import math

x_points = [0] * 100
y_points = [0] * 100
value = 0
i = 0
while i < len(x_points):
    y_points[i] = math.cos(3 * value) + math.sin(2 * value)
    x_points[i] = value
    i += 1
    value += 0.1

plt.plot(x_points, y_points)
plt.grid(True)
plt.show()

####################################################
# x_points = [0] * 500
# y_points = [0] * 500
# N = 8
# W = math.exp(1) ** complex(0, -2 * math.pi / N)
# m = 0
# while m < x_points:
#     k = 0
#     while k