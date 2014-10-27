#include "wrapper/LocalPose.h"

LocalPose::LocalPose()
{
    x = 0.0;
    y = 0.0;
    h = 0.0;
    vx = 0.0;
    vy = 0.0;
    vz = 0.0;
}

misc_msgs::Poseinfo LocalPose::wrapToLatLon()
{
    misc_msgs::Poseinfo info;
    info.lon = 1163081360;
    info.lat = 400071056;
    info.lat += (int32_t)(x*100.0/LATLON_TO_CM);
    info.lon += (int32_t)(y*100.0/LOCAL_LON_TO_CM);
    info.alt = (int32_t)(h*100);
    info.pos_DOP = 3;
    info.v_north = vx;
    info.v_east = vy;
    info.v_down = vz;
    info.speed_DOP = 4;
    return info;
}
