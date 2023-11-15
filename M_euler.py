import sympy as sp

A, B = sp.symbols('a b')
while True:
    try:
        func = input("Ingrese la diferencial en términos de A, B: ")
        function = sp.sympify(func)
        break
    except ValueError:
        pass
f = sp.lambdify((A, B), function)
a_0 = float(input("Ingrese el valor de a_0: "))
b_0 = float(input("Ingrese el valor de b_0: "))
a_f = float(input("Ingrese el valor de a_f: "))
n = int(input("Ingrese el número de intervalos: "))
h = (a_f - a_0) / n
print(h)
b_i = 0  # Cambié yi a b_i
print("||   A  ||    B    ||   f(a,b)   ||")
for i in range(n + 1):
    print("|| "+"{:.2f}".format(a_0)+" ||  "+"{:.3f}".format(b_0)+"  ||    "+"{:.3f}".format(f(a_0, b_0))+"   ||")
    b_i = (b_0 + (h * f(a_0, b_0)))
    a_0 += h
    b_0 = b_i