#! /bin/usr/python3
import numpy as np
import math
import yaml

with open(r'/home/kai/Scripts/T265/map.yaml') as stream:
    map_data = yaml.safe_load(stream)
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
    
class TRANSFORMATION(object):
    def __init__(self):
        x = map_data['map']['width']/2
        y = map_data['map']['height']/2
        z = 0
        R = Ry(0).dot(Rx(pi)).dot(Rz(pi/2))
        img_map_T = Rxyz(R, x, y, z)
        
        x = 0
        y = 0
        z = 0
        R = Rx(0).dot(Rz(0)).dot(Ry(0))
        map_car_T = Rxyz(R, x, y, z)
        
        x = 10
        y = 0
        z = 0
        R = Rx(0).dot(Ry(-pi/2)).dot(Rz(-pi/2))
        car_t265_T = Rxyz(R, x, y, z)
        
        self.map_car_T = map_car_T
        self.car_t265_T = car_t265_T
        self.img_map_T = img_map_T
        
    def get_t265_pose(self, x, y, z):
        t265_pose = np.array([[x],[y],[z],[1.0]])
        map_point = self.map_car_T.dot(self.car_t265_T).dot(t265_pose)        
        return map_point[:2]

    def get_car_pose(self, x, y, z):
        t265_pose = np.array([[x],[y],[z],[1.0]])
        map_point = self.map_car_T.dot(self.car_t265_T).dot(t265_pose)
        return map_point[:2]
        
    def get_img_pose(self, x, y, z):
        t265_pose = np.array([[x],[y],[z],[1.0]])
        img_point = self.img_map_T.dot(self.map_car_T).dot(self.car_t265_T).dot(t265_pose)        
        return img_point[:2]
