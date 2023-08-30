String msg = "0";

int r = 6;
int g = 7;
int b = 8;

void setup() {
  pinMode(r,OUTPUT);
  pinMode(g,OUTPUT);
  pinMode(b,OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  if(Serial.available()){                  //Check if any data is available on Serial
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

      Serial.println(values[0]); // prints "value1"
      Serial.println(values[1]); // prints "value2"
      Serial.println(values[2]); // prints "value3"  //Read message on Serial until new char(\n) which indicates end of message. Received data is stored in msg
    int x = msg.toInt();
  
//    if(x< 100){                         //If data is even, turn on Blue LED
//      analogWrite(r,255);
//      analogWrite(g,255);
//      analogWrite(b,0);
//    }
//    else{                                //If data is odd, turn on Red LED
//      analogWrite(r,0);
//      analogWrite(g,255);
//      analogWrite(b,255);
//    }
  }
}
