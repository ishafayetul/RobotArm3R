import sympy as sp
from .Solver3R import Solver3R
def rotationMatrix(theta, axis, link): 
    if axis == "y":
        return sp.Matrix([
            [sp.cos(theta), 0, sp.sin(theta), 0],
            [0, 1, 0, link],
            [-sp.sin(theta), 0, sp.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    elif axis == "x":
        return sp.Matrix([
            [1, 0, 0, 0],
            [0, sp.cos(theta), -sp.sin(theta), link],
            [0, sp.sin(theta), sp.cos(theta), 0],
            [0, 0, 0, 1],
        ])
    return sp.eye(4)

def inverseKinematics(x, y, z, l1, l2, l3):
    # Define the joint variables (a1, a2, a3, a4)
    a1, a2, a3 = sp.symbols('a1 a2 a3')
    
    # Define the rotation matrices for each joint
    h1 = rotationMatrix(a1, axis="y", link=0)
    h2 = rotationMatrix(a2, axis="x", link=l1)
    h3 = rotationMatrix(a3, axis="x", link=l2)
    h4 = rotationMatrix(0, axis="x", link=l3)
    
    # Forward kinematics
    ht = h1 * h2 * h3 * h4

    return Solver3R(x, y, z, l1, l2, l3)

'''
The Actual Homogeneous Transformation matrix is:
[cos(a1)  , sin(a1)*sin(a2)*cos(a3) + sin(a1)*sin(a3)*cos(a2) , -sin(a1)*sin(a2)*sin(a3) + sin(a1)*cos(a2)*cos(a3)  ,  4*sin(a1)*sin(a2)*cos(a3) + 6*sin(a1)*sin(a2) + 4*sin(a1)*sin(a3)*cos(a2)]
[  0      ,       -sin(a2)*sin(a3) + cos(a2)*cos(a3)          ,          -sin(a2)*cos(a3) - sin(a3)*cos(a2)         ,  -4*sin(a2)*sin(a3) + 4*cos(a2)*cos(a3) + 6*cos(a2) + 6                   ]
[-sin(a1) , sin(a2)*cos(a1)*cos(a3) + sin(a3)*cos(a1)*cos(a2) , -sin(a2)*sin(a3)*cos(a1) + cos(a1)*cos(a2)*cos(a3)  ,  4*sin(a2)*cos(a1)*cos(a3) + 6*sin(a2)*cos(a1) + 4*sin(a3)*cos(a1)*cos(a2)]
[  0      ,                          0                        ,                         0                           ,                               1                                           ]

The Symplified homogeneous transformation matrix ht is:
[ cos(a1), sin(a2 + a3)*sin(a1), cos(a2 + a3)*sin(a1), sin(a1)*(l3*sin(a2 + a3) + l2*sin(a2))]
[       0,         cos(a2 + a3),        -sin(a2 + a3),      l1 + l3*cos(a2 + a3) + l2*cos(a2)]
[-sin(a1), sin(a2 + a3)*cos(a1), cos(a2 + a3)*cos(a1), cos(a1)*(l3*sin(a2 + a3) + l2*sin(a2))]
[       0,                    0,                    0,                                      1]
'''