#!/usr/bin/env python

import rospy
import rosnode
from geometry_msgs.msg import Twist

import RPi.GPIO as GPIO

DUTY_CYCLE_HZ = 500

class Phoebe:
    def __init__(self):
        self.steering = GPIO.PWM(12, DUTY_CYCLE_HZ) # example pin output
        self.motor = GPIO.PWM(13, DUTY_CYCLE_HZ) # example pin output

        self.steering.start(50)
        self.motor.start(50)

        rospy.init_node("phoebe", anonymous=True)
        rospy.Subscriber("cmd_vel", Twist, self.didReceiveTwist)

        rospy.spin()

    def didReceiveTwist(self, twist):
        turn_normalized = (twist.twist.angular.y + 1) / 2.0
        forward_normalized = (twist.twist.linear.z + 1) / 2.0

        self.steering.ChangeDutyCycle(turn_normalized * 100)
        self.motor.ChangeDutyCycle(forward_normalized * 100)

if __name__ == '__main__':
    p = Phoebe()
    GPIO.cleanup()
