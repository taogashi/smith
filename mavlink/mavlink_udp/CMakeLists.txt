cmake_minimum_required(VERSION 2.8.3)
project(mavlink_udp)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
  mavlink_common
)

add_message_files(
   FILES
   MAV_RAW_DATA.msg
   	SENSOR_OFFSETS.msg
	SET_MAG_OFFSETS.msg
	MEMINFO.msg
	AP_ADC.msg
	DIGICAM_CONFIGURE.msg
	DIGICAM_CONTROL.msg
	MOUNT_CONFIGURE.msg
	MOUNT_CONTROL.msg
	MOUNT_STATUS.msg
	FENCE_POINT.msg
	FENCE_FETCH_POINT.msg
	FENCE_STATUS.msg
	AHRS.msg
	SIMSTATE.msg
	HWSTATUS.msg
	RADIO.msg
	LIMITS_STATUS.msg
	WIND.msg
	DATA16.msg
	DATA32.msg
	DATA64.msg
	DATA96.msg
	E_MAV_MOUNT_MODE.msg
	E_MAV_CMD.msg
	E_FENCE_ACTION.msg
	E_FENCE_BREACH.msg
	E_LIMITS_STATE.msg
	E_LIMIT_MODULE.msg

)
generate_messages(
    DEPENDENCIES
    std_msgs
    mavlink_common

)
catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS roscpp message_runtime
)

include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

    add_executable(mavlink_udp_node src/mavlink_udp.cpp)
    target_link_libraries(mavlink_udp_node ${catkin_LIBRARIES})
    add_dependencies(mavlink_udp_node  mavlink_udp_generate_messages_cpp)
    
install(TARGETS mavlink_udp_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


install(DIRECTORY include/${PROJECT_NAME}/
    DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
    FILES_MATCHING PATTERN "*.h"
    PATTERN ".svn" EXCLUDE
)
