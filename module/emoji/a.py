import cv2
import time
import robot
img_a = cv2.imread('a.jpg')
cv2.imshow('img_a',img_a)
time.sleep(3)
robot.basis.lcmd('python b.py')

