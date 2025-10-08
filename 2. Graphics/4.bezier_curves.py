import numpy as np
import matplotlib.pyplot as plt

# Function to compute a point on a Bezier curve using de Casteljau's algorithm
def de_casteljau(control_points, t):
    points = np.array(control_points, dtype=float)
    n = len(points)
    for r in range(1, n):
        points[:n-r] = (1 - t) * points[:n-r] + t * points[1:n-r+1]
    return points[0]

# Function to generate the full Bezier curve
def bezier_curve(control_points, num_samples=100):
    return np.array([de_casteljau(control_points, t) for t in np.linspace(0, 1, num_samples)])

# Example: Cubic Bezier curve (4 control points)
control_points = [(1, 1), (2, 3), (4, 3), (5, 1)]
curve = bezier_curve(control_points, num_samples=200)

# Plot
plt.figure(figsize=(6, 6))
control_points_np = np.array(control_points)

# Draw control polygon
plt.plot(control_points_np[:, 0], control_points_np[:, 1], 'ro--', label='Control Polygon')

# Draw Bezier curve
plt.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2, label='Bezier Curve')

plt.title("Bezier Curve (Cubic)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
