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
		print ('1')
		
	elif ( data.data == 'bedroom'):
		print ('2')
	elif (data.data == 'living room'):
		print ('3')



os.system("gnome-terminal -e 'bash -c \"roslaunch rbx1_speech task1_location.launch; exec bash\"'")
time.sleep(2)
os.system("rosrun sound_play say.py \"please tell me where i should go\"")
listener()








#if __name__ == '__main__':
#    listener()

