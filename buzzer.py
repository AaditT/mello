import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(15, GPIO.OUT) 

 
c_freq = 261
d_freq = 294
e_freq = 329 
f_freq = 349 
g_freq = 391 
gSH_freq = 415 
a_freq = 440 
aSH_freq = 455 
b_freq = 466 
cSH_freq = 554 
dSH_freq = 622 
fSH_freq = 740 
 


p = GPIO.PWM(15, 100)

def Blink(numTimes, speed, note):
    for i in range(0,numTimes): 
        print "Iteration " + str(i+1) 
        GPIO.output(7, True) 
        GPIO.output(15, True) 
        time.sleep(speed) ## Wait
        p.start(100)              
        p.ChangeDutyCycle(90)   
        if (note = "C"): p.ChangeFrequency(c_freq) 
        if (note = "C#"): p.ChangeFrequency(cSH_freq)  
        if (note = "D"): p.ChangeFrequency(d_freq)   
        if (note = "D#"): p.ChangeFrequency(dSH_freq) 
        if (note = "E"): p.ChangeFrequency(e_freq)   
        if (note = "F"): p.ChangeFrequency(f_freq) 
        if (note = "F#"): p.ChangeFrequency(fSH_freq) 
        if (note = "G"): p.ChangeFrequency(g_freq)    
        if (note = "G#"): p.ChangeFrequency(gSH_freq) 
        if (note = "A"): p.ChangeFrequency(a_freq) 
        if (note = "A#"): p.ChangeFrequency(aSH_freq)    
        if (note = "B"): p.ChangeFrequency(b_freq)    
        if (note = "C"): p.ChangeFrequency(c_freq)    
        p.stop()         

    GPIO.cleanup()
