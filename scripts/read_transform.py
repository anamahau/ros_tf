#! /usr/bin/env python

import rospy
import pickle
import tf2_ros
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = "transformation.txt"

    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    infile.close()

    #########################
    ##### STUDENT WRITES ####
    #########################

    tf_broad = tf2_ros.StaticTransformBroadcaster()

    # for key, el in stored_poses.items():
    #     #print(trans)
    #     tf_broad.sendTransform(el)

    tf_broad.sendTransform(stored_poses.values())

    #transformation = stored_poses['fransformacija']
    #print(transformation)

    #tf_broad.sendTransform([transformation])

    #########################
    rospy.spin()