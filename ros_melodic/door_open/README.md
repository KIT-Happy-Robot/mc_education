# door_open
# Overview
実機班の新入生教育のdoor_openの参考例
# Description
## src
- ### [door_open1.py]
  >速度と距離から目標タイムを計測し、目標タイム内で走らせるプログラム
  
- ### [enter_server.py]
  >door_open1.py をサービスサーバーに書き換えたもの

- ### [door_open2.py]
  >プロジェクトが作った自作モジュールを用いて、指定した速度と距離で走らせるプログラム

- ### [enter_server2.py]
  >door_open2.py をサービスサーバーに書き換えたもの
## srv
- ### [specify_value.srv]
  >enter_server.py,enter_server2.pyで使用するsrvファイル

# コード解説
### door_open1.py
現状独自のモジュールを使用しなければ、指定した速度と距離を走らせることが出来ない。そのため、今回のプログラムは時速の計測を用いて、進む速度と距離から目標タイムを計測し、目標タイムに到達したときにプログラムを終了させるプログラムだ。  
今回はtimeモジュールを用いて、時間計測を行った。しかし、機体が止まっていても時間は進み続けるため,かくブロックごとに時間の修正図った。詳細はプログラム内に書きの残した。また、時間計測に関しては下記の参考記事欄に残した。  

## enter_server.py コード解説
door_open1.pyのプログラムをもとに距離と速度をサービスサーバーで取得するプログラムに書き換えた。サービスサーバーの書き方に関しては下記の参考記事欄に残し、コードの重要な部分だけ下記に解説を残した。
### サービスのインポート
```
from door_open.srv import specify_value, specify_valueResponse
```
door_open パッケージの srv の中にある`specify_value`とその出力に関する`specify_valueResponse'をインポートしている。
### サービスサーバーの宣言例(インスタンス化)
サービスをインスタンスさせるために、サービス名を`door_open_server`,サービスの型を`specify_value`,サービスの引き返すコールバック関数名を`self.execute`とした場合、下記のように記せば良い。
```
service = rospy.Service('door_open_server', specify_value, self.execute)
```
### CMakeLists.txt の書き換え
CMakeLists.txt内の58行目からの`add_service_files`〜60行目までコメントアウトを外し下記のように変更する必要がある。
```
## Generate services in the 'srv' folder
add_service_files(
  DIRECTORY
  srv
  FILES
  specify_value.srv
)
```
上記のように書けたらOK
⚠注意 あくまでも参考例なのでFILESの部分は作ったファイル名を入れる必要がある。

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
## door_open2.py コード解説
このノードは、プロジェクトで開発された自作のモジュールを使用して、指定した速度と距離で走らせる。上記で解説したdoor_open1.pyのように時間で制御する必要がなくとてもシンプルなノードだ。  
⚠注意 下記のリポジトリの git clone が必要だ。  
[今回使用したリポジトリ](https://github.com/KIT-Happy-Robot/happymimi_apps.git)
# 参考記事欄
*時間計測に関する参考記事*
[pythonでストップウォッチをつくろう 参照日 2022/3/24](https://python-muda.com/python/python-stopwatch/)

*サービスサーバーの書き方参考記事*
[サービスの書き方 参照日 2022/3/24](https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_write_service)
