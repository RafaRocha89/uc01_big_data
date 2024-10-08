# Construa um programa para liberar acesso para maiores de 18 anos com elif
idade  = int(input("informe a idade: "))
if idade <18:
    print("Voce é menor de idade")
elif idade ==18:
    print("Quase la")
elif idade > 18 and idade < 65:
    print("Acesso Liberado")
else:
    print("acesso Liberado - Apreci com Moderação")
