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
## door_open1.py　コード解説
現状独自のモジュールを使用しなければ、指定した速度と距離を走らせることが出来ない。そのため、今回のプログラムは時速の計測を用いて、進む速度と距離から目標タイムを計測し、目標タイムに到達したときにプログラムを終了させるプログラムだ。  
今回はtimeモジュールを用いて、時間計測を行った。しかし、機体が止まっていても時間は進み続けるためかくブロックごとに時間の修正図った。詳細はプログラム内に書きの残した。また、時間計測に関しては下記内容を参考にした。  
[pythonでストップウォッチをつくろう 参照日 2022/3/24](https://python-muda.com/python/python-stopwatch/)
## enter

*サービスサーバーの書き方参考記事*
[サービスの書き方 参照日 2022/3/24](https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_write_service)
