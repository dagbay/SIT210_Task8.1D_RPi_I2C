#include <Wire.h>

int led = D7; // The in-built LED.

void setup() {
    Wire.begin(0x8); // Set slave device address as 0x8.
    Wire.onReceive(receiveEvent); // Receives data sent by the master.
    
    pinMode(led, OUTPUT); // Sets the LED as output.
    digitalWrite(led, LOW); // Sets the LED off.
}

void receiveEvent(int amount) { 
    while (Wire.available()) { // While the connection is available.
        char c = Wire.read(); // Variable c will read from its master.
        digitalWrite(led, c); // The LED will take in the byte sent by the master to either turn on or off.
    }
}
