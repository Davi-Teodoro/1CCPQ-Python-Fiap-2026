def checarNota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a Primeira nota: "))
notaA = checarNota(notaA)
notaB = float(input("Digite a Segunda nota: "))
notaB = checarNota(notaB)
media = (notaA + notaB)/2
print(media)