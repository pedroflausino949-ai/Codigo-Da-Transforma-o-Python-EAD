"""
Programador: as variaveis, serão inseridas no app - BACK-End

Dev: existe a interação com o usuario - Web Design (Front-End)

"""

import datetime
from faker import Faker
import modulo07.utilidades as utilidades

# Instancia a biblioteca Faker configurada para gerar dados fictícios no padrão brasileiro
fake = Faker("pt_BR")


# Comentário 1: Exibe no console os dados pessoais fictícios gerados aleatoriamente pelo Faker
print("**Dados Criados - Prova de Matemática**")
print(f"Nome de Mentira: {fake.name()}")
print(f"E-Mail de Mentira: {fake.email()}")
print(f"Telefone de Mentira: {fake.phone_number()}")


# Comentário 2: Captura e exibe a data e hora atuais do sistema formatadas (hora:minuto dia/mês/ano)
print("\n**Dados da Prova de Mentira**")

agora = datetime.datetime.now()
print(f"Data e hora atual: {agora.strftime('%H:%M %d/%m/%Y')}")


# Definição das variáveis numéricas que serão usadas nos cálculos do módulo de utilidades
num1 = 10
num2 = 5

print("\n⚙️ 🧱 Teste de Utilidades ⚙️ 🧱")
print(f"Números utilizados: {num1} e {num2}")


# Comentário 3: Exibe os resultados das operações matemáticas básicas importadas do módulo 'utilidades'
print(f"Usando Adição ({num1} + {num2}):", utilidades.soma(num1, num2))

print(f"Usando Subtração ({num1} - {num2}):", utilidades.subtrair(num1, num2))

print(f"Multiplicação ({num1} * {num2}):", utilidades.multiplicar(num1, num2))

print(f"Divisão ({num1} / {num2}):", utilidades.dividir(num1, num2))

print(
    f"Divisão Inteira ({num1} // {num2}):",
    utilidades.divisao_inteira(num1, num2),
)

print(f"Resto da Divisão ({num1} % {num2}):", utilidades.resto_divisao(num1, num2))

print(f"Potenciação ({num1} ^ {num2}):", utilidades.potencia(num1, num2))


# Comentário 4: Executa o teste de tratamento de exceção para garantir que a função lide com divisão por zero sem quebrar o programa
print("\n=== TESTE DE SEGURANÇA (DIVISÃO POR ZERO) ===")
print("Divisão por zero:", utilidades.dividir(10, 0))