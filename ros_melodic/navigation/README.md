# navigation
## Overview
[Turtlebot2](https://www.turtlebot.com/turtlebot2/)を用いて、Navigationを実践的に学ぶことを目的としたパッケージです。

## Description
[src](./src)には以下のファイルを含みます。
- ### [set_location.py](./src/set_location.py)
> マップ生成の際に使用すると便利なサービスサーバーです。

- ### [simple_navigation.py](./src/simple_navigation.py)
> Navigationをするために必要最低限の知識を学べるプログラムファイルです。

- ### [basic_navigation.py](./src/basic_navigation.py)
> 大会レベルのNavigationを実践的に学ぶことができるプログラムファイルです。

以上、Navigationについて実践的に学ぶことを目的としたパッケージです。

## Requirement

### Turtlebot2パッケージ群のインストール

```
cd ~/catkin_ws/src
curl -sLf https://raw.githubusercontent.com/gaunthan/Turtlebot2-On-Melodic/master/install_basic.sh | bash
catkin build
```
今入れたパッケージ軍のパスは以下のようになっています。</br>
/ home / user / catkin_ws / src / src / **パッケージ群**
