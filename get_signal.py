#!/usr/bin/env python

# This node is responsible for reading and printing the signal sent from the Raspberry Pi

PKG = 'hub_pr2' # this package name
import roslib; roslib.load_manifest(PKG)

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("%s",data.data)
    
def get_signal():

    rospy.init_node('get_signal', anonymous=True)

    rospy.Subscriber("hub_sensor", String, callback)
    
    rospy.spin()
        
if __name__ == '__main__':
    get_signal()
