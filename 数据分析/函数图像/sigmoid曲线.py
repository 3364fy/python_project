import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(-10,10,0.1)
y=[]
for t in x:
    y_1=1/(1+math.exp(-t))
    y.append(y_1)
plt.plot(x,y,label='sigmoid')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0,1)
plt.title('sigmoid')
plt.legend()
plt.show()