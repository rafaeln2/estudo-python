from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def ligar(self):
        print(f"Carro {self.modelo} ligado.")

            
class Moto(Veiculo):
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        # self.ligado = False

    def ligar(self):
        print(f"Moto {self.modelo} ligada.")
        
        

carro = Carro("vermelho", "Fusca")
carro.ligar()
carro.
Moto =  Moto("preto", "CB500")
Moto.ligar()