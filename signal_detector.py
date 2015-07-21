#!/usr/bin/env python
#----------------------------------------Importing Libraries-------------------------------------------------
PKG = 'hub_pr2'
import roslib; roslib.load_manifest(PKG)
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String

#----------------------------------------Setup the pins----------------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def hub_sensor_detector():
    pub = rospy.Publisher('hub_sensor', String)
    rospy.init_node('signal_detector', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        left_top = GPIO.input(16)
        left_bottom_left = GPIO.input(20)
        left_bottom_right = GPIO.input(12)
        right_top = GPIO.input(5)
        right_bottom_left = GPIO.input(26)
        right_bottom_right = GPIO.input(13)
        str = "Detecting Signal from Board, Pi1"
        if left_top==False or left_bottom_left==False or left_bottom_right==False or right_top==False or right_bottom_left==False or right_bottom_right==False:
                if left_top == False:
                        print("Left Top Circuit")
                        pub.publish("Red LED board, left circuit, LED on top detected signal")
                if left_bottom_left == False:
                        print("Left Bottom Left Circuit")
                        pub.publish("Red LED board, left circuit, LED lower left detected signal")
                if left_bottom_right == False:
                        print("Left Bottom Right Circuit")
                        pub.publish("Red LED board, left circuit, LED lower right detected signal")
                if right_top==False:
                        print("Right Top Circuit")
                        pub.publish("Red LED board, right circuit, LED on top detected signal")
                if right_bottom_left==False:
                        print("Right Bottom Left Circuit")
                        pub.publish("Red LED board, right circuit, LED lower left detected signal")
                if right_bottom_right==False:
                        print("Right Bottom Right Circuit")
                        pub.publish("Red LED board, right circuit, LED lower right detected signal")
        else:
                pub.publish(str)
                print("Detecting")
        r.sleep()

if __name__ == '__main__':
    try:
        hub_sensor_detector()
    except rospy.ROSInterruptException: pass
	