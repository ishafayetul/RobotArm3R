import numpy as np

def Solver3R(x,y,z,l1,l2,l3):
    # Compute the angles
    a1 = np.arctan2(x,z)  # cotinv(z/x) is equivalent to arctan(z/x)
    a2 = np.arccos((y - l1 + l3) / l2)

    # Convert to degrees
    a1_deg = np.degrees(a1)
    a2_deg = np.degrees(a2)

    # Compute a3
    a3_deg = 180 - a2_deg

    return a1_deg, a2_deg, a3_deg