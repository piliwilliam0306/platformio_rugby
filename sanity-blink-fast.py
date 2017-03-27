#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def upload():
    os.system('python upload.py 328p_left rugby-blink/rugby-328-blink-fast')	
    os.system('python upload.py 328p_right rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py 328p_pan rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py 328p_tilt rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py 328p_imu rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py 328p_dock rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py 328p_avoid rugby-blink/rugby-328-blink-fast')
    os.system('python upload.py mega_wheel rugby-blink/rugby-2560-blink-fast')
    os.system('python upload.py mega_head rugby-blink/rugby-2560-blink-fast')

if __name__ == '__main__':
	upload()
