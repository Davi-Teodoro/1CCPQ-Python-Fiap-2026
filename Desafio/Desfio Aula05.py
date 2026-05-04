listaNomes = []
combinacao = []
cont = 0
numP = int(input("Digite quantas Pessoas devem formar duplas: "))
while cont < numP:
    listaNomes.append(input("Digite um nome: "))
    cont+=1

for i in range(len(listaNomes)):
    for j in range(i + 1, len(listaNomes)):
        combinacao.append((listaNomes[i], listaNomes[j]))

tam = len(combinacao)

for i in range(tam):
    print(combinacao[i])
    print()


print(f'São Possives formar {tam} duplas diferentes, se houverem {numP} pessoas para agrupar')