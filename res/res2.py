import move_res as move
import os
import time
import wave
import path
import turn
import take_photo
import camera
import speech
#import laser2
import basis
#import turn_any as t

#camera.camera_init()
move.move_init()
#move.moveto_init()

bar_pose = basis.read_txt('bar_pose')
basis.lcmd('python turn_right.py')
time.sleep(1)
os.system('rosnode kill /turn_right')

while(1):

	basis.lcmd('python turn_left.py')
	time.sleep(1)
	os.system('rosnode kill /turn_left')
	#t.turn_any(-60)
	take_photo.take_photo('1')
	if wave.wave('1') == 1:
		break
	basis.lcmd('python turn_left.py')
	time.sleep(1)
	os.system('rosnode kill /turn_left')
	#t.turn_any(-60)
	take_photo.take_photo('1')
	if wave.wave('1') == 1:
		break
		
	basis.lcmd('python turn_right.py')
	time.sleep(1)
	os.system('rosnode kill /turn_right')
	take_photo.take_photo('1')
	if wave.wave('1') == 1:
		break
	basis.lcmd('python turn_right.py')
	time.sleep(1)
	os.system('rosnode kill /turn_right')
	take_photo.take_photo('1')
	if wave.wave('1') == 1:
		break


#moveto
#baizhen 
speech.speak('i saw a call')


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
os.system('python res3.py')



