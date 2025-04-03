class CarroClasse():
    def __init__(self, cor : str, modelo : str, ano : int):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"
    
    def ligar(self):
        return f"{self.modelo} está ligado"
    def desligar(self):
        return f"{self.modelo} está desligado"

carro = CarroClasse("prata", "Polo", 2000)
print(carro.descricao())
print(carro.ligar())
carro.cor = "azul"
print(carro.descricao())