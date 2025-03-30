# print("Rafael Nunes")
# print("o----")
# print(" ||||")
# print("*" * 10)
#
# price: int = 10
#
# print(price)

def nome ():
    print("teste nome")
nome()

# Função para adicionar 2 a cada número
def adicionar_dois(x):
    return x + 2

lista = [1, 2, 3, 4]

# Usando map para alterar os valores
nova_lista = list(map(lambda x: x * 10 if x == 2 else x, lista))

print(nova_lista)  # [3, 4, 5, 6]