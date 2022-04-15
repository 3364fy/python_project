import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
x=np.arange(0,pi/2,0.1)
y1=2*x/pi
y2=np.sin(x)
y3=x
plt.plot(x,y1,label='2x/pi')
plt.plot(x,y2,label='sin x',linestyle='dotted')
plt.plot(x,y3,label='x',linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()