#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy


def home():
    try:
        trigger = rospy.ServiceProxy('/go_home', Empty)
        print("Robo go to home.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def kitchen():
    try:
        trigger = rospy.ServiceProxy('/go_to_kitchen', Empty)
        print("Robo go to kitchen.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def stop():
    try:
        trigger = rospy.ServiceProxy('/stop', Empty)
        print("Stop!")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    kitchen()
    stop()
    home()
    stop()