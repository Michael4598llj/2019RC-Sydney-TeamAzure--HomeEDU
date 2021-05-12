import os
import time
def hear(launch_name):
	launch_name = "gnome-terminal -e \"bash -c 'roslaunch rbx1_speech " + launch_name + ".launch; exec bash'\""
	#print(launch_name)
	os.system(launch_name)
	#os.system("gnome-terminal -e 'bash -c \"roslaunch rbx1_speech voice_task2_commands.launch; exec bash\"'")
	#gnome-terminal -e "bash -c 'roslaunch rbx1_speech voice_task2_commands.launch; exec bash'"
	time.sleep(2)
def speak_init():
	os.system("gnome-terminal -e 'bash -c \"rosrun sound_play soundplay_node.py; exec bash\"'")
	time.sleep(2)
def speak(content):
	system_content = "rosrun sound_play say.py \"" + content + "\""
	#print(system_content)
	os.system(system_content)
	#os.system("rosrun sound_play say.py \"let's begin.\"")
#hear("rbx1_speech voice_task2_commands")
#os.system("gnome-terminal -e 'bash -c \"roscore; exec bash\"'")
#time.sleep(2)
#speak_init()
#speak("let's begin.")
#os.system("rosrun sound_play say.py \"let's begin.\"")
