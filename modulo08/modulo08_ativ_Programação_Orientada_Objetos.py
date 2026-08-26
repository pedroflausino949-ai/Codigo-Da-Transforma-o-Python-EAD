"""
MODULO 8 - PROGRAMACAO ORIENTADA A OBJETOS
Atividade pratica - 3 exercicios e desafio extra
Autor: Pedro Henrique
"""

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        # Comentário 1: Imprime o rótulo e o valor da marca armazenada no objeto
        print("Marca:", self.marca)
        
        # Comentário 2: Imprime o rótulo e o valor do modelo armazenado no objeto
        print("Modelo:", self.modelo)