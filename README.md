# HolaBot...
Hola bot is a 3- wheeled holonomic drive robot which can control all three degrees of freedom possible on a plane (Translation along the x and y-axis and rotation along the z-axis). Ultimately, we were required to create a Hola bot to draw complex art in the given plane.

# Video Demo (fast-forwarded)...

Complete Hola Bot        

https://github.com/NarenOO3/HolaBot/assets/98276114/a756ce81-f39d-4ce2-9923-da0e97ca74d5

Infinity Symbol

https://github.com/NarenOO3/HolaBot/assets/98276114/4b2ce358-d221-415d-9932-d4c478116c63
# 
# **Skills Learned :**
Linux, ROS, Gazebo, Solid Modeling, Python Programming, Arduino & C programming

# **Working Principle**
**Flow Chart**
![Untitled Diagram drawio (1)](https://github.com/NarenOO3/HolaBot/assets/98276114/c56d63c3-8df3-41cf-a86d-80a467945f77)

Initially the over Headcamera detect the aruco markers in the canvas and the aruco marker in the hola bot and send this information to the python node where we find the coordinates(x,y) of the Hola bot


| Arena (Canvas)               |Aruco Markers                |
| ---------------------- | ---------------------- |
| ![arena hola](https://github.com/NarenOO3/HolaBot/assets/98276114/e36fe4da-5eea-429b-982b-1ab001aa1460) | ![Hola bot and aruco markers](https://github.com/NarenOO3/HolaBot/assets/98276114/bddef082-c0a0-4953-84fb-bef05edb1719) |

Then we will feed the picture that we like to draw as a contour and get the coordinates of the points in the contour which the holabot will draw and Using PID controller script,which subcribe the coordinates data of holabot for Over headcamera detection script, the Speed for the three stepper motor is decided which is sent to esp32 in the hola bot via **wifi** through Socket Programming.

The Speed values in Esp32 will be send to ATmega2560 via hardware serial communication and Atmega2560 will control the stepper motors via A4988 Stepper Drivers.

# Design Pictures (done in Fusion 360)
| |         |
| ---------------------- | ---------------------- |
| ![Chassis body final new v20](https://github.com/NarenOO3/HolaBot/assets/98276114/d6dfaf7d-8c1b-4661-a664-0bbec103347b) | ![Chassis body final new v23](https://github.com/NarenOO3/HolaBot/assets/98276114/599df86f-f6e3-43e0-8a8d-94ee1298e7e1) |

# Gazebo Simulation Video
https://github.com/NarenOO3/HolaBot/assets/98276114/66dbb890-16b2-4fda-85fd-7b0090c1bab6


