#! /usr/bin/python3

import rospy
from std_msgs.msg import Float64
from time import sleep

rospy.init_node('tiltzbot')

publisher = rospy.Publisher('/tilt_angle', Float64, queue_size=1)

lookingDown = True

while not rospy.is_shutdown():
	msg = Float64()
	msg.data=-30 if lookingDown else 10
	publisher.publish(msg)
	rospy.loginfo('Message Published')
	lookingDown = not lookingDown
	sleep(4.20)
