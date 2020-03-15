import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)

fig = plt.figure()

axes = fig.add_axes([0.5,0.5,0.1,0.1])

axes.plot(x,y,'r')
axes.plot(x,z,'b')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('fig1')
"""axes.legend(['sin(x)','cos(x)'])"""

plt.show(block=True)