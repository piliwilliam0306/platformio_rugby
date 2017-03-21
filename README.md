# Platformio_rugby

## Upload bootloader
    $ cd bootloader
    $ sudo pio run -t uploadboot

## Programmer ID list
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
* We have added LEDs to pin digital 10 on each MCU for sanity test
* Upload "rugby-2560-blink" when testing 2560
* Upload "rugby-328-blink" when testing 328P

## Upload code (1st arg is the device, 2nd arg is the code to upload)
    $ sudo python upload.py 328p_follow rugby-328-blink

## Reference 
  http://docs.platformio.org/en/latest/installation.html
  
  http://docs.platformio.org/en/latest/platforms/atmelavr.html#custom-fuses
