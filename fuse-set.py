#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def upload():
    os.system('platformio run -d ArduinoISP/328p_left')
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/328p_right')	
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/328p_pan')	
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/328p_tilt')	
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/328p_imu')	
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/328p_follow')	
    os.system(328p_fuse)	
    os.system('platformio run -d ArduinoISP/mega_wheel')
    os.system(2560_fuse)	
    os.system('platformio run -d ArduinoISP/mega_head')
    os.system(2560_fuse)	

if __name__ == '__main__':
    328p_fuse = 'avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m328p -U efuse:w:0x05:m -U hfuse:w:0xDE:m -U lfuse:w:0xFF:m'
    2560_fuse = 'avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m2560 -U efuse:w:0xFD:m -U hfuse:w:0xD8:m -U lfuse:w:0xFF:m'
    upload()

