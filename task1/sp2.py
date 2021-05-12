import os
import time
import path
import basis as b
'''
helloFile = open("sp.txt")
fileContent = helloFile.read()
helloFile.close()
fileContent = eval(fileContent)
'''
fileContent = b.read_txt("sp")
if fileContent < 100:
	time.sleep(3)
	os.system("rosrun sound_play say.py \"next question.\"")
	time.sleep(2)
	os.system("gnome-terminal -e 'python sp1.1.py'")
else:
	os.system("rm -f sp.txt")

