#import path 
import robot as r

def turn_left():
       r.basis.lcmd("python turn_left.py")
#       r.time.sleep(2.4)
       r.time.sleep(1.3)
       r.os.system("rosnode kill /turn_left")
def turn_right():
       r.basis.lcmd("python turn_right.py")
#       r.time.sleep(2.4)
       r.time.sleep(1.3)
       r.os.system("rosnode kill /turn_right")
       

