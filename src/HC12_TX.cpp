#include <Arduino.h>

#define POT A0
#define LED 12
#define LDX 3
#define SET 2

String val;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(LDX,OUTPUT);
  pinMode(SET,OUTPUT);
  digitalWrite(LDX,LOW);
  digitalWrite(SET,HIGH);
  delay(80);
  Serial.begin(9600);
  digitalWrite(LED,HIGH);
}

void loop() {
if (Serial.available() > 0) {
  String val = Serial.readStringUntil('\n');  // or '\r' depending on sender
  val.trim();
  if (val == "MX") {
    digitalWrite(LDX, HIGH);
  }
}
  Serial.write(map(analogRead(POT),0,1023,0,255));
  delay(125);
}