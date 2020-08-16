# 概要
distフォルダにexeファイル同封

翼型解析ソフト[xflr5](http://www.xflr5.tech/xflr5.htm)の解析結果(polarファイル)からCl_alpha,Cl_Cdグラフの近似モデルを作成し、プロペラ設計ソフト[xrotor](http://web.mit.edu/drela/Public/web/xrotor/)のaeroファイルを出力するプログラム

自動で近似モデルを作成するが、各自が解析結果と見比べながら、パラメータを調整し、好みの近似モデルに変更することもできる。

出力ファイルはxrotorの
```
>>aero
>>read
>>出力ファイルパス
```
より読み取り可能。

以下デモ

![demo](./images/demo.gif)

# 動作環境
exeファイルが開ける端末

もしくは、以下python環境
```
python 3.7

certifi==2020.6.20
cycler==0.10.0
kiwisolver==1.2.0
matplotlib==3.3.1
numpy==1.19.1
Pillow==7.2.0
pyparsing==2.4.7
PyQt5==5.15.0
PyQt5-sip==12.8.0
python-dateutil==2.8.1
six==1.15.0
```

# セットアップ
方法は以下2つ

## 方法1
このレポジトリをダウンロード及び解凍し、distフォルダ内のxflr5_to_xrotor.exeを開く。

## 方法2
### 手順1
[python](https://www.python.org/)をダウンロード

### 手順2
このレポジトリをダウンロード及び解凍。

### 手順3
自分のpthon環境との干渉を防ぐために、仮想環境の構築を推奨。

特に、anacondaを使用している場合、干渉可能性が大きいため、強く推奨。

構築方法は以下、(python3系)
```
py -m venv [解凍したレポジトリのパス]
cd [解凍したレポジトリのパス]
Scripts\activate
pip install -r requirements.txt
```

仮想環境を終了する場合は、
```
Scripts\deactivate
```

以降

```
Scripts\activate
```
のみで同環境構築可能

# 使い方
準備中

デモ参照
