#!/usr/bin/env python
import rospy
import socket
from mavlink_ardupilotmega.msg import MAV_RAW_DATA

#define the udp socket
server_ip = ""
qgc_port = 0
locAddr=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def to_qgc_mav_raw_data_callback(message):
    global server_ip
    global qgc_port
    global locAddr
    rospy.loginfo("write to udp"+str(len(message.data))+"bytes")
#
    for i in range(0,len(message.data)):
        print "0x%x" %ord(message.data[i]),
    locAddr.sendto(message.data,(server_ip, qgc_port))

def node():
    global server_ip
    global qgc_port
    rospy.init_node("mavlink_qgc_node",anonymous=True)

#    if not rospy.has_param("/mav_raw_udp/server_ip"):
    if not rospy.has_param("~server_ip"):
        rospy.logwarn("no server ip spicified")
    else:
        server_ip = rospy.get_param("~server_ip")
        rospy.logwarn("%s", server_ip)

    if not rospy.has_param("~qgc_port"):
        rospy.logwarn("no port spicified")
    else:
        qgc_port = rospy.get_param("~qgc_port")
        rospy.logwarn("%d", qgc_port)

    pub=rospy.Publisher('/from_qgc_mav_raw_data',MAV_RAW_DATA,queue_size=10)
    rospy.Subscriber("/to_qgc_mav_raw_data",MAV_RAW_DATA,to_qgc_mav_raw_data_callback,queue_size=10)
    r=rospy.Rate(100)

    m=MAV_RAW_DATA()
    m.channel=0

    while not rospy.is_shutdown():
        
        m.data,ADDR=locAddr.recvfrom(255)
        rospy.loginfo(m.data)
        pub.publish(m)
        r.sleep()

if __name__=='__main__':
    try:
        node()
    except rospy.ROSInterruptException: pass
