#!/usr/bin/env python
#-*-coding: utf-8 -*-
#---------------------------------------------------------
# Desc: The node for basic smaching practis.
# Date: Mar 8, 2022
# Author: Hiroto Washio
#---------------------------------------------------------
import rospy
import smach

#　適当な状態を定義
class State1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done','exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('Executing state: State1')
        rospy.sleep(2.0)
        if self.counter < 3:
            self.counter += 1
            # outcome（結果）としてdoneを返す
            return 'done'
        else:
            # カウンターの値が3以上になったらexitを返す
            return 'exit'

class State2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['done'])

    def execute(self, userdata):
        rospy.loginfo('Executing state STATE2')
        rospy.sleep(2.0)
        return 'done'

def main():
    # ノード（sm_1）を作成
    rospy.init_node('sm_1')
    # 先頭の状態機械を作成
    sm_top = smach.StateMachine(outcomes=['succeeded'])
    # sm_topの内容
    with sm_top:
        smach.StateMachine.add('STATE1', State1(), transitions={'done':'STATE2', 'exit':'succeeded'})
        smach.StateMachine.add('STATE2', State2(), transitions={'done':'STATE1'})

    outcome = sm_top.execute()

if __name__ == '__main__':
    main()
