import robot as r 
from aip import AipBodyAnalysis
import os

r.move.move_init()
r.camera.camera_init()

APP_ID = '16534838'
API_KEY = 'AurtnvQq5UbnMac4zhSbW1Tu'
SECRET_KEY = 'GmU14UlkS8QRGpxQ09AYVxbLtyKmHx9d'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)



def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def body():
	image = get_file_content('example.jpg')
	result1 = client.bodyAnalysis(image)
	try:
		result2 = result1['person_info']
	except:
		pass
	#result31 = result2[1]
	for result3 in result2:
		result4 = result3['body_parts']
		result5 = result4['nose']
		result6 = result5['y']
		result7 = result4['left_wrist']
		result8 = result7['y']
		result9 = result4['right_wrist']
		result0 = result9['y']
		if ((result8 < result6) or (result0 < result6)) and (result8 != 0) and (result0 != 0):
			#print('yes')
			os.system("python goforward.py")
		#else:
			#print('no')
	#print(result81)
	
	
while(1):
	r.take_photo.take_photo('example')
	body()
