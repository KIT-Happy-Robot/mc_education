**![SPM is supported](https://img.shields.io/badge/mc_education-Basic_Functionalities-orange)**

# Basic_Functionalities

# Overview

:tada: 実機班新入生教育最後の教育内容:tada:    
RCJ2018年の競技プログラムのBasic Functionalitiesを実施(基本的なロボットの動作)    
大会ルールや流れは下記にあるので、よく読んでから取り組みましょう:bangbang:   
:point_right: [Basic Functionalities rules](https://github.com/RoboCupAtHomeJP/Rule2020/blob/master/rules/basicfunctionalities_ja.md)

# Description

## [src](https://github.com/KIT-Happy-Robot/mc_education/tree/main/ros_melodic/master/src)
- ### [Basic_Functionalities.py](https://github.com/KIT-Happy-Robot/mc_education/blob/main/ros_melodic/master/src/Basic_Functionalities.py)
   >ロボットの基本的な動作をまとめたマスタープログラム
   
# Requirement

## 今回使用したモジュールのパッケージ
### 使い方に関しては各パッケージにあるREADME.mdを読むと良いでしょう。:bangbang:    
:radioactive:今回はgit cloneする必要はありません  

:point_right:[enter_room](https://github.com/KIT-Happy-Robot/happymimi_apps/tree/develop/enter_room)  

:point_right:[happymimi_navigation](https://github.com/KIT-Happy-Robot/happymimi_apps/tree/develop/happymimi_navigation)

:point_right:[happymimi_teleop](https://github.com/KIT-Happy-Robot/happymimi_apps/tree/develop/happymimi_teleop)

:point_right:[happymimi_voice](https://github.com/KIT-Happy-Robot/happymimi_voice)

:point_right:[happymimi_manipulation](https://github.com/KIT-Happy-Robot/happymimi_manipulation)

:point_right:[happymimi_recognition](https://github.com/KIT-Happy-Robot/happymimi_recognition)


:point_right:[wdys_bf](https://github.com/happykoya/wdys_bf)

# Usage  

## Basic_Functionalities.py  

### mimiを起こす:robot:  
```
basic_launch
```
```
mani_launch
```
これでロボットの各機能を使用できる。:kissing_heart:  

### コマンドラインから使う  

仮想環境に入り、bf_conversation.pyを起動  

```
roscd happymimi_voices  
cd ../
source envs/mimienv/bin/activate
rosrun wdys_bf bf_conversation.py
```

enter_roomを起動  

```
rosrun enter_room enter_server.py
```

 Basic_Functionalities.pyを起動
 ```
 rosrun master Basic_Functionalities.py  
 ```
 
これで競技を始めることができる。:trollface:　　

これだけの工程をこなすのは大変だと感じたそこのあなた:thinking:  
今からでも遅くありません是非、bashを使って楽をしませんか:smirk:    
やり方はとても簡単　ミスも減ります  
是非やってみませんか:roll_eyes:  　　



