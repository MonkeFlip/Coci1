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
plt.grid(True)
plt.title("График исходной функции")
plt.bar(discrete_x_points, discrete_y_points,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()
#####################



####################################################
def W(k, m):
    return math.exp(1) ** complex(0, -2 * math.pi * k * m / N)

def W_FFT(k, m, N):
    return math.exp(1) ** complex(0, -2 * math.pi * k * m / N)

def DFT(points, size):
    result = [0] * size
    N = size
    m = 0
    while m < size:
        k = 0
        while k < N:
            result[m] += points[k] * W(k, m)
            k += 1
        m += 1
    return result

def reverseDFT(points, size):
    result = [0] * size
    m = 0
    while m < len(result):
        k = 0
        while k < N:
            result[m] += points[k] * W(-k, m)
            k += 1
        result[m] /= N
        m += 1
    return  result

#Прямое ДПФ
x_result = range(0, 8)
y_result = [0] * 8
N = 8
y_result = DFT(discrete_y_points, 8)



######График амплитуд
m = 0
amp_result = [0] * 8
while m < len(y_result):
    amp_result[m] = abs(y_result[m])
    m += 1

plt.grid(True)
plt.title("График амплитуды ДПФ")
plt.bar(x_result, amp_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()

####График фазы
m = 0
phase_result = [0] * 8
while m < len(y_result):
    phase_result[m] = y_result[m].imag
    m += 1

plt.grid(True)
plt.title("График фазы ДПФ")
plt.bar(x_result, phase_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()


###Обратное ДПФ
y_reverse = reverseDFT(y_result, 8)

plt.grid(True)
plt.title("График обратного ДПФ")
plt.bar(x_result, y_reverse,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()

#######################################################
###FFT
def FFT(a, N):
    result = [0] * N
    if len(a) == 1:
        return  a
    a_even = [0] * (int)(len(a) / 2)
    a_odd = [0] * (int)(len(a) / 2)
    k = 0
    e = 0
    o = 0
    while k < N:
        if k % 2 == 0:
            a_even[e] = a[k]
            e += 1
        else:
            a_odd[o] = a[k]
            o += 1
        k += 1
    b_even = FFT(a_even, (int)(N/2))
    b_odd = FFT(a_odd, (int)(N/2))
    wn = W_FFT(1, 1, N)
    w = 1
    j = 0
    while j < N / 2:
        result[j] = b_even[j] + w * b_odd[j]
        result[j + (int)(N/2)] = b_even[j] - w * b_odd[j]
        w *= wn
        j +=1
    return result

y_result = FFT(discrete_y_points, 8)

#############################
###График амплитуд БПФ
m = 0
amp_result = [0] * 8
while m < len(y_result):
    amp_result[m] = abs(y_result[m])
    m += 1

plt.grid(True)
plt.title("График амплитуды БПФ")
plt.bar(x_result, amp_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()

####График фазы БПФ
m = 0
phase_result = [0] * 8
while m < len(y_result):
    phase_result[m] = y_result[m].imag
    m += 1

plt.grid(True)
plt.title("График фазы БПФ")
plt.bar(x_result, phase_result,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()

################################
###reverseFFT
def reverseFFT(a, N):
    result = [0] * N
    if len(a) == 1:
        return  a
    a_even = [0] * (int)(len(a) / 2)
    a_odd = [0] * (int)(len(a) / 2)
    k = 0
    e = 0
    o = 0
    while k < N:
        if k % 2 == 0:
            a_even[e] = a[k]
            e += 1
        else:
            a_odd[o] = a[k]
            o += 1
        k += 1
    b_even = reverseFFT(a_even, (int)(N/2))
    b_odd = reverseFFT(a_odd, (int)(N/2))
    wn = W_FFT(-1, 1, N)
    w = 1
    j = 0
    while j < N / 2:
        result[j] = (b_even[j] + w * b_odd[j]) / (N / 2)
        result[j + (int)(N/2)] = (b_even[j] - w * b_odd[j]) / (N / 2)
        w *= wn
        j +=1
    return result

##############################################################
y_reverse = reverseFFT(y_result, 8)

plt.grid(True)
plt.title("График обратного БПФ")
plt.bar(x_result, y_reverse,
        width = 0.1, color = 'blue', alpha = 0.7,
        zorder = 2)
plt.show()