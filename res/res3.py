import move_res as move
import path
import speech
import basis


import time
import os
import rospy
from std_msgs.msg import String

def go_back():
	bar_pose = basis.read_txt('bar_pose')
	if bar_pose == 1:
		turn_time = 5.5
	if bar_pose == 0:
		turn_time = 4.5
	basis.lcmd('python turn_left.py')
	time.sleep(turn_time)
	os.system('rosnode kill /turn_left')

	basis.lcmd('python laser2.py')
	time.sleep(5)
	basis.lcmd('python goforward.py')

	while (1) :
		helloFile_read = open('laser_front.txt')
		i = helloFile_read.read()
		helloFile_read.close()
		print(i)
		if i != 'inf':
			try:
				i =eval(i)
			except:
				pass
			#print(i)
			#print(type(i))
			if i < 0.7:
				print ('1')
				os.system('rosnode kill /goforward')
				break

def listener():
	rospy.init_node('res1', anonymous=False)
	rospy.Subscriber('/recognizer/output', String, callback)
	rospy.spin()
	
def callback(data):
	rospy.loginfo('I heard %s' % data.data)
	#lista = r.basis.separate(data.data)
	if ( 'tea' == data.data ):
		speech.speak('i heard that you want the tea')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the tea')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'orange juice' == data.data ):
		speech.speak('i heard that you want the orange juice')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the orange juice')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'pepsi' == data.data ):
		speech.speak('i heard that you want the pepsi')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the pepsi')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'instant noodle' == data.data ):
		speech.speak('i heard that you want the instant noodle')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the instant noodle')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'baked bean' == data.data ):
		speech.speak('i heard that you want the baked bean')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the baked bean')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'tuna' == data.data ):
		speech.speak('i heard that you want the tuna')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the tuna')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'nutella' == data.data ):
		speech.speak('i heard that you want the nutella')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the nutella')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'jelly' == data.data ):
		speech.speak('i heard that you want the jelly')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the jelly')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	if ( 'pringles' == data.data ):
		speech.speak('i heard that you want the pringles')
		#move.moveto(0,0,0)
		go_back()
		speech.speak('the customer wants the pringles')
		basis.lcmd('python res4.py')
		os.system('rosnode kill /res1')
		
	
	

speech.hear('res2')
speech.speak('what would you like?')
listener()
	
	
