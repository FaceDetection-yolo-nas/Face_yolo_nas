import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
