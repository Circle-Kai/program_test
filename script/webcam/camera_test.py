#! /bin/usr/python3
import cv2

def show_webcam(mirror=False):
    num = 0
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # q to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
    
