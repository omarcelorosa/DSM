idade = int(input("Digite a idade: "))
pressao = int(input("Digite a pressão arterial: "))
colesterol = int(input("Digite o nível de colesterol: "))
fuma = input("O paciente é fumante? (s/n): ").upper() # Converte a resposta para maiúscula
fator = 0

if idade >= 50:
    fator += 1
if pressao >= 120:
    fator += 1
if colesterol >= 200:
    fator += 1
if fuma == 'S':
    fator += 1

if fator == 0:
    print(f"O paciente tem baixo risco de doença cardíaca.Indice de risco: {fator * 10}")

elif fator == 1 or fator == 2:
    print(f"O paciente tem risco moderado de doença cardíaca.Indice de risco: {fator * 10}")
    if idade >= 60:
        print(f"Exame extra recomendado.")

elif fator == 3:
    print(f"O paciente tem alto risco de doença cardíaca.Indice de risco: {fator * 10}")
    if  idade >= 60:
        print(f"Exame extra recomendado")
        

elif fator == 4:
    print(f"Procure emergência imediatamente! O paciente tem  risco crítico de doença cardíaca.Indice de risco: {fator * 10}")