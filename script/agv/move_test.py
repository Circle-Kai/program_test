#! /bin/usr/python3
"""
Packages: https://pypi.org/project/pynput/
"""
from pynput import keyboard
from time import sleep

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        global linear_vel, angular_vel, right_motor, left_motor
        
        if key.char == "w":
            linear_vel = linear_vel + 1
        elif key.char == "x":
            linear_vel = linear_vel - 1
        elif key.char == "a":
            angular_vel = angular_vel + 1
        elif key.char == "d":
            angular_vel = angular_vel - 1
        elif key.char == "s":
            linear_vel = 0; angular_vel = 0
        right_motor = round((linear_vel + angular_vel)/10, 1)
        left_motor = round((linear_vel - angular_vel)/10, 1)
        print("\nlinear_vel:{}, angular_vel:{}" .format(linear_vel/10, angular_vel/10))
        print("Left_motor:{}, Right_motor:{}" .format(left_motor, right_motor))
        
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
linear_vel = 0; angular_vel = 0
right_motor = 0.0; left_motor = 0.0
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

print("linear_vel:{}, angular_vel:{}" .format(linear_vel, angular_vel))
print("Left_motor:{}, Right_motor:{}" .format(left_motor, right_motor))
while (True):

    sleep(0.1)
