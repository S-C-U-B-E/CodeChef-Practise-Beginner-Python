import matplotlib.pyplot as plit
import numpy as np
import seaborn as sns

x= np.linspace(2,5,11)
y=x**2



fig = plit.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x ,y ,'r--')
axes.set_xlabel('lala')
axes.set_ylabel('haha')
axes.set_title('Title')



fig.savefig("name1.png",dpi = 1000)

fig,axes = plit.subplots(nrows=1,ncols=4)

for ax in axes:
    ax.plot(x,y,'b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Fig')
print(fig)

plit.show(block=True)
