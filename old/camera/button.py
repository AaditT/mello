import RPi.GPIO as GPIO
import time

# button boolean ensures that button is only pressed once
button = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  input_state = GPIO.input(18)
  if input_state == False:
    if button == False:
      print("Button pressed)
      # time delay prevents button spam
      time.sleep(2)
      # makes sure that button command is only ran once
      button = True
      # generate melody here...
    else:
      print("Button already pressed")
      time.sleep(2)
      
