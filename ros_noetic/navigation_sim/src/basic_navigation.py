#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------
# Title: 実装できるレベルのNavigation
# Author: Yusuke Kanazawa
# Date: 03/10
# Memo: 途中で異レギュラーな物体があっても回避可能
#--------------------------------------------

import rospy
import rosparam
import actionlib
import sys
from std_msgs.msg import String
from std_srvs.srv import Empty
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class BasicNavigation():
    def __init__(self):
        # Action
        self.ac = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        # Service
        self.clear_costmap = rospy.ServiceProxy('/move_base/clear_costmaps', Empty)
        # Value
        self.location_dict = rosparam.get_param('/navigation_sim/location_dict')
        self.location_name = 'NULL'
        self.location_list = []

    def serchLocationName(self, name):
        if name in self.location_dict:
            self.location_name = name
            print(self.location_dict[self.location_name])
            return self.location_dict[self.location_name]
        else:
            rospy.logerr("<" + name + "> doesn't exist.")
            sys.exit('False')

    def setGoal(self, location_param):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = location_param[0]
        goal.target_pose.pose.position.y = location_param[1]
        goal.target_pose.pose.orientation.z = location_param[2]
        goal.target_pose.pose.orientation.w = location_param[3]
        return goal

    def execute(self, location_name):
        # set goal
        self.location_list = self.serchLocationName(location_name)
        goal = self.setGoal(self.location_list)
        # clearing costmap
        rospy.loginfo("Clearing costmap...")
        rospy.wait_for_service('move_base/clear_costmaps')
        self.clear_costmap()
        rospy.sleep(0.5)
        # start Navigation
        self.ac.wait_for_server()
        self.ac.send_goal(goal)
        rospy.loginfo('During navigation ...')
        while not rospy.is_shutdown():
            rospy.sleep(0.5)
            state = self.ac.get_state()
            if state == 3:
                rospy.loginfo('Navigation Success!!')
                return True
            elif state == 4:
                rospy.loginfo('Navigation Failed ...')
                return False
            else:
                pass


if __name__ == '__main__':
    rospy.init_node('simple_navigation')
    bn = BasicNavigation()
    result = bn.execute('table')
    print(result)
