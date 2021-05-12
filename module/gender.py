# -*- coding: utf-8 -*-

import base64
import sys
import base64
#import take_photo as t

from aip import AipFace

def gender_detection(name):
	'''新建aipface的配置'''
	''' 你的 app id ak sk '''
	AppId = '14255146'
	ApiKey = 'UoyrHmKFG3nGPL5HmDiGo80G'
	SecretKey = 'HUo1z36aDc1UxOwuS8d7Vxldh4GsQg8l'
	client = AipFace(AppId, ApiKey, SecretKey)


	photo_name = name + '.jpg'
	with open(photo_name,"rb") as f:
		base64_data = base64.b64encode(f.read())    
	image64 = base64_data
	image_type = "BASE64"

	options = {}
	options["face_field"] = "gender"
	options["max_face_num"] = 10


	result = client.detect(image64, image_type, options)


	stra = str(result)
	sum2 = stra.count("female")
	sum1 = stra.count("male") -sum2
	listsum = [sum1,sum2]
	return listsum

#t.take_photo('1')
#gender_detection('1')




