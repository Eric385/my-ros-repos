#!/usr/bin/env python

#Import complex type
import rospy
from my_topics.msg import Complex


#Print function for real and imaginary numbers input from message stream
def callback(msg):
    print 'Real:', msg.real           
    print 'Imaginary:', msg.imaginary 
    print                             


#Initialize message subscriber
#Subscribes to message topic complex
#Runs function to output results to screen
rospy.init_node('message_subscriber') 

sub = rospy.Subscriber( 
  'complex',            
  Complex,              
  callback              
)

rospy.spin() # keep node running until shut down