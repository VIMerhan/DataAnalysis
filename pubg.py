import numpy as np
import matplotlib.pyplot as plt

n = 1024
# x = np.random.normal(0, 1, n)
# y = np.random.normal(0, 1, n)
z = np.arange(n)
x = np.linspace(-10,10,50)

y = 2*x
# plt.figure()
plt.plot(x, x*2)

# plt.scatter(x, y, s=75, c=T, alpha=0.5)

# plt.xlim(-10, 10)
# plt.xticks = np.arange(-10, 10, 0.5)
#
# plt.xlim(-10, 10)
# plt.yticks = np.arange(-10, 10, 0.5)

plt.show()
