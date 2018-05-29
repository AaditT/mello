from time import sleep
import RPi.GPIO as GPIO

short_len = 0.25
medium_len = 0.75
long_len = 1.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def ind_blink(pin):
  if (pin == 11) or (pin == 13) or (pin == 15):
    if (pin == 11):
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(13, GPIO.LOW)
      GPIO.output(15, GPIO.LOW)
    elif (pin == 13):
      GPIO.output(11, GPIO.LOW)
      GPIO.output(13, GPIO.HIGH)
      GPIO.output(15, GPIO.LOW)
    elif (pin == 15):
      GPIO.output(11, GPIO.LOW)
      GPIO.output(13, GPIO.LOW)
      GPIO.output(15, GPIO.HIGH)
  else: print("blink(): Invalid pin")
    
def mult_blink(pin1, pin2):
  GPIO.output(11, GPIO.LOW)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(15, GPIO.LOW)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.setup(pin2, GPIO.OUT)
  GPIO.output(pin1, GPIO.HIGH)
  GPIO.output(pin2, GPIO.HIGH)
    

def red(): ind_blink (11)
def green(): ind_blink (13)
def blue(): ind_blink (15)
  
def yellow(): mult_blink(11,13)
def cyan(): mult_blink(13,15)
def magenta(): mult_blink(11,15)
  
red()
sleep(0.5)
green()
sleep(0.5)
blue()
sleep(0.5)
yellow()
sleep(0.5)
cyan()
sleep(0.5)
magenta()
