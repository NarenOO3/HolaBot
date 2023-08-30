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
	//BLA::Matrix<3,1> body_vel = {Vx,Vy,W};
	//BLA::Matrix<3,3> trans_mat = {0.66667,0,1.90661,-0.333333,0.57737,1.90661,-0.333333,-0.57737,1.90661};
	//BLA::Matrix<3,1> wheel_vel = trans_mat* body_vel;
	// BLA::speed_of_each_wheel(wheel_vel(1,1),wheel_vel(2,1),wheel_vel(3,1));
  v1 = 0.66667*Vx + 1.90661*W;
  v2 = -0.333333*Vx + 0.57737*Vy + 1.90661*W;
  v3 = -0.333333*Vx - 0.57737*Vy + 1.90661*W;

  Serial.println(v1);

  ystepper.setSpeed(v1*400);
  rtstepper.setSpeed(v2*400);
  ltstepper.setSpeed(v3*400);
  ystepper.runSpeed();
  rtstepper.runSpeed();
  ltstepper.runSpeed();


}
void UD(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 6200 )
	{
		if (current_Time -t <= 3000)
		{
			inv_kin(0,1,0);

			current_Time = millis();	
		}
    if(3000< current_Time-t <3200){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    }
		if (current_Time - t >= 3200)
		{
			inv_kin(0,-1,0);
			current_Time = millis();
		}
	}
}

void LR(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 6500 )
	{
		if (current_Time -t <= 3000)
		{
			inv_kin(-1,0,0);
			current_Time = millis();	
		}
		if(3000< current_Time-t <3500){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    }
		if (current_Time - t >= 3500)
		{
			inv_kin(1,0,0);
			current_Time = millis();
		}
	}	
}

void Tri(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 15400 )
	{
		if (current_Time -t <= 5000)
		{
			inv_kin(0,1,0);
			current_Time = millis();	
		}
			if(5000< current_Time-t <5200){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    } 
		if (current_Time - t <= 10200 && current_Time - t>=5200) 
		{
			inv_kin(0.866025,-0.5,0);
			current_Time = millis();
		}
  	if(10200< current_Time-t <10400){
      inv_kin(0, 0, 0);
      	current_Time = millis();
    }
		if (current_Time - t >= 10400)
		{
			inv_kin(-0.866025,-0.5,0);
			current_Time = millis();	
		}

	}
}

void circ(unsigned long t)
{
	 int a=1;
	float arg;
	unsigned long current_Time = millis();
	while (current_Time - t <= 10000)
	{
		arg = 3.1416*0.2*((current_Time - t)/1000.0);
		inv_kin(-a*sin(arg),a*cos(arg),0);
    //delay(100);
		current_Time = millis();
   // Serial.println(-a*sin(arg));
 // Serial.println(a*cos(arg));
  
  
	}
}

void move_bot()
{
	start_Time = millis();
	UD(start_Time);
  delay(500);
  	start_Time = millis();
	LR(start_Time);
   delay(500);
  // start_Time = millis();
  // Tri(start_Time);
  // start_Time=millis();
  // circ(start_Time);
 }





void loop() {
  // put your main code here, to run repeatedly:
 move_bot();
 
}

