import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import pi
from numpy import *
#Set the font to bold to support Chinese display
mpl.rcParams['font.sans-serif']=['SimHei']
#Set the Chinese font to be able to display symbols normally
mpl.rcParams['axes.unicode_minus']=False

x=np.arange(0,10,0.01)
y=sqrt(2*x-x**2)
#plt.axes(polar=True)
plt.plot(x,y,label='129-体积')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()