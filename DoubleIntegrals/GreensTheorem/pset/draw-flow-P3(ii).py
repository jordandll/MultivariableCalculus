""" This is a script to animate the flow field found in problem 3 part ii) of pset9-part2.ipynb. """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

from itertools import product

# Create the domain of the density field, denoted as rho.
X = np.linspace(0.25,3,num=50)
Y = np.linspace(0,3,num=50)
X, Y = np.meshgrid(X,Y)

# Create the domain of the flow field 'F'.
X_v = np.linspace(0.25,3,num=5)
Y_v = np.linspace(0,3,num=5)
X_v, Y_v = np.meshgrid(X_v,Y_v)
t = np.linspace(0,4,num=100)

# Define the functions.
rho = X*Y
rho_v = X_v*Y_v

# Create the figure and axes.
fig, ax = plt.subplots()
ax.set_title('Flow P3(ii)',size=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
xlim = ax.set_xlim(0,3)
ylim = ax.set_ylim(0,3)
ax.grid()

# Plot the density, denoted as rho.
cmap = mpl.colormaps['ocean']
cs = ax.contour(X,Y,rho,levels=6,cmap=cmap)
cb = fig.colorbar(cs)

# Animate the flow field.
F = ax.barbs(X_v,Y_v,rho_v*X_v,-rho_v*Y_v)


def update(frame):
    F.set_UVC(rho_v*X_v/(1+frame),-rho_v*Y_v/(1+frame))
    return F,

ani = animation.FuncAnimation(fig, update, frames = t, interval = 50)
plt.show()