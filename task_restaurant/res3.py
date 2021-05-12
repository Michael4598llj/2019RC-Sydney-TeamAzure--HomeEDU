#!/usr/bin/env python

import rospy
import os
import path
import basis

x_res = 0
y_res = 0

from geometry_msgs.msg import PoseWithCovarianceStamped

def listener():
    rospy.init_node('listener_pose', anonymous=False)
    rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
    rospy.spin()

def callback(data):
	global x_res
	global y_res 
	x_res = data.pose.pose.position.x
	y_res = data.pose.pose.position.y
	basis.write_txt('/home/mustar/new/module/moveto_txt/x_res',x_res)
	basis.write_txt('/home/mustar/new/module/moveto_txt/y_res',y_res)
	rospy.loginfo('I heard x= %s' % data.pose.pose.position.x)
	rospy.loginfo('I heard y= %s' % data.pose.pose.position.y)
	os.system("rosnode kill /listener_pose")



listener()
os.system('python res4.py')
