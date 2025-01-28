import matplotlib.pyplot as plt
import numpy as np
import serial

# Set up the serial connection
ser = serial.Serial('COM3', 9600)                            # Change COM3 to match where your Arduino is plugged in, match Baud rate to Arduino

# Initialize the plot
plt.ion()                                                    # Use interactive plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})   # Set up polar axies
angles = np.deg2rad(np.arange(0, 360, 5))                    # Convert angles to radians
distances = np.zeros_like(angles)
sc = ax.scatter(angles, distances)

ax.set_ylim(0, 200)                                          # Adjust based on expected distance range (default 0 inches to 200 inches)
current_angle_index = 0                                      # Start at the first (0 degrees) position

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('ascii').strip()    # Read measurements/data from the Arduino program
            print(data)
            if data.isdigit():
                distance = int(data)                         # Save the measurement
                distances[current_angle_index] = distance
                current_angle_index = (current_angle_index + 1) % len(angles)

            sc.set_offsets(np.c_[angles, distances])
            fig.canvas.draw_idle()                           # Update the plot
            plt.pause(0.01)
    except KeyboardInterrupt:
        break

ser.close()
