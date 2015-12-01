#!/usr/bin/env python

import rospy
import rosnode
from geometry_msgs.msg import Twist
from phoebe.drive import Drive

import RPi.GPIO as GPIO

class Node:
    def __init__(self):
        self.driver = Drive()
        rospy.init_node("phoebe", anonymous=True)
        rospy.Subscriber("cmd_vel", Twist, self.didReceiveTwist)

        rospy.spin()

    def didReceiveTwist(self, twist):
        self.driver.steer(twist.twist.angular.y)
        self.driver.accelerate(twist.twist.linear.z)

if __name__ == '__main__':
    n = Node()
    GPIO.cleanup()
