from time import sleep
import RPi.GPIO as GPIO

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


def red(): ind_blink (11)
def green(): ind_blink (13)
def blue(): ind_blink (15)

# red()
# green()
# blue()
