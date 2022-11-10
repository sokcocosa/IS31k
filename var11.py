import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-100, 10)

y = (x ** 2) + (np.exp(x))

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()


