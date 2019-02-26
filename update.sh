#!/bin/bash

if [ "$1" != "" ]; then
    #echo "Positional parameter 1 contains something"
    PORT = "/dev/tty.wchusbserial"$1
else
    #echo "Positional parameter 1 is empty"
    ls /dev/tty.wchusbserial1420*
    PORT = '/dev/tty.wchusbserial1420'
fi

FIRMWARE = 'esp32-20180730-v1.9.4-414-gf6f6452b6.bin'

echo "Erace flash"
echo '--chip esp32 --port '${PORT}' erase_flash'
`esptool.py --chip esp32 --port ${PORT} erase_flash`
sleep 5
echo "Load fimware"
`esptool.py --chip esp32 --port ${PORT} write_flash -z 0x1000 ${FIRMWARE}`
sleep 5
echo "load lib MAX7219"
`ampy -d 0.5 -p ${PORT} -b 115200 put max7219.py`
sleep 2
echo "load code"
`ampy -d 0.5 -p ${PORT} -b 115200 put boot.py`
echo "Please reboot board"

