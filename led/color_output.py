import sys
import time
import random

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

def sad(num_notes):
    counter = 0
    colors = ["empty"]
    while (counter < num_notes):
        rand_color = random.randint(1, 3)
        if rand_color == 1: 
            if colors[counter] == "green": sad(num_notes - counter)
            else:
                turnOn(greenPin)
                colors.append("green")
        elif rand_color == 2: 
            if colors[counter] == "blue": sad(num_notes - counter)
            else:
                turnOn(bluePin)
                colors.append("blue")
        elif rand_color == 3:
            if colors[counter] == "magenta": sad(num_notes - counter)
            else:
                turnOn(bluePin)
                turnOn(redPin)
                colors.append("magenta")
        counter = counter + 1


#        time.sleep(0.25)
#        time.sleep(0.75)
#        time.sleep(1.5)
        counter = counter + 1

            
            
