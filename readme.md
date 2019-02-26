## Description
Code for running lap timer.

### Update code:
```
esptool.py --chip esp32 --port /dev/tty.wchusbserial1420 erase_flash
esptool.py --chip esp32 --port /dev/tty.wchusbserial1420 write_flash -z 0x1000 esp32-20180730-v1.9.4-414-gf6f6452b6.bin
ampy -d 0.5 -p /dev/tty.wchusbserial1420 -b 115200 put max7219.py
ampy -d 0.5 -p /dev/tty.wchusbserial1420 -b 115200 put boot.py
```

### Firmware:
* https://micropython.org/download/#esp32 (esptool.py --chip esp32 --port /dev/ttyUSB1 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin)

### Guides:
* https://boneskull.com/micropython-on-esp32-part-1/
* http://cxem.net/calc/ledcalc.php
* https://bytes.com/topic/python/answers/442320-converting-milliseconds-human-time
* http://docs.micropython.org/en/latest/pyboard/library/framebuf.html

### Datasheets:
* https://pdf1.alldatasheet.com/datasheet-pdf/view/218330/OSRAM/SFH4550.html

### ampy:
* ```ampy -d 0.5 -p /dev/tty.wchusbserial14130 -b 115200 ls```

### code_samples:
```
s=ms/1000
m,s=divmod(s,60)
```
