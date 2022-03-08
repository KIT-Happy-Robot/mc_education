#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------
# Title: 目的地に向かうだけのNavigation
# Author: Yusuke Kanazawa
# Date: 03/08
# Memo:
#--------------------------------------------

import rospy
import rosparam
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# rosparamで取得した値からsetGoal()でゴールの生成
def setGoal(location_param):
    print("pose= <" + str(location_param) + ">")
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = location_param[0]
    goal.target_pose.pose.position.y = location_param[1]
    goal.target_pose.pose.orientation.z = location_param[2]
    goal.target_pose.pose.orientation.w = location_param[3]
    return goal

def main():
    # ゴールのパラメータをrosparamで取得
    location_dict = rosparam.get_param('/navigation_sim/location_dict')
    location = location_dict['table']
    print "get location = " + str(location)

    # アクションクライアントを生成
    action_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # アクションサーバが起動するまで待つ
    print 'waiting for server'
    action_client.wait_for_server()

    # ゴールを生成してアクションサーバにgoalを送信
    goal = setGoal(location)
    action_client.send_goal(goal)
    # 結果が返ってくるまで待つ
    action_client.wait_for_result()

if __name__ == '__main__':
    rospy.init_node('simple_navigation')
    main()
