#ifndef UNIT_TEST

#include <Arduino.h>

void setup() {
    Serial.begin(115200);
}

void loop() {
  Serial.println("Hallo!!");
  delay(1000);
}

#endif
