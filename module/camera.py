import os
import time
#import gender as g
#import take_photo as t
def camera_init():
	os.system("gnome-terminal -e 'bash -c \"roslaunch astra_launch multi_astra.launch; exec bash\"'")
	#gnome-terminal -e "bash -c 'roslaunch astra_launch multi_astra.launch; exec bash'"
	time.sleep(5)


#camera_init()
#t.take_photo('1')
#g.gender_detection('1')



