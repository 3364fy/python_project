import numpy as np
import math
import matplotlib.pyplot as plt
from math import pi
from numpy import *
a=1
theta=np.linspace(0,2*pi,10000)
r=np.sqrt((a**2)*cos(2*theta))
plt.axes(polar=True)
plt.plot(theta,r,label='129')

# plt.xlabel('theta')
# plt.ylabel('r')
plt.legend(loc='best')
plt.show()