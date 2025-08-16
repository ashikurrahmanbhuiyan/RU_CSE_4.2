import turtle

def draw_koch_curve(t, order, size):
    """
    Recursively draws a Koch curve.
    
    :param t: Turtle object
    :param order: The order (depth) of the fractal
    :param size: The length of the side
    """
    if order == 0:
        t.forward(size)
    else:
        draw_koch_curve(t, order - 1, size / 3)
        t.left(60)
        draw_koch_curve(t, order - 1, size / 3)
        t.right(120)
        draw_koch_curve(t, order - 1, size / 3)
        t.left(60)
        draw_koch_curve(t, order - 1, size / 3)

def draw_koch_snowflake(order=4, size=300):
    """
    Draws the Koch Snowflake using turtle graphics.
    
    :param order: The order (depth) of the fractal (default: 4)
    :param size: The initial side length (default: 300)
    """
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(-size / 2, size / 3)  # Starting position for centering
    t.pendown()
    t.color("blue")

    for _ in range(3):
        draw_koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Call the function to draw the snowflake
# You can adjust the order and size as needed (higher order = more detail, but slower)
draw_koch_snowflake(order=4, size=400)












#code2


# draw the snowflake with matplotlib keep it to understand better later 

# import matplotlib.pyplot as plt
# import numpy as np

# def koch_curve(start, end, order):
#     """
#     Generate points for a Koch curve segment.
    
#     :param start: Starting point as numpy array [x, y]
#     :param end: Ending point as numpy array [x, y]
#     :param order: Recursion depth
#     :return: Numpy array of points along the curve
#     """
#     if order == 0:
#         return np.array([start, end])
#     else:
#         vec = end - start
#         length = np.linalg.norm(vec)
#         unit_vec = vec / length
#         perp_vec = np.array([-unit_vec[1], unit_vec[0]])  # Left perpendicular
        
#         # Points dividing the segment
#         p1 = start
#         p2 = start + (1/3) * vec
#         p4 = start + (2/3) * vec
#         p5 = end
        
#         # Peak point p3
#         rotate_60 = np.cos(np.pi/3) * unit_vec + np.sin(np.pi/3) * perp_vec
#         p3 = p2 + (length / 3) * rotate_60
        
#         # Recurse on each sub-segment
#         return np.vstack([
#             koch_curve(p1, p2, order-1),
#             koch_curve(p2, p3, order-1)[1:],
#             koch_curve(p3, p4, order-1)[1:],
#             koch_curve(p4, p5, order-1)[1:]
#         ])

# def draw_koch_snowflake(order=4, scale=400):
#     """
#     Generate and plot the Koch Snowflake using Matplotlib.
    
#     :param order: The order (depth) of the fractal (default: 4)
#     :param scale: The scale factor for the size (default: 400)
#     """
#     # Initial equilateral triangle vertices
#     height = scale * np.sqrt(3) / 2
#     p1 = np.array([-scale / 2, -height / 3])  # Bottom left
#     p2 = np.array([scale / 2, -height / 3])   # Bottom right
#     p3 = np.array([0, 2 * height / 3])       # Top
    
#     # Generate curves for each side
#     curve1 = koch_curve(p1, p2, order)
#     curve2 = koch_curve(p2, p3, order)
#     curve3 = koch_curve(p3, p1, order)
    
#     # Combine all points (close the shape by including the first point at the end if needed)
#     points = np.vstack([curve1, curve2[1:], curve3[1:], curve1[0:1]])  # Close the loop
    
#     # Plot
#     plt.figure(figsize=(8, 8))
#     plt.plot(points[:, 0], points[:, 1], 'b-', linewidth=1)
#     plt.title(f'Koch Snowflake (Order {order})')
#     plt.axis('equal')
#     plt.axis('off')  # Hide axes for cleaner look
#     plt.show()

# # Call the function to draw the snowflake
# # Adjust order and scale as needed (higher order = more detail)
# draw_koch_snowflake(order=5, scale=400)








#code3

# may be the correct code for mathplotlib, here for review later 

# """
# circle_koch_snowflake.py

# Draw a circular Koch Snowflake (fractal snowflake on a circle) using the Koch curve algorithm
# and display it with matplotlib.
# """

# import argparse
# import math
# from typing import List, Tuple
# import matplotlib.pyplot as plt

# Point = Tuple[float, float]


# def koch_curve(p1: Point, p2: Point, iterations: int) -> List[Point]:
#     if iterations == 0:
#         return [p1, p2]

#     (x1, y1), (x5, y5) = p1, p2
#     dx = (x5 - x1) / 3.0
#     dy = (y5 - y1) / 3.0

#     p2a = (x1 + dx, y1 + dy)
#     p4a = (x1 + 2 * dx, y1 + 2 * dy)

#     angle = math.radians(60)
#     vx = p4a[0] - p2a[0]
#     vy = p4a[1] - p2a[1]
#     px = p2a[0] + (vx * math.cos(angle) - vy * math.sin(angle))
#     py = p2a[1] + (vx * math.sin(angle) + vy * math.cos(angle))
#     p3 = (px, py)

#     seg1 = koch_curve(p1, p2a, iterations - 1)[:-1]
#     seg2 = koch_curve(p2a, p3, iterations - 1)[:-1]
#     seg3 = koch_curve(p3, p4a, iterations - 1)[:-1]
#     seg4 = koch_curve(p4a, p2, iterations - 1)

#     return seg1 + seg2 + seg3 + seg4


# def circular_koch_snowflake(iterations: int, radius: float, sides: int = 6) -> List[Point]:
#     points = []
#     angle_step = 2 * math.pi / sides

#     # compute vertices on the circle
#     circle_points = [(radius * math.cos(i * angle_step), radius * math.sin(i * angle_step)) for i in range(sides)]

#     # connect vertices with Koch curves
#     for i in range(sides):
#         p1 = circle_points[i]
#         p2 = circle_points[(i + 1) % sides]
#         seg = koch_curve(p1, p2, iterations)[:-1]
#         points.extend(seg)

#     points.append(points[0])
#     return points


# def plot_snowflake(points: List[Point], figsize=(8, 8), linewidth: float = 1.0, save_path: str = None):
#     xs = [p[0] for p in points]
#     ys = [p[1] for p in points]

#     plt.figure(figsize=figsize)
#     plt.plot(xs, ys, linewidth=linewidth)
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.axis('off')

#     if save_path:
#         plt.savefig(save_path, bbox_inches='tight', dpi=300)
#         print(f"Saved circular snowflake to {save_path}")
#     else:
#         plt.show()


# def main():
#     parser = argparse.ArgumentParser(description='Draw a circular Koch snowflake fractal')
#     parser.add_argument('--iterations', type=int, default=3, help='recursion depth (default: 3)')
#     parser.add_argument('--radius', type=float, default=200.0, help='radius of the circular layout (default: 200)')
#     parser.add_argument('--sides', type=int, default=6, help='number of sides forming the base polygon (default: 6)')
#     parser.add_argument('--linewidth', type=float, default=1.0, help='line width for plotting (default: 1.0)')
#     parser.add_argument('--save', type=str, default=None, help='optional path to save the image (PNG)')
#     args = parser.parse_args()

#     pts = circular_koch_snowflake(args.iterations, args.radius, args.sides)
#     plot_snowflake(pts, linewidth=args.linewidth, save_path=args.save)


# if __name__ == '__main__':
#     main()
