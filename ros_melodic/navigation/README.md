# navigation
## Overview
[Turtlebot2](https://www.turtlebot.com/turtlebot2/)を用いて、Navigationを実践的に学ぶことを目的としたパッケージです。

## Description
[**src**](./src)には以下のファイルを含みます。
- ### [set_location.py](./src/set_location.py)
> マップ生成の際に使用すると便利なサービスサーバです。

- ### [simple_navigation.py](./src/simple_navigation.py)
> Navigationをするために必要最低限の知識を学べるプログラムファイルです。

- ### [basic_navigation.py](./src/basic_navigation.py)
> 大会レベルのNavigationを実践的に学ぶことができるプログラムファイルです。

## Requirement
### GitHub
>- [turtlebot](https://github.com/turtlebot/turtlebot)
>- [turtlebot_msgs](https://github.com/turtlebot/turtlebot_msgs)
>- [turtlebot_apps](https://github.com/turtlebot/turtlebot_apps)
>- [turtlebot_simulator](https://github.com/turtlebot/turtlebot_simulator)
>- [kobuki_msgs](https://github.com/yujinrobot/kobuki_msgs)
>- [kobuki_bumper2pc](https://github.com/yujinrobot/kobuki/tree/melodic/kobuki_bumper2pc)
>- [kobuki_description](https://github.com/yujinrobot/kobuki/tree/melodic/kobuki_description)
>- [kobuki_keyop](https://github.com/yujinrobot/kobuki/tree/melodic/kobuki_keyop)
>- [kobuki_node](https://github.com/yujinrobot/kobuki/tree/melodic/kobuki_node)
>- [kobuki_safety_controller](https://github.com/yujinrobot/kobuki/tree/melodic/kobuki_safety_controller)
>- [kobuki_gazebo_plugins](https://github.com/yujinrobot/kobuki_desktop/tree/melodic/kobuki_gazebo_plugins)
>- [yocs_cmd_vel_mux](https://github.com/yujinrobot/yujin_ocs/tree/devel/yocs_cmd_vel_mux)
>- [yocs_controllers](https://github.com/yujinrobot/yujin_ocs/tree/devel/yocs_controllers)
### パッケージ
>- ros-melodic-kobuki-*
>- ros-melodic-ecl-streams
>- ros-melodic-depthimage-to-laserscan
>- ros-melodic-joy
>- ros-melodic-yocs-velocity-smoother

## Build Enviroment

### Turtlebot2パッケージ群のインストール

```
cd ~/catkin_ws/src
curl -sLf https://raw.githubusercontent.com/gaunthan/Turtlebot2-On-Melodic/master/install_basic.sh | bash
catkin build
```

今入れたパッケージ軍のパスは以下のようになっています。 </br>
/ home / user / catkin_ws / src / src / **パッケージ群** </br>
/src/srcとなっているのが気持ち悪いので以下コマンドでフォルダ名を変更してください。

```
cd ~/catkin_ws/src
mv src turtlebot_pkgs
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
