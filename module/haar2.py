
import camera
import take_photo
import os
import basis
import move
import haar


camera.camera_init()
move.move_init()
basis.lcmd('python turn_left.py')

while (1):
	take_photo.take_photo('/home/mustar/new/module/people')
	os.system('python haar.py')

 
 
