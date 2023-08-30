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

# Team ID:		[ Team-ID ]
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

############################ GLOBALS #############################

aruco_publisher = rospy.Publisher('detected_aruco', Pose2D,queue_size=10)
aruco_msg = Pose2D()

##################### FUNCTION DEFINITIONS #######################

# NOTE :  You may define multiple helper functions here and use in your code
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

def callback(data):
	# Bridge is Used to Convert ROS Image message to OpenCV image
	br = CvBridge()
	rospy.loginfo("receiving camera frame")
	get_frame = br.imgmsg_to_cv2(data, "mono8")		# Receiving raw image in a "grayscale" format
	current_frame = cv2.resize(get_frame, (500, 500), interpolation = cv2.INTER_LINEAR)
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
	# if(topRight_x != bottomLeft_x):
	# 	tan_thetha = (topRight_y - bottomLeft_y)/(topRight_x - bottomLeft_x)
	# 	theta = math.atan(tan_thetha)
	# else:
	# theta = (math.pi)/2
	# theta = theta - 0.7853981633974488
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

	aruco_msg.x = cX
	aruco_msg.y = cY
	aruco_msg.theta = yaw
	aruco_publisher.publish(aruco_msg)	
	cv2.imshow("window",image)
	k=cv2.waitKey(100)
	print(cX, cY, yaw)
		############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Use OpenCV to find ARUCO MARKER from the IMAGE
	#	-> You are allowed to use any other library for ARUCO detection, 
	#        but the code should be strictly written by your team and
	#	   your code should take image & publish coordinates on the topics as specified only.  
	#	-> Use basic high-school geometry of "TRAPEZOIDAL SHAPES" to find accurate marker coordinates & orientation :)
	#	-> Observe the accuracy of aruco detection & handle every possible corner cases to get maximum scores !

	############################################
      
def main():
	rospy.init_node('aruco_feedback_node')  
	rospy.Subscriber('overhead_cam/image_raw', Image, callback)
	rospy.spin()
  
if __name__ == '__main__':
  main()
