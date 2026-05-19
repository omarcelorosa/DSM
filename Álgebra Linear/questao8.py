a11=int(input("Digite o valor a11 da matriz A: "))
a12=int(input("Digite o valor a12 da matriz A: "))
a13=int(input("Digite o valor a13 da matriz A: "))
a21=int(input("Digite o valor a21 da matriz A: "))
a22=int(input("Digite o valor a22 da matriz A: "))
a23=int(input("Digite o valor a23 da matriz A: "))
a31=int(input("Digite o valor a31 da matriz A: "))
a32=int(input("Digite o valor a32 da matriz A: "))
a33=int(input("Digite o valor a33 da matriz A: "))

a14= a11
a15= a12
a24= a21
a25= a22
a34= a31
a35= a32

vetP= (a11 * a22 * a33) + (a12 * a23 * a34) + (a13 * a24 * a35)
vetS= (a13 * a22 * a31) + (a14 * a23 * a32) + (a15 * a24 * a33)
det= (vetP) - (vetS)


print(f"O determinante da matriz A é: {det}")

#vetP = vertical principal
#vetS = vertical secundária