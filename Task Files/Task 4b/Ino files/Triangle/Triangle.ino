#include <AccelStepper.h>
//#include <BasicLinearAlgebra.h>

/*Global Variable*/
unsigned long start_Time;

float v1;
float v2;
float v3;
/*CODE*/
const int STEP_PIN1 = oc4a;
const int STEP_PIN2 = oc2a;
const int STEP_PIN3 = oc5b;

const int DIR_PIN1 = oc4b;
const int DIR_PIN2 = oc1a;
const int DIR_PIN3 = oc5c;

unsigned long time1 = millis();
unsigned long time2 = millis();
unsigned long time3 = millis();

void runSpeed(float v1,float v2, float v3)

{
  v1>0?digitalWrite(DIR_PIN1,HIGH):digitalWrite(DIR_PIN1,LOW);
  v2>0?digitalWrite(DIR_PIN2,HIGH):digitalWrite(DIR_PIN2,LOW);
  v3>0?digitalWrite(DIR_PIN3,HIGH):digitalWrite(DIR_PIN3,LOW);

  if (millis() - time1 >= (1000/v1)) {
    digitalWrite(STEP_PIN1, HIGH);
    delayMicroseconds(2);
    digitalWrite(STEP_PIN1, LOW);
    time1 = millis();
  }
  if (millis() - time2 >= (1000 / v2)) {
    digitalWrite(STEP_PIN2, HIGH);
    delayMicroseconds(2);
    digitalWrite(STEP_PIN2, LOW);
    time2 = millis();
  }
  if (millis() - time3 >= (1000 / v3)) {
    digitalWrite(STEP_PIN3, HIGH);
    delayMicroseconds(2);
    digitalWrite(STEP_PIN3, LOW);
    time3 =millis();
    }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  // move_bot();
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
  Serial.println(v2);
  Serial.println(v3);
  runSpeed(v1*300, v2*300, v3*300);


}
void UD(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 6000 )
	{
		if (current_Time -t <= 3000)
		{
			inv_kin(0,1,0);

			current_Time = millis();	
		}
		if (current_Time - t >= 3000)
		{
			inv_kin(0,-1,0);
			current_Time = millis();
		}
	}
}

void LR(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 6000 )
	{
		if (current_Time -t <= 3000)
		{
			inv_kin(-1,0,0);
			current_Time = millis();	
		}
		
		if (current_Time - t >= 3000)
		{
			inv_kin(1,0,0);
			current_Time = millis();
		}
	}	
}

void Tri(unsigned long t)
{
	unsigned long current_Time = millis();
	while (current_Time - t <= 15000 )
	{
		if (current_Time -t <= 5000)
		{
			inv_kin(1,0,0);
			current_Time = millis();	
		}
		
		if (5000 <= current_Time - t <= 10000)
		{
			inv_kin(-0.5,0.866025,0);
			current_Time = millis();
		}

		if (current_Time - t >= 15000)
		{
			inv_kin(-0.5,-0.866025,0);
			current_Time = millis();	
		}

	}
	delay(1000);
	start_Time = millis();
}

// void circ(unsigned long t)
// {
// 	int a;
// 	float arg;
// 	unsigned long current_Time = millis();
// 	while (current_Time - t <= 4000)
// 	{
// 		arg = 3.1416*0.5*((current_Time - t)/1000);
// 		inv_kin(-a*sin(arg),a*cos(arg),0);
// 		current_Time = millis();
	
// 	}
// 	delay(1000);	
	
// }

void move_bot()
{
	start_Time = millis();
	UD(start_Time);
  	start_Time = millis();
	LR(start_Time);
  // start_Time = millis();
  // Tri(start_Time);
}





void loop() {
  // put your main code here, to run repeatedly:
 move_bot();
}


