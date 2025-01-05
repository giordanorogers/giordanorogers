import plotly.graph_objects as go
import numpy as np
from math import pi

# Define the function
def f(x):
    return 4 + 3 * np.sin((pi / 2) * x)

# Generate x and y values
x = np.linspace(0, 8, 100)
y = f(x)

# Create the plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='lines',
    line=dict(color='white', width=4),  # Thicker white line
    name=r"$f(x) = 4 + 3\sin\left(\frac{\pi}{2}x\right)$"
))

# Update layout for a black background and aesthetic fonts
fig.update_layout(
    title="Graph of $f(x)$",
    xaxis_title="$x$",
    yaxis_title="$f(x)$",
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(color="white", family="Courier New, monospace"),
    xaxis=dict(color="white"),
    yaxis=dict(color="white"),
    showlegend=True
)

# Save the plot as an HTML file
fig.write_html("interactive_graph.html")

print("Interactive plot saved as interactive_graph.html!")