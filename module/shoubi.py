import math
import os
import time
'''
def target(xt,yt):
	l = 10.4 * 2
	zt = math.sqrt(xt*xt+yt*yt)
	zt = float(zt)
	cos = zt / l 
	xt = float(xt)
	tan = xt / yt
	#print(cos)
	#print ("\n")
	#print(tan)
	theta_a = math.acos(cos)
	theta_b = math.atan(tan)
	value1 = theta_b - theta_a 
	value2 = theta_b + theta_a
	value3 = 1.5708 - theta_a - theta_b
	catch(0,value1,value2,value3,0)
'''
	
def arm_init():
	os.system("gnome-terminal -e 'bash -c \"roslaunch my_dynamixel_tutorials arm.launch; exec bash\"'")
	time.sleep(2.5)

def catch(a,b,c,d,e):

	a = str(a)
	a1 = "gnome-terminal -e 'bash -c \"rostopic pub -1 /waist_controller/command std_msgs/Float64 -- "
	a2 = "; exec bash\"'"
	a3 = a1 + a + a2
	os.system(a3)

	b = str(b)
	b1 = "gnome-terminal -e 'bash -c \"rostopic pub -1 /shoulder_controller/command std_msgs/Float64 -- "
	b2 = "; exec bash\"'"
	b3 = b1 + b + b2
	os.system(b3)

	c = str(c)
	c1 = "gnome-terminal -e 'bash -c \"rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- "
	c2 = "; exec bash\"'"
	c3 = c1 + c + c2
	os.system(c3)

	d = str(d)
	d1 = "gnome-terminal -e 'bash -c \"rostopic pub -1 /wrist_controller/command std_msgs/Float64 -- "
	d2 = "; exec bash\"'"
	d3 = d1 + d + d2
	os.system(d3)

	e = str(e)
	e1 = "gnome-terminal -e 'bash -c \"rostopic pub -1 /hand_controller/command std_msgs/Float64 -- "
	e2 = "; exec bash\"'"
	e3 = e1 + e + e2
	os.system(e3)

def shenshouda():

	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /shoulder_controller/command std_msgs/Float64 -- -2.0; exec bash\"'")	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- 1.7; exec bash\"'")	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /wrist_controller/command std_msgs/Float64 -- -1.0; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /hand_controller/command std_msgs/Float64 -- -0.2; exec bash\"'")	
	
	time.sleep(8)
	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /hand_controller/command std_msgs/Float64 -- 0.7; exec bash\"'")	
	
def shenshouxiao():

	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /shoulder_controller/command std_msgs/Float64 -- -2.0; exec bash\"'")	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- 2.2; exec bash\"'")	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /wrist_controller/command std_msgs/Float64 -- -1.7; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /hand_controller/command std_msgs/Float64 -- -0.2; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /wrast_controller/command std_msgs/Float64 -- 0.0; exec bash\"'")	
		
	time.sleep(8)
	
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /hand_controller/command std_msgs/Float64 -- 0.7; exec bash\"'")	
	
def shouhui():

	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- -0.2; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /shoulder_controller/command std_msgs/Float64 -- -0.5; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /wrist_controller/command std_msgs/Float64 -- 0.0; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- 0.8; exec bash\"'")
	
