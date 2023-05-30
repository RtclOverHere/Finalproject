#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def go_home(req):
    rospy.loginfo("Going to home.")
    time.sleep(2)
    rospy.loginfo("Arrived")
    return EmptyResponse()

def go_kitchen(req):
    rospy.loginfo("Going to kitchen.")
    time.sleep(2)
    rospy.loginfo("Arrived")
    return EmptyResponse()

def stop(req):
    rospy.loginfo("Stop!")
    return EmptyResponse()

def trigger_server():
    rospy.init_node('trigger_server')

    print("am ready to do something.")
    
    s1 = rospy.Service('/go_to_kitchen', Empty, go_kitchen)
    

    s2 = rospy.Service('/stop', Empty, stop)
   

    s3 = rospy.Service('/go_home', Empty, go_home)
    
    
    rospy.spin()

if __name__ == "__main__":
    trigger_server()