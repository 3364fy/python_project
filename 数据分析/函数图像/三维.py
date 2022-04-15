import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
figure=plt.figure()
axes=Axes3D(figure)
x=np.arange(-10,10,0.25)
y=np.arange(-10,10,0.25)
x,y=np.meshgrid(x,y)
z=np.sqrt(x*x+y*y)
axes.plot_surface(x,y,z,cmap='rainbow_r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

figure=plt.figure()
axes=Axes3D(figure)
x=np.arange(-10,10,0.25)
y=np.arange(-10,10,0.25)
x,y=np.meshgrid(x,y)
z=x*x+y*y
axes.plot_surface(x,y,z,cmap='rainbow_r')
plt.show()