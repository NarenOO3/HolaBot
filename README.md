# HolaBot...
Hola bot is a 3- wheeled holonomic drive robot which can control all three degrees of freedom possible on a plane (Translation along the x and y-axis and rotation along the z-axis). Ultimately, we were required to create a Hola bot to draw complex art in the given plane.

# Video Demo...

# **Skills Learned :**
Linux, ROS, Solid Modeling, Python Programming

# **Working Principle**
**Flow Chart**
![Untitled Diagram drawio](https://github.com/NarenOO3/HolaBot/assets/98276114/0c686e64-ad0d-4a7d-ba34-a581d8242807)

Initially the over Headcamera detect the aruco markers in the canvas and the aruco marker in the hola bot and send this information to the python node where we find the coordinates(x,y) of the Hola bot


| Arena (Canvas)               |Aruco Markers                |
| ---------------------- | ---------------------- |
| ![arena hola](https://github.com/NarenOO3/HolaBot/assets/98276114/e36fe4da-5eea-429b-982b-1ab001aa1460) | ![Hola bot and aruco markers](https://github.com/NarenOO3/HolaBot/assets/98276114/bddef082-c0a0-4953-84fb-bef05edb1719) |

Then we will feed the picture that we like to draw as a contour and Using PID controller script, the Speed for the three stepper motor is decided
