import robot as r 

r.move.move_init()
r.camera.camera_init()
while(1):
	r.take_photo.take_photo('example')
	r.os.system('python body.py')
