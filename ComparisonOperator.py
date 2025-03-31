temperature = 19

if temperature >= 30:
    print("Hot day")
elif temperature < 20:
    print("it's kinda cold")
else:
    print("it's alright")

name = "rafael"

if name.__len__() < 3:
    print("Nome deve ter ao menos 3 caracteres")
elif name.__len__() > 50:
    print("Nome pode ter até 50 caracteres")
else:
    print("Nome adequado")
