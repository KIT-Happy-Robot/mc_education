#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------
#Title: door_openのサービスサーバー
#Author: Shunsuke Wada
#Memo: 進行速度と距離を取得し、目標タイムを計算し、目標タイム内でプログラムを動かす。
#Memo: 扉が空いていても問題なし
#------------------------------------------------------------------------------------
import rospy
import time 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from door_open.srv import specify_value, specify_valueResponse

class EnterServer():
    def __init__(self):
        #サービスサーバーの宣言
        service = rospy.Service('/door_open_server', specify_value, self.execute)
        rospy.loginfo('Ready to set door_open_server')
        #パブリッシャの宣言
        self.twist_pub = rospy.Publisher('/vmegarover/diff_drive_controller/cmd_vel', Twist, queue_size = 10)
        #サブスクライバーの宣言
        rospy.Subscriber('/scan', LaserScan, self.laserCB)
        #値の初期化
        self.front_laser_dist = 999.9
    
    def laserCB(self, receive_msg):
        #LIDARの視野角
        self.front_laser_dist = receive_msg.ranges[359]

    def execute(self, srv_req):
        vel = Twist()
        #サービスで進む距離と速度の取得
        vel.linear.x = srv_req.velocity
        target_dist = srv_req.distance
        #安全距離
        safe_dist = 1.0
        #速度と進行距離から目標タイムを計算
        target_time = target_dist / vel.linear.x
        #実行開始時間を格納
        start_time = time.time()
        #値の初期化
        stop_time = 0
        stop_start = 0
        stop_end = 0
        rospy.loginfo('start door open')
        rospy.sleep(0.5)

        while not rospy.is_shutdown():
            #安全距離のときに実行
            if self.front_laser_dist >= safe_dist:
                self.twist_pub.publish(vel)
                rospy.sleep(0.5)
            #障害物があるときに実行
            elif self.front_laser_dist <= safe_dist:
                #現在の時間を格納
                stop_start = time.time()
                rospy.loginfo('Please open door')
                rospy.sleep(3.0)
                #止まっていた時間を格納
                stop_end = time.time() - stop_start
                stop_time += stop_end
            #終了時間を格納
            finish_time = time.time() - start_time - stop_time - 1.0
            #時間計測
            print ("now_time = ", time.time() - start_time - stop_time - 1.0)
            #目標タイムに到達したときに実行
            if finish_time >= target_time:
                print("enter_room finish [distance:", srv_req.distance, "velocity:", srv_req.velocity,"]")
                return specify_valueResponse(result = True)

if __name__ == '__main__':
    rospy.init_node('enter_server')
    es = EnterServer()
    rospy.spin()
