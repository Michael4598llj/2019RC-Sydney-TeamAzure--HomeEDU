#!/usr/bin/env python

import rospy
import os
import path
import move
import basis

x_now = 0
y_now = 0

from geometry_msgs.msg import PoseWithCovarianceStamped

def listener():
    rospy.init_node('listener_pose', anonymous=False)
    rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
    rospy.spin()

def callback(data):
	global x_now 
	global y_now 
	x_now = data.pose.pose.position.x
	y_now = data.pose.pose.position.y
	basis.write_txt('/home/mustar/new/module/moveto_txt/x_final',x_now)
	basis.write_txt('/home/mustar/new/module/moveto_txt/y_final',y_now)
	rospy.loginfo('I heard x= %s' % data.pose.pose.position.x)
	rospy.loginfo('I heard y= %s' % data.pose.pose.position.y)
	os.system("rosnode kill /listener_pose")

listener()
os.system('python final3.py')

