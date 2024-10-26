"""
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
"""

import matplotlib.pyplot as plt
import numpy as np

n_radii = 4
n_angles = 8

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

r = np.linspace(0.125,1.0,num=12)
theta = np.linspace(0,2*np.pi,num=36,endpoint=False)[:,None]

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

X = np.append(0,(r*np.cos(theta)).flatten())
Y = np.append(0,(r*np.sin(theta)).flatten())
X, Y = np.meshgrid(X,Y)


# Compute z to make the pringle surface.
z = np.sin(-x*y)

Z = np.sin(-X*Y)

# Create figure and axes objects.

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

ax.plot_trisurf(x, y, z, linewidth=0.8, antialiased=True, color=(0.1,0.2,1.0,0.4))
ax.plot_trisurf(x,y,[-0.25 for i in range(len(x))],color=(0.8,0.3,0.1,0.8))
# ax.plot_wireframe(X,Y,Z,color='tab:red',lw=0.2,ls='--')

plt.show()