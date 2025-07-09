from hub import light_matrix
from spike import PrimeHub, Motor, MotorPair, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds, Timer
import math
import runloop
#This Function runs the whole code so every thing must be here (as a Function as the main calls the function),
#Functions: If U have a piece of code that U wan to do multiple of times , for example u want to excute a block of code 10 times, is it better to just copy and paste it or to do another\
#block to do the code 10 times, this is the function, it is a code that u can call at any time u want , the function to be excuted does not run like normal main function, it needs to be called, 
#to just callthe function all u need is just call its name for example if the function is def func() the name of the function (which is func).

#async is like bread oven for example when U put 3 loaves of bread in the oven, it comes out sequentially, like the first comes out first then the second then the third, this happens due to await function
#The gather function is for agthering all the data and organizing the await calls to be it sequentially
# function, If u want every code to do at the same time , U have to assign the function to a variable then do the gather function.


# WRO 2025 JUNIOR - MARS EXPLORATION MISSION
#
# Team: N/A
#
# This program is structured with functions to make it easy to
# plan, build, and test your robot's mission to Mars!
# ==============================================================================

# --- STEP 1: IMPORTS & PRE-FLIGHT CHECK ---
# We need to import all the tools from the SPIKE library to control the robot.


# --- STEP 2: SETUP YOUR ROBOT HARDWARE HERE ---
# Tell the program which port everything is plugged into.
# IMPORTANT: Make sure these ports match your robot's build!
hub = PrimeHub()
#To Be Announced (Lines 32-59)
# Drive Motors (The Wheels)
left_motor = Motor('A')    # Port A for the left wheel motor
right_motor = Motor('B')    # Port B for the right wheel motor
drive_base = MotorPair('A', 'B')

# Attachment Motors (The Tools)
# This could be an arm for collecting things or pressing buttons.
tool_motor = Motor('C')    # Port C for your arm or tool

# Sensors (Your Robot's Senses)
# A color sensor on the bottom for following lines or seeing colored areas.
color_sensor_bottom = ColorSensor('F')
# A color sensor on the front for identifying the colored research samples.
color_sensor_front = ColorSensor('E')

# --- STEP 3: ROBOT CONSTANTS ---
# !!! YOUR TEAM MUST MEASURE AND CHANGE THESE VALUES FOR ACCURACY !!!
# Measure your robot to help it drive the correct distance and turn precisely.

WHEEL_DIAMETER_CM = 5.6        # Measure your wheels! (e.g., 5.6 cm for standard SPIKE wheels)
WHEEL_CIRCUMFERENCE_CM = WHEEL_DIAMETER_CM * math.pi

# The distance between the center of your two driving wheels.
AXLE_TRACK_CM = 11.2

# --- STEP 4: CORE MOVEMENT & ACTION FUNCTIONS (The Robot's Skills) ---
# These are the basic abilities of your robot. You will use these inside your missions.

def move_cm(centimeters, speed):
    """
    Drives the robot forward or backward in a straight line.
    A positive 'centimeters' value moves forward.
    A negative 'centimeters' value moves backward.
    """
    degrees_to_rotate = (centimeters / WHEEL_CIRCUMFERENCE_CM) * 360
    drive_base.move(degrees_to_rotate, 'degrees', speed=speed)
    print(f"Moved {centimeters} cm")

def turn_degrees(angle, speed):
    """
    Turns the robot on the spot.
    A positive 'angle' turns RIGHT.
    A negative 'angle' turns LEFT.
    """
    # This formula calculates how much the wheels need to turn to rotate the robot.
    distance_to_move_cm = (AXLE_TRACK_CM * math.pi / 360) * angle
    degrees_to_rotate = (distance_to_move_cm / WHEEL_CIRCUMFERENCE_CM) * 360

    # To turn on the spot, one motor goes forward and the other goes backward.
    drive_base.move_tank(degrees_to_rotate, 'degrees', left_speed=-speed, right_speed=speed)
    print(f"Turned {angle} degrees")

def follow_line(speed, stop_color='white'):
    """
    Follows the edge of a black line using the bottom color sensor.
    It will stop when the sensor detects the 'stop_color'.

    !!! YOUR TEAM MUST EXPERIMENT with the KP and TARGET_REFLECTION values!
    """
    KP = 0.7# "Proportional Gain". A small number (like 0.5 to 1.0) is a good start.
            # If it zig-zags too much, make it smaller. If it's too slow to react, make it bigger.

    # Calibrate this! Hold the sensor exactly on the edge of the black line and check
    # the reflected light percentage in the SPIKE app. Use that number here.
    TARGET_REFLECTION = 50

    while color_sensor_bottom.get_color() != stop_color:
        current_reflection = color_sensor_bottom.get_reflected_light()
        error = TARGET_REFLECTION - current_reflection

        steering = error * KP # Calculate how sharply to turn.
        drive_base.start(int(steering), speed=speed) # Use start() for continuous moving.

    drive_base.stop()
    print("Line following finished.")

# --- STEP 5: MARS MISSION FUNCTIONS (The Plan for Each Task) ---
# Here we create a function for each task from the rulebook.
# Your team's job is to fill in the code for each mission!

def mission_1_collect_drone():
    """Mission 3.1: Drives to the drone, collects it, and returns it to the start area."""
    print("Executing Mission 1: Collect Drone")
    # Your team's plan:
    # 1. Drive out from the start area towards the drone.
    # 2. Use a mechanism to hook or grab the drone model.
    # 3. Drive back to the start area.
    # 4. Release the drone so it's inside the start area.

    pass # <-- REMOVE 'pass' AND ADD YOUR CODE HERE

def mission_2_help_stranded_rover():
    """Mission 3.2: Drives to the stranded rover and pushes its solar panel to be flat."""
    print("Executing Mission 2: Help Stranded Rover")
    # Your team's plan:
    # 1. Navigate along the black lines to get to the rover.
    # 2. Align your robot carefully with the upright solar panel.
    # 3. Drive forward slowly or use an arm to push the panel down so it is horizontal.

    pass # <-- REMOVE 'pass' AND ADD YOUR CODE HERE

def mission_3_deliver_one_sample(sample_color):
    """
    Mission 3.3: Finds a research sample of a specific color, picks it up,
    and delivers it to the matching colored lab.
    """
    print(f"Executing Mission 3: Deliver {sample_color} sample")
    # Your team's plan for ONE sample:
    # 1. Navigate to the research sample area in the middle of the field.
    # 2. Search for the sample. You could drive slowly past the 6 locations, using
    #    the front color sensor to check each one until it sees the 'sample_color'.
    # 3. When you find it, use an arm to collect it.
    # 4. Navigate to the correct colored lab (e.g., the yellow hexagon).
    # 5. Drop the sample completely inside the lab area.

    pass # <-- REMOVE 'pass' AND ADD YOUR CODE HERE

def mission_4_release_water():
    """Mission 3.4: Drives to the water dispenser and activates it."""
    print("Executing Mission 4: Release Water Supply")
    # Your team's plan:
    # 1. Navigate from the start area to the left side of the field.
    # 2. Align the robot with the dispenser mechanism.
    # 3. Use your robot or a tool to push the lever, releasing the blue balls.

    pass # <-- REMOVE 'pass' AND ADD YOUR CODE HERE

def mission_5_cross_terrain_and_park():
    """Mission 3.5: Navigates the rough terrain and parks fully in the target area."""
    print("Executing Mission 5: Cross Rough Terrain and Park")
    # Your team's plan:
    # 1. Navigate to the start of the rough terrain area.
    # 2. Drive slowly and straight, right through the middle of the axles.
    # 3. Stop your robot so it is completely inside the white target area.

    pass # <-- REMOVE 'pass' AND ADD YOUR CODE HERE

# --- STEP 6: MAIN MISSION CONTROL (The Story of Your Run) ---
# This is where you decide the order of your missions to get the most points!
def main():
    # Countdown and start timer!
    hub.light_matrix.write("321")
    hub.speaker.beep()
    mission_timer = Timer()

    # --- YOUR MISSION PLAN ---
    # Choose which missions to run by "un-commenting" them (remove the #).
    # Arrange them in the order you want your robot to perform them.

    # Example Plan:
    mission_1_collect_drone()
    # mission_2_help_stranded_rover()
    # mission_4_release_water()
    # mission_3_deliver_one_sample('yellow') # Try to get one specific sample
    # mission_5_cross_terrain_and_park()

    # --- MISSION COMPLETE ---
    total_time = mission_timer.now()
    print(f"MARS MISSION FINISHED IN {total_time} SECONDS!")
    hub.light_matrix.show_image('HAPPY')
    hub.speaker.play_sound('Triumph')

# This is the line that starts the whole program by running the 'main' function.
main()

