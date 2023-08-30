#include <AccelStepper.h>

/*Global Variable*/
unsigned long start_Time;

float v1;
float v2;
float v3;

AccelStepper ystepper(1,oc4a,oc4b);
AccelStepper rtstepper(1,oc2a,oc1a);
AccelStepper ltstepper(1,oc5b,oc5c);

void setup() {
  // put your setup code here, to run once:
  ystepper.setMaxSpeed(1000);
  rtstepper.setMaxSpeed(1000);
  ltstepper.setMaxSpeed(1000);
  
}

void inv_kin(float Vx,float Vy,float W)
{
  v1 = 0.66667*Vx + 1.90661*W;
  v2 = -0.333333*Vx + 0.57737*Vy + 1.90661*W;
  v3 = -0.333333*Vx - 0.57737*Vy + 1.90661*W;
  ystepper.setSpeed(v1*400);
  rtstepper.setSpeed(v2*400);
  ltstepper.setSpeed(v3*400);
  ystepper.runSpeed();
  rtstepper.runSpeed();
  ltstepper.runSpeed();
}

void Tri(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 9100 )
	{
		if (current_Time -t <= 3000)
		{
			inv_kin(0,1,0);
			current_Time = millis();	
		}
			if(3000< current_Time-t <3050){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    } 
		if (current_Time - t <= 6050 && current_Time - t>=3050) 
		{
			inv_kin(0.866025,-0.5,0);
			current_Time = millis();
		}
  	if(6050< current_Time-t <6100){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    }
		if (current_Time - t >= 6100)
		{
			inv_kin(-0.866025,-0.5,0);
			current_Time = millis();	
		}
  }
}

void move_bot()
{
  start_Time = millis();
  Tri(start_Time);
  delay(1000);
}

void loop()
{
  // put your main code here, to run repeatedly:
 move_bot();
}

