#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (KB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[hb_1260 ]
# Author List:		[ Abhinav Srinivas,Annamalai,Narenthiran,Varun ]
# Filename:			task_0.py
# Functions:
# 			[callback,main,move_turtle ]
# Nodes:		Publishing node: /turtle1/cmd_vel
#                       Subscribing node: /turtle1/pose


####################### IMPORT MODULES #######################
import sys
import traceback
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math 
##############################################################

def callback(data):

    pose = Pose()
    pose = data
    pose.y = round(pose.y,4)
    pose.theta = round(pose.theta,4)
    move_turtle(pose.y,pose.theta)
    return

def main():   
   
    global pub
    rospy.init_node("Draw_D")
    rospy.loginfo("Turtle: I am going to Draw D !!")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown() :
        rospy.Subscriber("/turtle1/pose",Pose,callback)
        rate.sleep()


################# ADD GLOBAL VARIABLES HERE #################


##############################################################


################# ADD UTILITY FUNCTIONS HERE #################
def move_turtle(v,w):
    msg = Twist()
    if -0.01 <= w < 3.15  :
        msg.linear.x = 1.432
        msg.angular.z = (math.pi)/2
        print("My Turtlebot is: Moving in circle !!!")
        print(w)
        # radius check
        #if 1.54 <= w <= 1.58 :
        #    print(u)
    if w > 3.15 or -3.2 < w < -1.585:
        msg.angular.z = math.pi/2
        msg.linear.x  = 0
        print("My Turtlebot is : Rotating !!!")
        print(w)
    if  -1.585 <= w < -1.56 and 5.45 < v < 7.6 :
        
        msg.linear.x = 1
        msg.angular.z = 0
        print("My Turtlebot is : Moving Straight !!!")
        print(w)
    if v <= 5.45 :
        msg.linear.x = 0
        msg.angular.z = 0
        print("Done !!!") 
    pub.publish(msg)
    return
        
##############################################################


######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS PART #########
if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        main()

    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")
