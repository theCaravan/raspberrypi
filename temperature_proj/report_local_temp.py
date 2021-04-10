from sense_hat import SenseHat
from time import sleep
import socket
import time
import os
import random
from datetime import date
from datetime import datetime

OFFSET_LEFT = 1
OFFSET_TOP = 2

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,1,1,1]  # 9

# Gathers time and temperature stats
def get_weather():
  today = date.today()
  time_now = datetime.now()
  os_temp = os.popen('/opt/vc/bin/vcgencmd measure_temp')
  cputemp = os_temp.read()
  cputemp = cputemp.replace('temp=','')
  cputemp = cputemp.replace('\'C\n','')
  cputemp = (float(cputemp) * 1.8) + 32

  # Primary
  temp = (sense.get_temperature_from_pressure() * 1.8) + 32
  temp = temp - ((cputemp - temp) / 2)
  humidity = sense.get_humidity()
  pressure = sense.get_pressure() / 33.864
  orientation = sense.get_orientation_degrees()

  # Secondary
  dew_point = temp * (humidity / 100)

  return {
	"temp": temp,
	"humidity": humidity,
	"pressure": pressure,
	"dew_point": dew_point,
	"today": today,
	"time_now": time_now,
	"orientation": orientation
	}


# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])


# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)


# Randomize between green, blue, or red to allow even LED usage
r = 0
g = 0
b = 0

rgb_dominant = random.randint(1,3)

if rgb_dominant == 1:
  r = 200
  g = 20
  b = 20

elif rgb_dominant == 2:
  r = 20
  g = 200
  b = 20

elif rgb_dominant == 3:
  r = 20
  g = 20
  b = 200

##

sense = SenseHat()
sense.clear()

output_text = ""

weather  = get_weather()

output_text += "--- {} ~ Current as of {} @ {} ---\n".format(socket.gethostname(), weather["today"].strftime("%m/%d/%Y"), weather["time_now"].strftime("%H:%M:%S"))
output_text += "Temperature: {:.2f}*F\n".format(weather["temp"])
output_text += "Humidity: {:.2f}%\n".format(weather["humidity"])
output_text += "Dew Point: {:.2f}*F\n".format(weather["dew_point"])
output_text += "Pressure: {:.2f} inHg\n".format(weather["pressure"])
output_text += "\nOrientation: Pitch: {:.0f}* ~ Roll: {:.0f}* ~ Yaw: {:.0f}*\n".format(weather["orientation"]["pitch"], weather["orientation"]["roll"], weather["orientation"]["yaw"])

print(output_text)

while True:
  weather  = get_weather()
  show_number(int(weather["temp"]), r, g, b)
  with open ("temp_output", "w") as rw:
    to_write = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(weather["temp"],weather["humidity"],weather["dew_point"],weather["pressure"],weather["today"],weather["time_now"],weather["orientation"])
    rw.write(to_write)
    rw.close()
  time.sleep(3)


sense.clear()



