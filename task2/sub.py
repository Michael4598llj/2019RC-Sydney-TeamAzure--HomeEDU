#!/usr/bin/env python

import rospy
#from std_msgs.msg import String
from sensor_msgs.msg import Image
import path
import basis
import cv2
import os
#import robot as r

face_haar = cv2.CascadeClassifier("/home/mustar/new/task2/haarcascade_frontalcatface.xml")
eye_haar = cv2.CascadeClassifier("/home/mustar/new/task2/haarcascade_eye.xml")


#opencv_apps/RotatedRectStamped


def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber('/camera_top/rgb/image_raw', Image, callback)
    rospy.spin()

def callback(data):
	#rospy.loginfo('I heard %s' % data)
	cam = data
	img = cam
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_haar.detectMultiScale(gray_img, 1.3, 5)
	for face_x,face_y,face_w,face_h in faces:
		cv2.rectangle(img, (face_x, face_y), (face_x+face_w, face_y+face_h), (0,255,0), 2)
		roi_gray_img = gray_img[face_y:face_y+face_h, face_x:face_x+face_w]
		roi_img = img[face_y:face_y+face_h, face_x:face_x+face_w]
		eyes = eye_haar.detectMultiScale(roi_gray_img, 1.3, 5)
		for eye_x,eye_y,eye_w,eye_h in eyes:
			cv2.rectangle(roi_img, (eye_x,eye_y), (eye_x+eye_w, eye_y+eye_h), (255,0,0), 2)
	cv2.imshow('img', img)
	key = cv2.waitKey(30) & 0xff
	if key == 27:
		os.system('rosnode kill /listener')
	


while(1):
	listener()
#if __name__ == '__main__':
#    listener()

