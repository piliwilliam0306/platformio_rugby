#!/usr/bin/env python2
# upload using ArduinoISP
import argparse
import os
#os.system('sudo platformio run --target upload')
#os.system('sudo platformio run -t program')

def test(args):
	if args.target =='328p_left':
	    os.system('platformio run -d ArduinoISP/328L-isp')
	elif args.target =='328p_right':
	    os.system('platformio run -d ArduinoISP/328R-isp')
	elif args.target =='328p_pan':
            os.system('platformio run -d ArduinoISP/328P-isp')
        elif args.target =='328p_tilt':
            os.system('platformio run -d ArduinoISP/328T-isp')
	elif args.target =='328p_imu':
            os.system('platformio run -d ArduinoISP/328I-isp')
        elif args.target =='328p_avoid':
            os.system('platformio run -d ArduinoISP/328A-isp')
        elif args.target =='328p_follow':
            os.system('platformio run -d ArduinoISP/328F-isp')
        elif args.target =='mega_head':
            os.system('platformio run -d ArduinoISP/MegaH-isp')	
	elif args.target =='mega_wheel':
            os.system('platformio run -d ArduinoISP/MegaW-isp') 	
	else:
	    print("wtf")	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('target', type=str, help="MCU to program.")
	args = parser.parse_args()
	test(args)
