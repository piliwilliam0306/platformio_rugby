Import('env')
env.Replace(FUSESCMD="$UPLOADER $UPLOADERFLAGS -e -P $UPLOAD_PORT -b $UPLOAD_SPEED -Ulock:w:0x3F:m -Uefuse:w:0xfd:m -Uhfuse:w:0xDE:m -Ulfuse:w:0xff:m'")
