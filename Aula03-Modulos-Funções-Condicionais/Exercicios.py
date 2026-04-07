# # Exercicio 1
#
# from playsound3 import playsound
# # Reproduzir o áudio
#
# playsound('Audio.MP3')

# # Exercicio 2
#
# num = int(input("Digite um numero inteiro: "))
#
# if num % 2 == 0:
#     print(f"O número: {num} é par")
# else:
#     print(f"O número: {num} é impar")

# # Exercicio 3
#
# num1 = int(input("Digite um numero inteiro: "))
# num2 = int(input("Digite um numero inteiro: "))
#
# if num1 > num2:
#     print(f"O número: {num1} é maior")
# elif num2 > num1:
#     print(f"O número: {num2} é maior")
# else:
#     print("Os numeros são iguais")

# Exercicio 4

notas = []
for  i in range(1, 5):
    notas.append(float(input('Digite a {}º nota de 1 a 10: '.format(i))))
soma = sum(notas)
media = soma / 4
if media < 5:
    print("Reprovado")
elif media < 7:
    print("Exame")
else:
    print("Aprovado")

# # Exercicio 7
# idade = int(input("Digite sua idade: "))
#
# if idade < 16:
#  print ("Não Pode votar!")
# elif idade >= 16 and idade < 18 or idade > 70:
#     print ("Votar é opicional")
# else:
#     print ("Deve Votar")