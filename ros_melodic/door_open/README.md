# door_open
# Overview
実機班の新入生教育のdoor_openの参考例

# コード解説
## door_open1.py　コード解説
　現状独自のモジュールを使用しなければ、指定した速度と距離を走らせることが出来ない。そのため、今回のプログラムは時速の計測を用いて、進む速度と距離から目標タイムを計測し、目標タイムに到達したときにプログラムを終了させる。
今回はtimeモジュールを用いて、かくブロックごとに時間の修正を図っている。詳細はプログラムに残している。
##enter

*サービスサーバーの書き方参考記事*
[サービスの書き方 参照日 2022/3/24](https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_write_service)
