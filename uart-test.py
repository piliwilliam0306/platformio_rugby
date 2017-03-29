#!/usr/bin/env python2
# upload using ArduinoISP
import os
import time
import serial
import tty, sys,termios

def getchar():
   fd = sys.stdin.fileno()
   settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, settings)
   return ch

def main():
    head = serial.Serial('/dev/ttyUSB1', 57600, timeout=1)
    wheel = serial.Serial('/dev/ttyUSB2', 57600, timeout=1)
    dock = serial.Serial('/dev/ttyUSB3', 57600, timeout=1)
    avoid = serial.Serial('/dev/ttyUSB4', 57600, timeout=1)
    print('Press "l" to test 328p_left')
    print('Press "r" to test 328p_right')
    print('Press "i" to test 328p_imu')
    print('Press "p" to test 328p_pan')
    print('Press "t" to test 328p_tilt')
    print('Press "d" to test 328p_dock')
    print('Press "a" to test 328p_avoid')
    print('Press "q" to exit')
    while True:
	ch = getchar()
        if (ch == 'l') | (ch == 'r') | (ch == 'i'):
            wheel.write(ch)
        elif (ch == 'p') | (ch == 't'):
            head.write(ch)
        elif ch == 'd':
            dock.write(ch)
        elif ch == 'a':
            avoid.write(ch)
        elif ch == 'q':
	    print('Exiting')
	    break
    head.close()
    wheel.close()
    dock.close()
    avoid.close()

if __name__ == '__main__':
    main() 
