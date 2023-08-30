#include <AccelStepper.h>

/*Global Variable*/
unsigned long start_Time;

float v1;
float v2;
float v3;
/*CODE*/
AccelStepper ystepper(1,oc4a,oc4b);
AccelStepper rtstepper(1,oc2a,oc1a);
AccelStepper ltstepper(1,oc5b,oc5c);

void setup()
{
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

void circ(unsigned long t)
{
	float arg;
	unsigned long current_Time = millis();
	while (current_Time - t <= 15000)
	{
		arg = 3.1416*0.133333*((current_Time - t)/1000.0);
		inv_kin(-sin(arg),cos(arg),0);
		current_Time = millis();
	}
}

void move_bot()
{
	start_Time=millis();
  circ(start_Time);
}

void loop() {
  // put your main code here, to run repeatedly:
 move_bot();
}

