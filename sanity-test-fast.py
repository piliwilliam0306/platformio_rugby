#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def upload():
    os.system('python upload.py 328p_left rugby-328-blink-fast')	
    os.system('python upload.py 328p_right rugby-328-blink-fast')
    os.system('python upload.py 328p_pan rugby-328-blink-fast')
    os.system('python upload.py 328p_tilt rugby-328-blink-fast')
    os.system('python upload.py 328p_imu rugby-328-blink-fast')
    os.system('python upload.py 328p_follow rugby-328-blink-fast')
    os.system('python upload.py mega_wheel rugby-2560-blink-fast')
    os.system('python upload.py mega_head rugby-2560-blink-fast')

if __name__ == '__main__':
	upload()
