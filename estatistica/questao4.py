a11=int(input("Digite o valor a11 da matriz A: "))
a12=int(input("Digite o valor a12 da matriz A: "))
a21=int(input("Digite o valor a21 da matriz A: "))
a22=int(input("Digite o valor a22 da matriz A: "))
b11=int(input("Digite o valor b11 da matriz B: "))
b12=int(input("Digite o valor b12 da matriz B: "))
b21=int(input("Digite o valor b21 da matriz B: "))
b22=int(input("Digite o valor b22 da matriz B: "))


resA11= (a11 * b11) + (a12 * b21)
resA12= (a11 * b12) + (a12 * b22)
resA21= (a21 * b11) + (a22 * b21)
resA22= (a21 * b12) + (a22 * b22)

print(f"A matriz resultante é:\n{resA11} {resA12}\n{resA21} {resA22}")
