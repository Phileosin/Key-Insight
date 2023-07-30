#
# Created by Phileosin on 2023/7/29.
#
import csv
from pynput import keyboard
import time
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define a list to store the tapping data
tapping_data = []
recording = True

def on_key_press(key):
    global recording
    try:
        # Record the timestamp and key pressed
        timestamp = time.time()
        key_str = key.char
        # Append the data to the tapping_data list
        tapping_data.append((timestamp, key_str))
    except AttributeError:
        pass

    # Check if the recording should be stopped
    if not recording:
        return False

# Start listening for key presses
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

try:
    print("Recording... Press 'Ctrl+C' to stop recording.")
    # Keep the program running to record key presses
    while True:
        pass
except KeyboardInterrupt:
    # Stop the recording
    recording = False
    # Save the tapping data to a CSV file when the program is interrupted
    current_date = time.strftime("%m_%d_%y")
    filename = f"input_data_{current_date}.csv"
    with open(filename, 'w', newline='') as f:
        # Create a CSV writer
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(["timestamp", "key"])
        # Write the data rows
        for timestamp, key in tapping_data:
            writer.writerow([timestamp, key])

# Read the CSV file and load only the 'Timestamp' and 'Key' columns into a DataFrame
data = pd.read_csv(filename, usecols=['timestamp', 'key'])

# Count the occurrences of each letter in the 'Key' column
letter_counts = data['key'].value_counts()

# Plot the bar graph
plt.figure(figsize=(12, 8))  # Increase the figure size
plt.bar(letter_counts.index, letter_counts.values, color='skyblue')
plt.xlabel('Letter')
plt.ylabel('Occurrences')
plt.title(f'Letter Occurrences on {current_date}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'occurrences_{current_date}.png', dpi=600)  # Increase the DPI
plt.show()

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(letter_counts)
plt.figure(figsize=(12, 8))  # Increase the figure size
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f'Letter Cloud for {current_date}')
plt.tight_layout()
plt.savefig(f'letter_cloud_{current_date}.png', dpi=600)  # Increase the DPI
plt.show()