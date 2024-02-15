import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def f(x):
    return x**2

P_0 = (x_0,y_0) = (0.15, f(0.15))
P_1 = (x_1,y_1) = (1,1)
x = np.linspace(x_0,x_1,num=100)

fig, ax = plt.subplots(figsize=(3,3))
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
xlim = ax.set_xlim(0,1.125)
ylim = ax.set_ylim(0,1.125)

ax.plot(x,x**2,color='k')
ax.scatter([x_0, x_1],[y_0,y_1],color='k',marker='.')

mark = mpl.markers.MarkerStyle('>')
m = mark.rotated(rad=np.arctan(1))
ax.plot([0.5],[f(0.5)],color='k',marker=m)
ax.text(x_0-0.03,y_0+0.04,r'$P_0$')
ax.text(x_1+0.02,y_1+0.02,r'$P_1$')
ax.text(0.52,f(0.5)-0.02,r'$C$')
plt.savefig('Fundamental.png')