# door_open

# Overview
実機班の新入生教育のdoor_openの参考例  
各ノードの解説付き  
扉が開いたら前に進むノードを書いてもらう  
解説については自分が必要だと思ったところだけば読めば良い  
参考例なので自作できるなら自作しても良いただし以下の内容は守ってほしい  

***velocity は0.2[m/s]にしましょう。 衝突の恐れあり***

# Description

## src
- ### [door_open1.py]
  >速度と距離から目標タイムを計測し、目標タイム内で走らせるプログラム
  
- ### [enter_server.py]
  >door_open1.py をサービスサーバーに書き換えたもの

- ### [door_open2.py]
  >プロジェクトが開発したbase_controlモジュールを用いて、指定した速度と距離で走らせるプログラム

- ### [enter_server2.py]
  >door_open2.py をサービスサーバーに書き換えたもの

## srv
- ### [specify_value.srv]
  >enter_server.py,enter_server2.pyで使用するsrvファイル

# コード解説
## door_open1.py　コード解説
現状独自のモジュールを使用しなければ、指定した速度と距離を走らせることが出来ない。そのため、今回のプログラムは時速の計測を用いて、進む速度と距離から目標タイムを計測し、目標タイムに到達したときにプログラムを終了させるプログラムにした。  
今回はtimeモジュールを用いて、時間計測を行った。しかし、機体が止まっていても時間は進み続けるため,かくブロックごとに時間の修正図った。詳細はプログラム内に書きの残した。また、時間計測に関しては下記の参考記事欄に残した。  
⚠経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。

## enter_server.py コード解説
door_open1.py のプログラムをもとに距離と速度をサービスサーバーで取得するプログラムに書き換えた。サービスサーバーの書き方に関しては下記の参考記事欄に残し、コードの重要な部分だけ下記に解説を残した。

### サービスのインポート
```
from door_open.srv import specify_value, specify_valueResponse
```
door_open パッケージの srv の中にある`specify_value`とその出力に関する`specify_valueResponse`をインポートしている。

### サービスサーバーの宣言例(インスタンス化)
サービスをインスタンスさせるために、サービス名を`door_open_server`,サービスの型を`pecify_value`,サービスの引き返すコールバック関数名を`self.execute`とした場合、下記のように記せば良い。
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
⚠経験者は語る velocity は0.2[m/s]にしましょう。衝突の恐れあり。

## door_open2.py コード解説
このノードは、プロジェクトで開発されたbase_controlモジュールを使用して、指定した速度と距離で走らせる。上記で解説したdoor_open1.pyのように時間で制御する必要がなくとてもシンプルなノードだ。  
⚠注意 下記のリポジトリの git clone が必要だ。  
[今回使用したリポジトリ](https://github.com/KIT-Happy-Robot/happymimi_apps.git)  

*今回使用したメソッド*
- translateDist(dist, speed)  
> 前進、後進の処理を実行し、第一引数は進行距離[m], 第二引数は並進速度  [m/s]となっている。  
> ⚠経験者は語る 並進速度は0.2[m/s]にしましょう。衝突の恐れあり  

*base_controlモジュールの使い方*
- 1.パッケージのパスの取得
```
import roslib
file_path = roslib.packages.get_pkg_dir('happymimi_telop') + '/src/'
```
- 2.パスを通す
```
import sys
sys.path.insert(0, file_path)
from base_control import BaseControl

```
- 3.一連の流れまとめ
```
import roslib
import sys
file_path = roslib.packages.get_pkg_dir('happymimi_telop') + '/src/'
sys.path.insert(0, file_path)
from base_control import BaseControl
```
これで、base_controlモジュールを使えるようになる  
なお参考にした記事は下記の参考記事欄に残した。  

*モジュールの使い方*
- 1.import したモジュールの呼び出し
```
self.base_control = BaseControl()
```
- 2.メソッドを呼び出す  
今回使用するメソッドは、translateDist(dist, speed)なので
```
self.base_control.translateDist(dist, speed)
```

# enter_server2.py コード解説
door_open2.py のプログラムをもとに距離と速度をサービスサーバーで取得するプログラムに書き換えた。サービスサーバーの書き方に関しては下記の参考記事欄に残し、コードの重要な部分だけ下記に解説を残した。

### サービスのインポート
```
from door_open.srv import specify_value, specify_valueResponse
```
door_open パッケージの srv の中にある`specify_value`とその出力に関する`specify_valueResponse`をインポートしている。

### サービスサーバーの宣言例(インスタンス化)
サービスをインスタンスさせるために、サービス名を`door_open2_server`,サービスの型を`pecify_value`,サービスの引き返すコールバック関数名を`self.execute`とした場合、下記のように記せば良い。
```
service = rospy.Service('door_open2_server', specify_value, self.execute)
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

# 参考記事欄
*時間計測に関する参考記事*  
[pythonでストップウォッチをつくろう 参照日 2022/3/24](https://python-muda.com/python/python-stopwatch/)

*サービスサーバーの書き方参考記事*  
[サービスの書き方 参照日 2022/3/24](https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_write_service)

*ROS パッケージのパスに関する参考記事*  
[ROS プログラムからパッケージのパス取得 (Python/C++) 参照日 2022/3/24](https://qiita.com/hoshianaaa/item/60b2f5b266abcfbef368)

*自作モジュールの呼び出し参考記事*  
[ROSパッケージから自作pythonモジュールを呼び出す 参照日 2022/3/24](https://qiita.com/mu-777/items/b69473c6f652ea19c3d1)

