import os
import socket
import netifaces as ni
import psutil
import time
import I2C_LCD_driver
from collections import defaultdict

d = defaultdict(list)    
d[0].append(1)
#mylcd = I2C_LCD_driver.lcd()

while True:
#     # ip
#     # eth0
#     ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
#     ip_lcd = 'IP: '+ ip
#     print('IP:',ip)
#     mylcd.lcd_display_string(ip_lcd ,1)
    
#     # 有連上什麼IP 則一顯示
#     gw = os.popen("ip -4 route show default").read().split()
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect((gw[2], 0))
#     ip = s.getsockname()[0]
#     print('IP:', ip)
#     mylcd.lcd_display_string('IP:')
#     mylcd.lcd_display_string(ip ,2)
    
    # all_IP
    from netifaces import interfaces, ifaddresses, AF_INET
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        ifacename = ifaceName + ':'
        print(ifacename)
        print(' '.join(addresses), '\n')
#        mylcd.lcd_display_string(ifacename,1)
#        mylcd.lcd_display_string(' '.join(addresses) ,2)
        time.sleep(2)
#        mylcd.lcd_clear()
    
    # CPU
    temp1_str = os.popen("cat /sys/class/thermal/thermal_zone1/temp").read()
    temp1_int = int(temp1_str) /1000
    temp = str(temp1_int)
    util = str(psutil.cpu_percent())
    temp_lcd = 'CPU temp: '+ temp +'°C'
    util_lcd = 'CPU util: '+ util +' %'
    print('CPU temp:', temp + '°C')
    print('CPU util:', util, '%\n')
#    mylcd.lcd_display_string(temp_lcd ,1)
#    mylcd.lcd_display_string(util_lcd ,2)
    
    time.sleep(2)
#    mylcd.lcd_clear()
    
    # GPU
    temp2_str = os.popen("cat /sys/class/thermal/thermal_zone2/temp").read()
    temp2_int = int(temp2_str) /1000
    print('GPU temp: {:0.1f}°C'.format(temp2_int))
#    mylcd.lcd_display_string('GPU temp: {:0.1f}°C'.format(temp2_int) ,1)
    
    # ram
    s = str(psutil.virtual_memory().percent)
    s_lcd = 'RAM used: ' + s + ' %'
    print ('RAM used:', s, '%\n')
#    mylcd.lcd_display_string(s_lcd ,2)
    
    time.sleep(2)
#    mylcd.lcd_clear()
    
