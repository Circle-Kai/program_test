#! /bin/usr/python3
import numpy as np
import cv2
import cv2.aruco as aruco

marker_size  = 45 # [mm]

#--- Get the camera calibration path
WorkingSpace = "./../webcam"
camera_matrix = np.loadtxt(WorkingSpace + '/config/CameraMatrix.txt', delimiter=',')
camera_distortion = np.loadtxt(WorkingSpace + '/config/CameraDistortion.txt', delimiter=',')


#--- Define the aruco dictionary
aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters  = aruco.DetectorParameters_create()

def main():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #-- Find all the aruco markers in the image
    while True:
        ret_val, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                                                     cameraMatrix=camera_matrix, distCoeff=camera_distortion)
        if ids is not None:
            # -- Find the marker's 6-DOF pose
            rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)
            id_str = "id:{}".format(ids[0][0])
            rvecs_str = "rvecs:{:.1f},{:.1f},{:.1f}".format(rvecs[0][0][0],rvecs[0][0][1],rvecs[0][0][2])
            tvecs_str = "tvecs:{:.1f},{:.1f},{:.1f}".format(tvecs[0][0][0],tvecs[0][0][1],tvecs[0][0][2])
            cv2.putText(frame, id_str, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            cv2.putText(frame, rvecs_str, (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            cv2.putText(frame, tvecs_str, (0, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        cv2.imshow('my webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):    # q to quit
            break
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
