#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
import time

def test(args):
	if args.target =='328p_left':
	    os.system('platformio run -d ArduinoISP/328L-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
	elif args.target =='328p_right':
	    os.system('platformio run -d ArduinoISP/328R-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
	elif args.target =='328p_pan':
            os.system('platformio run -d ArduinoISP/328P-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
        elif args.target =='328p_tilt':
            os.system('platformio run -d ArduinoISP/328T-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
	elif args.target =='328p_imu':
            os.system('platformio run -d ArduinoISP/328I-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
        elif args.target =='328p_avoid':
            os.system('platformio run -d ArduinoISP/328A-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
        elif args.target =='328p_follow':
            os.system('platformio run -d ArduinoISP/328F-isp --target upload')
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
        elif args.target =='mega_head':
            os.system('platformio run -d ArduinoISP/MegaH-isp --target upload')	
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
	elif args.target =='mega_wheel':
            os.system('platformio run -d ArduinoISP/MegaW-isp --target upload') 	
	    os.system('platformio run -t program -d {}'.format(args.code))
	    os.system('platformio run -t program -d {}'.format(args.code))
	else:
	    print("wtf")	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('target', type=str, help="MCU to program.")
	parser.add_argument('code', type=str, help="code to upload.")
	args = parser.parse_args()
	test(args)
