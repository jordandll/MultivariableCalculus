import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sympy as sp

# Create the domain of the density field, denoted as rho.
X = np.linspace(0.25,3,num=50)
Y = np.linspace(0,3,num=50)
X, Y = np.meshgrid(X,Y)

# Create the domain of the position vector r.
t = np.linspace(0,3,num=100)

# Create the domain of the velocity field v.
X_v = np.linspace(0.5,2.75,num=5)
Y_v = np.linspace(0,3,num=5)
X_v, Y_v = np.meshgrid(X_v,Y_v)

# Define the functions.
rho = X*Y
v = (np.ones(X_v.shape),-Y_v/X_v)
rho_F = X_v*Y_v
F = (rho_F*v[0],rho_F*v[1])

# Create the figure and axes.
fig, ax = plt.subplots()
ax.set_title('Flow',size=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
xlim = ax.set_xlim(0,3)
ylim = ax.set_ylim(0,3)
ax.grid()

# Plot the fields and motion(s).
cmap = mpl.colormaps['ocean']
cs = ax.contour(X,Y,rho,levels=6,cmap=cmap)
cb = fig.colorbar(cs)

ax.quiver(X_v,Y_v,*v,angles='uv',scale=4,scale_units='inches', \
          width = 0.005,units='width',color='tab:blue')
ax.barbs(X_v,Y_v,*F)

plt.show()