#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Vector3

rospy.init_node('bumper_stop')

class BumperStop(object):
    def __init__(self):
        super(BumperStop, self).__init__()
        self.cmdPub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def run(self):
        r = rospy.Rate(10)
        i = 0
        while not rospy.is_shutdown():
            i += 1
            speed = 0.2 if i < 10 else 0
            velMsg = Twist(linear=Vector3(x = speed), angular=Vector3(z=0))
            self.cmdPub.publish(velMsg)
            r.sleep()


if __name__ == '__main__':
    BumperStop().run()
