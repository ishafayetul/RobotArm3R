from assets.CreateTable import CreateTable
from ArmController import ArmController
import open3d as o3d
import json
from CollisionDetection import checkCollision
import copy
class Environment():
    def __init__(self):
        self.vis = o3d.visualization.Visualizer()
        self.vis.create_window()
        self.createScene()

    def addTable(self):
        with open('config/table.json', 'r') as file:
            tableData = json.load(file)
            
        self.table = CreateTable(tableData['height'], tableData['width'], tableData['length'], self.vis)
    
    def addArm(self):
        self.arm = ArmController(self.vis)
        
    def addObject(self):
        self.objectRadius = 1.5
        self.object = o3d.geometry.TriangleMesh.create_sphere(self.objectRadius)
        self.object.paint_uniform_color([1, 0, 0])
        self.object.translate((0, self.objectRadius, 0))
        self.objectCopy = copy.deepcopy(self.object)
        self.objectX = 4.159773052493115
        self.objectY = 0
        self.objectZ = 4.159773052493116
        self.objectCopy.translate((self.objectX, self.objectY, self.objectZ))
        
        self.vis.add_geometry(self.objectCopy)
    
    def addFrame(self):
        self.frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=5, origin=[0, 0, 0])
        self.frame.translate((-self.table.width/2, 2, -self.table.depth/2))
        self.vis.add_geometry(self.frame)
        
    def createScene(self):
        self.addTable()
        self.addArm()
        self.addObject()
        self.addFrame()
        self.setArmJointAngles([0, 45, 45])
        
    def resetScene(self):
        self.vis.clear_geometries()
        self.vis.update_renderer()
        self.createScene()
    
    def setArmJointAngles(self, angles):
        angle1, angle2, angle3 = angles
        self.arm.moveArm(angle1, angle2, angle3)
    
    def getArmJointAngles(self):
        return self.arm.getCurrentJointAngles()
    
    def moveArmToGoal(self, goal):
        x, y, z = goal
        self.arm.moveArmTo(x, y, z)
    
    def pickNplaceObject(self, placeLocation, restLocation):
        # Move arm to the goal position above the object
        goal = self.objectX,self.objectY,self.objectZ
        #goal=(3,3,3)
        self.moveArmToGoal(goal)
        x,y,z=placeLocation
        # Check for collision with the object
        if checkCollision(self.arm.link3, self.objectCopy):
            self.vis.remove_geometry(self.objectCopy)
            
            # Pick up the object by linking it with the end effector
            self.objectCopy,self.objectX,self.objectY,self.objectZ = self.arm.moveArmWithObject(x,y,z, self.object,self.objectCopy)
            self.vis.update_geometry(self.objectCopy)
            
            # After placing, move the arm to the resting position
            self.moveArmToGoal(restLocation)
            
            # Detach the object from the arm once it is placed
            self.arm.hasObject = False
            self.vis.update_geometry(self.objectCopy)

    def run(self):
        self.vis.poll_events()
        self.vis.update_renderer()
        self.vis.run()
