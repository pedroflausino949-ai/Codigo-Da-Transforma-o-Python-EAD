"""
MÓDULO 9 - TRATAMENTO DE ERROS
Desafio Prático - Validação e Tratamento de Erros
Autor: Pedro Henrique

Sistema de cadastro de usuários com validação de dados
e tratamento de exceções.
"""


# ==========================================================
# EXCEÇÃO PERSONALIZADA
# ==========================================================

class DadosInvalidosError(Exception):
    """Exceção criada para representar dados inválidos."""
    pass


# ==========================================================
# VALIDAÇÃO DO NOME
# ==========================================================

def validar_nome(nome):
    nome = nome.strip()

    if nome == "":
        raise DadosInvalidosError("O nome não pode ficar vazio.")

    if len(nome) < 3:
        raise DadosInvalidosError(
            "O nome deve possuir pelo menos 3 caracteres."
        )

    if any(char.isdigit() for char in nome):
        raise DadosInvalidosError(
            "O nome não pode conter números."
        )

    return nome


# ==========================================================
# VALIDAÇÃO DA IDADE
# ==========================================================

def validar_idade(idade):
    try:
        idade = int(idade)
    except ValueError:
        raise DadosInvalidosError(
            "A idade deve ser um número inteiro."
        )

    if idade < 0 or idade > 120:
        raise DadosInvalidosError(
            "Digite uma idade válida entre 0 e 120 anos."
        )

    return idade


# ==========================================================
# VALIDAÇÃO DO E-MAIL
# ==========================================================

def validar_email(email):
    email = email.strip()

    if email == "":
        raise DadosInvalidosError(
            "O e-mail não pode ficar vazio."
        )

    if "@" not in email or "." not in email:
        raise DadosInvalidosError(
            "Digite um e-mail válido."
        )

    return email


# ==========================================================
# CADASTRO DO USUÁRIO
# ==========================================================

def cadastrar_usuario():
    print("\n" + "=" * 50)
    print("          CADASTRO DE USUÁRIO")
    print("=" * 50)

    try:
        # Entrada do nome
        nome = input("Digite seu nome: ")
        nome = validar_nome(nome)

        # Entrada da idade
        idade = input("Digite sua idade: ")
        idade = validar_idade(idade)

        # Entrada do e-mail
        email = input("Digite seu e-mail: ")
        email = validar_email(email)

    except DadosInvalidosError as erro:
        print(f"\n❌ Erro de validação: {erro}")

    except Exception as erro:
        print(f"\n❌ Ocorreu um erro inesperado: {erro}")

    else:
        print("\n" + "=" * 50)
        print("       CADASTRO REALIZADO COM SUCESSO!")
        print("=" * 50)

        print(f"Nome:  {nome}")
        print(f"Idade: {idade}")
        print(f"E-mail: {email}")

    finally:
        print("\nProcesso de cadastro finalizado.")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    while True:

        print("\n" + "=" * 50)
        print("       SISTEMA DE CADASTRO DE USUÁRIOS")
        print("=" * 50)

        print("1 - Cadastrar usuário")
        print("2 - Sair")

        try:
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_usuario()

            elif opcao == "2":
                print("\nPrograma encerrado. Até mais!")
                break

            else:
                raise DadosInvalidosError(
                    "Escolha apenas a opção 1 ou 2."
                )

        except DadosInvalidosError as erro:
            print(f"\n❌ Erro: {erro}")

        except Exception as erro:
            print(f"\n❌ Erro inesperado: {erro}")

        finally:
            print("-" * 50)


# ==========================================================
# EXECUÇÃO
# ==========================================================

if __name__ == "__main__":
    main()