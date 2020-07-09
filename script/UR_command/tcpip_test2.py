#! /bin/usr/python3
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "192.168.1.234"
PORT = 30001
BUFFER_SIZE = 1024
IO_True = "set_digital_out(0,True)\n"
MoveJ_Home = "movej([0.0, -1.57079632679, 0.0, -1.57079632679, 0.0, 0.0], a=1.4, v=1.05)\n"
MoveJ_Pose1 = "movej(p[0.10915, -0.4869, 0.43186, 0.0, 3.142, 0.0], a=1.4, v=1.05\n"
MoveJ_Pose2 = "movej(p[0.10915, -0.4869, -0.06308, 0.0, 3.142, 0.0], a=1.4, v=1.05)\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



s.send(MoveJ_Pose2.encode('utf-8'))




#data = s.recv(BUFFER_SIZE)
#print("received data:", data)

s.close()
