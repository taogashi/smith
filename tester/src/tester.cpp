#include "ros/ros.h"
#include "misc_msgs/Poseinfo.h"
#include "wrapper/LocalPose.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "tester");
    ros::NodeHandle nh;
    misc_msgs::Poseinfo info;
    LocalPose lp;
    info = lp.wrapToLatLon();

    ros::Rate loop_rate(10);

    while(ros::ok())
    {
        ROS_INFO("test OK!");
        ROS_INFO("lat : %d ", info.lat);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
