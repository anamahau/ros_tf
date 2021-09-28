#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped, Transform, Quaternion, Point
import numpy as np 
import pickle
import os
if __name__ == '__main__':
    rospy.init_node('tf_saver')

    saved_data = {} 

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)


    
    file_name = raw_input("Please wire the path for the pickle file:")

    file_dir = file_name[:file_name.find(file_name.split('/')[-1])]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    outfile = open(file_name,'wb')

    rospy.sleep(1)

    user_input = "input"
    while(user_input != ""):
        user_input = raw_input("Enter key where you want to save the position: ")
        frame = tf_buffer.lookup_transform(
            'world', 'frame_1', rospy.Time(0))
    
        saved_data[user_input] = frame

    pickle.dump(saved_data, outfile)