paisOri = input("Digite o país de origem do produto(UE ou Fora): ").lower()
tipo = input("Digite o tipo do produto (Eletrônico ou Outro): ").lower()
valor = float(input("Digite o valor do produto: R$"))
imposto = 0
tipoTrib= ""

if paisOri == "ue":
    
    if valor < 500:
        imposto = 0
        tipoTrib = "Isento"
    
    elif tipo == "eletrônico":
        imposto = valor * 0.12
        tipoTrib = "UE eletrônico (12%)"
    
    else:
        imposto = valor * 0.08
        tipoTrib = "UE outro (8%)"

elif paisOri == "fora":
    imposto = valor * 0.20
    tipoTrib = "Fora (20%)"
    
    if tipo == "eletrônico" and valor > 1000:
        extra = valor * 0.15
        imposto += extra
        tipoTrib += " + Extra (15%)"

    if valor <200:
        imposto += 100
        tipoTrib += "+ frete R$100"    

total = valor + imposto

print(f"O imposto a ser pago é: R${imposto:.2f}, \n Tipo de tributação: {tipoTrib}, \n Valor total do produto: R${total:.2f}")
