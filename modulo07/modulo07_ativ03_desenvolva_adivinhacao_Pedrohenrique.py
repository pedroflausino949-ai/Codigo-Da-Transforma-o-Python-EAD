import random


def jogar():
    numero_secreto = random.randint(1, 24)
    tentativas = 0
    acertou = False

    # Comentário 1: Exibe a mensagem de boas-vindas e as instruções do jogo
    print("=" * 40)
    print("  Bem-vindo ao Jogo da Adivinhação!  ")
    print("=" * 40)
    print("Tente adivinhar o número secreto entre 1 e 24.\n")

    while not acertou:
        try:
            chute = int(input("Digite um número de 1 a 24: "))

            if chute < 1 or chute > 24:
                # Comentário 2: Alerta o usuário quando o número inserido está fora do intervalo permitido
                print("Por favor, digite um número válido entre 1 e 24!")
                continue

            tentativas += 1

            if chute == numero_secreto:
                acertou = True
                # Comentário 3: Exibe a mensagem de vitória informando o número correto e o total de tentativas
                print(
                    f"\nParabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!"
                )
            elif chute < numero_secreto:
                # Comentário 4: Dá uma dica ao usuário informando que o número procurado é maior
                print("O número secreto é MAIOR. Tente novamente!")
            else:
                # Comentário 5: Dá uma dica ao usuário informando que o número procurado é menor
                print("O número secreto é MENOR. Tente novamente!")

        except ValueError:
            # Comentário 6: Trata erros de digitação caso o usuário insira algo que não seja um número inteiro
            print("Entrada inválida! Digite apenas números inteiros.")


if __name__ == "__main__":
    jogar()