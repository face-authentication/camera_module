face-authentication / camera_module
====


## 事前準備
ラズパイを起動する前に、カメラモジュールを本体に接続しておく。

## インストール
### 下準備
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

### opencvのインストール
[Raspberry Pi 3 Model B + Raspbian Jessie環境にOpenCv3.1.0をインストール](http://walking-succession-falls.com/raspberry-pi-3-model-b-raspbian-jessie%E7%92%B0%E5%A2%83%E3%81%ABopencv3-1-0%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/)

### cameraを有効にする
```
$ sudo raspi-config
```

### 必要なライブラリのインストール
```
$ sudo apt-get install python-picamera
```

### ソースコードのダウンロード
```
$ git clone https://github.com/face-authentication/camera_module.git
```

### python実行環境のセットアップ
```
$ cd camera_module
$ sudo pip install -r ./requirements.txt
```

### 実行
```
$ python src/main.py -m pycamera 
```

## 参考
[RaspberryPiのカメラモジュールV2から流れるストリーミングを、Pythonを使って顔認識するまで](http://walking-succession-falls.com/raspberrypi%E3%81%AE%E3%82%AB%E3%83%A1%E3%83%A9%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%ABv2%E3%81%8B%E3%82%89%E6%B5%81%E3%82%8C%E3%82%8B%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%9F%E3%83%B3/)

## License
[MIT](https://github.com/face-authentication/camera_module/blob/master/LICENSE)

## Author
[m.hirasaki](https://github.com/hirasaki1985)

