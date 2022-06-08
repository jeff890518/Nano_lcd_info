# 開機後自動運行在LCD螢幕上顯示Jetson nano的IP位址、RAM使用率、CPU溫度及使用率

### 安裝 GPIO 套件
您可以在terminal中輸入以下指令，安裝Jetson Nano 官方提供的GPIO函式庫。
本筆記以Python3.6實作
```
*裝pip3，之後pip3 install 裝的lib才會在/home/nvidia/.loacl/lib/python3.6/site_packages*

sudo apt-get install python3-pip
sudo pip3 install Jetson.GPIO
```
### I2C LCD 螢幕
I2C(Inter-Integrated Circuit)是一種IC之間的通訊協定，應用I2C的電子零件會使用SDA（串列資料）和SCL（串列時脈）來傳輸。

GND(棕線)接到pin6。
VCC(紅線)接到pin4。
SDA(澄線)接到pin3。
SCL(黃線)接到pin5。

完成接線power燈和面板背光會亮起來。
![](https://i.imgur.com/w9VsmA7.jpg)
在terminal中輸入以下指令，安裝I2C的函式庫，再查詢I2C的位址。
```
sudo apt-get install libi2c-dev i2c-tools
sudo i2cdetect -y -r 1
```
![](https://i.imgur.com/eOIjOj3.png)
上圖中顯示出27，即代表I2C的位址為0x27。

函式庫來源於：https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
您可以從上方網址內複製程式碼，或是從這篇文章的附檔下載I2C_LCD_driver.py。

其中一行程式碼為ADDRESS = 0x27，請記得更改成先前查詢到的位址！

記得將I2C_LCD_driver.py放在我們執行python的同一資料
### python顯示nano CPU等等資訊
https://github.com/jeff890518/nano_lcd_info
(下載 status 和 LCD.service)

將 status放在 /home/nvidia
將 LCD.service 放在 /etc/systemd/system

*I2C_LCD_driver.py 是 icd_lcd的lib*
*start.sh 是 開機自動化腳本* *windows硬轉.sh檔可能會無法執行，最好是在linux環境下編寫.sh檔*
*status_lcd.py 是 控制lcd顯示兩秒輪播info*
```
# 需要裝的lib
sudo pip install jetson-stats
pip3 install netifaces
pip3 install psutil
sudo apt-get install libi2c-dev i2c-tools
pip3 install smbus
```

### 更改腳本的執行權限
開機執行的腳本需增加可執行權限才能被systemd 運行，指令如下
```
chmod +x /home/nvidia/status/start.sh
```
### systemctl命令如下：

#### 手動執行 LCD資訊顯示 服務
```
sudo systemctl start LCD.service
```
#### 停止 LCD.service 服務
```
sudo systemctl stop LCD.service
```
#### 顯示 LCD資訊顯示 服務狀態
```
systemctl status LCD.service
```
若成功執行，查看服務狀態會顯示
Loaded: loaded
Active: active(running)
![](https://i.imgur.com/WAn8Sqb.png)
### 重新啟用服務 (若 *.service 檔案有修改過)
```
sudo systemctl daemon-reload
```
### 設定服務為 enable 狀態，使之能開機運行
確定手動執行都沒問題，要enable才會真正啟用此服務
```
sudo systemctl enable LCD.service
```
