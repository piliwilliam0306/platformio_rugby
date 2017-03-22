#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def upload():
    os.system('python upload.py 328p_left rugby-uart/rugby-left-uart')	
    os.system('python upload.py 328p_right rugby-uart/rugby-right-uart')	
    os.system('python upload.py 328p_pan rugby-uart/rugby-pan-uart')	
    os.system('python upload.py 328p_tilt rugby-uart/rugby-tilt-uart')	
    os.system('python upload.py 328p_imu rugby-uart/rugby-imu-uart')	
    os.system('python upload.py 328p_follow rugby-uart/rugby-follow-uart')	
    os.system('python upload.py 328p_avoid rugby-uart/rugby-avoid-uart')	
    os.system('python upload.py mega_head rugby-uart/rugby-mega-uart')	
    os.system('python upload.py mega_wheel rugby-uart/rugby-mega-uart')	

if __name__ == '__main__':
    upload()
