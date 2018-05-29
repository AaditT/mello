from time import sleep
import RPi.GPIO as GPIO
import os, sys
from random import randint

short_len = 0.25
medium_len = 0.75
long_len = 1.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.setwarnings(False)

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

colorDict = {
  1:
    red,
  2:
    green,
  3:
    blue,
  4:
    yellow,
  5:
    cyan,
  6:
    magenta,
}

themes = {
  'sadness':
    [2, 3, 6],
  'happiness':
    [2, 4, 5],
  'anger':
    [1, 2, 6],
  'disgust':
    [1, 2, 6],
  'contempt':
    [1, 2, 6],
  'surprise':
    [4, 5, 6],
  'neutral':
    [1, 3, 4],
  'fear':
    [1, 2, 6],
}

func_str = {
  red:
    "red",
  green:
    "green",
  blue:
    "blue",
  yellow:
    "yellow",
  cyan:
    "cyan",
  magenta:
    "magenta",
}

def play_all_themes():
  for key in themes:
    colorArray = themes[key]
    for color in colorArray:
      functionToCall = colorDict[color]
      functionToCall()
      sleep(0.5)

def play_theme(theme, length):
  GPIO.output(11, 0)
  GPIO.output(13, 0)
  GPIO.output(15, 0)
  colorArray = themes[theme]
  for color in colorArray:
    colorFunc = colorDict[color]
    colorFunc()
    sleep(length)

def play_theme_length(theme, length, colorlen):
  GPIO.output(11, 0)
  GPIO.output(13, 0)
  GPIO.output(15, 0)
  counterc = 0
  lastcolor = " "
  while (counterc < colorlen):
    colorArray = themes[theme]
    color = randint(0,2)
    colorFunc = colorDict[colorArray[color]]
    if (colorFunc != lastcolor):
      lastcolor = colorFunc
      print(func_str[lastcolor])
      colorFunc()
      sleep(length)
      counterc = counterc + 1
    else:
      print("repeat")
      counterc = counterc + 1
      
# def printt(): while True: print("mello")

global iteration
iteration = 0
global history
history = [' ']


def outColor(theme):
  colorArray = themes[theme]
  color = randint(0,2)
  colorFunc = colorDict[colorArray[color]]
  if (func_str[colorFunc] == history[iteration]):
      while (func_str[colorFunc] == history[iteration]):
        outColor(theme)
  else:
    global history
    history.append(func_str[colorFunc])
    print(history)
    colorFunc()
    global iteration
    iteration = iteration + 1
    print(iteration)
#  printt()
  
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
outColor("neutral")
sleep(0.5)
