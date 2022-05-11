# mc_education

## Overview
実機によるNavigationの教育内容をまとめたROSパッケージ

## Description
このパッケージが提供する機能は主に以下の4つです。
* マップ作成時のロケーション登録
* マップの保存
* ゴールに向かうだけのNavigation
* コストマップを利用したNavigation

## Usage
### set_location.py
[set_location.py](src/set_location.py)の使用方法を説明します。
#### Set Location
|Communication|Name|Type|Request|Result|
| :---: | :---: | :---: | :---: | :---: |
| Service | /set_location_server | [SetLocation](srv/SetLocation.srv) | string型： `state`, `name` | bool型： `result` |

#### stateの種類
|state|Contents|
| :---: | :---: |
| add | オブジェクトの座標を登録 |
| save | マップを保存 |

#### nameの種類
|name|Contents|
| :---: | :---: |
| 任意の名前(ex. shelfとかtableとか) | 指定した名前でオブジェクトの座標登録 or マップ保存 |

#### 実行
サービスサーバを立ち上げます。
```
rosrun navigation set_location.py
```

サービスサーバを呼び出します
```
rosservice call /set_location_server "state: ''
name: ''"
```
任意の名前で作業を続行してください。
</br>

### [basic_navigation.py](src/basic_navigation.py)
### [simple_navigation.py](src/simple_navigation.py)
