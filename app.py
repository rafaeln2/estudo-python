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
# lista.stream.foreach(x -> x == 10 ? x*10 : x);

print(nova_lista)  # [3, 4, 5, 6]

preco = 10
avaliacao = 4.9
nome = "Rafa"
is_publicado = True

print(type(preco))
print(True if isinstance(preco, int) else False)

check_type = lambda x: True if isinstance(x, int) else False

print(check_type(10))    # Saída: True
print(check_type("Olá")) # Saída: False
print(check_type(3.14))  # Saída: False




