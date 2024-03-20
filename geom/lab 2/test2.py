import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

# Определение вершин и граней октаэдра
vertices = np.array([
    [-3, 0, 0],
    [3, 0, 0],
    [0, -3, 0],
    [0, 3, 0],
    [0, 0, -3],
    [0, 0, 3]
])

faces = [[vertices[i] for i in face] for face in [
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 4],
    [1, 3, 4],
    [0, 2, 5],
    [0, 3, 5],
    [1, 2, 5],
    [1, 3, 5]
]]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Функция для вращения октаэдра
def rotate_3d(vertices, angle):
    theta = np.deg2rad(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

def rotate(vertices, axis, angle):
    """
    Rotate a set of 3D points around a given axis by a given angle.

    Args:
    - vertices: The points to rotate (list of lists of 3 floats).
    - axis: The rotation axis (list of 3 floats with length 1).
    - angle: The rotation angle in radians (float).

    Returns:
    - The rotated points (list of lists of 3 floats).
    """
    # Create a rotation matrix from the axis and angle
    a, b, c = axis
    ca = np.cos(angle)
    sa = np.sin(angle)
    cpa = 1 - ca
    xx = a * a * cpa
    yy = b * b * cpa
    zz = c * c * cpa
    xy = a * b * cpa
    xz = a * c * cpa
    yz = b * c * cpa

    # Apply the rotation matrix to each point
    rotated_vertices = []
    for point in vertices:
        rotated_point = [
            xx * point[0] + xy * point[1] + xz * point[2],
            xy * point[0] + yy * point[1] + yz * point[2],
            xz * point[0] + yz * point[1] + zz * point[2]
        ]
        rotated_vertices.append(rotated_point)

    return rotated_vertices

def scale(vertices, scale_factor):
    """
    Scale a set of 3D points by a given scale factor.

    Args:
    - vertices: The points to scale (list of lists of 3 floats).
    - scale_factor: The scale factor (float).

    Returns:
    - The scaled points (list of lists of 3 floats).
    """
    # Apply the scale factor to eachpoint
    scaled_vertices = []
    for point in vertices:
        scaled_point = [scale_factor * x for x in point]
        scaled_vertices.append(scaled_point)

    return scaled_vertices

def move(vertices, movement):
    """
    Move a set of 3D points by a given movement vector.

    Args:
    - vertices: The points to move (list of lists of 3 floats).
    - movement: The movement vector (list of 3 floats).

    Returns:
    - The moved points (list of lists of 3 floats).
    """
    # Add the movement vector to each point
    moved_vertices = []
    for point in vertices:
        moved_point = [x + y for x, y in zip(point, movement)]
        moved_vertices.append(moved_point)

    return moved_vertices

'''
# example of rotation
rotation_axis = [1, 1, 1]
rotation_angle = np.pi / 4
rotated_vertices = rotate(vertices, rotation_axis, rotation_angle)

# example of scaling
scale_factor = 2
scaled_vertices = scale(vertices, scale_factor)

# example of movement
movement = [1, 1, 1]
moved_vertices = move(vertices, movement)
'''

"""
# example of rotation
rotation_axis = [1, 1, 1]
rotation_angle = np.pi / 4
rotated_vertices = rotate(vertices, rotation_axis, rotation_angle)

# update faces to reflect the new vertex positions
rotated_faces = [[rotated_vertices[i] for i in face] for face in [
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 4],
    [1, 3, 4],
    [0, 2, 5],
    [0, 3, 5],
    [1, 2, 5],
    [1, 3, 5]
]]

# example of scaling
scale_factor = 2
scaled_vertices = scale(vertices, scale_factor)

# update faces to reflect the new vertex positions
scaled_faces = [[scaled_vertices[i] for i in face] for face in [
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 4],
    [1, 3, 4],
    [0, 2, 5],
    [0, 3, 5],
    [1, 2, 5],
    [1, 3, 5]
]]

# example of movement
movement = [1, 1, 1]
moved_vertices = move(vertices, movement)

# update faces to reflect the new vertex positions
moved_faces = [[moved_vertices[i] for i in face] for face in [
    [0, 2, 4],
    [0, 3, 4],
    [1, 2, 4],
    [1, 3, 4],
    [0, 2, 5],
    [0,3, 5],
    [1, 2, 5],
    [1, 3, 5]
]]
"""

# Рисуем и вращаем октаэдр
def draw_and_rotate_3d(vertices, faces, angle):
    rotated_vertices = rotate_3d(vertices, angle)
    ax.clear()
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Rotation of Octahedron')
    return rotated_vertices

angle = 130
rotated_vertices = draw_and_rotate_3d(vertices, faces, angle)
plt.show()
