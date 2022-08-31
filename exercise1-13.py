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

r0 = np.array([0.0, 0.0])   # posisjon til ladning [m]
q0 = -0.1e-6                 # ladning [C]
r1 = np.array([0.5e-3, 0.0])
q1 = 0.1e-6
L = 2e-3                       # lengde fra origo
N = 21                      # antall punkter mellom lengdene fra origo
x = np.linspace(-L,L,N)     # x-aksen (når N=21): [-5, -4.5, 4,..., 0,..., 4, 4.5, 5]
y = np.linspace(-L,L,N)     # y-aksen (når N=21): [-5, -4.5, 4,..., 0,..., 4, 4.5, 5]
rx,ry = np.meshgrid(x,y)    # lager et 2D koordinatsystem (matrise) med x og y
Ex = np.zeros((N,N),float)  # lager en tom matrise for x-verdiene til E-feltet
Ey = np.zeros((N,N),float)  # lager en tom matrise for y-veridene til E-feltet
# rx.flat (når N=21) -> [-5.0, -4.5,..., 0.0,..., 4.5, 5.0, -5.0, -4.5,..., 0.0,..., 4.5, 5.0, -5.0, ...]
# rx.flat legger altså alle elementene i matrisen etter hverandre i en liste
# på denne måten går man igjennom alle punktene i koordinatsystemet rx,ry
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i],ry.flat[i]])
    Ex.flat[i],Ey.flat[i] = efieldq(q0,r,r0) + efieldq(q1,r,r1)# Bestemmer E-feltet i hver punkt i koord.sys.
plt.quiver(rx,ry,Ex,Ey) # Lager et pilplot 
plt.axis('equal')
plt.show()

Q1 = 0.1e-3 # C
r1 = np.array([0.001, 0.0]) # m
F1 = efieldq(q0, r1, r0) * Q1 # N

Q2 = -0.1e-3 # C
r2 = np.array([0.001, 0.0]) # m
F2 = efieldq(q0, r2, r0) * Q2 # N

Q3 = 0.2e-3 # C
r3 = np.array([0.001, 0.002]) # m
F3 = efieldq(q0, r3, r0) * Q3 # N

print(f"F1 = ({F1[0]:.2f}, {F1[1]:.2f})N")
print(f"F2 = ({F2[0]:.2f}, {F2[1]:.2f})N")
print(f"F3 = ({F3[0]:.2f}, {F3[1]:.2f})N")


