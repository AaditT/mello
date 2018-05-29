# mello.py - Mello.
# Written by Srihari Nanniyur.
# Please do not change this file in Git. Copy it into your system instead.

from random import shuffle
import os
import json
import requests
# import RPi.GPIO as GPIO
import time
import led

CHROMATIC = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
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

def get_emotion():
    os.system('curl --upload-file ./img.jpg https://transfer.sh/img.jpg > TRANSFER_OUTPUT')
    transfer_url = open('TRANSFER_OUTPUT', 'r').read()
    print(transfer_url)

    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
    headers = {'Ocp-Apim-Subscription-Key': 'a5516f68a93944fbabe4458aaf8843ea'}
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion'
    }

    response = requests.post(
        face_api_url, params=params, headers=headers, json={"url": transfer_url})
    emotions = response.json()[0]['faceAttributes']['emotion']
    largest = 'neutral'
    for elem in emotions:
        if emotions[str(elem)] >= emotions[str(largest)]:
            largest = str(elem)
    print(largest)
    return largest

def choose_melody_params():
    emotion = get_emotion()
    key = ''
    speed = ''
    scale = []
    if emotion == 'happiness':
        key = 'C'
        scale = NATURAL_MAJOR
        speed = 'med'
    elif emotion == 'sadness':
        key = 'C'
        scale = BLUES
        speed = 'long'
    elif emotion == 'anger':
        key = 'E'
        scale = CHROMATIC
        speed = 'short'
    elif emotion == 'fear':
        key = 'D#'
        scale = WHOLE_TONE
        speed = 'med'
    elif emotion == 'surprise':
        key = 'G#'
        scale = PENTA_MAJOR
        speed = 'short'
    elif emotion == 'contempt':
        key = 'Dm'
        scale = HARMONIC_MINOR
        speed = 'med'
    elif emotion == 'disgust':
        key = 'Gm'
        scale = BLUES
        speed = 'med'
    else:
        key = 'G'
        scale = NATURAL_MAJOR
        speed = 'med'
    return {'emotion': emotion,
            'key'    : key,
            'scale'  : scale,
            'speed'  : speed}

wav_files = {
    "A" : "A.wav",
    "B" : "B.wav",
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

os.system('fswebcam img.jpg')
melody_params = choose_melody_params()

def play_notes(notes, length, c):
    cmd = c + " "
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
        cmd += directory + wav_files[note] + " "
        print(cmd)
        print(melody_params['emotion'])
        led.outColor(melody_params['emotion'])
        os.system(cmd)
        cmd = c + ' '

play_notes(Generator(melody_params['key']).melody(melody_params['scale'], 16), melody_params['speed'], "play")
