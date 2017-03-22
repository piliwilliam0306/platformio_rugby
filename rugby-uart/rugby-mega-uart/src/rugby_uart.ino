void setup() {
  // initialize digital pin 10 as an output.
  pinMode(13, OUTPUT);
  Serial.begin (57600);
  Serial1.begin (57600);
  Serial2.begin (57600);
  Serial3.begin (57600);
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available() > 0) {
    char readChar = (char)Serial.read();
    //mega_base
    if (readChar == 'l')
      Serial1.write('l');
    if (readChar == 'r')
      Serial2.write('r');
    if (readChar == 'i')
      Serial3.write('i');
    //mega_head
    if (readChar == 'p')
      Serial1.write('p');
    if (readChar == 't')
      Serial2.write('t');
  }
}
