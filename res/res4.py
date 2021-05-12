import move_res as move
import path
import speech
import basis

import time
import os

#speech.speak_init()
def go_back():
	basis.lcmd('python turn_left.py')
	time.sleep(1.4)
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

time.sleep(5)
go_back()
speech.speak('here you are')
time.sleep(6)
go_back()


