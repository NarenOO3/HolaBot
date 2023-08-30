import numpy as np
vx=vy=-1.0
max1=max2=max3=0
while(vx<=1):
    vy=-1
    print("hello")
    while(vy<=1):
        ([v1],[v2],[v3])=np.dot(([0.66667, 0, 1.90661], [-0.333333, 0.57737, 1.90661], [-0.333333, -0.57737,1.90661]),([vx],[vy],[0]))
        if(v1>max1):
            max1=v1
        if(v2>max2):
            max2=v2
        if(v3>max3):
            max3=v3
        print('hi')
        vy=vy+0.01
    vx=vx+0.01
print(max1,max2,max3)