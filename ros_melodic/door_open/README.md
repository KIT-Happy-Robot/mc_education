**![SPM is supported](https://img.shields.io/badge/mc_education-door_open-orange)**

# door_open

# Overview
実機班の新入生教育のdoor_openの参考例  
各ノードの解説付き  
扉が開いたら前に進むノードを書いてもらう  
解説については自分が必要だと思ったところだけば読めば良い  
あくまでも参考例なので自作できるなら自作しても良いただし以下の内容は守ってほしい  

***:radioactive: velocity は0.2[m/s]にしましょう。 衝突の恐れあり***

# Description

## src
- ### [door_open1.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/door_open1.py)
  >速度と距離から目標タイムを計測し、目標タイム内で走らせるプログラム
  
- ### [enter_server.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/enter_server.py)
  >door_open1.py をサービスサーバーに書き換えたもの

- ### :beginner: [door_open2.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/door_open2.py)
  >プロジェクトが開発したbase_controlモジュールを用いて、指定した速度と距離で走らせるプログラム

- ### [enter_server2.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/enter_server2.py)
  >door_open2.py をサービスサーバーに書き換えたもの

## srv
- ### [specify_value.srv](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/srv/specify_value.srv)
  >enter_server.py,enter_server2.pyで使用するsrvファイル

# Requirement

## door_open2.py enter_server2.pyで使用するモジュールのパッケージ

### :point_right: [happymimi_apps](https://github.com/KIT-Happy-Robot/happymimi_apps.git)

### happymimi_appsのgit clone  

```
cd ~/catkin_ws/src
git clone https://github.com/KIT-Happy-Robot/happymimi_apps.git
catkin build 
catkin build happymimi_apps
cd happymimi_apps
catkin build happymimi_teleop
```

### :ballot_box_with_check: /base_control.pyの変更  
/base_control.pyを開いてください。

```
roscd happymimi_teleop/src/
vim base_control.py
```

22行目を変更します。  
:ballot_box_with_check: 変更前  
```
22 self.twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
```
:ballot_box_with_check: 変更後  
```
22   self.twist_pub = rospy.Publisher('/vmegarover/diff_drive_controller/cmd_vel', Twist, queue_size = 1)
```

# Usage

## enter_server.py 

|Communication|Name|Type|Request|Result|
| :---: | :---: | :---: | :---: | :---: |
| Service | /door_open_server | specify_value | float32型: `distance`,`velocity` | bool型: `result` |
</br>

### コマンドラインから使う

サービスサーバー /enter_server.py起動  

```
$ rosrun door_open enter_server.py
```
距離`distance`と速度`velocity`を指定
```
$ rosservice call /door_open_server "distance: 0.0 velocity: 0.0"
```
:radioactive: 経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。

## enter_server2.py  

|Communication|Name|Type|Request|Result|
| :---: | :---: | :---: | :---: | :---: |
| Service | /door_open2_server | specify_value | float32型: `distance`,`velocity` | bool型: `result` |
</br>

### コマンドラインから使う

サービスサーバー /enter_server.py起動  

```
$ rosrun door_open enter_server2.py
```
距離`distance`と速度`velocity`を指定
```
$ rosservice call /door_open2_server "distance: 0.0 velocity: 0.0"
```
:radioactive: 経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。

# 解説

## ノード内にもコメントを残しましたがもっと詳しい解説が欲しい人は下記にあります:bangbang:   

:point_right: [ソフト班/実機/教育/新入生教育 実機 door open 解説](https://kithappyrobot.esa.io/posts/277)

