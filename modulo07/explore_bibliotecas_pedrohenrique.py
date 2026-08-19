from datetime import datetime
from Faker import Faker

# Inicializa o gerador de dados falsos em português
fake = Faker("pt_PT")


def criar_utilizador_ficticio():
    # 1. Gerar dados falsos com a biblioteca 'faker'
    nome = fake.name()
    email = fake.email()

    # Gera uma data de nascimento do tipo datetime.date (entre 18 e 65 anos atrás)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)

    # 2. Trabalhar com datas usando a biblioteca 'datetime'
    data_atual = datetime.now().date()

    # Calcular a idade correta considerando o mês e o dia
    idade = (
        data_atual.year
        - data_nascimento.year
        - (
            (data_atual.month, data_atual.day)
            < (data_nascimento.month, data_nascimento.day)
        )
    )

    # Formatar a data para o padrão português (Dia/Mês/Ano)
    data_formatada = data_nascimento.strftime("%d/%m/%Y")

    # Exibir os resultados
    print("--- Perfil de Utilizador Gerado ---")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Data de Nascimento: {data_formatada}")
    print(f"Idade Calculada: {idade} anos")


# Executar o programa
if __name__ == "__main__":
    criar_utilizador_ficticio()
