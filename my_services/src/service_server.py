#!/usr/bin/env python

#Import the service file to count the words and respond the number of words output
import rospy
from my_services.srv import WordCount, WordCountResponse

#Define function to count the number of words in a sentence based on spaces
def count_words(request):
  return len(request.words.split())


# Initilize server that counts the number of words in an input from a client
# Creates service called word_count that client can use
# Runs continously
rospy.init_node('service_server')

service = rospy.Service( 
  'word_count', 
  WordCount,    
  count_words   
)

rospy.spin()