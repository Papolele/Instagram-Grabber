int x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(D4, OUTPUT);
  digitalWrite(D4, HIGH);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.print("Returned:");
  Serial.print(x);
  if (x == 1){
    Serial.print("Recieved 1!");
    digitalWrite(D4, LOW);
    delay(2000);
    digitalWrite(D4, HIGH);
    delay(2000);
    Serial.print("Drill Spinned");
  }
}
