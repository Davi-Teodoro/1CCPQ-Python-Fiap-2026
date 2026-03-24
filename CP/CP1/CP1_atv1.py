
# Primeira Questão

nomeP = input ("Digite o nome do produto: ")
preco = float (input ("Digite o preço unitário: "))
qntd = int (input ("Digite a quantidade comprada: "))
desconto = float (input ("Digite o percentual do desconto até 100: "))

while desconto > 100:
    print ("Por favor digite a porcentagem do desconto até 100%\n")
    desconto = float (input ("Digite o percentual do desconto até 100: "))

else:
    vbruto = preco*qntd

    vdesconto = vbruto*(desconto/100)

    vfinal = vbruto-vdesconto

    print (f"Produto: {nomeP} \n" )
    print (f"Valor Bruto: R${vbruto} \n" )
    print (f"Desconto: R${vdesconto} \n" )
    print (f"Valor Final: R${vfinal} \n" )

