import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 
a = 0
b = 1

n = 10

x = np.linspace(a, b, n+1)
y = f(x)

plt.plot(x, y, 'b')
plt.fill_between(x, y, 0, alpha=0.2)

area = np.trapz(y, x)

print("El área bajo la curva es:", area)
