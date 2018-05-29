from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def mult_blink(pin1, pin2):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin1, GPIO.OUT)
  GPIO.setup(pin2, GPIO.OUT)
  GPIO.output(pin1, GPIO.HIGH)
  GPIO.output(pin2, GPIO.LOW)
    

def red(): ind_blink (11)
def green(): ind_blink (13)
def blue(): ind_blink (15)
  
def yellow(): mult_blink(11,13)
def cyan(): mult_blink(13,15)
def magenta(): mult_blink(11,15)
