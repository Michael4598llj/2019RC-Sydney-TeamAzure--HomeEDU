#!/usr/bin/env python

import rospy
#from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

import os

laser_decet = 0
#opencv_apps/RotatedRectStamped


def listener():
    rospy.init_node('listener_scan', anonymous=False)   
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

def callback(data):
	global laser_decet
	#rospy.loginfo('I heard %s' % data)
	#print(data)
	#os.system('rosnode kill /listener')
	count = int(data.scan_time / data.time_increment)
	for i in range(0,count):
		degree = (data.angle_min + data.angle_increment * i)*180/3.14
		print(degree,data.ranges[i])
	#print(data.ranges[89])
	#print(data.ranges[269])
	#print(data.ranges[0],count)
	if data.ranges[89] >  data.ranges[269] : #left is far
		laser_decet = 0 #right
	else  :
		laser_decet = 1
	os.system('rosnode kill listener_scan')

def laser_decet():
	listener()
	return laser_decet


