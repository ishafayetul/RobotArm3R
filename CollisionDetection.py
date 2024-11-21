import numpy as np
import open3d as o3d

# Function to compute the 8 vertices of an oriented bounding box (OBB)
def computeOBBVertices(cube):
    # Get the oriented bounding box (OBB) of the cube
    obb = cube.get_oriented_bounding_box()
    center = obb.center  # Center of the OBB
    rotation = obb.R  # Rotation matrix of the OBB
    extent = obb.extent  # Extents (half-dimensions) of the OBB along each axis

    # Compute the 8 vertices of the OBB by adding/subtracting the extent in each direction
    vertices = []
    for sign in np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                          [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]):
        vertex = center + np.dot(rotation, sign * extent)  # Rotate and translate the vertex
        vertices.append(vertex)  # Add the vertex to the list
    return np.array(vertices)  # Return the list of vertices as a NumPy array

# Function to check if two cubes (OBBs) are colliding
def checkCollision(cube1, cube2):
    # Get the vertices of both cubes
    vertices1 = computeOBBVertices(cube1)
    vertices2 = computeOBBVertices(cube2)

    # Get the rotation matrices of both cubes
    obb1 = cube1.get_oriented_bounding_box()
    obb2 = cube2.get_oriented_bounding_box()
    rotation1 = obb1.R
    rotation2 = obb2.R

    # Get the axes of the OBBs (each OBB has its own coordinate system)
    axes1 = [rotation1[:, i] for i in range(3)]  # Axes of cube1
    axes2 = [rotation2[:, i] for i in range(3)]  # Axes of cube2
    
    # Combine axes from both cubes to check for collisions along each axis
    axes = axes1 + axes2

    # Check if there’s any separation between the cubes along each axis
    for axis in axes:
        # Project both cubes onto this axis
        projection1 = np.dot(vertices1, axis)
        projection2 = np.dot(vertices2, axis)

        # Get the min and max projection values for both cubes
        min_proj1, max_proj1 = np.min(projection1), np.max(projection1)
        min_proj2, max_proj2 = np.min(projection2), np.max(projection2)

        # If there’s no overlap along this axis, there’s no collision
        if max_proj1 < min_proj2 or max_proj2 < min_proj1:
            return False  # No overlap, so no collision

    return True  # There’s overlap along all axes, so a collision occurs
