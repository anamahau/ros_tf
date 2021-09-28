#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped, Transform, Quaternion, Point
import numpy as np 
import pickle

if __name__ == '__main__':
    rospy.init_node('tf_loader')

    file_name = raw_input("Please wire the path for the pickle file:")

    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    infile.close()

    for transform in stored_poses.values():
        rospy.loginfo(transform)