#! /bin/usr/python3
# -*- coding: utf-8 -*-
# sudo pip3 install pymodbus

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
HOST = "192.168.1.234"
PORT = 502
client = ModbusClient(HOST, PORT)
client.connect()

import time
# 0~65535
RealValue = [0]*6
def Modbus2Real(ModbusValue, RealValue):
    for i in range(0, 6):
        if i < 3:
            RealValue[i] = ((ModbusValue[i]-65535) if ModbusValue[i] > 32768 else ModbusValue[i])/(1e+4)    # unit: Meter
        else:
            RealValue[i] = ((ModbusValue[i]-65535) if ModbusValue[i] > 32768 else ModbusValue[i])/(1e+3)    # unit: Radian
            
        print(RealValue[i])

TCP_ModbusValue = client.read_holding_registers(400,6)
data = TCP_ModbusValue.registers
print('TCP :', data)
Modbus2Real(data, RealValue)
