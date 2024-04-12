import matplotlib.pyplot as plt
import numpy as np

# Define the years and the smooth decline in accuracy to mimic the provided chart
years = np.arange(1985, 2016)
accuracy_smooth = np.linspace(0.35, 0.2, len(years))

# Sort node_count in ascending order for visual similarity to the provided chart
node_count_sorted = np.sort(np.random.uniform(10000, 60000, len(years)))

# Create figure and axis objects with the adjusted font sizes
fig, ax1 = plt.subplots()

# Plot the accuracy with a thicker and brighter red line
ax1.plot(years, accuracy_smooth, 'o-', color='firebrick', linewidth=2)
ax1.set_xlabel('Year', fontsize=20)
ax1.set_ylabel('Accuracy', color='firebrick', fontsize=20)
ax1.tick_params(axis='y', labelcolor='firebrick', labelsize=18)
ax1.tick_params(axis='x', labelsize=18)

# Remove the vertical gridlines and make horizontal gridlines darker
ax1.grid(True, linestyle='--', linewidth=0.5, color='gray', axis='y')
ax1.set_facecolor('white')

# Instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()

# Plot the node count
ax2.bar(years, node_count_sorted, alpha=0.6, color='tab:blue')
ax2.set_ylabel('#Node', color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue', labelsize=18)

# Show every third year for clarity
plt.xticks(years[::3])

# Tight layout to adjust for the second y-axis
fig.tight_layout()

plt.show()
