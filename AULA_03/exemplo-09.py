# Para dizer o peso ideal com base na altura.
nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))
sexo = input("Informe M para Masculino e F para Feminino: ")
M = (72.7* altura) - 58
F = (62.1* altura) -44.7
if sexo == "M" or sexo == "m":
    print("o seu peso ideal é: ",M)
elif sexo == "F" or sexo == "f":
    print('o seu peso ideal é: ',F)
else:
    print("VERIFIQUE O SEXO iNFORMADO")  
#print(f"O PESO IDEAL PARA OS HOMENS É {M:.2f} E O PESO IDEAL PARA MULHERES É {F:.2f}" )


    