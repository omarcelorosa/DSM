matriz = []

i = 1
while i < 4:
    linha = []
    j = 1
    while j < 5:
        valor = int(input(f"Digite o valor para posição A[{i}][{j}] ou resultado: "))
        linha.append(valor)
        j += 1
    
    matriz.append(linha)
    i += 1

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)
#linha 1: a11(x), a12(y), a13(z), t1(resultado)
a11 = matriz[0][0]
a12 = matriz[0][1]
a13 = matriz[0][2]
t1 = matriz[0][3]
#linha 2: a21, a22, a23, t2 
a21 = matriz[1][0]
a22 = matriz[1][1]
a23 = matriz[1][2]
t2 = matriz[1][3]
#linha 3: a31, a32, a33, t3
a31 = matriz[2][0]
a32 = matriz[2][1]
a33 = matriz[2][2]
t3 = matriz[2][3]

det = (a11*a22*a33+a12*a23*a31+a13*a21*a32)-(a13*a22*a31+a11*a23*a32+a12*a21*a33)

if det == 0:
    print("A matriz é singular, não é possível resolver o sistema.")
else:
    x = ((t1*a22*a33 + a12*a23*t3 + a13*t2*a32) - (a13*a22*t3 + t1*a23*a32 + a12*t2*a33)) / det
    y = ((a11*t2*a33 + t1*a23*a31 + a13*a21*t3) - (a13*t2*a31 + a11*a23*t3 + t1*a21*a33))/ det
    z = ((a11*a22*t3 + a12*t2*a31 + t1*a21*a32) - (t1*a22*a31 + a11*t2*a32 + a12*a21*t3)) / det
    print("Determinante da matriz A:", det)
    print("Determinante de X:", x)
    print("Determinante de Y:", y)
    print("Determinante de Z:", z)
