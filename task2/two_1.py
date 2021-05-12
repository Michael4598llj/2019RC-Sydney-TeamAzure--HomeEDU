#!/usr/bin/env python

import rospy
import path
#import arm
import move
import os
import time
import shoubi as arm
import speech
import basis
from std_msgs.msg import String

sumx = 0

def listener():
	rospy.init_node('listener', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
 	rospy.spin()

def callback(data):
	global sumx
	rospy.loginfo('I heard %s' % data.data)
	if(sumx == 0):
		if(data.data =="follow me"):
			sumx = 1
			speech.speak('i will follow you')
			#basis.lcmd('roslaunch navi_help.launch')
			move.follow2()
	if(sumx == 1):
		if("stop follow me" in data.data):
			speech.speak('ok,i arrived the car.')
			os.system("rosnode kill  /turtlebot_follower")
			os.system("rosnode kill  /recognizer")
			arm.arm_init()
			time.sleep(5)
			arm.tiqu()
			basis.lcmd('python two_2.py')
			os.system("rosnode kill  /listener")

#arm.arm_init()
speech.hear('voice_task1_commands')
speech.speak_init()
#arm.arm_init()
listener()
