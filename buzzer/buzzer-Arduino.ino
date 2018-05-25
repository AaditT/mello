/*
Modified from https://www.arduino.cc/en/Tutorial/toneMelody
Open-source tone melody library
/*

#include "pitches.h"

/*
   this melody will be auto-generated based on machine learning by mellogen.py
   the melody below is just a placeholder
*/
int melody[] = {NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4};

int outputPin = 8;

/*
   the note durations will also be auto-generated based on machine learning by mellogen.py
   the note durations below are just placeholders
   these note durations correspond with the above melody
*/
int durations[] = {4, 8, 8, 4, 4, 4, 4, 4};

void setup() {
  for (int note = 0; note < 8; note++) {
    int noteDuration = 1000 / durations[note];
    tone(outputPin, melody[note], noteDuration);
    int pause = noteDuration * 1.30;
    delay(pause);
    noTone(8);
  }
}

void loop() {}
