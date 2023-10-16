from sympy import symbols, expand

def lagrange(points):
    x = symbols('x')
    L = 0
    for i in range(len(points)):
        p = 1
        for j in range(len(points)):
            if i != j:
                p *= (x - points[j][0]) / (points[i][0] - points[j][0])
        temp=p*points[i][1]
        print(f"L{i} = {expand(temp)}","\n")
        L += temp
    return expand(L)

points=[]
while(True):
    try:
        print("Ingrese una letra para terminar.")
        temp=[]
        for i in range(2):
            temp.append(float(input("Ingrese una coordenada: ")))
        print(temp,"\n")
        points.append(list(temp))
        temp.clear()
    except ValueError:
        break

polynomial = lagrange(points)
print("Pn(X)= "+str(polynomial))