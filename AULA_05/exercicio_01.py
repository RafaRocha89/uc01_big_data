# Entrada de dados
salario_hora = float(input("Informe o salário por hora: "))
horas_trab = int(input("Informe horas trabalhadas: "))

# Cálculo do salário bruto
salario_bruto = salario_hora * horas_trab
print("Salário Bruto: R$", salario_bruto)

# Cálculo dos descontos
irrf = salario_bruto * 0.11  # 11% para o Imposto de Renda
inss = salario_bruto * 0.08   # 8% para o INSS
sindicato = salario_bruto * 0.05  # 5% para o sindicato

# Cálculo do salário líquido
salario_liquido = salario_bruto - (irrf + inss + sindicato)

# Saída dos resultados
print("Total pago de IRRF: R$", irrf)
print("Total pago de INSS: R$", inss)
print("Total pago de Sindicato: R$", sindicato)
print("Salário Líquido: R$", salario_liquido)


