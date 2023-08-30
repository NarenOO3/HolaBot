#include <AccelStepper.h>

/*Global Variable*/
String msg = "0";
unsigned long start_Time;

float v1 = 0;
float v2 = 0;
float v3 = 0;

AccelStepper ystepper(1,oc4a,oc4b);
AccelStepper rtstepper(1,oc2a,oc1a);
AccelStepper ltstepper(1,oc5b,oc5c);

void aruco_feedback_Cb()
{  while(Serial.available()){                   //Check if any data is available on Serial
    msg = Serial.readStringUntil('\n');  
    String myString = msg;
    char * token;
    int index = 0;
    String values[3]; // create an array to store the values

    token = strtok((char *)myString.c_str(), ","); // convert the string to a character array and pass it to strtok

    while (token != NULL) {
      values[index] = token; // store the token in the array
      index++;
      token = strtok(NULL, ","); // get the next token
    }
    
      v1 = values[0].toFloat();
      v2 = values[1].toFloat();
      v3 = values[2].toFloat();
      ystepper.setSpeed(v1*10);
      rtstepper.setSpeed(v2*10);
      ltstepper.setSpeed(v3*10);
      ystepper.runSpeed();
      rtstepper.runSpeed();
      ltstepper.runSpeed();

}



    
}
/*CODE*/
void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  ystepper.setMaxSpeed(1000);
  rtstepper.setMaxSpeed(1000);
  ltstepper.setMaxSpeed(1000);
  ystepper.setSpeed(0);
  rtstepper.setSpeed(0);
  ltstepper.setSpeed(0);
  ystepper.runSpeed();
  rtstepper.runSpeed();
  ltstepper.runSpeed();
}

void loop() {
  // put your main code here, to run repeatedly: 
  aruco_feedback_Cb();

}
