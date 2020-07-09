#! /bin/usr/python3
# -*- coding: utf-8 -*-
import socket
from pynput import keyboard
import time

LMotorType="LS"; RMotorType="RS"; LMotorVal=0; RMotorVal=0; cmd="LS,0,RS,0"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))  # Socket: IP / Port, Port: 1024 ~ 65535

def on_press(key):
    global LMotorType, RMotorType, LMotorVal, RMotorVal
    buttons = ["w", "x", "a", "d", "s"]
    msg ='''\n#################################################
 Plsase use these buttons to control your robot.
 ESC : Exit the keyboard listener
 
 W : Go Forward
 A : Turn Left
 S : Stop
 D : Turn Right
 X : Go Back
#################################################'''
    try:
        if key.char in buttons:
            #print('alphanumeric key {0} pressed'.format(key.char))
                        
            if key.char == buttons[0]:     # w
                LMotorVal += 1; RMotorVal += 1
            elif key.char == buttons[1]:   # x
                LMotorVal -= 1; RMotorVal -= 1
            elif key.char == buttons[2]:   # a
                LMotorVal -= 1; RMotorVal += 1
            elif key.char == buttons[3]:   # d
                LMotorVal += 1; RMotorVal -= 1
            elif key.char == buttons[4]:   # s
                LMotorVal = 0; RMotorVal = 0
            
            # Motor Val Limited
            if LMotorVal > 12: LMotorVal = 12
            elif LMotorVal < -12: LMotorVal = -12
            if RMotorVal > 12: RMotorVal = 12
            elif RMotorVal < -12: RMotorVal = -12
            
            # Motor Type
            if LMotorVal == 0:  LMotorType = "LS"
            elif LMotorVal > 0: LMotorType = "LF"
            elif LMotorVal < 0: LMotorType = "LB"
            if RMotorVal == 0:  RMotorType = "RS"
            elif RMotorVal > 0: RMotorType = "RF"
            elif RMotorVal < 0: RMotorType = "RB"

            cmd = "{},{},{},{}".format(LMotorType,abs(LMotorVal),RMotorType,abs(RMotorVal))
            client.sendall(cmd.encode())
            #client.close()
        else:
            print(msg)
            
    except AttributeError:
        if key == keyboard.Key.esc: print('Special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener
        return False

def main():
    # keyboard -- keyboard -- keyboard
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()
    while(True):
        time.sleep(0.2)
if __name__ == "__main__":
    main()
