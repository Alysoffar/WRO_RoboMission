🚀 SPIKE Prime – WRO 2025 Junior: Mars Exploration Mission
📋 Overview
This program controls a LEGO® SPIKE™ Prime robot built for the WRO 2025 Junior - Mars Exploration Mission. It is structured into modular functions to handle different robot tasks (missions) such as collecting a drone, releasing water, and delivering colored samples.

The program is written in Python using the SPIKE Prime Python SDK (with spike and hub libraries), and supports multi-mission automation, line following, and motorized arm/sensor control.

🧠 Code Structure
main()
The entry point of the program. It:

Initializes the hub.

Starts a timer.

Calls mission functions in sequence.

Shows a happy face and plays a sound on completion.

✅ Missions
Each mission has a placeholder function:

mission_1_collect_drone()

mission_2_help_stranded_rover()

mission_3_deliver_one_sample(sample_color)

mission_4_release_water()

mission_5_cross_terrain_and_park()

You can call or skip them in main() by commenting/uncommenting the lines.

🤖 Core Movement Functions
Reusable robot actions:

move_cm(cm, speed): Drive straight by a certain distance.

turn_degrees(angle, speed): Turn on the spot.

follow_line(speed, stop_color): Follow a line until a specific color is detected.

🔌 Port Setup
Component	Port
Left Motor	A
Right Motor	B
Tool/Arm Motor	C
Front Color Sensor	E
Bottom Color Sensor	F

⚙️ Robot Constants
These values affect driving precision and must be calibrated:

WHEEL_DIAMETER_CM = 5.6

AXLE_TRACK_CM = 11.2

Adjust these based on your actual robot build.

🧪 Line Following Parameters
KP = 0.7: Adjust if the robot zigzags or reacts too slowly.

TARGET_REFLECTION = 50: Calibrate by reading the reflection value at the line edge.

⏱️ Timing
The Timer object is used to track total mission time, useful for optimizing your run.

🛠️ Customization Tips
Replace pass in each mission with your robot’s movement strategy.

Add delays, conditional logic, or loops based on sensor input as needed.

Use tool_motor.run_for_degrees(...) to control arms or tools.

🧵 Async Notes (Advanced)
The original notes include references to async, await, and gather()—these aren't used in this basic implementation, but may be useful if you upgrade to asynchronous multitasking for complex actions.

🎮 How to Run
Make sure your robot is paired and in Python mode. Upload this code using the SPIKE Prime app or VS Code + SPIKE Prime extension, then run it from the hub or remotely.

📦 File Info
main.py – Main program file (this script)

README.md – Project documentation (you are here)
