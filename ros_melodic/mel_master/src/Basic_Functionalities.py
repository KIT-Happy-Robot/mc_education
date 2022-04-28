#!/usr/bin/env python 
# -*- coding utf-8 -*-
#--------------------------------------------------
#Title: 新入生教育最終内容(ロボットの基本的な動作)
#Data: 2022/3/28
#Author: Shunsuke Wada
#Memo: RCJ2018のBasic Functionalitiesを実施
#--------------------------------------------------
import rospy
import smach
import smach_ros
import actionlib
from happymimi_recognition_msg.srv import RecognitionList, RcognitionFind
from enter_room.srv import EnterRoom
from happymimi_msgs.srv import StrTrg
from happymimi_navigation.srv import NaviLocation
from happymimi_manipulation_msg.srv import RecognitionToGrasping, RecognitionToGraspingRequest
from happymimi_voice_msgs.srv import *
from std_msgs.msg import String, Float64
import roslib
import sys 
file_path = roslib.packages.get_pkg_dir('happymimi_telop') + '/src/'
from base_control import BaseControl 

class EnterRoom(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['pass'])
        #Service 
        self.enter_srv = rospy.ServiceProxy('enter_room_server', EnterRoom)
        self.tts_srv = rospy.ServiceProxy('/tts', TTS)

    def execute(self, userdata):
        rospy.loginfo('Start Enter Room')
        self.tts_srv('Start Basic Functionalities')
        #enter_room_serverを使って Enter Room
        self.enter_srv(distance = 0.8, velocity = 0.2)
        return 'pass'

class MoveAndPick(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            outcomes = ['success','failed'],
                            input_keys = ['object_name_in']
                            output_keys = ['object_name_out'])
        #Publisher
        self.head_pub = rospy.Publisher('/servo/head', Float64, queue_size = 1)
        #Service 
        self.grasp_srv = rospy.ServiceProxy('/recognition_to_grasping', RecognitionToGrasping)
        self.arm_srv = rospy.ServiceProxy('/servo/arm', StrTrg)
        self.navi_srv = rospy.ServiceProxy('navi_location_server' NaviLocation)
        self.recog_srv = rospy.ServiceProxy('/rcognition/list', RecognitionList)
        self.bc = BaseControl()
        self.recog_result = []

    def execute(self, userdata):
        #ナビゲーションのロケーション名
        self.navi_srv('storage')
        #オブジェクト名の格納
        sm_name = userdata.object_name_in
        rospy.sleep(0.5)
        #value
        grasp_count = 0
        rospy.loginfo('Pick')
        #首を25°を下げる
        self.head_pub.publish(25.0)
        rospy.sleep(2.0)
        #認識結果 既知
        self.recog_result = self.recog_srv('cup', 'left')
        print self.recog_result.object_list
        #物体把持の結果
        grasp_result = self.grasp_srv(RecognitionToGraspingRequest(target_name = 'any')).result
        #未知だったとき
        if not self.recog_result.object_list:
            pass
        else:
            sm_name = 'cup'
            userdata.object_name_out = sm_name
        print sm_name
        rospy.sleep(0.5)
        #機体を90°回転
        self.bc.rotateAngle(90, 0.4)
        #物体把持できたとき
        if self.grasp_result == True:
            return 'success'
        else:
            return 'failed'

class MoveAndPlace(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            outcomes = ['completed']
                            input_keys = ['object_name_in'])
        #Publisher
        self.current_pub = rospy.Publisher('/current_location', String, queue_size = 1 )
        #Service
        self.navi_srv = rospy.ServiceProxy('/navi_location_server', NaviLocation)
        self.arm_srv = rospy.ServiceProxy('/servo/arm', StrTrg)
        self.recognition_srv = rospy.ServiceProxy('/recognition/list', RecognitionList)
        self.bc = BaseControl()

    def execute(self, userdata):
        print userdata.object_name_in
        #既知
        if userdata.object_name_in in == 'NULL':
            self.navi_srv('Tall table') #ナビゲーションのロケーション名
            self.current_pub.publish('table') #置く場所
            self.arm_srv('place') #置く
            self.bc.rotateAngle(180, 0.4) #機体を180°回転
        #未知
        else:
            self.navi_srv('box1') #ナビゲーションのロケーション名
            self.current_pub.publish('couch') #置く場所
            self.arm_srv('place') #置く
            self.bc.rotateAngle(180, 0.4) #機体を180°回転
        return 'completed'

class AvoidThat(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['to_WDYS'])
        #Service
        self.navi_srv = rospy.ServiceProxy('/navi_location_server', NaviLocation)

    def execute(self):
        self.navi_srv('operator')
        rospy.sleep(0.5)
        return 'to_WDYS'

class PersonSerach(smach.State):
    def __init__(self, outcomes = ['found']):
        #Publisher
        self.head_pub = rospy.Publisher('/servo/head', Float64, queue_size = 1 )
        #Service
        self.tts_srv = rospy.ServiceProxy('/tts', TTS)
        self.find_srv = = rospy.ServiceProxy('/recognition/find', RecognitionFind)

    def execute(self, userdata):
        rospy.loginfo('serach')
        #頭上げる
        self.head_pub.publish(-10)
        rospy.sleep(1.0)
        #サーチ 結果
        self.find_result = self.find_srv(RecognitionFindRequest(target_name = 'person')).result
        #人を発見できたとき
        if self.find_result == True:
            self.tts_srv('I found the Ouestioner')
        #人を発見できなかったとき
        else:
            self.tts_srv('Pleace come in front of me')
            rospy.sleep(8.0)
            self.tts_srv('Thank You')
        return 'found'

class QuestionResponse(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            outcomes = ['completed']
                            input_keys = ['success_count_in', 'start_time_in']
                            output_keys = ['success_count_out', 'start_time'])
        #Service
        self.tts_srv = rospy.ServiceProxy('/tts', StrTrg)
        self.wdys_self_srv = rospy.ServiceProxy('/bf/conversation_srvserver', WhatDisYouSay)
        self.yesno_srv = rospy.ServiceProxy('/yes_no', YesNo)
        #value
        self.cnt = 0
        self.bc = BaseControl()

        def execute(self, userdata):
            rospy.loginfo('Are you ready?')
            self.tts_srv('Are you ready?')
            #返答がYesのとき
            if self.yesno_srv().result == True:
                for i in range(3): #3回質問させる
                    self.tts_srv('Talk to ne')
                    result = self.wdys_srv().result #レスポンス 結果
                    if result == True: #成功
                        cnt += 1
            #機体を90°回転させる
            self.bc.rotateAngle(90, 0.4)
            return 'completed'

class ExitRoom(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['to_finish')]
        #Service
        self.navi_srv = rospy.ServiceProxy('/navi_location_server', NaviLocation)
        self.tts_srv = rospy.ServiceProxy('/tts', StrTrg)

    def execute(self, userdata):
        rospy.loginfo('exit')
        self.tts_srv('Go to the entrance')
        #ナビゲーションのロケーション名
        self.navi_srv('entrance')
        rospy.sleep(0.5)
        self.tts_srv('Finish Basic Functionalities')
        self.tts_srv('Thank you very mach')
        return 'to_finish'

if __name__ == '__main__':
    rospy.init_node('Basic_Functionalities')
    sm_top = smach.StateMachine(outcomes = ['finish_sm'])
    #value
    sm_top.userdata.cmd_count = 1
    sm_top.userdata.sm_name = 'NULL'
    
    with sm_top:
        smach.StateMachine.add('ENTER', EnterRoom(), transitions = {'pass':'MoveAndPick'})

        smach.StateMachine.add('MoveAndPick', MoveAndPick(),
                        transitions = {'success':'MoveAndPlace',
                                       'failed':'AvoidThat'}
                        remapping = {'object_name_out':'sm_name',
                                      'objcet_name_in':'sm_name'})

        smach.StateMachine.add('MoveAndPlace', MoveAndPlace(),
                        transitions = {'completed':'AvoidThat'},
                        remapping = {'object_name_in':'sm_name'})

        smach.StateMachine.add('AvoidThat', AvoidThat(), transitions = {'to_WDYS':'PersonSearch'})

        smach.StateMachine.add('PersonSearch', PerosnSearch(), transitions = {'found':'QuestionResponse'})

        smach.StateMachine.add('QuestionResponse', QuestionResponse(),
                        transitions = {'completes':'ExitRoom'},
                        remapping = {'success_count_in':'sm_success',
                                     'success_count_out':'sm_success',
                                     'start_time_in':'sm_time',
                                     'start_time_out':'sm_time'})

        smach.StateMachine.add('ExitRoom', ExitRoom(), transitions = {'to_finish':'finish_sm'})
    
    outcome = sm_top.execute()
