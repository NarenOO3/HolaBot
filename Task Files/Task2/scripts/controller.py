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


################### IMPORT MODULES #######################

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

################## GLOBAL VARIABLES ######################

PI = 3.14
hola_x = 0
hola_y = 0
hola_theta = 0
roll = 0
pitch = 0
x_d = 0
y_d = 0
theta_d = 0

x_goals = [350,50,50,350,250]
y_goals = [350,350,50,50,250]
theta_goals = [0.785, 2.335, -2.335, -0.785, 0]

# right_wheel_pub = None
# left_wheel_pub = None
# front_wheel_pub = None


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
# def task2_goals_Cb(msg):
# 	global x_goals, y_goals, theta_goals
# 	x_goals.clear()
# 	y_goals.clear()
# 	theta_goals.clear()

# 	for waypoint_pose in msg.poses:
# 		x_goals.append(waypoint_pose.position.x)
# 		y_goals.append(waypoint_pose.position.y)

# 		orientation_q = waypoint_pose.orientation
# 		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
# 		theta_goal = euler_from_quaternion (orientation_list)[2]
# 		theta_goals.append(theta_goal)

def aruco_feedback_Cb(msg): 
	############ ADD YOUR CODE HERE ############
	print()
	global hola_x, hola_y,hola_theta
	# INSTRUCTIONS & HELP : 
	#	-> Receive & store the feedback / coordinates found by aruco detection logic.
	#	-> This feedback plays the same role as the 'Odometry' did in the previous task.
	hola_x = msg.x
	hola_y = msg.y
	hola_theta = msg.theta
	hola_x = ((hola_x - 249.5)/190)
	hola_y = (249.5 - hola_y)/190

	############################################
def inverse_kinematics(v_x, v_y, v_z):
	############ ADD YOUR CODE HERE ############
	msg = Wrench()
	body_vel = ([v_x],[v_y],[v_z])
	hola_matrix = ([0.6666667,0,1.906614],[-0.33333333,0.57736721,1.906614],[-0.33333333,-0.57736721,1.906614])
	wheel_vel = np.dot(hola_matrix,body_vel)
	# print(wheel_vel)
    #V_est = (wheel_vel[1]+wheel_vel[2])/2
    #wheel_vel[1] = wheel_vel[2] = V_est
    #wheel_vel[0] = -2*V_est
	msg.force.x = 1000*float(wheel_vel[0]) 
    #msg.force.x = 333.333335
	# msg.force.x = 0 
	# print("A:",msg.force.x)
	front_wheel_pub.publish(msg)
	msg.force.x = 1000*float(wheel_vel[2])
    #msg.force.x = -166.666665
	# msg.force.x = -300 
	# print("B:",msg.force.x)
	right_wheel_pub.publish(msg)
	msg.force.x = 1000*float(wheel_vel[1])
    #msg.force.x = -166.666665
	# msg.force.x = 300
	# print("C:",msg.force.x)
	left_wheel_pub.publish(msg)

def move_hola_bot(x_d, y_d, theta_d):
	print()
	global hola_x, hola_y, hola_theta
	print("******inside move fucntion*******")

	print(hola_x,hola_y,hola_theta)

	print("hi...")
	x_d = ((x_d - 249.5)/190)
	y_d = (249.5 -y_d)/190
	print(x_d, y_d, theta_d)	
	# while(sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)) >= 0.01):
	# 	vel.linear.x = (Kp*(x_d - (hola_x)))*cos(hola_theta) + (Kp*(y_d - (hola_y)))*sin(hola_theta)
	# 	vel.linear.y = -(Kp*(x_d - (hola_x)))*sin(hola_theta) + (Kp*(y_d - (hola_y)))*cos(hola_theta)
	# 	pub.publish(vel)
	# vel.linear.x = 0
	# vel.linear.y = 0
	# pub.publish(vel)
	# while(abs(theta_d - hola_theta)>= 0.01):
	# 	# vel.angular.z =(Kp+2.5)*(atan2(y_d - hola_y, x_d - hola_x) - hola_theta)
	# 	vel.angular.z =(5)*(theta_d - hola_theta)
	# 	pub.publish(vel)
	Kp = 0.5
	# while((sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)) >= 0.01) or (abs(theta_d - hola_theta)>= 0.1)) :
	# 	vel.linear.x = (Kp*(x_d - (hola_x)))*cos(hola_theta) + (Kp*(y_d - (hola_y)))*sin(hola_theta)
	# 	vel.linear.y = -(Kp*(x_d - (hola_x)))*sin(hola_theta) + (Kp*(y_d - (hola_y)))*cos(hola_theta)
	# 	vel.angular.z =(2)*(theta_d - hola_theta)
	# 	pub.publish(vel)
	while((sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)) >= 0.01) or abs(theta_d - hola_theta)>= 0.05) :
		print("********inside vel_while********")
		v_x = (Kp*(x_d - (hola_x)))*cos(hola_theta) + (Kp*(y_d - (hola_y)))*sin(hola_theta)		
		v_y = -(Kp*(x_d - (hola_x)))*sin(hola_theta) + (Kp*(y_d - (hola_y)))*cos(hola_theta)
		v_z =-1*(0.5)*(theta_d - hola_theta)
		inverse_kinematics(v_x,v_y,v_z/100)
	inverse_kinematics(0,0,0)
	# while(abs(theta_d - hola_theta)>= 0.01):
	# 	print("*****inside theta_vel*******")

	# while(() :
	# 	print("****abs theta error******")
		
	# 	print( abs(theta_d - hola_theta))
	# inverse_kinematics(0,0,0)
	rospy.sleep(1)
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
	global right_wheel_pub, left_wheel_pub, front_wheel_pub
	rospy.init_node('controller_node')
	
	signal.signal(signal.SIGINT, signal_handler)

	# NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	#	Use the below given topics to generate motion for the robot.
	right_wheel_pub = rospy.Publisher('/right_wheel_force', Wrench, queue_size=10)
	front_wheel_pub = rospy.Publisher('/front_wheel_force', Wrench, queue_size=10)
	left_wheel_pub = rospy.Publisher('/left_wheel_force', Wrench, queue_size=10)

	rospy.Subscriber('detected_aruco',Pose2D,aruco_feedback_Cb)
	# rospy.Subscriber('task2_goals',PoseArray,task2_goals_Cb)
	rate = rospy.Rate(100)
	vel = Twist()

	############ ADD YOUR CODE HERE ############

	# INSTRUCTIONS & HELP : 
	#	-> Make use of the logic you have developed in previous task to go-to-goal.
	#	-> Extend your logic to handle the feedback that is in terms of pixels.
	#	-> Tune your controller accordingly.
	# 	-> In this task you have to further implement (Inverse Kinematics!)
	#      find three omni-wheel velocities (v1, v2, v3) = left/right/center_wheel_force (assumption to simplify)
	#      given velocity of the chassis (Vx, Vy, W)
	#	   

	i=0	
	while not rospy.is_shutdown():
		
		# Calculate Error from feedback

		# Change the frame by using Rotation Matrix (If you find it required)

		# Calculate the required velocity of bot for the next iteration(s)
		# inverse_kinematics(1,1,1.57)
		# inverse_kinematics(1,-1,3.14)
		# inverse_kinematics(-1,1,-1.57)
		# inverse_kinematics(0,0,0)
		if(len(x_goals)!=0):
			
			if(i < 5):
				move_hola_bot(x_goals[i],y_goals[i],theta_goals[i])
				i = i + 1
		# Find the required force vectors for individual wheels from it.(Inverse Kinematics)

		# Apply appropriate force vectors

		# Modify the condition to Switch to Next goal (given position in pixels instead of meters)

		rate.sleep()

    ############################################

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass

