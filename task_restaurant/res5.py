import move_res as move
import path
import speech
import basis

import time
import os

x_res= basis.read_txt('/home/mustar/new/module/moveto_txt/x_res')
x_res= basis.read_txt('/home/mustar/new/module/moveto_txt/y_res')
move.moveto(x_res,y_res,0)
speech.speak('here you are')
time.sleep(4)
move.moveto(0,0,0)
os.system('python res2.py')
