#Calcule o valor da prestação em atraso
Prestacao = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a Taxa de juros mensal: "))
tempo = int(input("Informe a quantidade de meses em atraso: "))
valor_final =  Prestacao + (Prestacao * taxa/100 *tempo)
print(f"o valor em ataraso sera de R${valor_final:.2f}")
