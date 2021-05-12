from aip import AipBodyAnalysis
import os

APP_ID = '16534838'
API_KEY = 'AurtnvQq5UbnMac4zhSbW1Tu'
SECRET_KEY = 'GmU14UlkS8QRGpxQ09AYVxbLtyKmHx9d'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)



def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def body(name):
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
		result6 = result5['y']
		result7 = result4['left_wrist']
		result8 = result7['y']
		result9 = result4['right_wrist']
		result0 = result9['y']
		if ((result8 < result6) or (result0 < result6)) and (result8 != 0) and (result0 != 0):
			return 1
		else :
			return 0
		

