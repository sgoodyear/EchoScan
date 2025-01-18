import serial
import numpy as np

import matplotlib.pyplot as plt

# Set up the serial connection
ser = serial.Serial('COM3', 1000000)  # Change 'COM3' to your Arduino's serial port

# Set up the plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_ylim(0, 100)  # Adjust the range according to your sensor's range

# Initialize an array to store the distances
angles = np.arange(0, 360, 5)
distances = np.zeros_like(angles)

# Function to update the plot
def update_plot(angle, distance):
    index = angle // 5
    distances[index] = distance
    ax.clear()
    ax.set_ylim(0, 100)
    ax.plot(np.deg2rad(angles), distances, 'bo')
    plt.draw()
    plt.pause(0.01)

# Read and plot the data
try:
    while True:
        line = ser.readline().decode('ascii').strip()
        if line:
            angle, distance = map(int, line.split())
            update_plot(angle, distance)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
    plt.show()