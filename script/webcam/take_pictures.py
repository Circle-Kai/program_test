#! /bin/usr/python3
import cv2
WorkingSpace = "."

def take_pictures(mirror, num):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('s'):    # s to save image
            FileName = WorkingSpace + '/image/img_{}.jpg'.format(num)
            cv2.imwrite(FileName, img, [cv2.IMWRITE_JPEG_QUALITY, 90])
            num += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):    # q to quit
            break
    cv2.destroyAllWindows()

def main():
    take_pictures(mirror=True, num = 0)

if __name__ == '__main__':
    main()
