#Pedir para o usuario informar o nome e senha se existir der o ok, caso contrario, nao.
Usuarios = ["Alessandro", "Pedro", "Yasmin", "Gabrielle", "Lucas"]
Senhas = ["123", "14@os", "0203", "2807", "1234"]
usuario = input("Informe o nome de acesso ao sistema: ")
for i in range(len(Usuarios)):
    if Usuarios[i] == usuario:
        resp = "Usuario Encontrado"
        break
    else:
        resp = "Usuario nao Encontrado"
print(resp)




