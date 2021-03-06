# Platformio_rugby

## RB block diagram
<!--
![](https://github.com/piliwilliam0306/platformio_rugby/blob/master/RB_block.jpg)
-->
<img src="https://github.com/piliwilliam0306/platformio_rugby/blob/master/RB_block.jpg" alt="" align="left">

## Target ID list
  
Target ID | Part# | UART Thru   |
:--------:|:-----:|:-----------:|
328p_left |  U19  |mega_wheel U9|
328p_right|  U16  |mega_wheel U9|
328p_imu  |  U11  |mega_wheel U9|
328p_pan  |  U25  |mega_head U12|
328p_tilt |  U22  |mega_head U12|
328p_avoid|  U3   |FTDI U4      |
328p_dock |  U1   |FTDI U2      |
mega_head |  U12  |FTDI U13     |
mega_wheel|  U9   |FTDI U10     |

## Connector Pins 

Pins| Left (M1) right (M2)|Pan (M3) | (S1) | (S2) | Tilt (M4) | (S3) | (S4) | 328p_dock (J1)|
:--:|:-------------------:|:-------:|:----:|:----:|:---------:|:----:|:----:|:-------------:|
6   | OUT_A               | OUT_A   |  --  |  --  |  OUT_A    |  --  |  --  |  --           |
5   | OUT_B               | OUT_B   |  --  |  --  |  OUT_B    |  --  |  --  |  --           |
4   | GND                 | GND     |  --  |  --  |  GND      |  --  |  --  |  5V           |
3   | 5V                  | 5V      |  5V  |  5V  |  5V       |  5V  |  5V  |  Gnd          |
2   | HALL_A              | HALL_A  |  LA  |  LB  |  HALL_A   |  LA  |  LB  |  D5           |
1   | HALL_B              | HALL_B  |  GND |  GND |  HALL_B   |  GND |  GND |  D6           |

Pins| 328p_avoid (J3) | (J4) | (J5) | (J6) | 328p_program (J8) | 328p_IMU (J9) | mega_head (J10) | (J11) |        
:--:|:---------------:|:----:|:----:|:----:|:-----------------:|:-------------:|:---------------:|:-----:|
 7  |        --       |  --  | --   | 5V   |  --               |        --     |  --             | --    |
 6  |        --       |  --  | 5V   | GND  |  GND              |        --     |  --             | --    |
 5  |        --       |  --  | Gnd  | D10  |  RESET            |        5V     |  5V             | SCL   |
 4  |        5V       |  5V  | D6   | D11  |  MOSI             |        --     |  Gnd            | SDA   |
 3  |        Gnd      |  Gnd | D7   | D12  |  SCK              |        Gnd    |  SA0            | --    |
 2  |        D2       |  D4  | D8   | D13  |  5V               |        SCL    |  SA1            | GND   |
 1  |        D3       |  D5  | D9   | RESET|  MISO             |        SDA    |  SD2            | GND   |


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
    - programming uart functions to each MCU
    $ python uart-test.py
    - send a character to each MCU, see instruction when running this code.

## Checking target fuse 
    $ sudo platformio run -d ArduinoISP/328p_dock --target upload
    - replace 328p_dock when checking other targets
    $ avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m328p -v
    - fuse for 328p: efuse=0x05 hfuse=0xDA lfuse0xFF
    $ avrdude -P /dev/ttyUSB5 -b 19200 -c avrisp -p m2560 -v
    - fuse for 2560: efuse=0xFD hfuse=0xD8 lfuse0xFF

## Upload code for individual target (1st arg is the target, 2nd arg is the code to upload)
    $ sudo python upload.py 328p_dock rugby-blink/rugby-328-blink 
    
## Reference 
  [Installation Guide](http://docs.platformio.org/en/latest/installation.html)
  
  [Setting Custom Fuses](http://docs.platformio.org/en/latest/platforms/atmelavr.html#custom-fuses)

  [Setting Fuse with AVRdude](http://heliosoph.mit-links.info/arduinoisp-reading-writing-fuses-atmega328p/)
  
  [Fuse Table](http://www.martyncurrey.com/arduino-atmega-328p-fuse-settings/)
  
  [Arduino Default Fuse Settings](http://www.codingwithcody.com/2011/06/25/arduino-default-fuse-settings/)
  

