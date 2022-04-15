import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(-4,4,0.1)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label='sin x')
plt.plot(x,y2,label='cos x',linestyle='dotted')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()