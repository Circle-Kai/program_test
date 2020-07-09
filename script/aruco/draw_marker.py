#! /bin/usr/python3
import cv2
import cv2.aruco as aruco
WorkingSpace = "."

aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
marker_size = 400 # [pixel]
first_marker = 110
last_marker =119

for i in range(first_marker, last_marker+1):
    marker_id = i
    img	= aruco.drawMarker(aruco_dict, marker_id, marker_size, borderBits=1)
    FileName = WorkingSpace + '/image/original_aruco_{}_pixel/marker_{}.jpg'.format(marker_size, i)
    cv2.imwrite(FileName, img, [cv2.IMWRITE_JPEG_QUALITY, 90])
    
