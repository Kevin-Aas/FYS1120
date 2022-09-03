import numpy as np
import matplotlib.pyplot as plt

L = 10
N = 50
a = 5
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
rx, ry = np.meshgrid(x, y)
Ex = np.zeros((N, N), float)
Ey = np.zeros((N, N), float)

for i in range(len(rx.flat)):
    xi = rx.flat[i]
    yi = ry.flat[i]
    Ex.flat[i] = 0
    Ey.flat[i] = a/(yi*(yi-a))

plt.streamplot(rx, ry, Ex, Ey)
plt.title("Streamplot av E(x,y)")
plt.xlabel("[x]")
plt.ylabel("[y]", rotation=0)
plt.axhline(0,color='blue') # x = 0
plt.axhline(a,color='red') # y = 0
plt.show()

##############################################

L = 8
N = 26
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
rx, ry = np.meshgrid(x, y)
Ex = np.zeros((N, N), float)
Ey = np.zeros((N, N), float)

for i in range(len(rx.flat)):
    xi = rx.flat[i]
    yi = ry.flat[i]
    Ex.flat[i] = -1/xi
    Ey.flat[i] = 1/yi

plt.quiver(rx, ry, Ex, Ey)
plt.title("Pilplot av E(x,y)")
plt.xlabel("[x]")
plt.ylabel("[y]", rotation=0)
plt.axhline(0,color='red') # x = 0
plt.axvline(0,color='blue') # y = 0
plt.show()