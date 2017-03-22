#define RELAY 10

void setup() {
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY,HIGH);
  Serial.begin (57600);
}

void loop() {
  if (Serial.available() > 0) {
    char readChar = (char)Serial.read();
    if (readChar == 'n')
      digitalWrite(RELAY,HIGH);
    if (readChar == 'f')
      digitalWrite(RELAY,LOW);  
  }

}
