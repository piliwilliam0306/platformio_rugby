#define RELAY 10

void setup() {
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY, LOW);
  Serial.begin (57600);
}

void loop() {
  if (Serial.available() > 0) {
    char readChar = (char)Serial.read();
    if (readChar == 'f')
      {	
        digitalWrite(RELAY, HIGH);
        delay(100);
        digitalWrite(RELAY, LOW);  
      }
  }
}
