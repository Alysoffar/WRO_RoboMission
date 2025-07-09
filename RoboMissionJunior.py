from hub import light_matrix
from spike import PrimeHub, Motor, MotorPair, ColorSensor, TouchSensor
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
arm_forward_motor = Motor('')
arm_backward_motor = Motor('')
# Sensors (Your Robot's Senses)
# A color sensor on the bottom for following lines or seeing colored areas.
color_sensor_bottom = ColorSensor('F')
# A color sensor on the front for identifying the colored research samples.
color_sensor_front = ColorSensor('E')

# The trigger sensor
touch_sensor = TouchSensor('') ## NEW ##


# --- STEP 3: ROBOT CONSTANTS ---
# !!! YOUR TEAM MUST MEASURE AND CHANGE THESE VALUES FOR ACCURACY !!!
# Measure your robot to help it drive the correct distance and turn precisely.

WHEEL_DIAMETER_CM = 5.6        # Measure your wheels! (e.g., 5.6 cm for standard SPIKE wheels)
WHEEL_CIRCUMFERENCE_CM = WHEEL_DIAMETER_CM * math.pi

# The distance between the center of your two driving wheels.
AXLE_TRACK_CM = 11.2
# --- GLOBAL STATE VARIABLES ---
# These variables act as the robot's memory during the run.

has_drone = False
samples_collected = [] # A list to store the colors of samples we pick up, e.g., ['red', 'green']
number_of_samples_in_hopper = 0# The maximum number of samples your robot can hold at once.

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

#optional according to if u want tp add line tracking or not
'''def follow_line(speed, stop_color='white'):
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
    print("Line following finished.")'''

# === Arm A Functions ===
# Arm A is responsible for collecting and dropping two samples.

def execute_collect_mechanism_arm_a():
    """
    This function closes the claw of Arm A to collect two samples.
    The claw is closed by rotating the motor backwards (negative degrees).
    """
    print("ARM A: Closing claw to collect samples.")

    # Rotate the motor backward to close the claw and grip the samples.
    arm_forward_motor.run_for_degrees(-90, speed=50)# -90 degrees closes the claw. Adjust as needed.

    # Short pause to ensure the movement completes before moving on.
    wait_for_seconds(0.5)

def execute_drop_mechanism_arm_a():
    """
    This function opens the claw of Arm A to drop the two collected samples.
    The claw is opened by rotating the motor forward (positive degrees).
    """
    print("ARM A: Opening claw to drop samples.")

    # Rotate the motor forward to open the claw and release the samples.
    arm_forward_motor.run_for_degrees(90, speed=50)# 90 degrees opens the claw. Adjust as needed.

    # Short pause to allow the mechanism to fully open before proceeding.
    wait_for_seconds(0.5)

# === Arm B Functions ===
# Arm B is used to take two balls and lower the satellite arm after placing them.

def execute_collect_mechanism_arm_b():
    """
    This function closes the claw of Arm B to pick up two balls.
    """
    print("ARM B: Closing claw to take balls.")

    # Close the claw by rotating the motor backwards.
    arm_backward_motor.run_for_degrees(-90, speed=50)

    # Brief delay to ensure completion.
    wait_for_seconds(0.5)

def execute_drop_mechanism_arm_b():
    """
    This function opens the claw of Arm B to drop the two balls into the desired area.
    """
    print("ARM B: Opening claw to release balls.")

    # Open the claw by rotating the motor forward.
    arm_backward_motor.run_for_degrees(90, speed=50)

    # Delay for smooth operation.
    wait_for_seconds(0.5)


# === Sample Usage Flow ===
# Here's an example of how these functions could be used in sequence.
# You might call these in response to button presses, sensor inputs, or autonomous logic.

"""
# Example sequence of operations:
execute_collect_mechanism_arm_a()
# (Robot moves to drop location for samples)
execute_drop_mechanism_arm_a()

execute_collect_mechanism_arm_b()
# (Robot moves to drop zone for balls)
execute_drop_mechanism_arm_b()
lower_satellite_arm()
"""




# --- STEP 5: MARS MISSION FUNCTIONS (The Plan for Each Task) ---
# These functions represent each mission from the rulebook.
# They now utilize the correct robotic arms for specific tasks.

#NOTE Add speed to moves

def run_mission_get_water():
    """
    Mission: Push the water dispenser.
    Simple drive and push action.
    """

    print("Executing Mission: Get Water")

    move_cm(25, speed=40)        # Approach the water station
    turn_degrees(-90)            # Face the dispenser
    move_cm(18)                    # Close in carefully
    move_cm(5, speed=75)        # Push sharply to activate dispenser
    move_cm(-23)                # Back away
    turn_degrees(90)            # Reorient to original direction

def run_mission_get_drone():
    """
    Mission: Pick up the drone using Arm B.
    The drone is a special object handled by the second arm.
    """
    global has_drone, samples_collected
    print("Executing Mission: Get Drone")

    move_cm(50)                        # Move to drone pickup area
    execute_collect_mechanism_arm_b()# Use Arm B to grab the drone
    has_drone = True                    # Mark that the drone is now onboard
    move_cm(-10)                        # Back away to avoid collisions

def run_mission_help_rover():
    """
    Mission: Locate the rover using a line-following strategy,
    gently push it, and then back off.
    """
    print("Executing Mission: Help Rover")

    turn_degrees(-30)# Slight angle to align with line
    drive_base.se
    move_cm(20)

    # Follow the line until the bottom color sensor detects black
    while color_sensor_bottom.get_color() != 'black':
        pass
    drive_base.stop()

    turn_degrees(30)        # Re-align toward rover
    move_cm(15, speed=20)# Carefully approach rover
    move_cm(5, speed=40)    # Small push to assist rover
    move_cm(-20)            # Back off safely

def run_mission_sample_sweep():
    """
    Mission: Drive to up to three sample positions, scan for valid colors,
    and collect if valid. Uses Arm A for sample collection.
    """
    global has_drone, samples_collected
    print("Executing Mission: Sample Sweep")

    valid_sample_colors = ['red', 'green', 'white', 'yellow']# Valid samples


    move_cm(15)        # Move to next sample area
    turn_degrees(-90)# Face sample
    move_cm(5)        # Get close to the sample

    detected_color = color_sensor_front.get_color()
    print(f"Sensor sees: {detected_color}")

    if detected_color in valid_sample_colors:
        execute_collect_mechanism_arm_a()# Use Arm A to collect sample
        samples_collected.append(detected_color)
        print(f"Collected {detected_color}! Hopper: {samples_collected}")

    move_cm(-5)        # Back away from sample
    turn_degrees(90)    # Return to forward-facing


def run_mission_park():

    """
    Drives the robot forward slowly until the touch sensor is pressed,
    then stops and moves an extra 2 cm.
    """
    move_cm(-20)
    turn_degrees(90)
    move_cm(5)
    turn_degrees(-90)

    print("Moving forward until touch sensor is activated...")

    # Start moving forward at a slow, controlled speed
    drive_base.start(speed=20)

    # This function will pause the code until the condition is met
    touch_sensor.wait_until_pressed()

    # As soon as it's pressed, stop immediately.
    drive_base.stop()
    print("Touch sensor activated!")

    # Now, perform the small 2 cm nudge.
    print("Nudging forward 2 cm.")
    move_cm(2, speed=15) # Use a very slow speed for precision




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
    run_mission_get_water()
    run_mission_get_drone()
    run_mission_help_rover()
    run_mission_sample_sweep('yellow') # Try to get one specific sample
    run_mission_park()

    # --- MISSION COMPLETE ---
    total_time = mission_timer.now()
    print(f"MARS MISSION FINISHED IN {total_time} SECONDS!")
    hub.light_matrix.show_image('HAPPY')
    hub.speaker.play_sound('Triumph')

# This is the line that starts the whole program by running the 'main' function.
main()

