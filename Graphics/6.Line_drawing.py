import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

# Example usage
x_start, y_start = 10, 10
x_end, y_end = 70, 40

line_points = bresenham_line(x_start, y_start, x_end, y_end)

# Plotting
plt.figure(figsize=(6, 6))
for point in line_points:
    plt.plot(point[0], point[1], 'bo')  # blue pixel
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.show()











# this code may not incorrect so it will still stay for further study, once i understnad the theory fully then we will decide

# import matplotlib.pyplot as plt

# def bresenham_line(x1, y1, x2, y2):
#     """Generate points for a line using Bresenham's algorithm."""
#     points = []

#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     sx = 1 if x1 < x2 else -1
#     sy = 1 if y1 < y2 else -1

#     err = dx - dy

#     while True:
#         points.append((x1, y1))
#         if x1 == x2 and y1 == y2:
#             break
#         e2 = 2 * err
#         if e2 > -dy:
#             err -= dy
#             x1 += sx
#         if e2 < dx:
#             err += dx
#             y1 += sy

#     return points

# # Example usage
# x1, y1 = 2, 3
# x2, y2 = 15, 8
# line_points = bresenham_line(x1, y1, x2, y2)

# # Plotting
# x_coords, y_coords = zip(*line_points)
# plt.figure(figsize=(6, 6))
# plt.plot(x_coords, y_coords, marker='o', color='green')
# plt.title(f"Bresenham Line from ({x1},{y1}) to ({x2},{y2})")
# plt.grid(True)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()
