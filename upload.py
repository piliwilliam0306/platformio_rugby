#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def update(args):
	if args.target =='328p_left':
	    os.system('platformio run -d ArduinoISP/328L-isp --target upload')
	elif args.target =='328p_right':
	    os.system('platformio run -d ArduinoISP/328R-isp --target upload')
	elif args.target =='328p_pan':
            os.system('platformio run -d ArduinoISP/328P-isp --target upload')
        elif args.target =='328p_tilt':
            os.system('platformio run -d ArduinoISP/328T-isp --target upload')
	elif args.target =='328p_imu':
            os.system('platformio run -d ArduinoISP/328I-isp --target upload')
        elif args.target =='328p_avoid':
            os.system('platformio run -d ArduinoISP/328A-isp --target upload')
        elif args.target =='328p_follow':
            os.system('platformio run -d ArduinoISP/328F-isp --target upload')
        elif args.target =='mega_head':
            os.system('platformio run -d ArduinoISP/MegaH-isp --target upload')	
	elif args.target =='mega_wheel':
            os.system('platformio run -d ArduinoISP/MegaW-isp --target upload') 	
	else:
	    print("wtf")	

def upload(args):
	os.system('platformio run -t program -d {}'.format(args.code))
        os.system('platformio run -t program -d {}'.format(args.code))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('target', type=str, help="MCU to program.")
	parser.add_argument('code', type=str, help="code to upload.")
	args = parser.parse_args()
	update(args)
	upload(args)
