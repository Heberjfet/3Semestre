#heber jafet alvaro
import numpy as np

def jacobi(A, b, x0, itera):
    n = len(A)
    x = x0.copy()
    print("Iteración 0:", x0)
    for j in range(itera):
        x_prev = x.copy()
        for i in range(n):
            s = sum(A[i][j] * x_prev[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
        print("Iteración {}:".format(j+1), x)
    return x, itera

def solicitar_datos():
    A = np.array([[10, 1, 2], [4, 6, -1], [-2, 3, 8]])
    b = np.array([3, 9, 51])
    
    print("Introduce el vector inicial x0:")
    x0 = np.array([float(x) for x in input().split()])
    
    itera = int(input('Ingrese el número de iteraciones:'))
    
    return A, b, x0, itera

A, b, x0, itera = solicitar_datos()
x, iteraciones = jacobi(A, b, x0, itera)

print("\nSolución final:")
for i in range(len(x)):
    print("x{} = {:.6f}".format(i+1, x[i]))

print("Número total de iteraciones realizadas:", iteraciones)

input()