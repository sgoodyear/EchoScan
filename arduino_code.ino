int PWMin = 3;
float distance;
int enPin = 2;

////////////
// Include the Arduino Stepper Library
#include <Stepper.h>
// Number of steps per output rotation
const int stepsPerRevolution = 200;
// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
////////////////

void setup() {
  Serial.begin(9600);
  pinMode(PWMin, INPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(enPin, LOW);

  // set the speed at 60 rpm:
	myStepper.setSpeed(30);

  delay(100);
}

void loop() {
  digitalWrite(enPin, HIGH);
  delayMicroseconds(50);
  digitalWrite(enPin, LOW);
  distance = pulseIn(PWMin, HIGH)/25.4;

  if(distance){
  myStepper.step(stepsPerRevolution/(2*40*(4/3)));
  Serial.println(distance, 0);
  }
}