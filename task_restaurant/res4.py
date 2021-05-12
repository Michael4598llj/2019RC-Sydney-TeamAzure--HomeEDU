import move_res as move
import path
import speech
import basis


import time
import os
import rospy
from std_msgs.msg import String


def listener():
	rospy.init_node('res1', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
	rospy.spin()
	
def callback(data):
	rospy.loginfo('I heard %s' % data.data)
	#lista = r.basis.separate(data.data)
	if ( 'tea' == data.data ):
		speech.speak('i heard that you want the tea')
		move.moveto(0,0,0)
		speech.speak('the customer wants the tea')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'orange juice' == data.data ):
		speech.speak('i heard that you want the orange juice')
		move.moveto(0,0,0)
		speech.speak('the customer wants the orange juice')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'pepsi' == data.data ):
		speech.speak('i heard that you want the pepsi')
		move.moveto(0,0,0)
		speech.speak('the customer wants the pepsi')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'instant noodle' == data.data ):
		speech.speak('i heard that you want the instant noodle')
		move.moveto(0,0,0)
		speech.speak('the customer wants the instant noodle')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'baked bean' == data.data ):
		speech.speak('i heard that you want the baked bean')
		move.moveto(0,0,0)
		speech.speak('the customer wants the baked bean')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'tuna' == data.data ):
		speech.speak('i heard that you want the tuna')
		move.moveto(0,0,0)
		speech.speak('the customer wants the tuna')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'nutella' == data.data ):
		speech.speak('i heard that you want the nutella')
		move.moveto(0,0,0)
		speech.speak('the customer wants the nutella')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'jelly' == data.data ):
		speech.speak('i heard that you want the jelly')
		move.moveto(0,0,0)
		speech.speak('the customer wants the jelly')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	if ( 'pringles' == data.data ):
		speech.speak('i heard that you want the pringles')
		move.moveto(0,0,0)
		speech.speak('the customer wants the pringles')
		#basis.lcmd('python res5.py')
		os.system('rosnode kill /res1')
		
	
	
speech.speak_init()
speech.speak('what would like?')
speech.hear('res2')
listener()
	
	
