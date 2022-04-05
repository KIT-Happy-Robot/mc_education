# mc_education
## Overview
実機班の教育内容をまとめたROSメタパッケージ
</br>

## Description
以下のパッケージを含みます。

### ros_melodic
ROS melodicに対応した教育用パッケージが入っています。
- ### [door_open](./ros_melodic/door_open)
  > 前方のドアや障害物の対応に関する教育用パッケージ

- ### [navigation](./ros_melodic/navigation)
  > ロボットの自律走行に関する教育用パッケージ

- ### [navigation_sim](./ros_melodic/navigation_sim)
  > シミュレータ上で実行できるロボットの自律走行に関する教育用パッケージ

- ### [smach_samples](./ros_melodic/smach_samples)
  > Smachに関する教育用パッケージ
</br>

## Requirement
各パッケージのREADMEをご覧ください。
</br>

## Build Enviroment
</br>

### Turtlebot2パッケージ群のインストール

```
cd ~/catkin_ws/src
curl -sLf https://raw.githubusercontent.com/gaunthan/Turtlebot2-On-Melodic/master/install_basic.sh | bash
```

今入れたパッケージ軍のパスは以下のようになっています。 </br>
/ home / user / catkin_ws / src / src / **パッケージ群** </br>
/ src / src となっているのが気持ち悪いので以下コマンドでフォルダ名を変更してください。

```
cd ~/catkin_ws/src
mv src turtlebot_pkgs
catkin build
````

### /amcl_demo.launchの変更
/amcl_demo.launchを開いてください

```
roscd turtlebot_navigation/launch
vim amcl_demo.launch
```

15行目から変更していきます。 </br>
変更前

```
14  <!-- Map server -->
15  <arg name="map_file" default="$(env TURTLEBOT_MAP_FILE)"/>
16  <node name="map_server" pkg="map_server" type="map_server" args="$(arg map_file)" />
```

変更後

```
14  <!-- Map server & Load location -->
15  <arg name="file_name" default="yumeko" />
16  <arg name="map_file" default="$(find turtlebot_navigation)/maps/$(arg file_name).yaml" />
17  <arg name="location_file" default="$(find navigation)/location/$(arg file_name).yaml" />
18  <node name="map_server" pkg="map_server" type="map_server" args="$(arg map_file)" />
19  <rosparam file="$(arg location_file)" command="load" ns="/navigation/location_dict" />
```

### /3dsensor.launchの変更
/3dsensor.launchを開いてください

```
roscd turtlebot_bringup/launch
vim 3dsensor.launch
```

41行目から変更していきます。 </br>
変更前

```
40  <!-- Laserscan topic -->
41  <arg name="scan_topic" default="scan" />
```

変更後

```
40  <!-- Laserscan topic -->
41  <arg name="scan_topic" default="kinect_scan"/>
42  <node name="laser_driver" pkg="urg_node" type="urg_node">
43    <param name="frame_id" value="base_laser_link" />
44    <param name="angle_min" value="-1.5707963" />
45    <param name="angle_max" value="1.5707963" />
46  </node>
 ```
</br>

### よくあるエラーへの対処
よくあるエラー

```
ERROR: cannot launch node of type [laptop_battery_monitor/laptop_battery.py]: laptop_battery_monitor
```

対処法

```
cd ~/catkin_ws/src
git clone https://github.com/ros-drivers/linux_peripheral_interfaces.git
cd ~/catkin_ws/src/linux_peripheral_interfaces
rm -rf libsensors_monitor
catkin build
```

## Bring Up
各パッケージのREADMEをご覧ください。
</br>

## Usage
各パッケージのREADMEをご覧ください。
