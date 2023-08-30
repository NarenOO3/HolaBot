#!/usr/bin/env python3

from ftplib import error_reply
from pickle import TRUE

from numpy import rate
import rospy

# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Twist
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry

# for finding sin() cos() 
from math import pow, atan2, sqrt, pi, sin, cos

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from tf.transformations import euler_from_quaternion

from geometry_msgs.msg import PoseArray


hola_x = 0
hola_y = 0
hola_theta = 0
roll = 0
pitch = 0
x_d = 0
y_d = 0
theta_d = 0
x_goals =[]
y_goals =[]
theta_goals =[]

def task1_goals_Cb(msg):
	global x_goals, y_goals, theta_goals
	
	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)
		
		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion (orientation_list)[2]
		theta_goals.append(theta_goal)
	# print(x_goals, y_goals)

def odometryCb(msg):
	global hola_x, hola_y,roll,pitch,hola_theta
	# Write your code to take the msg and update the three variables
	orientation_hola_bot = msg.pose.pose.orientation
	hola_x = msg.pose.pose.position.x # from echo we got the position and orientation
	hola_y = msg.pose.pose.position.y 
	orientation_list = [orientation_hola_bot.x, orientation_hola_bot.y, orientation_hola_bot.z,orientation_hola_bot.w]
	(roll,pitch,hola_theta) = euler_from_quaternion(orientation_list)
	# print("X:",round(hola_x,4)," Y:",round(hola_y,4) ," yaw:",round(hola_theta,4))

def main():
	# Initialze Node
	# We'll leave this for you to figure out the syntax for 
	# initialising node named "controller"
	rospy.init_node("controller",anonymous=True)
	# Initialze Publisher and Subscriber
	# We'll leave this for you to figure out the syntax for
	# initialising publisher and subscriber of cmd_vel and odom respectively
	pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
	rospy.Subscriber("/odom",Odometry,odometryCb)
	rospy.Subscriber('task1_goals', PoseArray, task1_goals_Cb)
	# Declare a Twist message
	vel = Twist()
	# Initialise the required variables to 0
	# <This is explained below>
	
	# For maintaining control loop rate.
	rate = rospy.Rate(100)

	# Initialise variables that may be needed for the control loop
	# For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
	# and also Kp values for the P Controller
	# global x_d, y_d, theta_d
	# # x_d = 0
	# # y_d = 0
	# theta_d = 3.14
	global Kp , x_d, y_d, theta_d
	Kp = 1.5
	i=0
	# Control Loop goes here
	while not rospy.is_shutdown():
		# Find error (in x, y and theta) in global frame

		# the /odom topic is giving pose of the robot in global frame
		# the desired pose is declared above and defined by you in global frame
		# therefore calculate error in global frame

		# (Calculate error in body frame)
		# But for Controller outputs robot velocity in robot_body frame, 
		# i.e. velocity are define is in x, y of the robot frame, 
		# Notice: the direction of z axis says the same in global and body frame
		# therefore the errors will have have to be calculated in body frame.
		# 
		# This is probably the crux of Task 1, figure this out and rest should be fine.

		# Finally implement a P controller 
		# to react to the error with velocities in x, y and theta.
		# vel.linear.x = Kp*(sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)))
		print(hola_x,hola_y,hola_theta)
		if(len(x_goals)!=0):
			
			if(i < 5):
				move_hola_bot(x_goals[i],y_goals[i],theta_goals[i])
				i = i + 1
		# 
		# 	i =i +1
		# vel.angular.z = (Kp+4.5)*(atan2(y_d - hola_y, x_d - hola_x) - hola_theta)
		# Safety Check
		# make sure the velocities are within a range.
		# for now since we are in a simulator and we are not dealing with actual physical limits on the system 
		# we may get away with skipping this step. But it will be very necessary in the long run.

		# vel.linear.x = vel_x
		# vel.linear.y = vel_y
		# vel.angular.z = vel_z

		# pub.publish(vel)
		rate.sleep()

def move_hola_bot(x_d,y_d,theta_d):
	print("******inside move fucntion*******")
	print(x_d, y_d, theta_d)
	vel  = Twist()
	pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
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

	while((sqrt(pow((x_d - hola_x), 2) + pow((y_d - hola_y), 2)) >= 0.01) or (abs(theta_d - hola_theta)>= 0.01)) :
		vel.linear.x = (Kp*(x_d - (hola_x)))*cos(hola_theta) + (Kp*(y_d - (hola_y)))*sin(hola_theta)
		vel.linear.y = -(Kp*(x_d - (hola_x)))*sin(hola_theta) + (Kp*(y_d - (hola_y)))*cos(hola_theta)
		vel.angular.z =(2.5)*(theta_d - hola_theta)
		pub.publish(vel)
	vel.linear.x = 0
	vel.linear.y = 0
	vel.angular.z =0
	pub.publish(vel)
	rospy.sleep(1)
	error_x = x_d - hola_x
	error_y = y_d - hola_y
	error_theta = theta_d - hola_theta
	print("X:",round(error_x,4)," Y:",round(error_y,4) ," yaw:",round(error_theta,4))

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
