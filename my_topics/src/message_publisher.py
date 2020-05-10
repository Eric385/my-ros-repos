#!/usr/bin/env python
#Shebang, executable, interpereter Python

# Imports complex message type
import rospy
from my_topics.msg import Complex 
from random import random 

# Initialize Message Publisher node, called complex, and rate of message output
rospy.init_node('message_publisher') 

pub = rospy.Publisher(    
  'complex',             
  Complex,                
  queue_size=3            
)

rate = rospy.Rate(2) 


#While loop of message output, 
#generates random numbers for real and complex output, 
#publishes message and waits for rate
while not rospy.is_shutdown(): 
  msg = Complex()           
  msg.real = random()       
  msg.imaginary = random()  

  pub.publish(msg)  
  rate.sleep()      