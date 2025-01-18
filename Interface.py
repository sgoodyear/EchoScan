import matplotlib.pyplot as plt
import numpy as np
import serial

# Set up the serial connection
ser = serial.Serial('COM3', 9600)

# Initialize the plot
plt.ion()
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
angles = np.deg2rad(np.arange(0, 360, 5))  # Convert angles to radians
distances = np.zeros_like(angles)
sc = ax.scatter(angles, distances)

ax.set_ylim(0, 200)  # Adjust based on expected distance range

current_angle_index = 0

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('ascii').strip()
            print(data)
            if data.isdigit():
                distance = int(data)
                distances[current_angle_index] = distance
                current_angle_index = (current_angle_index + 1) % len(angles)

            sc.set_offsets(np.c_[angles, distances])
            fig.canvas.draw_idle()
            plt.pause(0.01)
    except KeyboardInterrupt:
        break

ser.close()