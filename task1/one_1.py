import path
import move
import time
import os

move.move_init()
os.system("gnome-terminal -e 'bash -c \"rosrun sound_play soundplay_node.py; exec bash\"'")
time.sleep(2)
os.system("rosrun sound_play say.py \"lets begin\"")
time.sleep(10)
#os.system("gnome-terminal -e 'bash -c \"roslaunch opencv_apps face_detection.launch image:=/camera_02/rgb/image_raw; exec bash\"'")
#time.sleep(5.5)
os.system("gnome-terminal -e 'bash -c \"python turn.py; exec bash\"'")
time.sleep(2.9)
os.system("rosnode kill  /turn")
#os.system("gnome-terminal -e 'bash -c \"python goforward.py; exec bash\"'")
os.system('python one_2.py')
