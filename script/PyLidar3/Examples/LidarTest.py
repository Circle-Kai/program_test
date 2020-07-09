import PyLidar3
from numpy import pi
import matplotlib.pyplot as plt
import time # Time module
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
#port = input("Enter port name which lidar is connected:") #windows
port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarG4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)
def main():
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        t = time.time() # start time 
        while (time.time() - t) < 30: #scan for 30 seconds
            print(next(gen))
            time.sleep(0.5)
        Obj.StopScanning()
        Obj.Disconnect()
    else:
        print("Error connecting to device")

if __name__ == "__main__":
    try:
        main()
    except IndexError as ERROR_MESSAGE:
        Obj.StopScanning()
        Obj.Disconnect()
        print(ERROR_MESSAGE)
