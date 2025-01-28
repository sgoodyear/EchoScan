int PWMin = 3;     // connect pin 3 of the Arduino to the PWM output pin of the ultrasonic sensor
float distance;
int enPin = 2;     // connect pin 2 of the Arduino to the enable/disable pin of the ultrasonic sensor

////////////
#include <Stepper.h>
const int stepsPerRevolution = 200;                    // Number of steps per output rotation
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
////////////////

void setup() {
  Serial.begin(9600);                                  // Make sure this Baud rate matches the Python program
  pinMode(PWMin, INPUT);
  pinMode(enPin, OUTPUT);

  digitalWrite(enPin, LOW);

  // set the speed at 60 rpm:
  myStepper.setSpeed(30);

  delay(100);
}

void loop() {
  digitalWrite(enPin, HIGH);                          // Trigger a measurement from the sensor
  delayMicroseconds(50);
  digitalWrite(enPin, LOW);
  distance = pulseIn(PWMin, HIGH)/25.4;               // Recieve the PWM output from the sensor (Converting the output from centimeters to inches)

  if(distance){                                       // Ignore non-data results
  myStepper.step(stepsPerRevolution/(2*40*(4/3)));    // Rotate the stepper motor by 5 degrees
  Serial.println(distance, 0);                        // Print the distance for the Python program to use
  }
}
