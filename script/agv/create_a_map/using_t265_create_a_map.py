#! /bin/usr/python3
import time
from transformation import TRANSFORMATION
tf = TRANSFORMATION()

# < --- --- Yaml/CSV import --- --->
import csv
import yaml
with open('/home/kai/Scripts/agv/create_a_map/config/map.yaml', 'r') as stream:
    map_data = yaml.safe_load(stream)

# < --- --- OpenCV import --- --->
import cv2
import numpy as np 
drawing = False # true if mouse is pressed
t265_P0 = tf.get_img_pose(0, 0, 0)
pt1_x , pt1_y = int(t265_P0[0][0]) , int(t265_P0[1][0])

# < --- --- T265 import --- --->
# First import the library
import pyrealsense2 as rs
# Declare RealSense pipeline, encapsulating the actual device and sensors
pipe = rs.pipeline()
# Build config object and request pose data
cfg = rs.config()
cfg.enable_stream(rs.stream.pose)
# Start streaming with requested config
pipe.start(cfg)

def updata_t265_pose():
    # Wait for the next set of frames from the camera
    frames = pipe.wait_for_frames()
    # Fetch pose frame
    pose = frames.get_pose_frame()

    if pose:
        # Print some of the pose data to the terminal
        data = pose.get_pose_data()
        #print("Frame #{}".format(pose.frame_number))
        x_t265_imu_pose = data.translation.x
        # y_t265_imu_pose = data.translation.y*100  # y_t265_imu_pose is 0
        z_t265_imu_pose = data.translation.z
        t265_pose_frame_img = tf.get_img_pose(x_t265_imu_pose*100, 0, z_t265_imu_pose*100)
        car_pose_frame_map = tf.get_car_pose(x_t265_imu_pose, 0, z_t265_imu_pose)
        # Add new pose(x, y) to array
        csv_data.append([car_pose_frame_map[0][0],car_pose_frame_map[1][0]]) 
    return (t265_pose_frame_img[0][0], t265_pose_frame_img[1][0])

def line_drawing():
    global pt1_x,pt1_y,drawing
    
    point = updata_t265_pose()
    x , y = int(round(point[0])), int(round(point[1]))
    
    cv2.line(img,(pt1_x,pt1_y),(x,y),color=(255,255,255),thickness=1)
    pt1_x,pt1_y=x,y   

def main():
    global img, csv_data
    img = np.zeros((600,800,3), np.uint8)
    cv2.namedWindow('test draw')
    csv_data = []
    
    while(True):
        line_drawing()
        cv2.imshow('test draw',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('/home/kai/Scripts/agv/create_a_map/docs/map.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            with open('/home/kai/Scripts/agv/create_a_map/map/map.csv', 'w', newline='') as csvfile:
                csv_file = csv.writer(csvfile)
                for i in range(len(csv_data)):
                    csv_file.writerow([csv_data[i][0], csv_data[i][1]])
            break
        time.sleep(0.1)
    cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main()
