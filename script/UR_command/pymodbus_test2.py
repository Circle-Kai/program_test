#! /bin/usr/python3
# -*- coding: utf-8 -*-
# sudo pip3 install pymodbus
import socket
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

'''
def check_joint(joint):
    while(True):
        if abs(ur.modbus_value2meter(400)-pose[0])<=0.001 and abs(ur.modbus_value2meter(401)-pose[1])<=0.001 and abs(ur.modbus_value2meter(402)-pose[2])<=0.001:
            break
        print("wait")
        time.sleep(1)
    print("Finish")
'''

def check_pose(pose):
    while(True):
        if abs(ur.modbus_value2meter(400)-pose[0])<=0.001 and abs(ur.modbus_value2meter(401)-pose[1])<=0.001 and abs(ur.modbus_value2meter(402)-pose[2])<=0.001:
            break
        print("wait")
        time.sleep(1)
    print("Finish")

class UniversalRobotsCommand():
    def __init__(self):
        robot_host = '192.168.1.234'
        modbus_port = 502
        socket_port = 30001
        m = ModbusClient(robot_host, modbus_port)
        m.connect()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((robot_host, socket_port))
        self.modbus = m
        self.socket = s
        
    def modbus_value2meter(self, address):
        m = self.modbus
        value = m.read_holding_registers(address,1)
        position_original = value.registers
        position_meter = ((position_original[0]-65535) if position_original[0] > 32768 else position_original[0])/(1e+4)     # unit: Meter
        return position_meter
        
    def modbus_value2radian(self, address):
        m = self.modbus
        value = m.read_holding_registers(address,1)
        position_original = value.registers
        position_radian = ((position_original[0]-65535) if position_original[0] > 32768 else position_original[0])/(1e+3)    # unit: Radian
        return position_radian

    def socket_moveJ_joint(self, joint_global, acc, vel):
        s = self.socket
        move_command = ("movej(%s, a=%s, v=%s)\n" %(joint_global, acc, vel))
        s.send(move_command.encode('utf-8'))
        return check_pose(joint_global[:3])

    def socket_moveJ_pose(self, pose_global, acc, vel):
        s = self.socket
        move_command = ("movej(p%s, a=%s, v=%s)\n" %(pose_global, acc, vel))
        s.send(move_command.encode('utf-8'))
        return check_pose(pose_global[:3])

ur = UniversalRobotsCommand()
'''
#ur.socket_moveJ_joint([0.0, -1.57079632679, 0.0, -1.57079632679, 0.0, 0.0], acc=1.4, vel=1.05)
ur.socket_moveJ_pose([-0.109, -0.4868, 0.0, 0.0, 3.142, 0.0], acc=1.4, vel=1.05)
ur.socket_moveJ_pose([-0.109, -0.4868, 0.4319, 0.0, 3.142, 0.0], acc=1.4, vel=1.05)
'''
while(True):
    print("[%s, %s, %s, %s, %s, %s]" %(ur.modbus_value2meter(400),ur.modbus_value2meter(401),ur.modbus_value2meter(402),
                                       ur.modbus_value2meter(403),ur.modbus_value2meter(404),ur.modbus_value2meter(405)))

    time.sleep(1)

