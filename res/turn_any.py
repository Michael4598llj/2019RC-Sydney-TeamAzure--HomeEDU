
import os
import time
import rospy
from geometry_msgs.msg import Twist


#os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_bringup minimal.launch; exec bash\"'")
#time.sleep(3)

def turn_any(degree):
	if degree<0:
		degree = -degree
		count_i = int(degree/3.6)
		# initiliaze
		rospy.init_node('turn_left', anonymous=False)
		
		cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
		 

		r = rospy.Rate(10);


		move_cmd = Twist()

		move_cmd.linear.x = 0.0
		move_cmd.angular.z = 0.8
		
		for count_i in range(0,count_i):
			cmd_vel.publish(move_cmd)
			r.sleep()
	else:
		count_i = int(degree/3.6)
		# initiliaze
		rospy.init_node('turn_right', anonymous=False)
		
		cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
		 

		r = rospy.Rate(10);


		move_cmd = Twist()

		move_cmd.linear.x = 0.0
		move_cmd.angular.z = -0.8
	

		for count_i in range(0,count_i):
			cmd_vel.publish(move_cmd)
			r.sleep()
