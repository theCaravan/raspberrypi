#!/usr/bin/env python3
# /etc/init.d/noor.py
### BEGIN INIT INFO
# Provides:          sample.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

#list = ["N", "o", "o", "r"]

#for i in list:
#	sense.show_letter(i)
#	sleep(0.5)

sense.clear()

sense.set_pixel(1, 1, (0, 0, 255))
sleep(0.1)
sense.set_pixel(1, 2, (0, 0, 255))
sleep(0.1)
sense.set_pixel(1, 3, (0, 0, 255))
sleep(0.1)
sense.set_pixel(1, 4, (0, 0, 255))
sleep(0.1)
sense.set_pixel(1, 5, (0, 0, 255))
sleep(0.1)
sense.set_pixel(1, 6, (0, 0, 255))
sleep(0.1)
sense.set_pixel(2, 2, (0, 0, 255))
sleep(0.1)
sense.set_pixel(3, 3, (0, 0, 255))
sleep(0.1)
sense.set_pixel(4, 4, (0, 0, 255))
sleep(0.1)
sense.set_pixel(5, 5, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 6, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 1, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 2, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 3, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 4, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 5, (0, 0, 255))
sleep(0.1)
sense.set_pixel(6, 6, (0, 0, 255))

temp = (sense.get_temperature_from_pressure() * 1.8) + 32
print(temp)

sleep(5)
sense.clear()
