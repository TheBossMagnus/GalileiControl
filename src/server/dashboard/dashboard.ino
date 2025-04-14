// Arduino sketch for controlling multiple RGB LEDs via serial communication
// Format for serial input: "X.RRR.GGG.BBB" where X is LED index (0-1), RRR, GGG, BBB are RGB values (000-255)

const int ledPins[2][3] = {
    {3, 5, 6},  // LED 0: R,G,B pins
    {9, 10, 11} // LED 1: R,G,B pins
};

void setup() {
    Serial.begin(9600); // Initialize serial communication
    
    // Set all LED pins as OUTPUT
    for(int i=0; i<2; i++){      // Fixed: loop over 2 LEDs, not 3
        for(int j=0; j<3; j++){
            pinMode(ledPins[i][j], OUTPUT);
        }
    }
    
    // Confirm device is ready
    Serial.println("RGB LED Controller Ready");
}

void rgbLedDisplay(int ledPinR, int ledPinG, int ledPinB, int red, int green, int blue) {
    // Set three ledPin to output the PWM duty cycle
    analogWrite(ledPinR, constrain(red, 0, 255));
    analogWrite(ledPinG, constrain(green, 0, 255));
    analogWrite(ledPinB, constrain(blue, 0, 255));
}

void loop() {
    if(Serial.available() > 0) { // Check if data is available
        String input = Serial.readStringUntil('\n'); // Read string until newline
        input.trim(); // Remove whitespace
        
        // Check if input has the correct format and length
        if(input.length() >= 13) {
            // Extract values from received string (e.g., "1.200.200.200" -> LED 1, R 200, G 200, B 200)
            int indiceLed = input.substring(0, 1).toInt(); // LED index
            int r = input.substring(2, 5).toInt();         // Red value
            int g = input.substring(6, 9).toInt();         // Green value
            int b = input.substring(10, 13).toInt();       // Blue value
          
            // Debug output to serial
            Serial.print("LED: ");
            Serial.print(indiceLed);
            Serial.print(" | RGB: ");
            Serial.print(r);
            Serial.print(", ");
            Serial.print(g);
            Serial.print(", ");
            Serial.println(b);
            
            // Set LED color if index is valid (0 or 1)
            if(indiceLed >= 0 && indiceLed < 2){  // Fixed: check for < 2, not < 3
                rgbLedDisplay(ledPins[indiceLed][0], ledPins[indiceLed][1], ledPins[indiceLed][2], r, g, b);
                Serial.println("LED color set successfully");
            } else {
                Serial.println("Error: Invalid LED index (must be 0 or 1)");
            }
        } else {
            Serial.println("Error: Invalid input format. Use 'X.RRR.GGG.BBB'");
        }
    }
}
