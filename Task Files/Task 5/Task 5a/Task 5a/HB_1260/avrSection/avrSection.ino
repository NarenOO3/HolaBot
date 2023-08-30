const int r0 = oc5c;
const int y0 = oc5a;
const int g0 = oc1a;
const int r1 = oc2b;
const int y1 = oc4b;
const int g1 = oc3a;
const int r2 = oc4a;
const int y2 = oc4c;
const int g2 = oc2a;
const int r3 = oc1b;
const int y3 = oc0a;
const int g3 = oc5b;
typedef union {
  int floatingPoint;
  byte binary[2];
} binaryFloat;

int incoming[4];

int r = 6;
int g = 8;
int b = 7;

void publish(unsigned long T);


void setup() {
  Serial.begin(115200);

  pinMode(r0,OUTPUT);
  pinMode(y0,OUTPUT);
  pinMode(g0,OUTPUT);
    pinMode(r1,OUTPUT);
  pinMode(y1,OUTPUT);
  pinMode(g1,OUTPUT);
    pinMode(r2,OUTPUT);
  pinMode(y2,OUTPUT);
  pinMode(g2,OUTPUT);
    pinMode(r3,OUTPUT);
  pinMode(y3,OUTPUT);
  pinMode(g3,OUTPUT);
      pinMode(r,OUTPUT);
  pinMode(g,OUTPUT);
  pinMode(b,OUTPUT);
  
  // put your setup code here, to run once:}

   analogWrite(r,255);
   analogWrite(g,255);
   analogWrite(b,255);
}

void loop() {
  if (Serial.available() >= sizeof(incoming)) { // check if the array has been received
    Serial.readBytes((byte*)incoming,sizeof(incoming));
    
}
publish(); 
  Serial.println(incoming[0]);
  Serial.println(incoming[1]);
  Serial.println(incoming[2]); 
  Serial.println(incoming[3]);
  
 
  
}

void publish(){
if(incoming[0]==1){
  digitalWrite(r0,HIGH);
  digitalWrite(g0,HIGH);

  digitalWrite(y0,HIGH);
  digitalWrite(g0,LOW);
}



if(incoming[1]==1){
  digitalWrite(r1,HIGH);
  digitalWrite(g1,HIGH);

  digitalWrite(y1,HIGH);
  digitalWrite(g1,LOW);
        }

if(incoming[2]==1){
  digitalWrite(r2,HIGH);
  digitalWrite(g2,HIGH);

  digitalWrite(y2,HIGH);
  digitalWrite(g2,LOW);
}if(incoming[3]==1){
  digitalWrite(r3,HIGH);
  digitalWrite(g3,HIGH);

  digitalWrite(y3,HIGH);
  digitalWrite(g3,LOW);
}
if(incoming[0]==0){
  digitalWrite(r0,HIGH);
  digitalWrite(g0,HIGH);
 
  
  digitalWrite(y0,HIGH);
  digitalWrite(r0,LOW);
}
if(incoming[1]==0){
  digitalWrite(r1,HIGH);
  digitalWrite(g1,HIGH);
  

  digitalWrite(y1,HIGH);
  digitalWrite(r1,LOW);
}
if(incoming[2]==0){
  digitalWrite(r2,HIGH);
  digitalWrite(g2,HIGH);
  

  digitalWrite(y2,HIGH);
  digitalWrite(r2,LOW);
}
if(incoming[3]==0){
  digitalWrite(r3,HIGH);
  digitalWrite(g3,HIGH);


  digitalWrite(y3,HIGH);
  digitalWrite(r3,LOW);
}
  }