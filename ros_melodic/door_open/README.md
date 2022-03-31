**![SPM is supported](https://img.shields.io/badge/mc_education-door_open-orange)**

# door_open

# Overview
実機班の新入生教育のdoor_openの参考例  
各ノードの解説付き  
扉が開いたら前に進むノードを書いてもらう  
解説については自分が必要だと思ったところだけば読めば良い  
あくまでも参考例なので自作できるなら自作しても良いただし以下の内容は守ってほしい  

***velocity は0.2[m/s]にしましょう。 衝突の恐れあり***

# Description

## src
- ### [door_open1.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/door_open1.py)
  >速度と距離から目標タイムを計測し、目標タイム内で走らせるプログラム
  
- ### [enter_server.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/enter_server.py)
  >door_open1.py をサービスサーバーに書き換えたもの

- ### [door_open2.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/door_open2.py)
  >プロジェクトが開発したbase_controlモジュールを用いて、指定した速度と距離で走らせるプログラム

- ### [enter_server2.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/src/enter_server2.py)
  >door_open2.py をサービスサーバーに書き換えたもの

## srv
- ### [specify_value.srv](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/door_open/srv/specify_value.srv)
  >enter_server.py,enter_server2.pyで使用するsrvファイル



# コード解説



### Usage
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
⚠経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。


### Usage
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
⚠経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。

