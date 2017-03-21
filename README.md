# Platformio_rugby

## Upload bootloader for programmer
    $ cd bootloader
    $ sudo pio run -t uploadboot
    
## Setting fuse
    $ sudo python fuse-set.py
    
## Checking target fuse
    $ avrdude -P /dev/ttyUSB5 -b 57600 -c arduino -p m328p -v

## Device ID list
   * 328p_left  (U19 on RB)
   * 328p_right (U16 on RB)
   * 328p_pan   (U25 on RB)
   * 328p_tilt  (U22 on RB)
   * 328p_IMU   (U11 on RB)
   * 328p_avoid (U03 on RB)
   * 328p_follow(U01 on RB) 
   * mega_head  (U12 on RB)
   * mega_wheel (U09 on RB)

## Rugby_board sanity test 
    $ sudo python sanity-test.py

## Upload code (1st arg is the device, 2nd arg is the code to upload)
    $ sudo python upload.py 328p_follow rugby-328-blink

## Reference 
  http://docs.platformio.org/en/latest/installation.html
  
  http://docs.platformio.org/en/latest/platforms/atmelavr.html#custom-fuses

  http://heliosoph.mit-links.info/arduinoisp-reading-writing-fuses-atmega328p/
  
  http://www.martyncurrey.com/arduino-atmega-328p-fuse-settings/
  
  http://www.codingwithcody.com/2011/06/25/arduino-default-fuse-settings/
