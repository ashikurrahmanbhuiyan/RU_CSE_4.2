import matplotlib.pyplot as plt

# Check if point is inside a clipping edge
def inside(p, edge_start, edge_end):
    # Using cross product to check if point is inside (assuming clockwise clip polygon)
    return (edge_end[0] - edge_start[0]) * (p[1] - edge_start[1]) - \
           (edge_end[1] - edge_start[1]) * (p[0] - edge_start[0]) >= 0

# Find intersection of subject polygon edge with clip edge
def compute_intersection(p1, p2, cp1, cp2):
    dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
    dp = [p1[0] - p2[0], p1[1] - p2[1]]
    n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
    n2 = p1[0] * p2[1] - p1[1] * p2[0]
    n3 = dc[0] * dp[1] - dc[1] * dp[0]
    if n3 == 0:
        return None  # parallel lines
    x = (n1 * dp[0] - n2 * dc[0]) / n3
    y = (n1 * dp[1] - n2 * dc[1]) / n3
    return (x, y)

# Main Sutherland–Hodgman polygon clipping
def sutherland_hodgman(subject_polygon, clip_polygon):
    output_list = subject_polygon
    cp1 = clip_polygon[-1]

    for cp2 in clip_polygon:
        input_list = output_list
        output_list = []
        if not input_list:
            break
        s = input_list[-1]

        for e in input_list:
            if inside(e, cp1, cp2):
                if not inside(s, cp1, cp2):
                    output_list.append(compute_intersection(s, e, cp1, cp2))
                output_list.append(e)
            elif inside(s, cp1, cp2):
                output_list.append(compute_intersection(s, e, cp1, cp2))
            s = e
        cp1 = cp2

    return output_list

# Example subject polygon and clipping window
subject_polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300), (200, 250), (150, 350), (100, 250), (100, 200)]
clip_polygon = [(100, 100), (300, 100), (300, 300), (100, 300)]

# Perform clipping
clipped_polygon = sutherland_hodgman(subject_polygon, clip_polygon)

# Plot original polygon
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.fill(*zip(*subject_polygon), fill=False, edgecolor='blue', linewidth=1.5)
plt.plot(*zip(*(clip_polygon + [clip_polygon[0]])), 'r-', linewidth=1.5)
plt.title('Original Polygon & Clipping Window')
plt.gca().set_aspect('equal')

# Plot clipped polygon
plt.subplot(1, 2, 2)
if clipped_polygon:
    plt.fill(*zip(*clipped_polygon), fill=False, edgecolor='green', linewidth=1.5)
plt.plot(*zip(*(clip_polygon + [clip_polygon[0]])), 'r-', linewidth=1.5)
plt.title('Clipped Polygon')
plt.gca().set_aspect('equal')

plt.show()
