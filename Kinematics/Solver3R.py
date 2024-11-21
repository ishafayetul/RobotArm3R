import numpy as np

# Function to solve for joint angles of a 3R robotic arm
def Solver3R(x, y, z, l1, l2, l3):
    # Calculate the first joint angle (a1) 
    a1 = np.arctan2(x, z)  # This gives the angle for rotation around the base (first joint)
    
    # Calculate the second joint angle (a2) 
    a2 = np.arccos((y - l1 + l3) / l2)  # This gives the angle for the first arm segment
    
    # Convert a1 and a2 from radians to degrees
    a1_deg = np.degrees(a1)
    a2_deg = np.degrees(a2)
    
    # To Pick an object, end effector must be rotated at 180 degrees, this rotation can be achieved if a2+a3 = 180
    a3_deg = 180 - a2_deg  # Angle for the third segment (typically complementary to a2)
    
    # Return all joint angles in degrees
    return a1_deg, a2_deg, a3_deg
