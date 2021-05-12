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


camera.camera_init()
#move.move_init()
#move.moveto_init()
speech.speak_init()
basis.lcmd('roslaunch rplidar_ros rplidar.launch')
time.sleep(2)

bar_sum = 0
if laser.laser_decet() == 1:
	bar_pose = 'right'
	bar_sum = 1
else:
	bar_pose = 'left'
	bar_sum = 0
bar =  'the bar is on my ' + bar_pose
speech.speak(bar)
basis.write_txt('bar_pose',bar_sum)


os.system('python res2.py')




