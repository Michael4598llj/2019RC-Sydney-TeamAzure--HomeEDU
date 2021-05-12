#!/usr/bin/env python
import time
import os
import path
import shoubi as arm
import rospy
import basis
import move

from std_msgs.msg import String

x_pose = 0
y_pose = 0



def listener():
	rospy.init_node('listener2', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
	rospy.spin()

def callback(data):
	rospy.loginfo('I heard %s' % data.data)
	#lista = basis.separate(data.data)
	if (data.data == 'kitchen'  ):
		os.system("rosnode kill /recognizer")
		basis.lcmd('python two_3.py')
		#
		move.moveto(-4.39,-3.02,0.0)
		#
		arm.fangxia()
		x_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/x_pose.txt')
		y_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/y_pose.txt')
		move.moveto(x_pose,y_pose,0.0)
		os.system("rosnode kill  /listener2")
	elif ( data.data == 'bedroom'):
		os.system("rosnode kill /recognizer")
		#
		basis.lcmd('python two_3.py')
		#
		move.moveto(-1.26,-4.43,0.0)
		arm.fangxia()
		x_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/x_pose.txt')
		y_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/y_pose.txt')
		move.moveto(x_pose,y_pose,0.0)
		os.system("rosnode kill  /listener2")
	elif (data.data == 'living room'):
		os.system("rosnode kill /recognizer")
		basis.lcmd('python two_3.py')
		#
		move.moveto(0.726,1.05,0.0)
		#
		arm.fangxia()
		x_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/x_pose.txt')
		y_pose = basis.read_txt('/home/mustar/new/module/moveto_txt/y_pose.txt')
		move.moveto(x_pose,y_pose,0.0)
		os.system("rosnode kill  /listener2")



os.system("gnome-terminal -e 'bash -c \"roslaunch rbx1_speech task1_location.launch; exec bash\"'")
time.sleep(2)
os.system("rosrun sound_play say.py \"please tell me where i should go\"")
listener()








#if __name__ == '__main__':
#    listener()

