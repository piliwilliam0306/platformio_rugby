# Platformio_rugby

## Target ID list
   * 328p_left  (U19 on RB, uart thru mega_wheel U9)
   * 328p_right (U16 on RB, uart thru mega_wheel U9)
   * 328p_IMU   (U11 on RB, uart thru mega_wheel U9)   
   * 328p_pan   (U25 on RB, uart thru mega_head U12)
   * 328p_tilt  (U22 on RB, uart thru mega_head U12)
   * 328p_avoid (U03 on RB, uart thru ftdi U4)
   * 328p_follow(U01 on RB, uart thru ftdi U2) 
   * mega_head  (U12 on RB, uart thru ftdi U13)
   * mega_wheel (U09 on RB, uart thru ftdi U10)

## Upload bootloader for programmer with Arduino Uno
    $ cd bootloader
    $ sudo pio run -t uploadboot

## Checking programmer fuse
    $ avrdude -P /dev/ttyUSB5 -b 57600 -c arduino -p m328p -v

## Setting fuse for all target devices
    $ sudo python fuse-set.py

## Rugby_board sanity test 
    $ sudo python sanity-blink.py 
    - LED should blink every 500ms
    $ sudo python sanity-blink-fast.py 
    - LED should blink every 100ms
    - we should see all LEDs blinking, if not, check if target fuse set correctly
    $ sudo python sanity-uart.py

## Checking target fuse 
    $ sudo platformio run -d ArduinoISP/328p_follow --target upload
    - replace 328p_follow when checking other targets
    $ avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m328p -v
    - fuse for 328p: efuse=0x05 hfuse=0xDA lfuse0xFF
    $ avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m2560 -v
    - fuse for 2560: efuse=0xFD hfuse=0xD8 lfuse0xFF

## Upload code for individual target (1st arg is the target, 2nd arg is the code to upload)
    $ sudo python upload.py 328p_follow rugby-blink/rugby-328-blink 
    
## Reference 
  http://docs.platformio.org/en/latest/installation.html
  
  http://docs.platformio.org/en/latest/platforms/atmelavr.html#custom-fuses

  http://heliosoph.mit-links.info/arduinoisp-reading-writing-fuses-atmega328p/
  
  http://www.martyncurrey.com/arduino-atmega-328p-fuse-settings/
  
  http://www.codingwithcody.com/2011/06/25/arduino-default-fuse-settings/
