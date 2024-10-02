#Tendo como dado de entrada a altura (h)de uma pessoa, construaum programa que calcula seu peso ideal, utilizando as seguintes formulas:
nome = input("Insira seu nome: ")
altura = float(input("Insira sua altura: "))
sexo = input("Insira seu sexo: ")
M = (72.7* altura) - 58
F = (62.1* altura) -44.7
print(f"O PESO IDEAL PARA OS HOMENS É {M:.2f} E O PESO IDEAL PARA MULHERES É {F:.2f}" )



