#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Smach template

import rospy
import smach

class State1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = [""])
        
    def execute(self, userdata):
        rospy.loginfo("Executing state: State1")

        
        return ''

class State2(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=[""],
                             input_keys=[""])
 
    def execute(self, userdata):
        print("Executing state : State2")
        
if __name__ == '__main__':
    rospy.init_node('<enter a node name>')
    rospy.loginfo('Start **<enter a node name>**')
    top_smach = smach.StateMachine(outcomes = [''])
    # way of 
    top_smach.userdata.example_userdata = 0
    with top_smach:
        smach.StateMachine.add('State1',
                                State1(),
                transitions = {'':''})
        smach.StateMachine.add('State2',
                                State2(),
                transitions = {'':''})

    outcome = top_smach.execute()

