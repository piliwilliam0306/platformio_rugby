Import("env")

#env.Replace(FUSESCMD="avrdude $UPLOADERFLAGS -e -Ulock:w:0x3F:m -Uhfuse:w:0xDE:m -Uefuse:w:0x05:m -Ulfuse:w:0xFF:m")
env.Replace(
        SETFUSECMD='$UPLOADER $UPLOADERFLAGS -e -P $UPLOAD_PORT -b $UPLOAD_SPEED -Ulock:w:0x3F:m -Uefuse:w:0xfd:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xff:m',
        UPLOADBOOTCMD='$UPLOADER $UPLOADERFLAGS -P $UPLOAD_PORT -b $UPLOAD_SPEED -Uflash:w:$SOURCES:i -Ulock:w:0xcF:m'
)

#bootloader_path = "../../arduino-1.6.10/hardware/arduino/avr/bootloaders/optiboot/optiboot_atmega328.hex"
bootloader_path = "../../arduino-1.6.10/hardware/arduino/avr/bootloaders/atmega/ATmegaBOOT_168_atmega328.hex"
uploadboot = env.Alias(
    "uploadboot", bootloader_path,
    [env.VerboseAction(env.AutodetectUploadPort, "Looking for upload port..."),
     env.VerboseAction("$SETFUSECMD", "Setting fuses"),
     env.VerboseAction("$UPLOADBOOTCMD", "Uploading bootloader $SOURCE")])
AlwaysBuild(uploadboot)
