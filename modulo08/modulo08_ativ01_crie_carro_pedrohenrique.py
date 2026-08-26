class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


# Comentário 1: Exibe o cabeçalho inicial para o usuário no terminal
print("🚗 CADASTRO DE VEÍCULO 🚗\n")

marca_digitada = input("Digite a marca do carro: ")
modelo_digitado = input("Digite o modelo do carro: ")

meu_carro = Carro(marca_digitada, modelo_digitado)

# Comentário 2: Exibe o separador/título antes de mostrar os dados cadastrados
print("\n--- Informações do Carro Cadastrado ---")

# Comentário 3: Imprime no console o resultado retornado pelo método exibir_info() do objeto
print(meu_carro.exibir_info())