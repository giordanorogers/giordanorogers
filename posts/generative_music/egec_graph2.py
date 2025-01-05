import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the function
def f(x):
    return 4 + 3 * np.sin((pi / 2) * x)

# Generate x and y values
x = np.linspace(0, 8, 100)
y = f(x)

# Set a dark background style
plt.style.use('dark_background')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color="white", linewidth=3)
# plt.title("Graph of $f(x)$", fontsize=16, fontweight='bold', family="monospace", color="white")
plt.xlabel("$x$", fontsize=14, family="monospace", color="white")
plt.ylabel("$f(x)$", fontsize=14, family="monospace", color="white")
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')  # Add x-axis
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')  # Add y-axis
plt.grid(color='gray', alpha=0.3)  # Add grid lines
plt.tick_params(colors='white')  # Change tick colors
plt.legend(fontsize=12)

# Save and show the plot
plt.savefig("cool_graph.svg", format="svg")
plt.show()