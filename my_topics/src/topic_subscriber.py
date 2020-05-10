#!/usr/bin/env python
# Shebang, shows executable, interpereter python

# import rospy and std_msgs, found also in Package.xml
import rospy
from std_msgs.msg import Int32


#callback function that prints to terminal
def callback(msg):  
  print(msg.data)   

#Initialize subscriber
rospy.init_node('topic_subscriber') 

#Subscribe to topic 'counter' of type Int32, perform callback (print counter)
sub = rospy.Subscriber('counter', Int32, callback) 

rospy.spin() # wait for node to be shut down
