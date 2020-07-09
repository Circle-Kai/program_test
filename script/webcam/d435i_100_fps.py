#! /bin/usr/python3
import cv2
import time

def show_webcam(mirror=False):
    prevTime = 0
    cam = cv2.VideoCapture(2)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
    while True:
        prevTime = time.time()
        
        ret_val, img = cam.read()
        
        curTime = time.time()
        sec = curTime - prevTime
        print(prevTime, curTime, sec)
        prevTime = curTime
        fps = 1/(sec)
        str = "FPS : {:.1f}".format(fps)
        cv2.putText(img, str, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # q to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
    
