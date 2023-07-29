#
# Created by Phileosin on 2023/7/29.
# This is a grapher visualize data in data.csv
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Read the CSV file and load only the 'Timestamp' and 'Key' columns into a DataFrame
data = pd.read_csv('data.csv', usecols=['Timestamp', 'Key'])

# Count the occurrences of each letter in the 'Key' column
letter_counts = data['Key'].value_counts()

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar(letter_counts.index, letter_counts.values, color='skyblue')
plt.xlabel('Letter')
plt.ylabel('Occurrences')
plt.title('Letter Occurrences')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(letter_counts)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Letter Word Cloud')
plt.tight_layout()
plt.show()
