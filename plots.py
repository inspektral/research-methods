import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV files
data_summary = pd.read_csv('data_summary.csv', index_col=0)
livebench = pd.read_csv('livebench.csv', index_col=0)

# Calculate the average scores for each row
data_summary['average'] = data_summary.mean(axis=1)
livebench['average'] = livebench.mean(axis=1)

# Create a bar graph
x = np.arange(len(data_summary))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 5))
bars1 = ax.bar(x - width/2, data_summary['average'], width, label='Data Summary Average')
bars2 = ax.bar(x + width/2, livebench['average'], width, label='Livebench Average')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Score')
ax.set_title('Comparison of collected averages and livebench averages')
ax.set_xticks(x)
ax.set_xticklabels(data_summary.index, rotation=45, ha='right')
ax.legend()

ax.grid(True)

fig.tight_layout()
