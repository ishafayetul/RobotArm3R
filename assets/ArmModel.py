import open3d as o3d  # Open3D for 3D graphics

class ArmModel:
    def __init__(self):
        # Define link lengths
        self.link1Length = 6
        self.link2Length = 6
        self.link3Length = 4

        # Create base plate and color it green
        self.basePlate = o3d.geometry.TriangleMesh.create_box(5, 0.5, 5)
        self.basePlate.translate((-2.5, 0, -2.5))
        self.basePlate.paint_uniform_color([0.522, 1, 0])
        
        # Create link1 and color it yellow
        self.link1 = o3d.geometry.TriangleMesh.create_box(1, self.link1Length, 1)
        self.link1.translate((-0.5, 0, -0.5))
        self.link1.paint_uniform_color([1, 0.984, 0])
    
        # Create link2 and color it brown
        self.link2 = o3d.geometry.TriangleMesh.create_box(1, self.link2Length, 1)
        self.link2.translate((-0.5, 0, -0.5))
        self.link2.paint_uniform_color([0.549, 0.541, 0])
        
        # Create link3, end effector, and fingers, then position them
        link3 = o3d.geometry.TriangleMesh.create_box(1, self.link3Length, 1)
        endef = o3d.geometry.TriangleMesh.create_box(3, 0.1, 1)
        rFinger = o3d.geometry.TriangleMesh.create_box(0.1, 1.5, 1)
        lFinger = o3d.geometry.TriangleMesh.create_box(0.1, 1.5, 1)
        endef.translate((-1, self.link3Length, 0))
        rFinger.translate((-1, self.link3Length, 0))
        lFinger.translate((2, self.link3Length, 0))
        
        # Combine link3 parts and color them orange
        self.link3 = link3 + endef + rFinger + lFinger
        self.link3.translate((-0.5, 0, -0.5))
        self.link3.paint_uniform_color([0.812, 0.369, 0])
        
        # Compute normals for lighting/shading
        self.link1.compute_vertex_normals()
        self.link2.compute_vertex_normals()
        self.link3.compute_vertex_normals()
