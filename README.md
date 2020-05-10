# my-ros-repos
ROS repository for ME477 project submission.
Eric Smith

For Dr. Rico Picone

# ROS Packages: my_topics; my_services; my_actions

	my_topics

		topic publisher/subscriber

			The topic publisher initializes a node which advertises a counter, that can be subscribed to by the topic subscriber, which will print out the counter value. 

		message publisher/subscriber

			The message publisher/subscriber functions in the same way as the topic publisher/subscriber with the exception that it publishes a custom message type containing real and imaginary numbers.

	my_services

		service server/client

			The service server initializes a node which can count the number of words in a string separated by white space. The service client sends a string to the server from the command line input, and requests the number of words back. The client the prints the number of words as an output.

	my_actions

		simple action server/client

			The server performs actions asynchronously with the client. In this case, the client requests a timer action performed by the server, the server counts to the appropriate time for completion and sends back the results.

		fancy action server/client

			This server/client pair functions the same as the prior one, with the exception that the server sends feedback to the client during the performance of the action as an update status.

# Requirements

	ros distro: melodic
	ros version: 1.14.4
	python version: 2.7.17


# Installation and configuration

	These packages should be installed into the src folder of a working ROS workspace.


# Getting Started

	Prior to running any launch files: 

		The packages should be built and sources with the following commands from within the workspace root directory:

			catkin_make

			source devel/setup.bash

	Running a launch file:

		Running a launch file requires using the command:

			roslaunch <package> <file.launch>

		In the case of the service.launch file, extra arguments are passed via input:="Your Words Here", as such:

			roslaunch my_services service.launch input:="Your Words Here"

# Usage

	To Run Any Launchers contained within this repository:


	my_topics topic publisher/subscriber

		Enter in the command line:

	----	roslaunch my_topics topic.launch

				This enables a counter publisher, and the subscriber will output the counter numbers counting up.


	my_topics message publisher/subscriber

		Enter in the command line:

	----	roslaunch my_topics message.launch

				This enables a message publisher, and the subscriber will output the messages of real and imaginary numbers.


	my_services wordcount client/server

		Enter in the command line:

	----	roslaunch my_services service.launch input:="Hello World Sweet World"
		
				This enables a server which will count the number of words in an input argument string, and send the number of words back to the client for display.

				Use any other combination of words within the quotations you wish.
				service_client.py has been altered from the original Robotics Book Codeto cut off sys.argv at char "_", Logging name inputs were being accepted from sys.argv.
			
				Sometimes error(EBADF, 'Bad file descriptor') shows up, sometimes not, functionality still exists.


	my_actions simple timer

		Enter in the command line:

	----	roslaunch my_actions simple_action.launch

				This enables an action server which waits until the goal timer has elapsed and then send goal completion to the client. The client will report completion to the user interface.
		

	my_actions fancy timer

		Enter in the command line:

	----	roslaunch my_actions fancy_action.launch

				This enables an action server which waits until the goal timer sent by the client has elapsed and then sends goal completion to the client. During operation, the server sends status updates to the client. The client reports all status updates and completion to the user via the user interface.
