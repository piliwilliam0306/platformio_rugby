# Platformio_rugby

## Upload bootloader
    $ cd bootloader
    $ sudo pio run -t uploadboot

## Programmer ID list
   * RESET_L     10 //328p_left  (U19 on RB)
   * RESET_R     9 //328p_right  (U16 on RB)
   * RESET_P     8 //328p_pan    (U25 on RB)
   * RESET_T     7 //328p_tilt   (U22 on RB)
   * RESET_I     6 //328p_IMU    (U11 on RB)
   * RESET_A     5 //328p_avoid  (U03 on RB)
   * RESET_F     4 //328p_follow (U01 on RB) 
   * RESET_H     3 //mega_head   (U12 on RB)
   * RESET_W     2 //mega_wheel  (U09 on RB)

## Rugby_board sanity test 
* We have added LEDs to pin digital 10 on each MCU for sanity test
* Upload "rugby-2560-blink" when testing 2560
* Upload "rugby-328-blink" when testing 328P

## Upload code (1st arg is the device, 2nd arg is the code to upload)
    $ sudo python upload.py 328p_follow rugby-328-blink

## Reference 
  http://docs.platformio.org/en/latest/installation.html
  
  http://docs.platformio.org/en/latest/platforms/atmelavr.html#custom-fuses
