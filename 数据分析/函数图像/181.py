import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
x1=np.arange(1,2,0.00001)
y1=x1
y2=np.sqrt(x1)
x2=np.arange(2,4,0.00001)
y3=x2-x2+2
y4=np.sqrt(x2)
plt.plot(x1,y1,label='x')
plt.plot(x1,y2,label='x^1/2.csv')
plt.plot(x2,y3,label='2.csv')
plt.plot(x2,y4,label='x^1/2.csv')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()