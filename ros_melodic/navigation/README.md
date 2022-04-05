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

