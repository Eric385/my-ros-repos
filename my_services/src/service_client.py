#!/usr/bin/env python

#Inports service ability for word counting
import rospy
from my_services.srv import WordCount
import sys


#initilialize client that sends sentence words to server
#server counts words, send back number of words
#Prints to screen results
rospy.init_node('service_client')

rospy.wait_for_service('word_count') 
word_counter = rospy.ServiceProxy( 
  'word_count', 
  WordCount     
)

# Edited to allow for roslaunch functionality, log file sysargs were being passed in
words_unsorted = ' '.join(sys.argv[1:]) 

# Inclusion of the key _ will tell client when user input sys srgs are done, others are tossed
words = words_unsorted.split("_")[0]
word_count = word_counter(words) 

print(words+'--> has '+str(word_count.count)+' words')