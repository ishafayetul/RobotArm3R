import open3d as o3d  # Import Open3D for 3D graphics

class CreateTable:
    def __init__(self, height, width, length, vis):
        """
        Set up the table with given dimensions and a visualizer.
        """
        self.vis = vis  # Store the visualizer
        self.width = width  # Table width
        self.height = height  # Table leg height
        self.depth = length  # Table depth
        self.table = self.drawTable()  # Create the table
        self.vis.add_geometry(self.table)  # Add table to the visualizer
        
    def drawTable(self):
        """
        Build the table by making the top and legs.
        """
        # Create the top part of the table
        topSurface = o3d.geometry.TriangleMesh.create_box(self.width, 1, self.depth)
        topSurface.translate((0,0,0),relative=False)  # Position it in space
        
        # Create four table legs
        legs = []
        for i in range(4):
            legs.append(o3d.geometry.TriangleMesh.create_box(1, self.height, 1))  # Legs as boxes
            
        # Position the legs
        legs[0].translate((-self.width/2, -self.height, -self.depth/2))  # Front-left leg
        legs[1].translate((self.width/2 - 1, -self.height, -self.depth/2))  # Front-right leg
        legs[2].translate((-self.width/2, -self.height, self.depth/2 - 1))  # Back-left leg
        legs[3].translate((self.width/2 - 1, -self.height, self.depth/2 - 1))  # Back-right leg
        
        # Put everything together
        table = topSurface + legs[0] + legs[1] + legs[2] + legs[3]
        table.paint_uniform_color([0.133, 0.529, 0.502])  # Color it teal
        
        return table
    
    def viewTable(self, vis):
        """
        Show the table in the visualizer.
        """
        vis.add_geometry(self.table)  # Add table to the viewer
        return vis
