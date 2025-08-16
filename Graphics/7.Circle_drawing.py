import matplotlib.pyplot as plt

def bresenham_circle(x_center, y_center, radius):
    points = []
    x = 0
    y = radius
    d = 3 - 2 * radius

    while y >= x:
        # Each iteration plots eight symmetric points
        points.extend([
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x),
        ])

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Parameters
x_center, y_center = 50, 50
radius = 30

# Get points for the circle
circle_points = bresenham_circle(x_center, y_center, radius)

# Plot
plt.figure(figsize=(6, 6))
for point in circle_points:
    plt.plot(point[0], point[1], 'ro')  # red pixel
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Bresenham Circle Drawing Algorithm")
plt.grid(True)
plt.show()
