#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------
#Title: door_open2のサービスサーバー
#Author: Shunsuke Wada
#Memo: base_control.pyを用いて、進む距離と速さはサーバーから取得し走らせる。
#Memo: 自作モジュールの git clone が必要
#--------------------------------------------------------------------------
import rospy
import roslib
import sys
from door_open.srv import specify_value, specify_valueResponse
from sensor_msgs.msg import LaserScan
file_path = roslib.packages.get_pkg_dir('happymimi_teleop') + '/src/'
sys.path.insert(0, file_path)
from base_control import BaseControl

class DoorServer():
    def __init__(self):
        #サービスサーバーの宣言
        service = rospy.Service('/door_open2_server', specify_value, self.execute)
        #サブスクライバーの宣言
        rospy.Subscriber('/scan', LaserScan, self.laserCB)
        #値の初期化
        self.front_laser_dist = 999.9
        self.base_control = BaseControl()
        rospy.loginfo('start door open')
    def laserCB(self, receive_msg):
        self.front_laser_dist = receive_msg.ranges[359]

    def execute(self, srv_req):
        #安全距離
        safe_dist = 2.0
        rospy.sleep(0.3)
        while not rospy.is_shutdown():
            #前に障害物がないとき
            if self.front_laser_dist >= safe_dist:
                rospy.loginfo('start forward')
                rospy.sleep(0.1)
                #一回繰り返す
                for i in range(1):
                    #メソッドの呼び出し
                    self.base_control.translateDist(srv_req.distance, srv_req.velocity)
                    rospy.loginfo('finish door open')
                    return specify_valueResponse(result = True)
            #前に障害物があったとき
            elif self.front_laser_dist <= safe_dist:
                rospy.loginfo('Please open the door')
                rospy.sleep(3.0)
if __name__ == '__main__':
    rospy.init_node('enter_server2')
    ds = DoorServer()
    rospy.spin()
