import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,2*np.pi,50)
b = np.sin(a)
plt.plot(a, b)
mask = b >= 0
#【】用于bool判断，只筛选为true的值
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()
