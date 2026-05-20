aC=int(input("Quantas cervejas a pessoa A comprou? ")) # pessoa A cerveja
aE=int(input("Quantos espetos a pessoa A comprou? ")) # pessoa A espeto
aR=int(input("Quantos refrigerantes a pessoa A comprou? ")) # pessoa A refrigerante
bC=int(input("Quantas cervejas a pessoa B comprou? ")) # pessoa B 
bE=int(input("Quantos espetos a pessoa B comprou? ")) 
bR=int(input("Quantos refrigerantes a pessoa B comprou? ")) 
cC=int(input("Quantas cervejas a pessoa C comprou? ")) # pessoa C 
cE=int(input("Quantos espetos a pessoa C comprou? ")) 
cR=int(input("Quantos refrigerantes a pessoa C comprou? "))
dC=int(input("Quantas cervejas a pessoa D comprou? ")) # pessoa D
dE=int(input("Quantos espetos a pessoa D comprou? ")) 
dR=int(input("Quantos refrigerantes a pessoa D comprou? "))
eC=int(input("Quantas cervejas a pessoa E comprou? ")) # pessoa E
eE=int(input("Quantos espetos a pessoa E comprou? ")) 
eR=int(input("Quantos refrigerantes a pessoa E comprou? "))

#valores
#cerveja=6,50 espeto=8 e refrigerante=4,50

aT= (aC * 6.5) + (aE * 8) + (aR * 4.5) # pessoa A total
bT= (bC * 6.5) + (bE * 8) + (bR * 4.5) # pessoa B 
cT= (cC * 6.5) + (cE * 8) + (cR * 4.5) # pessoa C 
dT= (dC * 6.5) + (dE * 8) + (dR * 4.5) # pessoa D
eT= (eC * 6.5) + (eE * 8) + (eR * 4.5) # pessoa E 

print(f"O valor total gasto pela pessoa A foi: R${aT}" f"\nO valor total gasto pela pessoa B foi: R${bT}" f"\nO valor total gasto pela pessoa C foi: R${cT}" f"\nO valor total gasto pela pessoa D foi: R${dT}" f"\nO valor total gasto pela pessoa E foi: R${eT}" )
