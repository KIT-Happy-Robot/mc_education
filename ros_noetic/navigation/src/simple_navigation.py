#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------
# Title: 目的地に向かうだけのNavigation
# Author: Yusuke Kanazawa
# Date: 03/31
# Memo: 途中で異レギュラーな物体があっても避けません
#--------------------------------------------

import rospy
import rosparam
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# ゴールの生成
def setGoal(location_param):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = location_param[0]
    goal.target_pose.pose.position.y = location_param[1]
    goal.target_pose.pose.orientation.z = location_param[2]
    goal.target_pose.pose.orientation.w = location_param[3]
    return goal


def main():
    # ゴールのパラメータを取得
    location_dict = rosparam.get_param('/navigation/location_dict')
    location = location_dict['BinA']
    print("get location = " + str(location))

    # アクションクライアントを生成
    action_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # アクションサーバが起動するまで待つ
    print('waiting for server')
    action_client.wait_for_server()

    # ゴールを生成してアクションサーバにgoalを送信
    goal = setGoal(location)
    print('send goal')
    action_client.send_goal(goal)
    print('During navigation ...')

    # Navigationの状態を取得して状況に応じて結果を出力
    while not rospy.is_shutdown():
        state = action_client.get_state()
        rospy.sleep(0.2)
        if state == 3:
            rospy.loginfo('Success!!')
            break
        elif state == 4:
            rospy.loginfo('Failed')
            break
        else:
            pass


if __name__ == '__main__':
    rospy.init_node('simple_navigation')
    main()
