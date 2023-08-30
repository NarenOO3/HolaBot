import numpy		# If you find it required
# import rospy 				
# from sensor_msgs.msg import Image 	# Image is the message type for images in ROS
# from cv_bridge import CvBridge	# Package to convert between ROS and OpenCV Images
import cv2			
from cv2 import aruco	# OpenCV Library
import math				# If you find it required
import socket
from time import sleep

import signal		# To handle Signals by OS/user
import sys		# To handle Signals by OS/user
from math import pow, atan2, sqrt, pi, sin, cos	# If you find it useful


ip = "192.168.197.74"
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

cap = cv2.VideoCapture(1)
cap.set(3,500)
cap.set(4,500)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#       s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#       s.bind((ip, 8002))
#       s.listen()
#       conn, addr = s.accept()
#       with conn:
#         print(f"Connected by {addr}")
while True:
          sucess,img = cap.read()
          current_frame = cv2.resize(img, (500, 500), interpolation = cv2.INTER_LINEAR)
          current_frame = cv2.cvtColor(current_frame,cv2.COLOR_BGR2GRAY)
          arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
          arucoParams = cv2.aruco.DetectorParameters_create()
          (corners, ids, rejected) = cv2.aruco.detectMarkers(current_frame, arucoDict,parameters=arucoParams)
          #print(corners[0][0])
          (topLeft, topRight, bottomRight, bottomLeft) = corners[0][0]

          # convert each of the (x, y)-coordinate pairs to integers
          image=current_frame	
          topRight = (topRight[0]), (topRight[1])
          bottomRight = (bottomRight[0]), (bottomRight[1])
          bottomLeft = (bottomLeft[0]), (bottomLeft[1])
          topLeft = (topLeft[0]), (topLeft[1])
          cX = (topLeft[0] + bottomRight[0]) / 2.0
          cY = (topLeft[1] + bottomRight[1]) / 2.0    
          
          # # draw the ArUco marker ID on the image
          
          
          topRight_x = topRight[0]
          topRight_y = topRight[1] 
          bottomLeft_x = bottomLeft[0]
          bottomLeft_y = bottomLeft[1] 
          topRight_x = ((topRight_x- 249)/190)
          topRight_y = (249 - topRight_y)/190
          bottomLeft_x = ((bottomLeft_x - 249)/190)
          bottomLeft_y = (249 - bottomLeft_y)/190
          topRight_x = (topRight[0]-249)/190
          topLeft_x = (topLeft[0]-249)/190
          bottomRight_x = (bottomRight[0]-249)/190
          bottomLeft_x = (bottomLeft[0]-249)/190
          
          topRight_y = (249-topRight[1])/190
          bottomRight_y = (249-bottomRight[1])/190
          topLeft_y = (249-topLeft[1])/190
          bottomLeft_y = (249-bottomLeft[1])/190
          cX_converted = ((cX - 249)/190)
          cY_converted = (249 -cY)/190

          cv2.circle(image, (int(cX),int(cY)), 4, (255, 255, 255), -1)
          cv2.putText(image, str(ids),(int(cX), int(cY) - 15), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)

          if(topRight_y>=topLeft_y):
            if(topRight_y>=cY_converted):
              yaw=angle_between((topRight_x-bottomLeft_x,topRight_y-bottomLeft_y),(1,0))-math.pi/4
            else:
              yaw=(-1)*angle_between((topRight_x-bottomLeft_x,topRight_y-bottomLeft_y),(1,0))+math.pi*7/4
          else:
              if(topRight_y>=cY_converted):
                yaw=angle_between((topRight_x-bottomLeft_x,topRight_y-bottomLeft_y),(1,0))-math.pi/4
              else:
                yaw=(-1)*(angle_between((topRight_x-bottomLeft_x,topRight_y-bottomLeft_y),(1,0))+math.pi/4)
          print(cX, cY,round(yaw,4))
          cv2.putText(image, str('('+str(int(cX))+','+str(int(cY))+','+str(yaw)+')'),(30, 30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  
          cv2.imshow("window",image)
          cv2.waitKey(1)
          # data = conn.recv(1024)
          # print(data)
          # conn.sendall(str.encode(str(cX)+','+str(cY)+','+str(round(yaw,4))))
          #sleep(1)    

