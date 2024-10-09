#O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um 
#programa que armazene em um vetor um conjunto indeterminado de temperaturas,
#ao final ,informe a menor, a maior e a média das temperaturas.
temperatura = []
resp = "s"
while resp == "S" or resp == "s":
    temperatura.append(float(input("informe a temperatura: ")))
    resp = input("Deseja Continuar(S/N)? ")
print(f" A menor temperatura registrada foi{min(temperatura)}ºC")
print(f" A maior temperatura registrada foi{max(temperatura)}ºC")
print(f" A temperatura media registrada foi{(sum(temperatura)/len(temperatura)):.1f}ºC")
    

      


