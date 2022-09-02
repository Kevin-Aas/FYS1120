import sympy as sy
r = sy.Symbol('r')
a = sy.Symbol('a')
z = sy.Symbol('z')
f = r/(r**2 + z**2)**(3/2)
print(sy.integrate(f, (r,0,a)))

import numpy as np
import matplotlib.pyplot as plt
rho_A = 1
epsilon0 = 8.854187817e-12
a = 1
z = np.linspace(0, 10, 1000)

u = np.linspace(0,10,1000)
Eu = (1-u/(u**2 + 1)**1.5)
plt.plot(u,Eu)
plt.show()

E = (1/z - 1/(z**2 + a**2)**(1/2))

plt.plot(z, E)
plt.xlabel("z")
plt.ylabel("E", rotation=0)
plt.show()
