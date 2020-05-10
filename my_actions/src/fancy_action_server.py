#! /usr/bin/env python

# Import time: normally use sleep for proper timing
# Import my_actions for timer operation
import rospy

import time
import actionlib
from my_actions.msg import TimerAction, TimerResult, TimerFeedback

# Define timer funcitonality
def do_timer(goal):

    #Count time start
    start_time = time.time()
    update_count = 0

    #Time too long exit condition
    if goal.time_to_wait.to_sec() > 60.0:
        result = TimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        server.set_aborted(result, "Timer aborted due to too-long wait")
        return

    #Normal Timing Operations, sends feedback message of time elapsed, time remaining
    while (time.time() - start_time) < goal.time_to_wait.to_sec():
        if server.is_preempt_requested():
            result = TimerResult()
            result.time_elapsed = rospy.Duration.from_sec(
                    time.time() - start_time)
            result.updates_sent = update_count
            server.set_preempted(result, "Timer preempted")
            return
        feedback = TimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(
                time.time() - start_time)
        feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)
        update_count += 1
        time.sleep(1.0)

    #When timer completed, give results, time elapsed, completion message    
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    server.set_succeeded(result, "Timer completed successfully")

#Action code, initialize timer server
#Do all do_timer code
#Setup node
rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()