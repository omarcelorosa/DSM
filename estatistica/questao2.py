while True:
    operacao= input("Digite a operação (+, -, *, /) ou (sair): ")

    if operacao == "sair":
        break
    elif operacao not in ["+", "-", "*", "/"]: # Validação das operções
        print("Operação inválida! Insira uma operação válida ou 'sair' para encerrar.")
        continue

    fracao1 = input("Digite a primeira fração (ex: 1/2): ")
    numerador1, denominador1 = fracao1.split("/") #quebra em string e atribui valores as variáveis
    fracao2 = input("Digite a segundafração (ex: 1/2): ")
    numerador2, denominador2 = fracao2.split("/")
    
    #conversão de string para inteiro
    n1 = int(numerador1)
    d1 = int(denominador1)
    n2 = int(numerador2)
    d2 = int(denominador2)

    if operacao == "+":
        numerador = ((n1 * d2) + (n2 * d1))
        denominador = (d1 * d2)
        resultado = f"{numerador}/{denominador}"
    elif operacao == "-":
        numerador = ((n1 * d2) - (n2 * d1))
        denominador = (d1 * d2)
        resultado = f"{numerador}/{denominador}"
    elif operacao == "*":
        numerador = (n1 * n2)
        denominador = (d1 * d2)
        resultado = f"{numerador}/{denominador}"
    elif operacao == "/":
        numerador = (n1 * d2)
        denominador = (d1 * n2)
        resultado = f"{numerador}/{denominador}"
    else:
        print("Operação inválida!")
        continue

    print("Resultado:", resultado)