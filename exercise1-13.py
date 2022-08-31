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

r0 = np.array([0.0,0.0])    # origo
q0 = 1.0                    # ladning
L = 5                       # lengde fra origo
N = 21                      # antall punkter mellom lengdene fra origo
x = np.linspace(-L,L,N)     # x-aksen: [-5, -4.5, 4,..., 0,..., 4, 4.5, 5]
y = np.linspace(-L,L,N)     # y-aksen: [-5, -4.5, 4,..., 0,..., 4, 4.5, 5]
rx,ry = np.meshgrid(x,y)    # lager et 2D koordinatsystem (matrise) med x og y
Ex = np.zeros((N,N),float)  # lager en tom matrise for x-verdiene til E-feltet
Ey = np.zeros((N,N),float)  # lager en tom matrise for y-veridene til E-feltet
# rx.flat -> [-5.0, -4.5,..., 0.0,..., 4.5, 5.0, -5.0, -4.5,..., 0.0,..., 4.5, 5.0, -5.0, ...]
# rx.flat legger altså alle elementene i matrisen etter hverandre i en liste
# på denne måten går man igjennom alle punktene i koordinatsystemet rx,ry
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i],ry.flat[i]])
    Ex.flat[i],Ey.flat[i] = efieldq(q0,r,r0) # Bestemmer E-feltet i hver punkt i koord.sys.
plt.quiver(rx,ry,Ex,Ey) # Lager et pilplot 
plt.axis('equal')
plt.show()