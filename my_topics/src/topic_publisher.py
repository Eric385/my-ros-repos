#!/usr/bin/env python
#Cannot edit shebang line. Shows file is executable and interpereted by python
#uses rospy and std_msgs (for ints) as linked in Package.xml
import rospy
from std_msgs.msg import Int32 

# All the setup, initialize node, register with roscore, set rate
rospy.init_node( 
  'topic_publisher' 
)
pub = rospy.Publisher( 
  'counter', 
  Int32, 
  queue_size=5 
)
rate = rospy.Rate(2) 

# While loop, while not exited w/ ctrl-c, publish incrementing counter
count = 0
while not rospy.is_shutdown(): 
    pub.publish(count) 
    count += 1 
    rate.sleep() 