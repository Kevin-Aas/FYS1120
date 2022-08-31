import numpy as np
import matplotlib.pyplot as plt

def efield(q0, r0, r):
    R = r - r0
    R_norm = np.sqrt(R.dot(R))
    epsilon0 = 8.854187817e-12
    E = q0/(4*np.pi*epsilon0) * R/(R_norm**3)
    return E

r0 = np.array([0.0, 0.0])
q0 = 1.0

L = 5
N = 21

x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
rx, ry = np.meshgrid(x, y)
Ex = np.zeros((N, N), float)
Ey = np.zeros((N, N), float)

for i in range(len(rx.flat)):
    r = np.array([rx.flat[i], ry.flat[i]])
    Ex.flat[i],Ey.flat[i] = efield(q0, r0, r)

#plt.quiver(rx, ry, Ex, Ey)
plt.streamplot(rx, ry, Ex, Ey)
plt.axis('equal')
plt.show()
