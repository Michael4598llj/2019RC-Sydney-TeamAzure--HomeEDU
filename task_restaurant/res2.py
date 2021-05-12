import move_res as move
import os
import time
import wave
import path
import turn
import take_photo
import camera
import speech
import laser2
import basis

camera.camera_init()

suma = 0
i = 0
while(i<3)and(suma == 0):
	i = i + 1
	if i == 1:
		basis.lcmd('turn_left')
		time.sleep('1')
		os.system('rosnode kill /turn_left')
	else :
		basis.lcmd('turn_right')
		time.sleep('1')
		os.system('rosnode kill /turn_right')
	take_photo.take_photo(str(i))
	if wave.wave(str(i)) == 1:
		suma = 1
#moveto
#baizhen 
basis.lcmd('python goforward.py')
while (laser2.laser_front < 1.5):
	os.system('rosnode kill /goforward')
os.system('python res3.py')



