import RPi.GPIO as GPIO
import time
import datetime
from LCD import LCD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def get_date():
  now = datetime.datetime.now()
  return (now.strftime("%a ") + now.strftime("%b ") + now.strftime("%d, ") + now.strftime("%Y"))

def get_time():
  now = datetime.datetime.now()
  return (now.strftime("%I:") + now.strftime("%M ") + now.strftime("%p"))

def start():
  display.write(get_time())
  display.new_line()
  display.write(get_date())
  now = datetime.datetime.now()
  sec = int(now.strftime("%S"))
  time.sleep(60-sec)
  display.clear_display()
  display.write(get_time())
  display.new_line()
  display.write(get_date())

def update():
  display.clear_display()
  display.write(get_time())
  display.new_line()
  display.write(get_date())
  
display = LCD(12, 16, 18, 22, 24, 26, 32, 36, 10, 8)

display.function_set()
display.init_cursor()
display.clear_display()

#start()

#while True:
  #time.sleep(60)
  #date = get_date()
  #time1 = get_time()
  #display.clear_display()
  #display.write(time1)
  #display.new_line()
  #display.write(date) 

# update()

current_time = ''
while True:
  t = get_time()
  if t != current_time:
    current_time = t
    update()
  time.sleep(1)
    
