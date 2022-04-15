import numpy as np
import matplotlib.pyplot as plt
from numpy import *
x=arange(e,e**2,0.1)
b=(e,x,0.1)
y1=(log(x))**2
y2=(log(b))**2
plt.plot(x,y1,label='ln x')
plt.plot(x,y2,label='ln b',linestyle='dotted')
# plt.plot(x,y3,label='x',linestyle='--')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
plt.show()