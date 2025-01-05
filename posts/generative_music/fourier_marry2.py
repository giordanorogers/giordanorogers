import numpy as np
import matplotlib.pyplot as plt

# Define the melody as integers
melody = [4, 2, 0, 2, 4, 4, 4, 2, 2, 2, 4, 7, 7, 4, 2, 0, 2, 4, 4, 4, 4, 2, 2, 4, 2, 0]
N = len(melody)  # Number of terms in the melody
x_vals = np.arange(0, N)  # Melody indices

# Extend melody for visualization
repeats = 3
extended_melody = melody * repeats
extended_x_vals = np.arange(0, N * repeats)

# Compute Fourier series approximation
def fourier_series(x, num_terms=10):
    a0 = np.mean(melody)  # Mean value (DC component)
    approx = a0  # Start with the DC component
    for n in range(1, num_terms + 1):
        an = (2 / N) * np.sum(melody * np.cos(2 * np.pi * n * x_vals / N))
        bn = (2 / N) * np.sum(melody * np.sin(2 * np.pi * n * x_vals / N))
        approx += an * np.cos(2 * np.pi * n * x / N) + bn * np.sin(2 * np.pi * n * x / N)
    return approx

# Generate Fourier approximation
x_approx = np.linspace(0, N * repeats, 1000)  # Smooth x values
y_approx = fourier_series(x_approx)

# Limit x-axis range to focus on the first loop
x_zoom = np.linspace(0, N, 1000)  # Smooth x values within the first melody loop
y_zoom = fourier_series(x_zoom)

# Set a dark background style
plt.style.use('dark_background')

# Create the zoomed-in plot
plt.figure(figsize=(10, 6))

# Plot the original melody (first loop only)
plt.scatter(x_vals, melody, color="cyan", label="Original Melody (Discrete)", zorder=3)

# Plot the Fourier approximation (zoomed)
plt.plot(x_zoom, y_zoom, color="white", linewidth=3, label="Fourier Approximation (Zoomed)", zorder=2)

# Adjust axes, labels, and grid
plt.xlabel("$x$", fontsize=14, family="monospace", color="white")
plt.ylabel("$f(x)$", fontsize=14, family="monospace", color="white")
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--', zorder=1)  # Add x-axis
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--', zorder=1)  # Add y-axis
plt.grid(color='gray', alpha=0.3)  # Add grid lines
plt.tick_params(colors='white')  # Change tick colors
plt.legend(fontsize=12, loc="upper right")

# Set x-axis limits to zoom in on the first loop
plt.xlim(0, N)  # Display only the first melody loop
plt.ylim(-1, 8)  # Adjust y-axis limits for better view of pitch range

# Save and show the zoomed-in plot
plt.savefig("fourier_zoomed_graph.svg", format="svg")
plt.show()