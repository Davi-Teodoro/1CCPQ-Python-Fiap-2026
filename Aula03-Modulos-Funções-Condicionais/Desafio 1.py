# Desafio 1
idade = int(input("Digite sua idade: "))

if idade < 16:
 print ("Não Pode votar!")
elif idade >= 16 and idade < 18 or idade > 70:
    print ("Votar é opicional")
else:
    print ("Deve Votar")