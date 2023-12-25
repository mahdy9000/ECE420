import numpy as np
import matplotlib.pyplot as plt
import os
# def peak_detection(t, sig):
#     peaks = []
#     max_val = -np.Inf
#     N = len(sig)
#     for i in range (0,N):
#         if sig[i] > max_val:
#             max_val = sig[i]
#             position = t[i]
#
#     peaks.append((position, max_val))
#     return np.array(peaks)
def peak_detection(t, sig,thresh):
    peaks = []
    max_val = -np.Inf
    N = len(sig)
    for i in range (0,N):
        if sig[i] > thresh  and sig[i] > sig[i-2] and sig[i]> sig[i+2]:
            max_val = sig[i]
            position = t[i]
            peaks.append((position, sig[i]))

    return np.array(peaks)

csv_filename = "sample_sensor_data.csv"
data = np.genfromtxt(csv_filename, delimiter= ",").T
timestamps = (data[0] - data [ 0,0 ]) / 1000
accel_data = data[1:4]
gyro_data = data [4:-1]
max_peaks = peak_detection(timestamps, accel_data[0], 5)
plt.scatter(max_peaks[:,0], max_peaks[:,1], color = 'red')
plt.plot(timestamps, accel_data[0])
plt.title("First axis of accelerometer data")
plt.xlabel("Time")
plt.ylabel("Meters per second")
plt.show()
