import path
import move
import basis
import os
import time

#move.move_init()
basis.lcmd('python turn_left.py')
time.sleep(5.5)
os.system('rosnode kill /turn_left')

