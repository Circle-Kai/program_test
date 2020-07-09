#! /bin/usr/python3
# -*- coding: utf-8 -*-
import socket
import time

HOST = '127.0.0.1'
PORT = 8000
def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        num = 0
        while(True):
            clientMessage = "@Num:{}\n".format(num)
            client.sendall(clientMessage.encode())
            
            num+=1
            #serverMessage = str(client.recv(1024), encoding='utf-8')
            #print('Server:', serverMessage)
            time.sleep(1) #[s]
            #client.close()
    finally:
        client.close()
if __name__ == "__main__":
    main()
