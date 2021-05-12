from aip import AipBodyAnalysis
import path
import move
import camera
import take_photo
import time
import speech 
import take_photo
import os
import turn


APP_ID = '16669481'
API_KEY = 'ceVI2dXNUGuU6LRHWpUfFGzR'
SECRET_KEY = 'QoddetzthEglNeG9UIdA4Z33yvcDZe0U'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def body():
	i = 0
	sumi = 0
	while(sumi==0):
		i = i + 1
		turn.turn_left()
		take_photo.take_photo('people')
		try :
			image = get_file_content('people.jpg')
			client.bodyAttr(image);
			options = {}
			options["type"] = "gender"
			result = client.bodyAttr(image, options)
			result = result['person_num']
			if result > 0 :
				speech.speak("i have found you ")
				speech.speak("follow me")
				sumi = 1
		except :
			pass

camera.camera_init()
move.move_init()
os.system("gnome-terminal -e 'bash -c \"rosrun sound_play soundplay_node.py; exec bash\"'")
time.sleep(2)	
body()
	
