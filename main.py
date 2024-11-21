from ControlPanel import ControlPanel
from Environment import Environment
import threading
import time
import json
from filelock import FileLock

def runRobot():
    # Initializes the environment and continuously performs pick and place actions based on command status
    env = Environment()
    
    # Loop to continually check the play and reset commands
    while(True):
        time.sleep(1)  # Delay to reduce CPU usage

        # Load the latest command from the JSON file with file locking to ensure safe reading
        with FileLock('config/Command.json.lock'):
            with open('config/Command.json', 'r') as file:
                cmd = json.load(file)
        
        # If 'play' command is set (play = 1), execute pick and place operations
        if(cmd['play'] * -1 == 1):
            # Perform a sequence of pick-and-place operations with different locations
            env.pickNplaceObject((-4.7289, 3, -3.49922), (3.6742, 5, 3.6742))
            time.sleep(2)  # Pause for 2 seconds between actions
            env.pickNplaceObject((6, 3, 4.5), (3.6742, 5, 3.6742))
            time.sleep(2)
            env.pickNplaceObject((-6, 3, -4.5), (3.6742, 5, 3.6742))
            time.sleep(2)
            env.pickNplaceObject((4.7289, 3, -3.49922), (3.6742, 5, 3.6742))
            time.sleep(2)
        
        # If 'reset' command is set (reset = 1), reset the scene
        if (cmd['reset'] * -1 == 1):
            env.resetScene()

    # Run the environment's visualization loop
    env.run()

if __name__ == "__main__":
    # Initialize the control panel and start the GUI in a separate thread
    panel = ControlPanel()
    
    # Start the robot's task execution in a new thread to run concurrently with the GUI
    robot_thread = threading.Thread(target=runRobot, daemon=True)
    robot_thread.start()
    
    # Start the Tkinter event loop for the control panel
    panel.run()
