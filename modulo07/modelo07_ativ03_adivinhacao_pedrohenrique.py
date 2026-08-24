import random


def jogar():
    numero_secreto = random.randint(1, 24)
    tentativas = 0
    acertou = False

    print("=" * 40)
    print("  Bem-vindo ao Jogo da Adivinhação!  ")
    print("=" * 40)
    print("Tente adivinhar o número secreto entre 1 e 24.\n")

    while not acertou:
        try:
            chute = int(input("Digite um número de 1 a 24: "))

            if chute < 1 or chute > 24:
                print("Por favor, digite um número válido entre 1 e 24!")
                continue

            tentativas += 1

            if chute == numero_secreto:
                acertou = True
                print(
                    f"\nParabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!"
                )
            elif chute < numero_secreto:
                print("O número secreto é MAIOR. Tente novamente!")
            else:
                print("O número secreto é MENOR. Tente novamente!")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


if __name__ == "__main__":
    jogar()