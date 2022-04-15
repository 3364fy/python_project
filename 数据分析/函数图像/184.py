import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
x=np.arange(0,10,0.00001)
y=np.sqrt(1-x)
plt.plot(x,y,label='184')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()