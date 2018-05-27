import sys
import time

import RPi.GPIO as GPIO

redPin = 11
greenPin = 13
bluePin = 15

def turnOn(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

# pre-made color classes

class color:
    class red:
        def on(self): turnOn(redPin)
        def off(self): turnOff(redPin)
    class green:
        def on(self): turnOn(greenPin)
        def off(self): turnOff(greenPin)
    class blue:
        def on(self): turnOn(bluePin)
        def off(self): turnOff(bluePin)
    class yellow:
        def on(self):
            turnOn(redPin)
            turnOn(greenPin)
        def off(self):
            turnOff(redPin)
            turnOff(greenPin)
    class magenta:
        def on(self):
            turnOn(redPin)
            turnOn(bluePin)
        def off(self):
            turnOff(redPin)
            turnOff(bluePin)
    class cyan:
        def on(self):
            turnOn(bluePin)
            turnOn(greenPin)
        def off(self):
            turnOff(bluePin)
            turnOff(greenPin)

myRed = color.red
myGreen = color.green
myBlue = color.blue       
myYellow = color.yellow
myMagenta = color.magenta
myCyan = color.cyan
