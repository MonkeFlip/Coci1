import matplotlib.pyplot as plt
import numpy as np
import math

x_points = [0] * 64
y_points = [0] * 64
value = 0
i = 0
while i < len(x_points):
    y_points[i] = math.cos(value) + math.sin(value)
    x_points[i] = value
    i += 1
    value += 0.1

plt.plot(x_points, y_points)
plt.grid(True)
plt.show()
#####################
discrete_x_points = [0] * 8
discrete_y_points = [0] * 8
i=0
while i < len(discrete_x_points):
    discrete_x_points[i] = x_points[i*8]
    discrete_y_points[i] = y_points[i*8]
    i +=1
plt.plot(discrete_x_points, discrete_y_points)
plt.grid(True)
plt.show()
#####################



####################################################
def W(k, m):
    return math.exp(1) ** complex(0, -2 * math.pi * k * m / N)

#Прямое ДПФ
x_result = range(0, 8)
y_result = [0] * 8
N = 8
m = 0
while m < len(y_result):
    k = 0
    while k < N:
        y_result[m] += discrete_y_points[k] * W(k, m)
        k += 1
    m += 1



######График амплитуд
m = 0
amp_result = [0] * 8
while m < len(y_result):
    amp_result[m] = abs(y_result[m])
    m += 1

plt.grid(True)
plt.bar(x_result, amp_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()

####График фаз
m = 0
phase_result = [0] * 8
while m < len(y_result):
    phase_result[m] = y_result[m].imag
    m += 1

plt.grid(True)
plt.bar(x_result, phase_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()


###Обратное ДПФ
y_reverse = [0] * 8
m = 0
while m < len(y_reverse):
    k = 0
    while k < N:
        y_reverse[m] += y_result[k] * W(-k, m)
        k += 1
    y_reverse[m] /= N
    m += 1

plt.plot(x_result, y_reverse)
plt.grid(True)
plt.show()

#####################
array = np.fft.fft(discrete_y_points)
f = 0
while f < len(array):
    array[f] = abs(array[f])
    f += 1


plt.plot(x_result, array)
plt.grid(True)
plt.show()

##############################
x = np.asarray(discrete_y_points, dtype=float)
N = x.shape[0]
n = np.arange(N)
k = n.reshape((N, 1))
M = np.exp(-2j * np.pi * k * n / N)
res = np.dot(M, x)

plt.plot(x_result, res)
plt.grid(True)
plt.show()

