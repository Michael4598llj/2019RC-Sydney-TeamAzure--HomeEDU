import move_res as move
import os
import time
import body
import path
import turn
import take_photo
import camera
import speech
import laser
import basis


#camera.camera_init()
move.move_init()
#move.moveto_init()
speech.speak_init()
basis.lcmd('roslaunch rplidar_ros rplidar.launch')
time.sleep(2)


if laser.laser_decet() == 1:
	bar_pose = 'right'
else:
	bar_pose = 'left'
bar =  'the bar is on my ' + bar_pose
speech.speak(bar)


os.system('python res2.py')




