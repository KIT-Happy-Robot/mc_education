# navigation
## Overview
[Turtlebot2](https://www.turtlebot.com/turtlebot2/)を用いて、Navigationを実践的に学ぶことを目的としたパッケージです。

## Description
[**src**](./src)には以下のファイルを含みます。
- ### [set_location.py](./src/set_location.py)
> マップ生成の際に使用すると便利なサービスサーバーです。

- ### [simple_navigation.py](./src/simple_navigation.py)
> Navigationをするために必要最低限の知識を学べるプログラムファイルです。

- ### [basic_navigation.py](./src/basic_navigation.py)
> 大会レベルのNavigationを実践的に学ぶことができるプログラムファイルです。

## Requirement

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

15行目から変更していきます。
変更前

```{number="yes"}
14 <!-- Map server -->
15 <arg name="map_file" default="$(env TURTLEBOT_MAP_FILE)"/>
16 <node name="map_server" pkg="map_server" type="map_server" args="$(arg map_file)" />
```



```
