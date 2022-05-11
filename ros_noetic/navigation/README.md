# mc_education

## Overview
実機によるNavigationの教育内容をまとめたROSパッケージ

## Description
このパッケージが提供する機能は主に以下の4つです。
* Map作成時のロケーション登録
* Mapの保存
* ゴールに向かうだけのNavigation
* コストマップを利用したNavigation

## Usage
### [set_location.py](src/set_location.py)
#### Set Location
|Communication|Name|Type|Request|Result|
| :---: | :---: | :---: | :---: | :---: |
| Service | /set_location_server | [SetLocation](srv/SetLocation.srv) | string型： `state`, `name` | bool型： `result` |

### [basic_navigation.py](src/basic_navigation.py)
### [simple_navigation.py](src/simple_navigation.py)
