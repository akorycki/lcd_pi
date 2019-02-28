import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class LCD:
  def __init__(self, d0, d1, d2, d3, d4, d5, d6, d7, EN, RS):
    self.d0 = d0
    self.d1 = d1
    self.d2 = d2
    self.d3 = d3
    self.d4 = d4
    self.d5 = d5
    self.d6 = d6
    self.d7 = d7
    self.EN = EN
    self.RS = RS    

    GPIO.setup(d0, GPIO.OUT)
    GPIO.setup(d1, GPIO.OUT)
    GPIO.setup(d2, GPIO.OUT)
    GPIO.setup(d3, GPIO.OUT)
    GPIO.setup(d4, GPIO.OUT)
    GPIO.setup(d5, GPIO.OUT)
    GPIO.setup(d6, GPIO.OUT)
    GPIO.setup(d7, GPIO.OUT)
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(RS, GPIO.OUT)


  
  def init_cursor(self):
    GPIO.output(self.RS, False)    
    GPIO.output(self.d0, False)
    GPIO.output(self.d1, False)
    GPIO.output(self.d2, True)
    GPIO.output(self.d3, True)
    GPIO.output(self.d4, False)
    GPIO.output(self.d5, False)
    GPIO.output(self.d6, False)
    GPIO.output(self.d7, False)

    GPIO.output(self.EN, True)
    time.sleep(0.0001)
    GPIO.output(self.EN, False)

  def clear_display(self):
    GPIO.output(self.RS, False)    
    GPIO.output(self.d0, True)
    GPIO.output(self.d1, False)
    GPIO.output(self.d2, False)
    GPIO.output(self.d3, False)
    GPIO.output(self.d4, False)
    GPIO.output(self.d5, False)
    GPIO.output(self.d6, False)
    GPIO.output(self.d7, False)

    GPIO.output(self.EN, True)
    time.sleep(0.0015)
    GPIO.output(self.EN, False)

  def write(self, str):
    GPIO.output(self.RS, True)

    for character in str:
      n = ord(character)
      #b0------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d0, a)
      #b1------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d1, a)
      #b2------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d2, a)
      #b3------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d3, a)
      #b4------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d4, a)
      #b5------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d5, a)
      #b6------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d6, a)
      #b7------------
      if n <= 0:
        a = False
      else:
        a = bool(float(n%2))
      n = (n-a)/2
      GPIO.output(self.d7, a)

      GPIO.output(self.EN, True)
      time.sleep(0.0015)
      GPIO.output(self.EN, False)

  def new_line(self):
    GPIO.output(self.RS, False)
    
    GPIO.output(self.d0, False)
    GPIO.output(self.d1, False)
    GPIO.output(self.d2, False)
    GPIO.output(self.d3, False)
    GPIO.output(self.d4, False)
    GPIO.output(self.d5, False)
    GPIO.output(self.d6, True)
    GPIO.output(self.d7, True)
 
    GPIO.output(self.EN, True)
    time.sleep(0.0001)
    GPIO.output(self.EN, False) 

  def function_set(self):
    GPIO.output(self.RS, False)
    
    GPIO.output(self.d0, False)
    GPIO.output(self.d1, False)
    GPIO.output(self.d2, True)
    GPIO.output(self.d3, True)#1-line mode= low, 2-line mode=high
    GPIO.output(self.d4, True)#8-bit mode = high, 4-bit mode = low
    GPIO.output(self.d5, True)
    GPIO.output(self.d6, False)
    GPIO.output(self.d7, False)
 
    GPIO.output(self.EN, True)
    time.sleep(0.0001)
    GPIO.output(self.EN, False)
    





  
  