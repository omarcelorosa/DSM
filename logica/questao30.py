#Não terminado
idade = int(input("Digite a idade: "))
risco = str(input("Digite se a profissão é de risco (S/N): ")).lower()
historico = str(input("Digite se há histórico médico (S/N): ")).lower()
valor = float(input("Digite o valor da cobertura: R$"))
condicao = ""


if idade < 40 and risco == "n" and historico == "n":
    premio = valor * 0.02
    condicao = "Aprovado Pleno."
    cobertura = valor + premio
elif (idade >= 40 and idade < 60) or risco == "s":
    premio = valor * 0.04
    cobertura = valor + premio
    condicao = "Aprovado Condicional."
    if historico == "s" and idade >50:
        condicao ="Cobertura negada."
if idade >= 60:
    condicao ="Cobertura negada."
    if valor < 100000 and historico == "n":
            premio = valor * 0.06
            cobertura = valor + premio

print(f"Condição: {condicao}")
print(f"Cobertura: R$ {cobertura:.2f}")
print(f"Prêmio: R$ {premio:.2f}")