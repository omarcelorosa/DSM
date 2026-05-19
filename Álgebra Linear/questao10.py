a11=int(input("Digite o valor de X da PRIMEIRA linha: "))
a12=int(input("Digite o valor de Y da PRIMEIRA linha: "))
l1Res=int(input("Digite o valor do RESULTADO(após o '=') da PRIMEIRA linha: "))
a21=int(input("Digite o valor de X da SEGUNDA linha: "))
a22=int(input("Digite o valor de Y da SEGUNDA linha: "))
l2Res =int(input("Digite o valor do RESULTADO(após o '=') da SEGUNDA linha: "))

detP= (a11 * a22) - (a12 * a21)
if detP == 0:
    print("O sistema não possui solução única.")
else:
    #det apos troca da coluna X
    detX= (l1Res * a22) - (a12 * l2Res)

    #det apos troca da coluna Y
    detY= (a11 * l2Res) - (l1Res * a21)

    x=detX / detP
    y=detY / detP

    print(f"O valor de X é: {x} \nO valor de Y é: {y}")

#detp = determinante principal
#detX = determinante apos troca da coluna X 
#detY = determinante apos troca da coluna Y