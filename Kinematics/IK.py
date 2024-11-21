import sympy as sp  # Import SymPy for symbolic mathematics
from .Solver3R import Solver3R  # Main Inverse Kinematics solver

# Function to create Symbolic rotation matrix for given axis (X or Y)
def rotationMatrix(theta, axis, link): 
    if axis == "y":  # Rotation around Y-axis
        return sp.Matrix([
            [sp.cos(theta), 0, sp.sin(theta), 0],
            [0, 1, 0, link],
            [-sp.sin(theta), 0, sp.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    elif axis == "x":  # Rotation around X-axis
        return sp.Matrix([
            [1, 0, 0, 0],
            [0, sp.cos(theta), -sp.sin(theta), link],
            [0, sp.sin(theta), sp.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    return sp.eye(4)  # Identity matrix if axis is not X or Y

# Function to calculate inverse kinematics (position to joint angles)
def inverseKinematics(x, y, z, l1, l2, l3):
    # Define the joint angles as symbolic variables
    a1, a2, a3 = sp.symbols('a1 a2 a3')
    
    # Get the transformation matrices for each joint
    h1 = rotationMatrix(a1, axis="y", link=0)  # Base rotation
    h2 = rotationMatrix(a2, axis="x", link=l1)  # First link rotation
    h3 = rotationMatrix(a3, axis="x", link=l2)  # Second link rotation
    h4 = rotationMatrix(0, axis="x", link=l3)  # End effector rotation
    
    # Perform forward kinematics (multiply transformations)
    ht = h1 * h2 * h3 * h4

    # Call the Solver3R class to solve for joint angles based on end effector position
    return Solver3R(x, y, z, l1, l2, l3)

'''
The Actual Homogeneous Transformation matrix is:
[cos(a1)  , sin(a1)*sin(a2)*cos(a3) + sin(a1)*sin(a3)*cos(a2) , -sin(a1)*sin(a2)*sin(a3) + sin(a1)*cos(a2)*cos(a3)  ,  4*sin(a1)*sin(a2)*cos(a3) + 6*sin(a1)*sin(a2) + 4*sin(a1)*sin(a3)*cos(a2)]
[  0      ,       -sin(a2)*sin(a3) + cos(a2)*cos(a3)          ,          -sin(a2)*cos(a3) - sin(a3)*cos(a2)         ,  -4*sin(a2)*sin(a3) + 4*cos(a2)*cos(a3) + 6*cos(a2) + 6                   ]
[-sin(a1) , sin(a2)*cos(a1)*cos(a3) + sin(a3)*cos(a1)*cos(a2) , -sin(a2)*sin(a3)*cos(a1) + cos(a1)*cos(a2)*cos(a3)  ,  4*sin(a2)*cos(a1)*cos(a3) + 6*sin(a2)*cos(a1) + 4*sin(a3)*cos(a1)*cos(a2)]
[  0      ,                          0                        ,                         0                           ,                               1                                           ]

The Simplified homogeneous transformation matrix ht is:
[ cos(a1), sin(a2 + a3)*sin(a1), cos(a2 + a3)*sin(a1), sin(a1)*(l3*sin(a2 + a3) + l2*sin(a2))]
[       0,         cos(a2 + a3),        -sin(a2 + a3),      l1 + l3*cos(a2 + a3) + l2*cos(a2)]
[-sin(a1), sin(a2 + a3)*cos(a1), cos(a2 + a3)*cos(a1), cos(a1)*(l3*sin(a2 + a3) + l2*sin(a2))]
[       0,                    0,                    0,                                      1]
'''

