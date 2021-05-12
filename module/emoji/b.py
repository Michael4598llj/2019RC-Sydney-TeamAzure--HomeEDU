import cv2
import time
import robot
img = cv2.imread('b.jpg')
cv2.imshow('img_b',img)
time.sleep(3)
cv2.destroyAllWindows()
robot.basis.lcmd('python c.py')
