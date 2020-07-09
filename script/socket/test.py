#! /bin/usr/python3
# -*- coding: utf-8 -*-
import socket
HOST = '127.0.0.1'
PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
try:
    clientMessage = ""
    while True:
        if clientMessage == "":
            conn, address = server.accept()
            clientMessage = str(conn.recv(1024), encoding='utf-8')
        else:
            print(clientMessage)
            print(address)
            clientMessage = str(conn.recv(1024), encoding='utf-8')
        #serverMessage = 'I\'m here!'
        #conn.sendall(serverMessage.encode())
finally:
    conn.close()

