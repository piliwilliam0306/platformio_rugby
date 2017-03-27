#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def upload():
    os.system('platformio run -d ArduinoISP/328p_left --target upload')
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_right --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_pan --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_tilt --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_imu --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_dock --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/328p_avoid --target upload')	
    os.system(fuse328p)	
    os.system(fuse328p)	
    os.system('platformio run -d ArduinoISP/mega_wheel --target upload')
    os.system(fuse2560)	
    os.system(fuse2560)	
    os.system('platformio run -d ArduinoISP/mega_head --target upload')
    os.system(fuse2560)	
    os.system(fuse2560)	

if __name__ == '__main__':
    fuse328p = 'avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m328p -U efuse:w:0x05:m -U hfuse:w:0xDA:m -U lfuse:w:0xFF:m'
    fuse2560 = 'avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m2560 -U efuse:w:0xFD:m -U hfuse:w:0xD8:m -U lfuse:w:0xFF:m'
    upload()

