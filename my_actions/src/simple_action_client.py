#! /usr/bin/env python


#Import timer action actions
import rospy

import actionlib
from my_actions.msg import TimerAction, TimerGoal, TimerResult


#Start node
#wait for server
#set timer goal to 5 seconds
#get and print results
rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal)
client.wait_for_result()
print('Time elapsed: %f' % (client.get_result().time_elapsed.to_sec()))