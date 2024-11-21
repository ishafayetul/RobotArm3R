
# User Guide for Robot Arm Control System

## System Requirements

- Python 3.x
- The following Python libraries:
  - `tkinter` (for GUI)
  - `open3d` (for 3D visualization)
  - `json` (for reading/writing JSON configuration files)
  - `threading` (for parallel processing)
  - `time` (for delays between actions)
  - `filelock` (for safe file access in multi-threaded environments)

## Steps to Run the Code

### 1. Install Dependencies

Ensure the required libraries are installed in your Python environment. You can install the necessary libraries using pip:

```bash
pip install open3d filelock
```

### 2. Prepare Configuration Files

The system uses JSON configuration files that store settings for the robot's arm, table, and commands. These files should be in the `config/` directory. Ensure the following files exist and are correctly formatted:

- `config/Command.json`: Stores the control commands such as play and reset status.
- `config/ArmPose.json`: Stores the current joint angles of the robot arm.
- `config/table.json`: Stores the dimensions of the table to be added to the scene.

### 3. Running the Code

The program consists of three main modules:

- **ControlPanel**: Handles the GUI for controlling the robot.
- **Environment**: Sets up the 3D environment and controls the robot's movements.
- **Main Application**: Starts the robot control in a separate thread and runs the GUI.

To run the program, simply execute the main Python file. Open a terminal and run:

```bash
python main.py
```

### 4. Understanding the GUI

When you run the program, a GUI window will appear with buttons to control the robot arm:

- **Play**: Start or pause the robot's movements.
- **Reset**: Reset the scene (clear all objects and restart the setup).

The GUI will display:

- **Roll, Pitch, Yaw**: The current orientation of the robot arm.
- **Angle1, Angle2, Angle3**: The current joint angles of the robot arm.

The GUI allows you to control the robot via the Play and Reset buttons.

### 5. How It Works

- **Robot Movement**: The robot moves based on commands from the control panel. When you press the Play button, the robot will start performing pick-and-place tasks in the 3D environment.
- **Object Pick-and-Place**: The robot picks up and places objects at different positions in the 3D space. The pick-and-place operation checks for collisions before picking up an object to avoid errors.
- **Scene Reset**: Pressing the Reset button clears the 3D scene and resets the robot's arm.

### 6. Background Process

The code runs the robot in a background thread to handle pick-and-place actions. The robot continuously checks for command changes (`Play` or `Reset`) from the `Command.json` file. When the Play command is set to `-1`, the robot picks and places objects at predefined positions. When the Reset command is set to `-1`, the environment is cleared and reset.

### 7. Stopping the Program

To stop the program, simply close the GUI window or terminate the script in the terminal using `Ctrl+C`.

## Example Workflow

1. **Launch the Program**:
   - Execute `python main.py` to start the program.
   
2. **Control the Robot**:
   - Press **Play** to start the robot's pick-and-place operations. The robot will move objects at predefined positions.
   - Press **Reset** to clear and reset the scene.

3. **Monitor the Arm's Status**:
   - The GUI will show real-time updates for the arm's joint angles and orientation (Roll, Pitch, Yaw).
   
## File Structure
project_root/
│
├── config/
│   ├── Table.json 
│   ├── Command.json
│   ├── ArmPose.json
│  
├── assets/
│   └── CreateTable.py
|   |__ ArmModel.py
|
|───|Kinematics/
|   |___FK.py
|   |___IK.py
|   |___Solver3R.py
│
├── ControlPanel.py
├── Environment.py
├── ArmController.py
├── CollisionDetection.py
└── main.py


