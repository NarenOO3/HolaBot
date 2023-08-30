const int STEP_PIN1 = oc4a;
const int STEP_PIN2 = oc2a;
const int STEP_PIN3 = oc5b;

const int DIR_PIN1 = oc4b;
const int DIR_PIN2 = oc1a;
const int DIR_PIN3 = oc5c;


// set desired velocities for each stepper motor
// start time for each motor


void setup() {
  // configure step and direction pins for each motor
  pinMode(STEP_PIN1, OUTPUT);
  pinMode(DIR_PIN1, OUTPUT);
  pinMode(STEP_PIN2, OUTPUT);
  pinMode(DIR_PIN2, OUTPUT);
  pinMode(STEP_PIN3, OUTPUT);
  pinMode(DIR_PIN3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(x>= -300){
    runSpeed(x,200,200);
    Serial.println("Hello");
    delayMicroseconds(100);

  }
  
}
