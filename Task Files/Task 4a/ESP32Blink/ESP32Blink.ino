int ledPin = 18;

void setup() {
  pinMode(ledPin , OUTPUT);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(ledPin , HIGH);
  Serial.println("Hi");
  delay(500);
  digitalWrite(ledPin , LOW);
  delay(500);
}
