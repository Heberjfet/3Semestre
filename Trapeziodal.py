import numpy as np
import matplotlib.pyplot as plt

def f(x):
<<<<<<< HEAD
    return x**3 + y

# Definimos los límites de integración
=======
    return x**3 
>>>>>>> c52db537f4f1118eb1f39b27b9c800058bc747e5
a = 0
b = 1

n = 10

x = np.linspace(a, b, n+1)
y = f(x)

plt.plot(x, y, 'b')
plt.fill_between(x, y, 0, alpha=0.2)

area = np.trapz(y, x)

print("El área bajo la curva es:", area)

input("Pulse enter para cerrar la ventana: ")