from typing import Callable, TypeVar

T = TypeVar("T")


def pedir_dado_validado(
    mensagem_input: str,
    mensagem_erro: str,
    conversor: Callable[[str], T],
    validador: Callable[[T], bool],
) -> T:
    """Solicita uma entrada ao usuário até que ela seja convertida e validada com sucesso."""
    while True:
        try:
            entrada = input(mensagem_input).strip()
            valor = conversor(entrada)

            if validador(valor):
                return valor

            print(f"❌ {mensagem_erro}\n")
        except ValueError:
            print(f"❌ Entrada inválida! Verifique o formato digitado.\n")


def main():
    print("=" * 50)
    print(" 🛠️  SISTEMA DE ENTRADA DE DADOS PRO (VS CODE)")
    print("=" * 50 + "\n")

    try:
        # Validação de Idade (Inteiro > 0)
        idade = pedir_dado_validado(
            mensagem_input="👉 Digite sua idade: ",
            mensagem_erro="A idade deve ser um número inteiro maior que zero.",
            conversor=int,
            validador=lambda x: x > 0,
        )

        # Exemplo extra: Reaproveitando a mesma função para outro dado!
        altura = pedir_dado_validado(
            mensagem_input="👉 Digite sua altura em metros (ex: 1.75): ",
            mensagem_erro="A altura deve ser um valor entre 0.5m e 2.5m.",
            conversor=float,
            validador=lambda x: 0.5 <= x <= 2.5,
        )

        print("\n" + "-" * 50)
        print(f"✅ Dados Cadastrados: Idade = {idade} anos | Altura = {altura}m")
        print("-" * 50)

    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ Processo cancelado pelo usuário.")


if __name__ == "__main__":
    main()