import cv2
import time
import robot
img = cv2.imread('a.jpg')
cv2.imshow('img_a',img)
time.sleep(3)
cv2.destroyAllWindows()
robot.basis.lcmd('python b.py')

