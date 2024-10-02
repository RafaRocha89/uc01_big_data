# Calcular a idade de uma pessoa a partir do ano de nascimento
import datetime
num = int(input("Informe o Ano de nascimento: "))
nome = input("Informe o seu nome: ")
data_atual = datetime.date.today()
dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year
result = ano_atual - num
print("Sr(a)", nome, "a sua idade é: ",result,"anos.")




