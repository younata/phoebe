#!/usr/bin/env python

import rospy
import rosnode
import geometry_msgs
#from geometry_msgs.msg import Twist

def didReceiveTwist(twist):
    forward = twist.twist.linear.z
    turn = twist.twist.angular.y
    rospy.loginfo(rospy.get_caller_id() + "forward %f, turning %f" % (forward, turn))

def main():
    rospy.init_node("phoebe", anonymous=True)
    rospy.Subscriber("cmd_vel", geometry_msgs.msg.Twist, didReceiveTwist)

    rospy.spin()

if __name__ == '__main__':
    main()
