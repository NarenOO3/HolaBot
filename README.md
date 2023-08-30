# HolaBot...
Hola bot is a 3- wheeled holonomic drive robot which can control all three degrees of freedom possible on a plane (Translation along the x and y-axis and rotation along the z-axis). Ultimately, we were required to create a Hola bot to draw complex art in the given plane.

# Video Demo...

# **Skills Learned :**
Linux, ROS, Solid Modeling, Python Programming, Arduino & C programming

# **Working Principle**
**Flow Chart**
![Untitled Diagram drawio (1)](https://github.com/NarenOO3/HolaBot/assets/98276114/c56d63c3-8df3-41cf-a86d-80a467945f77)

Initially the over Headcamera detect the aruco markers in the canvas and the aruco marker in the hola bot and send this information to the python node where we find the coordinates(x,y) of the Hola bot


| Arena (Canvas)               |Aruco Markers                |
| ---------------------- | ---------------------- |
| ![arena hola](https://github.com/NarenOO3/HolaBot/assets/98276114/e36fe4da-5eea-429b-982b-1ab001aa1460) | ![Hola bot and aruco markers](https://github.com/NarenOO3/HolaBot/assets/98276114/bddef082-c0a0-4953-84fb-bef05edb1719) |

Then we will feed the picture that we like to draw as a contour and get the coordinates of the points in the contour where the holabot will draw and Using PID controller script,which subcribe the coordinates data of holabot for Over headcamera detection script, the Speed for the three stepper motor is decided which is sent to esp32 in the hola bot via **wifi** through Socket Programming.

The Speed values in Esp32 will be send to ATmega2560 via hardware serial communication and Atmega2560 will control the stepper motors via A4988 Stepper Drivers.

