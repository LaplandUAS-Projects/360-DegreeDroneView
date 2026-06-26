#include <Arduino.h>

#define THRESHOLD 5

#define FEEDBACK_PIN A0
#define SET 4
#define MOT_HIGH 5
#define MOT_LOW 6

uint8_t val = 0;

unsigned long lastSerialTime = 0;
const unsigned long timeout = 100; // ms — stop motor if no input in this time

// PWM timing
const unsigned long pwmPeriod = 10; // 10ms period = 100Hz
unsigned long pwmStart = 0;
bool motorOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(FEEDBACK_PIN, INPUT);
  pinMode(MOT_HIGH, OUTPUT);
  pinMode(MOT_LOW, OUTPUT);
  StopMotor();
}

void loop() {
  unsigned long now = millis();

  // --- Read serial input ---
  if (Serial.available() > 0) {
    val = Serial.read();
    lastSerialTime = now;
  }

  // --- Run PWM motor control ---
  if ((now - lastSerialTime) < timeout && val > THRESHOLD) {
    updateMotorPWM(val, now);
  } else {
    StopMotor();
  }

  // --- Feedback signal ---
  if (digitalRead(FEEDBACK_PIN)) {
    Serial.println("MX");
  }
}

void updateMotorPWM(uint8_t pulse, unsigned long now) {
  float duty = pulse / 255.0;
  unsigned long onTime = pwmPeriod * duty;
  unsigned long offTime = pwmPeriod - onTime;

  unsigned long elapsed = now - pwmStart;

  if (!motorOn && elapsed >= offTime) {
    // Turn motor ON
    digitalWrite(MOT_HIGH, HIGH);
    digitalWrite(MOT_LOW, LOW);
    pwmStart = now;
    motorOn = true;
  } else if (motorOn && elapsed >= onTime) {
    // Turn motor OFF
    digitalWrite(MOT_HIGH, LOW);
    digitalWrite(MOT_LOW, LOW);
    pwmStart = now;
    motorOn = false;
  }
}

void StopMotor() {
  digitalWrite(MOT_HIGH, LOW);
  digitalWrite(MOT_LOW, LOW);
  motorOn = false;
}