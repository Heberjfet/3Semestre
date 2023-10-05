def gauss_seidel(matriz, b, num_iteraciones):
    n = len(matriz)
    x = valor


    for iteracion in range(num_iteraciones):
        x_antiguo = x.copy() 

        for i in range(n):
            suma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / matriz[i][i]

        print(f"Iteración {iteracion + 1}: {x}")

    return x

matriz = [
    [5, 2],
    [1, -4],
    
]

b = [1,0]

num_iteraciones = int(input("Ingrese el número de iteraciones: "))
valor = []
for i in range(len(b)):
    valor_inicial = float(input(f"Ingrese el valor inicial para x{i + 1}: "))
    valor.append(valor_inicial)

resultado = gauss_seidel(matriz, b, num_iteraciones)

print("\nResultado aproximado:")
for i, solucion in enumerate(resultado):
    print(f"x{i+1} ≈ {solucion:.6f}")
