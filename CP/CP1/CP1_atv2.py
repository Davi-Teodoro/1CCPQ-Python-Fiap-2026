# Segunda Questão

nomeC = input ("Digite o nome do colaborador: ")
valorHT = float (input ("Digite o valor da hora trabalhada: "))
horaT = float (input ("Digite a quantidade de horas trabalhadas: "))
bonusF = float (input ("Digite o valor do bônus fixo: "))
desconto = float (input ("Digite o valor do desconto: "))

sbruto = valorHT*horaT+bonusF

sliquido = sbruto-desconto

print (f"Colaborador(a): {nomeC} \n" )
print (f"Salário Bruto: R${sbruto} \n" )
print (f"Salário Liquido: R${sliquido} \n" )