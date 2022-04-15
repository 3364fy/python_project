import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
x=np.arange(-10,10,0.00001)
y=x**3+5*x**2+3*x+1
plt.plot(x,y,label='184')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()