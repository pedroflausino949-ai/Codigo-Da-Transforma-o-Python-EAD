# ==============================================================================
# BLOCO 1: Operações Matemáticas via Módulo Externo
# ==============================================================================
import modulo07.utilidades as utilidades

print("=== Utilizando o módulo utilidades ===")

# Recebe os dois números digitados pelo usuário e converte para decimal (float)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Executa e exibe as funções importadas do módulo 'utilidades'
print(f"Soma: {utilidades.soma(n1, n2)}")
print(f"Subtração: {utilidades.subtracao(n1, n2)}")
print(f"Potência: {utilidades.potencia(n1, n2)}")


# ==============================================================================
# BLOCO 2: Exibição de Data e Hora Atuais
# ==============================================================================
from datetime import datetime

print("\n=== Data e Hora Atual ===")

# Captura a data/hora exata do sistema e formata nos padrões brasileiros
agora = datetime.now()
print("Data:", agora.strftime("%d/%m/%Y"))
print("Hora:", agora.strftime("%H:%M:%S"))


# ==============================================================================
# BLOCO 3: Geração de Dados Fictícios com Faker
# (Corrigido: 'faker' com 'f' minúsculo)
# ==============================================================================
from faker import Faker

fake = Faker("pt_BR")

print("\n=== Dados Fictícios Criados ===")
print("Nome:", fake.name())
print("Endereço:", fake.address())
print("Email:", fake.email())


# ==============================================================================
# BLOCO 4: Jogo da Adivinhação com Cálculo de Distância
# ==============================================================================
import random
import math

numero = random.randint(1, 100)
tentativas = 0

print("\n=== Jogo da Adivinhação ===")

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if palpite == numero:
        print("\nParabéns! Você acertou!")
        print(f"Número correto: {numero}")
        print(f"Total de tentativas: {tentativas}")
        break
    elif palpite < numero:
        print("O número é maior!")
    else:
        print("O número é menor!")

    # Exibe a diferença/distância do palpite atual em relação ao número secreto
    distancia = math.fabs(numero - palpite)
    print(f"Diferença do seu último palpite: {distancia}\n")


# ==============================================================================
# BLOCO 5: Gerador de Senhas Aleatórias
# ==============================================================================
import string

print("\n=== Gerador de Senha ===")
tamanho = int(input("Digite o tamanho da senha: "))

# Junta letras (maiúsculas e minúsculas), dígitos e símbolos pontuais
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("\nSenha segura gerada:")
print(senha)


# ==============================================================================
# BLOCO 6: Funções Personalizadas e Execução
# ==============================================================================
def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero * 3

def boas_vindas():
    print("\nBem-vindo ao Projeto Grande!")

# Execução do bloco final
boas_vindas()

numero = int(input("Digite um número para calcular o dobro e triplo: "))
print("Dobro:", dobro(numero))
print("Triplo:", triplo(numero))