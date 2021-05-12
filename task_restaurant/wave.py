from aip import AipBodyAnalysis
import os
import numpy as np
import cv2

APP_ID = '16534838'
API_KEY = 'AurtnvQq5UbnMac4zhSbW1Tu'
SECRET_KEY = 'GmU14UlkS8QRGpxQ09AYVxbLtyKmHx9d'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)



def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def wave(name):
	sumbody = 0
	name = name + ".jpg"
	image = get_file_content(name)
	result1 = client.bodyAnalysis(image)
	try:
		result2 = result1['person_info']
	except:
		pass
	for result3 in result2:
		result4 = result3['body_parts']
		result5 = result4['nose']
		result6 = 0
		rwx3 = int(result5['x'])
		result6 = int(result5['y'])
		result7 = result4['left_wrist']
		lwx1 = result7['x']
		result8 = result7['y']
		result9 = result4['right_wrist']
		rwx2 = result9['x']
		result0 = result9['y']
        #lwx1 = result7['x']
        #rwx2 = result9['x']
        #rwx3 = result5['x']
		if ((result8 < result6) or (result0 < result6)) and (result8 != 0) and (result0 != 0):		
			img = cv2.imread(name)
			cv2.circle(img, (rwx3,result6), 30, (0,0,255),2) 
			cv2.imwrite('body2.jpg',img)
			sumbody = 1
	return sumbody
	
wave('hand')
		
