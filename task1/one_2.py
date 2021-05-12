import path
import move
import speech as s
import time
import os
import basis as b

import camera
import gender as g
import take_photo as t


s.speak('cheese')
camera.camera_init()
t.take_photo('1')
result_list = g.gender_detection('1')
s.speak_init()
sum_pop = result_list[0]+result_list[1]
sum_pop = str(sum_pop)
male = str(result_list[0])
famale = str(result_list[1])
b.write_txt('sumpop',sum_pop)
b.write_txt('male',male)
b.write_txt('famale',famale)


s.speak('there are '+ sum_pop + ' persons')
s.speak( male + ' males and ' +famale +' famales')

os.system('python one_3.py')
