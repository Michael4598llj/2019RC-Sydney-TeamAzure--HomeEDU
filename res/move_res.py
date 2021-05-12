import os
import time
import change

def move_init():
	os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_bringup minimal.launch; exec bash\"'")
	time.sleep(3)
def moveto_init():
	#os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_navigation rplidar_amcl_demo.launch; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"export TURTLEBOT_MAP_FILE=~/new/task_restaurant/map/empty_map.yaml\nroslaunch turtlebot_navigation amcl_demo.launch; exec bash\"'")
	time.sleep(3)
	os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_rviz_launchers view_navigation.launch --screen; exec bash\"'")
	time.sleep(4)
def moveto(x,y,w):
	a = str(x) 
	helloFile1 = open("/home/mustar/new/module/moveto_txt/x.txt","w")
	helloFile1.write(a)
	helloFile1.close()
	b = str(y) 
	helloFile2 = open("/home/mustar/new/module/moveto_txt/y.txt","w")
	helloFile2.write(b)
	helloFile2.close()
	c = str(w) 
	helloFile3 = open("/home/mustar/new/module/moveto_txt/w.txt","w")
	helloFile3.write(c)
	helloFile3.close()
	os.system("roslaunch rchomeedu_navigation navigation.launch")
	#os.system("gnome-terminal -e 'bash -c \"roslaunch rchomeedu_navigation navigation.launch; exec bash\"'")
def follow():
	os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_follower follower.launch; exec bash\"'")
def follow2():
	os.system("gnome-terminal -e 'bash -c \"roslaunch navi_help.launch; exec bash\"'")
