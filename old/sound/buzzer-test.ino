/*
   Modified from https://tkkrlab.nl/wiki/Arduino_KY-038_Microphone_sound_sensor_module
*/
int val = 0;
void setup ()
{
  pinMode (13, OUTPUT) ;
  pinMode (3, INPUT) ;
}
void loop ()
{
  val = digitalRead(buttonpin);
  if (val == HIGH)
  {
    digitalWrite (Led, HIGH);
  }
  else
  {
    digitalWrite (Led, LOW);
  }
}
