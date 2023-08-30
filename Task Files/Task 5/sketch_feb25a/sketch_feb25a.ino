#include <WiFi.h>

// WiFi credentials
const char* ssid = "Pixel Dude...";                    //Enter your wifi hotspot ssid
const char* password = "hehehe...";               //Enter your wifi hotspot password
const uint16_t port = 8002;
const char * host = "192.168.197.140";                   //Enter the ip address of your laptop after connecting it to wifi hotspot



char incomingPacket[80];
WiFiClient client;

String msg = "0";

int ledPin = 18;


void setup(){
   pinMode(ledPin , OUTPUT);
  Serial.begin(115200);                          //Serial to print data on Serial Monitor
  Serial1.begin(115200,SERIAL_8N1,33,32);        //Serial to transfer data between ESP and AVR. The Serial connection is inbuilt.
  
  
  //Connecting to wifi
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
}


void loop() {
digitalWrite(ledPin , HIGH);


  if (!client.connect(host, port)) {
    Serial.println("Connection to host failed");
    delay(200);
    return;
  }

  while(1){
      msg = client.readStringUntil('\n');         //Read the message through the socket until new line char(\n)
      client.print("Hello from ESP32!");          //Send an acknowledgement to host(laptop) 
      Serial.println(msg);                        //Print data on Serial monitor
      Serial1.println(msg);                       //Send data to AVR
      Serial1.flush();
    }
}
