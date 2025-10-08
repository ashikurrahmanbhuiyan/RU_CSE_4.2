import numpy as np
import matplotlib.pyplot as plt

# --- Transformation Functions ---

def translate(points, tx, ty):
    """Translate points by tx, ty."""
    translation_matrix = np.array([[1, 0, tx],
                                    [0, 1, ty],
                                    [0, 0, 1]])
    return apply_transform(points, translation_matrix)

def rotate(points, angle_deg):
    """Rotate points around the origin by angle in degrees."""
    angle_rad = np.radians(angle_deg)
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                 [np.sin(angle_rad),  np.cos(angle_rad), 0],
                                 [0,                 0,                 1]])
    return apply_transform(points, rotation_matrix)

def scale(points, sx, sy):
    """Scale points by sx, sy."""
    scaling_matrix = np.array([[sx, 0,  0],
                                [0, sy,  0],
                                [0,  0,  1]])
    return apply_transform(points, scaling_matrix)

def apply_transform(points, matrix):
    """Apply a transformation matrix to a set of points."""
    homogeneous_points = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed_points = homogeneous_points @ matrix.T
    return transformed_points[:, :2]

# --- Original Shape (Triangle Example) ---
shape = np.array([[0, 0], [2, 0], [1, 2], [0, 0]])  # Closed triangle

# Apply transformations
translated_shape = translate(shape, 3, 2)
rotated_shape = rotate(shape, 45)
scaled_shape = scale(shape, 2, 0.5)

# --- Plot ---
plt.figure(figsize=(8, 8))

plt.plot(shape[:, 0], shape[:, 1], 'b-', label="Original Shape")
plt.plot(translated_shape[:, 0], translated_shape[:, 1], 'r-', label="Translated")
plt.plot(rotated_shape[:, 0], rotated_shape[:, 1], 'g-', label="Rotated")
plt.plot(scaled_shape[:, 0], scaled_shape[:, 1], 'm-', label="Scaled")

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.title("2D Geometric Transformations: Translation, Rotation, Scaling")
plt.show()
