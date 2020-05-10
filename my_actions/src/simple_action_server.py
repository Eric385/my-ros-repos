#! /usr/bin/env python


# import time for timing, normally use sleep
# import timer action/goal/result from my_actions timer.
import rospy

import time
import actionlib
from my_actions.msg import TimerAction, TimerGoal, TimerResult

# Define timer
# start time based on time 
#calculate time elapsed, time remaining
def do_timer(goal):
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0
    server.set_succeeded(result)

# initialize server node
#continuously run until ctrl-c
rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()