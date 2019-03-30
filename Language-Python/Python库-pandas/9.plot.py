import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = x**4 +1
plt.figure()
plt.plot(x,y)
plt.show()