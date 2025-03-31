peso = float(input("Insira o seu peso em : "))

metrica = input("(K)g or (L)bs: ");
peso_convertido = 0
if  metrica.upper() == 'K':
    peso_convertido = peso / 0.453592  # kg to lb
    print("Peso convertido: {}".format(peso_convertido))
elif metrica.upper() == 'L':
    peso_convertido = peso * 0.453592  # lb to kg
    print("Peso convertido: {}".format(peso_convertido))
else: print("Métrica invalida")


# peso_convertido = peso * 0.453592 # kg to lb
# peso_convertido = peso / 0.453592 # lb to kg
