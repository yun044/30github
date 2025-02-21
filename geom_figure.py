import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()


square = plt.Rectangle((8, 1), 2, -2, fill=False, edgecolor='red', linewidth=10)
ax.add_patch(square)


circle = plt.Circle((3, 0), 1, fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(circle)


triangle = plt.Polygon([[5, -1], [6, 1], [7, -1]], fill=True, facecolor='green', edgecolor='green', linewidth=6)
ax.add_patch(triangle)


n_sides = 5
radius = 1
angles = np.linspace(0, 2 * np.pi, n_sides + 1)

x_coords = radius * np.cos(angles)
y_coords = radius * np.sin(angles)

pentagon = plt.Polygon(list(zip(x_coords, y_coords)), fill=True, facecolor='yellow', edgecolor='green', linewidth=6)
ax.add_patch(pentagon)



ax.set_xlim(-2, 14)
ax.set_ylim(-2, 4)
ax.set_aspect('equal')
plt.grid(True)
plt.show()