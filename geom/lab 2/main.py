import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the 3D polygon vertices
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# Define the 3D polygon faces
faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
         [vertices[4], vertices[5], vertices[6], vertices[7]],
         [vertices[0], vertices[1], vertices[5], vertices[4]],
         [vertices[2], vertices[3], vertices[7], vertices[6]],
         [vertices[1], vertices[2], vertices[6], vertices[5]],
         [vertices[0], vertices[3], vertices[7], vertices[4]]]

# Plot the original 3D polygon
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the polygon
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

# Perform affine transformations (rotation, scaling, translation)
# For example, rotate the polygon around the z-axis
theta = np.pi / 4  # Rotation angle in radians
c, s = np.cos(theta), np.sin(theta)
rotation_matrix = np.array(((c, -s, 0),
                            (s, c, 0),
                            (0, 0, 1)))

# Apply rotation transformation
rotated_vertices = np.dot(vertices, rotation_matrix)

# Plot the transformed 3D polygon
ax.add_collection3d(Poly3DCollection(faces, facecolors='yellow', linewidths=1, edgecolors='b', alpha=0.5))

# Set plot limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

plt.show()
