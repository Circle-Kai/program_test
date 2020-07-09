#! /bin/usr/python3
import numpy as np
import math

global pi
pi = math.pi
def Rx(theta):
    Rx_array = np.array([[ 1,         0      ,          0      , 0],
                         [ 0, math.cos(theta), -math.sin(theta), 0],
                         [ 0, math.sin(theta),  math.cos(theta), 0],
                         [ 0,         0      ,          0      , 1]])
    return Rx_array
def Ry(theta):
    Ry_array = np.array([[ math.cos(theta), 0, math.sin(theta), 0],
                         [         0      , 1,        0       , 0],
                         [-math.sin(theta), 0, math.cos(theta), 0],
                         [         0      , 0,        0       , 1]])
    return Ry_array
def Rz(theta):
    Rz_array = np.array([[ math.cos(theta), -math.sin(theta), 0, 0],
                         [ math.sin(theta),  math.cos(theta), 0, 0],
                         [         0      ,          0      , 1, 0],
                         [         0      ,          0      , 0, 1]])
    return Rz_array

def Rxyz(R,x,y,z):
    R[0,3] = x
    R[1,3] = y
    R[2,3] = z
    return R

B_point = np.array([[0.0], [0.0],[2000.0],[1.0]])

R = Ry(0).dot(Rz(pi/2)).dot(Rx(pi))
x = -500
y = 1500
z = 3000
AB_T = Rxyz(R, x, y, z)
A_point = AB_T.dot(B_point)
print(A_point)

'''
header:
  seq: 3
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
pose:
  position:
    x: 1.0
    y: 0.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 0.0
'''
