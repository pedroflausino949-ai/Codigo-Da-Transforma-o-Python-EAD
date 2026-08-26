# Solicitando dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calculando as operações
soma = num1 + num2
diferenca = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
resto = num1 % num2 if num2 != 0 else "N/A"

# Exibindo os resultados
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão (%): {resto}")


# Solicita dois números inteiros
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Verifica qual número é maior
if n1 > n2:
    print(f"O maior número é {n1}.")
elif n2 > n1:
    print(f"O maior número é {n2}.")
else:
    print("Os dois números são iguais.")


    # Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Classifica a faixa etária
if idade < 0:
    print("Idade inválida!")
elif idade <= 12:
    print("Categoria: Criança")
elif idade <= 17:
    print("Categoria: Adolescente")
elif idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")