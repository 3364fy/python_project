import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
figure=plt.figure()
axes=Axes3D(figure)
x=np.arange(-10,10,0.25)
y=np.arange(-10,10,0.25)
x,y=np.meshgrid(x,y)
z=np.cos(x*x+y*y)
axes.plot_surface(x,y,z,cmap='rainbow_r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x=np.arange(0,10,0.00001)
y1=np.sqrt(1-x**2)

plt.plot(x,y1,label='179')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
