cmake_minimum_required(VERSION 2.8.3)
project(mavlink_udpdevice)

find_package(catkin REQUIRED COMPONENTS
	mavlink_ardupilotmega
	roscpp
	rospy
)

catkin_package(

)

include_directories(
	${catkin_INCLUDE_DIRS}
)
