# This is a Python script to record my keyboard tapping data.

from pynput import keyboard
import time

# Define a list to store the tapping data
tapping_data = []

def on_key_press(key):
    try:
        # Record the timestamp and key pressed
        timestamp = time.time()
        key_str = key.char

        # Append the data to the tapping_data list
        tapping_data.append((timestamp, key_str))
    except AttributeError:
        pass

# Start listening for key presses
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

try:
    # Keep the program running to record key presses
    while True:
        pass
except KeyboardInterrupt:
    # Save the tapping data to a file when the program is interrupted
    current_date = time.strftime("%m_%d_%y")
    filename = f"input_data_{current_date}.txt"
    with open(filename, 'w') as f:
        for timestamp, key in tapping_data:
            f.write(f"{timestamp}, {key}\n")
