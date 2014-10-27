#!/usr/bin/env python

import rospy
import serial
from sensor_msgs.msg import Range

#===============================================================================
#  Edit the serial port parameters to adapt to your device (3DR radio receiver)
#===============================================================================
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)

#===============================================================================
# ROS Node to receive data from sonar rangefinder 
#===============================================================================
def node():
    rospy.init_node('sonar_node', anonymous=True)
    range_msg = Range()
    range_msg.radiation_type = range_msg.ULTRASOUND
    pub = rospy.Publisher("/msg_from_sonar", Range, queue_size=10)
    r = rospy.Rate(20)
    rospy.loginfo("reading sonar range")
    while not rospy.is_shutdown():
        #trigger sonar to measure
        cmd = chr(0x22)+chr(0x00)+chr(0x00)+chr(0x22)
        ser.write(cmd)
        data = ser.read(4)
        if len(data)==4 and (ord(data[0])+ord(data[1])+ord(data[2]))&255 == ord(data[3]):
            sonar_range = ord(data[1])*256+ord(data[2])
            range_msg.range = sonar_range
            pub.publish(range_msg)
            rospy.loginfo("distance : %d", sonar_range)
        else:
            rospy.logwarn("sonar error!")
        r.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException: 
        pass
