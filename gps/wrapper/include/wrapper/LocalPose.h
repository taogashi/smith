#ifndef _LOCALPOSE_H_
#define _LOCALPOSE_H_

#include "misc_msgs/Poseinfo.h"

//@ Tsinghua Main Building
#define LATLON_TO_CM 1.113195
#define LOCAL_LON_TO_CM 0.853947569

class LocalPose {
    public:
        LocalPose();
        misc_msgs::Poseinfo wrapToLatLon();
        float x,y,h;
        float vx,vy,vz;
};

#endif
