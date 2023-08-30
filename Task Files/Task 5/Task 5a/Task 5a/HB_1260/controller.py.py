#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (HB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:		[ Team-ID 1260]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:		feedback.py
# Functions:
#			[ Comma separated list of functions in this file ]
# Nodes:		Add your publishing and subscribing node


######################## IMPORT MODULES ##########################

import numpy				# If you find it required
import rospy 				
from sensor_msgs.msg import Image 	# Image is the message type for images in ROS
from cv_bridge import CvBridge	# Package to convert between ROS and OpenCV Images
import cv2				# OpenCV Library
import math				# If you find it required
from geometry_msgs.msg import Pose2D	# Required to publish ARUCO's detected position & orientation
import socket
from time import sleep
import signal
import struct
import rospy
import signal		# To handle Signals by OS/user
import sys		# To handle Signals by OS/user
import numpy as np
from geometry_msgs.msg import Wrench		# Message type used for publishing force vectors
from geometry_msgs.msg import PoseArray	# Message type used for receiving goals
from geometry_msgs.msg import Pose2D		# Message type used for receiving feedback
from math import pow, atan2, sqrt, pi, sin, cos	# If you find it useful
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion	# Convert angles

############################ GLOBALS #############################

aruco_publisher = rospy.Publisher('detected_aruco', Pose2D,queue_size=10)
aruco_msg = Pose2D()
ip = "192.168.231.140" 

PI = 3.14
hola_x = 0
hola_y = 0
hola_theta = 0
roll = 0
pitch = 0
x_d = 0
y_d = 0
theta_d = 0
x_goals,y_goals,theta_goals=[],[],[]

x_goals=[530,150,150,350]
y_goals = [300,300,150,150]
theta_goals = [PI/4,3*PI/4,-3*PI/4,-PI/4]
cX = 0
cY = 0
yaw = 0


##################### FUNCTION DEFINITIONS #######################

# NOTE :  You may define multiple helper functions here and use in your code

def signal_handler(sig, frame):
	  
	# NOTE: This function is called when a program is terminated by "Ctr+C" i.e. SIGINT signal 	
	print('Clean-up !')
	cleanup()
	sys.exit(0)

def cleanup():
	############ ADD YOUR CODE HERE ############
	print()
	# INSTRUCTIONS & HELP : 
	#	-> Not mandatory - but it is recommended to do some cleanup over here,
	#	   to make sure that your logic and the robot model behaves predictably in the next run.

	############################################

def inverse_kinematics(v_x, v_y, v_z):
	############ ADD YOUR CODE HERE ############
	global wheel_vel
	# msg = Wrench()
	body_vel = ([v_x],[v_y],[v_z])

	hola_matrix = ([0.6666667,0,1.906614],[-0.33333333,0.57736721,1.906614],[-0.33333333,-0.57736721,1.906614])
	# wheel_vel = np.dot(hola_matrix,body_vel)
	wheel_vel = np.dot(hola_matrix,body_vel)
	for i in range(3):
		wheel_vel[i][0]*= 60
	# conn.sendall(str.encode(str(wheel_vel[0][0])+','+str(wheel_vel[1][0])+','+str(wheel_vel[2][0])))
	data = struct.pack('fff',wheel_vel[0][0],wheel_vel[1][0],wheel_vel[2][0])
	# data = struct.pack('fff',cX,cY,yaw)
	conn.sendall(data)     	
	sleep(0.1)
	
	# while True:
	# 	print("******inverse_kinematics*******")

	# 	conn.sendall(str.encode(str(cX)))

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

def callback(data):
	global cX,cY,yaw
	# Bridge is Used to Convert ROS Image message to OpenCV image
	br = CvBridge()
	rospy.loginfo("receiving camera frame")
	get_frame = br.imgmsg_to_cv2(data, "mono8")		# Receiving raw image in a "grayscale" format
	current_frame = cv2.resize(get_frame, (500, 500), interpolation = cv2.INTER_LINEAR)
	arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
	arucoParams = cv2.aruco.DetectorParameters_create()

	width,height=500,500
	pts1=np.float32([[99,93],[324,83],[106,439],[332,424]])
	pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
	matrix=cv2.getPerspectiveTransform(pts1,pts2)
	image=cv2.warpPerspective(current_frame,matrix,(width,height))
	# convert each of the (x, y)-coordinate pairs to integers
	(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,parameters=arucoParams)
	(topLeft, topRight, bottomRight, bottomLeft) = corners[0][0]
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
	cv2.putText(image, str('('+str(int(cX))+','+str(int(cY))+','+str(yaw)[0:5]+')'),(10, 70), cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 255, 255), 2)
	# aruco_msg.x = int(cX)
	# aruco_msg.y = int(cY)
	# aruco_msg.theta = yaw
	aruco_publisher.publish(aruco_msg)	
	cv2.imshow("window",image)
	k=cv2.waitKey(1)
	print(cX, cY, yaw)

def move_hola_bot(x_d, y_d, theta_d):
	print()
	global hola_x, hola_y, hola_theta
	print("******inside move fucntion*******")
	hola_x = cX
	hola_y = cY
	hola_theta = yaw
	hola_x = ((hola_x - 249.5) / 190)
	hola_y = (249.5 - hola_y) / 190
	print("hi...")
	x_d = ((x_d - 249.5)/190)
	y_d = (249.5 -y_d)/190
	print(x_d, y_d, theta_d)	

	Kp = 0.8
	error_theta = theta_d - hola_theta
	error_x = x_d - hola_x
	error_y = y_d - hola_y
	while((sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)) >= 0.1) or (abs(theta_d - hola_theta)>= 0.1)) :
		hola_x = cX
		hola_y = cY
		hola_theta = yaw
		hola_x = ((hola_x - 249.5) / 190)
		hola_y = (249.5 - hola_y) / 190
		print("********inside vel_while********")
		v_z =-1*(1)*(theta_d - hola_theta)
		# inverse_kinematics(0,0,v_z/20)
		hola_x = cX
		hola_y = cY
		hola_theta = yaw
		hola_x = ((hola_x - 249.5) / 190)
		hola_y = (249.5 - hola_y) / 190


		v_x = (Kp*(x_d - (hola_x))+ 0.6*(error_x - (x_d - hola_x)))*cos(hola_theta) + (Kp*(y_d - (hola_y))+ 0.6*(error_y - (y_d - hola_y)))*sin(hola_theta)  
		error_x = x_d - hola_x
		v_y = (Kp*(x_d - (hola_x))+ 0.6*(error_x - (x_d - hola_x)))*sin(hola_theta) -(Kp*(y_d - (hola_y))+ 0.6*(error_y - (y_d - hola_y)))*cos(hola_theta) 
		error_y = y_d - hola_y
		inverse_kinematics(1.2*v_x*3,1.2*v_y*3,1.6*v_z/20)

	
	error_x = x_d - hola_x
	error_y = y_d - hola_y
	error_theta = theta_d - hola_theta
	print("X:",round(error_x,4)," Y:",round(error_y,4) ," yaw:",round(error_theta,4))
	# INSTRUCTIONS & HELP : 
	#	-> Use the target velocity you calculated for the robot in previous task, and
	#	Process it further to find what proportions of that effort should be given to 3 individuals wheels !!
	#	Publish the calculated efforts to actuate robot by applying force vectors on provided topics
	############################################

def main():
	global client_socket,conn
	rospy.init_node('aruco_feedback_node')  
	rospy.Subscriber('usb_cam/image_rect', Image, callback)
	rate = rospy.Rate(100)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.bind((ip, 8002))
		s.listen()
		conn, addr = s.accept()	

	with conn:
		i=0
		while True:
			
			print(f"Connected to {ip}")
			if(len(x_goals)!=0):
				while(i < len(x_goals)):
					move_hola_bot(x_goals[i],y_goals[i],theta_goals[i])
					i = i + 1
				while(i>=len(x_goals)):
					inverse_kinematics(0,0,0)



if __name__ == '__main__':
  main()

		