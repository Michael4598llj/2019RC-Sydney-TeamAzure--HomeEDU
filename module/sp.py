import os
import time
import path
import basis as b

helloFile1 = open("sp.txt","w")
helloFile1.write("1")
helloFile1.close()

os.system("gnome-terminal -e 'bash -c \"roslaunch rbx1_speech voice_task2_commands.launch; exec bash\"'")
time.sleep(2)
os.system("gnome-terminal -e 'bash -c \"rosrun sound_play soundplay_node.py; exec bash\"'")
time.sleep(2)
#move.move_init()
os.system("rosrun sound_play say.py \"let's begin.\"")

os.system('python luyin.py')
os.system('python test.py')

os.system("python try.py")
