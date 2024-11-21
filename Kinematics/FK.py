import numpy as np  
# Function to create a rotation matrix based on an axis and angle
def rotationMatrix(theta, axis, link): 
    theta = np.radians(theta)  # Convert angle to radians
    if axis == "y":  # Rotation around the Y-axis
        return np.array([
            [np.cos(theta), 0, np.sin(theta), 0],
            [0, 1, 0, link],
            [-np.sin(theta), 0, np.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    elif axis == "x":  # Rotation around the X-axis
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(theta), -np.sin(theta), link],
            [0, np.sin(theta), np.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    return np.eye(4)  # Return identity matrix if no valid axis

# Function to compute a series of transformations
def homogeneousTransformationMatrix(a1, l1, a2, l2, a3, l3):
    ht1 = rotationMatrix(a1, axis="y", link=0)  # First transformation
    ht2 = ht1 @ rotationMatrix(a2, axis="x", link=l1)  # second transformation
    ht3 = ht2 @ rotationMatrix(a3, axis="x", link=l2)  # third transformation
    ht4 = ht3 @ rotationMatrix(0, axis="x", link=l3)  # fourth transformation (no rotation)
    return ht1, ht2, ht3, ht4  # intermediate transformation matrices
