import haar
import path 
import move
import camera
import take_photo
import basis
import speech
import os
import time
import shoubi as arm
#import decet


speech.speak('ok i will take takeaway for you')
#door
#os.system("gnome-terminal -e 'bash -c \"python turn.py; exec bash\"'")
#time.sleep(2.9)
#os.system("rosnode kill  /turn")

move.moveto(-1.96,3.83,0)
'''

while(1):
	take_photo.take_photo('people')
	if haar.haar() == 1:
		speech.speak('i have found you')
		break
	else:
		speech.speak('i can not see you, please face to me')
'''


speech.speak('please put the takeaway in my hand')


#1
arm.shenshouda()
arm.shouhui()
speech.speak('thank you')


x_final = basis.read_txt('x_final')
y_final = basis.read_txt('y_final')

#move.moveto(x_final,y_final,0)

#2
arm.shenshouxiao()
#

speech.speak('here you are')


