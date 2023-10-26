#include <Servo.h>

const int analogIn = A0;    // Assuming A0 is the analog pin
const int servoPin = 9;     // Pin 9 is connected to the motor
int temperatureLimit = 23;  // Initial temperature limit
int RawValue = 0;
double Voltage = 0;
double tempC = 0;
double tempF = 0;
Servo Servo1;

void setup() {
  Serial.begin(9600);  // Assuming 9600 is the baud rate
  Servo1.attach(servoPin);
}

void loop() {
  // If there are data available on the serial port
  if (Serial.available()) {
    temperatureLimit = Serial.parseInt();  // Read the temperature limit from C#
    RawValue = analogRead(analogIn);
    Voltage = (RawValue / 1023.0) * 5000;  // Use 1023 for a 10-bit ADC and multiply by 5000 to get millivolts
    tempC = Voltage / 10;                  // Assuming a 10mV per degree Celsius scale
    tempF = (tempC * 1.8) + 32;            // Convert to Fahrenheit
    Serial.println(tempC, 1);
    if (tempC > temperatureLimit) {
      // Make servo go to 0 degrees
      Servo1.write(0);
      delay(1000);  // Assuming a delay of 1 second

      // Make servo go to 90 degrees
      Servo1.write(90);
      delay(1000);  // Assuming a delay of 1 second

      // Make servo go to 180 degrees
      Servo1.write(180);
      delay(1000);
    } else {            // Assuming a delay of 1 second
      Servo1.detach();  // Detach the servo
    }
    delay(500);  // Assuming a delay of half a second
  }
}
