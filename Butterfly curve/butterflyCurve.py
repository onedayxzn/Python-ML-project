import numpy as np
import matplotlib.pyplot as plt
import math


def butterfly_curve(t):
    x = np.zeros(t.size)
    y = np.zeros(t.size)

    for k in range(0, t.size):
        x[k] = 100*(math.sin(t[k])*(math.exp(math.cos(t[k])) -
                    2*math.cos(4*t[k])-math.sin(t[k]/12)**5))
        y[k] = 100*(math.cos(t[k])*(math.exp(math.cos(t[k])) -
                    2*math.cos(4*t[k])-math.sin(t[k]/12)**5))

    return x, y


time = np.arange(0, 12 * math.pi, 0.01)
plt.plot(butterfly_curve(time)[0], butterfly_curve(time)[1])
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title('Butterfly Curve')

plt.show()
