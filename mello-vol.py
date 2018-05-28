# mello.py - algorithms for Mello.
# Written by Srihari Nanniyur and Aadit Trivedi

from random import shuffle
import os
import RPi.GPIO as GPIO
import time

WHOLE_TONE = [2, 2, 2, 2, 2]
NATURAL_MAJOR = [2, 2, 1, 2, 2, 2]
NATURAL_MINOR = [2, 1, 2, 2, 1, 2]
HARMONIC_MINOR = [2, 1, 2, 2, 1, 3]
PENTA_MAJOR = [2, 2, 3, 2]
PENTA_MINOR = [3, 2, 2, 3]
BLUES = [3, 2, 1, 1, 3]

class Generator():
    def __init__(self, key):
        self.key = key
        if len(self.key) > 2 or len(self.key) < 1:
            raise Exception('Invalid key signature!')
        if len(self.key) == 1:
            self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'A#']
        elif self.key[1] == '#':
            self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        elif self.key[1] == 'b':
            self.notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    def melody(self, intervals, num):
        result = []
        options = []
# And now for the greatest line of code ever written
        order = self.notes[self.notes.index(self.key):len(self.notes)] + self.notes[0:self.notes.index(self.key)]
        j = 0
        for i in intervals:
            if j > len(order):
                break
            options.append(order[j])
            j += i
        options.append(order[j])
        for x in range(0, num):
            shuffle(options)
            result.append(options[int(len(options) / 2)])
        return result


wav_files = {
    "A" : "A.wav",
    "Bb": "Bflat.wav",
    "A#": "Bflat.wav",
    "C" : "C.wav",
    "Db": "Csharp.wav",
    "C#": "Csharp.wav",
    "D" : "D.wav",
    "Eb": "Eflat.wav",
    "D#": "Eflat.wav",
    "E" : "E.wav",
    "F" : "F.wav",
    "Gb": "Fsharp.wav",
    "F#": "Fsharp.wav",
    "G" : "G.wav",
    "Ab": "Gsharp.wav",
    "G#": "Gsharp.wav"
}

def get_vol():
	# insert code to retrieve value from potentiometer
	# below line is just a filler line
	return(0.5)

def play_notes(notes, length, c):
	
	# get the volume factor from potentiometer value
	volume_factor = 0.5
    
	cmd = c + " "
	
	vol = "-v "
	vol += str(volume_factor)
    
	directory = ""
    if length == "short":
        directory = "shortWAV/"
    elif length == "med":
        directory = "medWAV/"
    elif length == "long":
        directory = "longWAV/"
    else:
        raise Exception("play_note(): Invalid length!")
    for note in notes:
        cmd += "-v " + str(get_vol()) + " " + directory + wav_files[note] + " "
    print(cmd)
    os.system(cmd)

def analyze_face():
    pass

button = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        if button == False:
            print("Button pressed.")
            time.sleep(2)
            button = True
            os.system("fswebcam face.jpg")
            play_notes(Generator('A').melody(BLUES, 16), "short", "play")
        else:
            print("Button already pressed.")
            time.sleep(2)
