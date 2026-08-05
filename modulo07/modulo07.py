# Módulo de funções matemáticas

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def potencia(base, expoente):
    return base ** expoente

import utilidades

print("=== Utilizando o módulo utilidades ===")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"Soma: {utilidades.soma(n1, n2)}")
print(f"Subtração: {utilidades.subtracao(n1, n2)}")
print(f"Potência: {utilidades.potencia(n1, n2)}")

from datetime import datetime

print("=== Data e Hora Atual ===")

agora = datetime.now()

print("Data:", agora.strftime("%d/%m/%Y"))
print("Hora:", agora.strftime("%H:%M:%S"))

from faker import Faker

fake = Faker("pt_BR")

print("Nome:", fake.name())
print("Endereço:", fake.address())
print("Email:", fake.email())

import random
import math

numero = random.randint(1, 100)

tentativas = 0

print("=== Jogo da Adivinhação ===")

while True:

    palpite = int(input("Digite um número entre 1 e 100: "))

    tentativas += 1

    if palpite == numero:
        print("Parabéns! Você acertou!")
        break

    elif palpite < numero:
        print("O número é maior!")

    else:
        print("O número é menor!")

distancia = math.fabs(numero - palpite)

print(f"Número correto: {numero}")
print(f"Tentativas: {tentativas}")
print(f"Diferença do último palpite: {distancia}")

import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("\nSenha segura gerada:")
print(senha)

def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero * 3

def boas_vindas():
    print("Bem-vindo ao Projeto Grande!")

    from matematica.calculos import dobro, triplo
from textos.mensagens import boas_vindas

boas_vindas()

numero = int(input("Digite um número: "))

print("Dobro:", dobro(numero))
print("Triplo:", triplo(numero))

