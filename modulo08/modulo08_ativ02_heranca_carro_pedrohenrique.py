# Bloco 1: Classe base (Carro) que define atributos e métodos gerais do veículo
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Bloco 2: Classe filha (CarroEletrico) que herda de Carro e adiciona a autonomia da bateria
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia da Bateria: {self.autonomia} km"

meu_carro = CarroEletrico("BYD", "Dolphin", 600)
print(meu_carro.exibir_info())