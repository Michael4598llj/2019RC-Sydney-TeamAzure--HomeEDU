import wave
import path 
import move
import camera
import take_photo
import speech
import basis
import os
import time
import shoubi as arm


move.move_init()
arm.arm_init()
speech.speak_init()
move.moveto_init()
#basis.lcmd('roslaunch /home/mustar/catkin_ws/src/ros_astra_launch/launch/astra_top2.launch ')
#time.sleep(3)
'''
basis.lcmd('roslaunch rplidar_ros rplidar.launch')
time.sleep(2)

while(1):
	take_photo.take_photo('wave')
	if wave.wave('wave') == 1:
		break

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

speech.speak('what can i do for you')

os.system('python final2.py')'''
