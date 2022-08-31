import numpy as np
import matplotlib.pyplot as plt

def efieldq(q0,r,r0):
    # Input: charge q in Coulomb
    #        r: position to find field (in 1,2 or 3 dimensions) in meters
    #        r0: position of charge q0 in meters
    # Output: electric field E at position r in N/C
    dr = r-r0
    drnorm = np.sqrt(dr.dot(dr))
    epsilon0 = 8.854187817e-12
    return q0/(4.0*np.pi*epsilon0)*dr/drnorm**3

r0 = np.array([0.0,0.0])
q0 = 1.0
L = 5
N = 21
x = np.linspace(-L,L,N)
y = np.linspace(-L,L,N)
rx,ry = np.meshgrid(x,y)
Ex = np.zeros((N,N),float)
Ey = np.zeros((N,N),float)
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i],ry.flat[i]])
    Ex.flat[i],Ey.flat[i] = efieldq(q0,r,r0)
plt.quiver(rx,ry,Ex,Ey)
plt.axis('equal')
plt.show()