//Activates buzzer
//Created by Aadit Trivedi

//still needs to configure specific notes

int speakerPin = 8;
void setup () {
  pinMode (speakerPin, OUTPUT);
}
void loop () {
  analogWrite (speakerPin, 185);
  delay(1);
  analogWrite (speakerPin, 0);
  delay(1);
}
