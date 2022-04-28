#!/usr/bi/env python
#-*-coding: utf-8 -*-

import rospy
import smach
import smach_ros

class Foo(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome1','outcome2'],
                                   input_keys = ['foo_counter_in'],
                                   output_keys= ['foo_counter_out'])

    def execute(self, userdata):
        rospy.loginfo('Executing state: Foo')
            if userdata.foo_counter_in < 3:
                userdata.foo_counter_out = userdata.foo_counter_in + 1
                return 'outcome1'
            else:
                return 'outcome2'

class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome1'],
                                   input_keys=['bar_counter_in'])

    def execute(self, userdata):
        rospy.loginfo('Executing state: Bar')
        rospy.loginfo('Counter = %f'%userdata.bar_counter_in)
        return 'outcome1'

def main():
    sm = smach.StateMachine(outcomes=['outcome4'])
    sm.userdata.sm_counter = 0

    with sm:
        smach.StateMachine.add('Foo',
                                Foo(),
                                transitions={'outcome1':'Bar',
                                             'outcome2':'outcome4'},
                                remapping={'foo_counter_in': 'sm_counter',
                                           'foo_counter_out':'sm_counter'})
        smach.StateMachime,add('Bar',
                                Bar(),
                                transitions={'outcome1':'Foo'},
                                remapping={'bar_counter_in':'sm_counter'})

    outcome = sm.execute()
    rospy.spin()

if __name__ == '__main__':
    #　ノード（sm_4）を作成
    rospy.init_node('sm_4')
    main()
