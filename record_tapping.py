# This is a Python script to record my keyboard tapping data.

import keyboard
import time

# Define a list to store the tapping data
tapping_data = []


def on_key_press(event):
    # Record the timestamp and key pressed
    timestamp = time.time()
    key = event.name

    # Append the data to the tapping_data list
    tapping_data.append((timestamp, key))


# Start listening for key presses
keyboard.on_press(on_key_press)

try:
    # Keep the program running to record key presses
    while True:
        pass
except KeyboardInterrupt:
    # Save the tapping data to a file when the program is interrupted
    with open('tapping_data.txt', 'w') as f:
        for timestamp, key in tapping_data:
            f.write(f"{timestamp}, {key}\n")

