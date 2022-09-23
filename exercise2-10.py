import numpy as np
import matplotlib.pyplot as plt


a = 5

x = np.linspace(-a, a, 1000)
V = 1/(abs(x-a)) + 1/(abs(x+a))

plt.plot(x, V)
plt.show()