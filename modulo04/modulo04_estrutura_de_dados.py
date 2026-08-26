compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ").strip()
        if item:
            compras.append(item)
            print(f"'{item}' adicionado com sucesso!")
    elif opcao == "2":
        item = input("Digite o item para remover: ").strip()
        if item in compras:
            compras.remove(item)
            print(f"'{item}' removido com sucesso!")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("\nItens na lista:")
        if not compras:
            print("(Lista vazia)")
        else:
            for i, item in enumerate(compras, start=1):
                print(f"{i}. {item}")
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")


        aluno = {
    "nome": "Ana Silva",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")
media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média: {media:.2f}")


numeros = {12, 7, 3, 44, 19, 20, 5, 8, 10}

pares = set()
impares = set()

for num in numeros:
    if num % 2 == 0:
        pares.add(num)
    else:
        impares.add(num)

print(f"Números Pares: {sorted(list(pares))}")
print(f"Números Ímpares: {sorted(list(impares))}")


tarefas = []

while True:
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Exibir tarefas em ordem alfabética")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ").strip()
        if tarefa:
            tarefas.append(tarefa)
            print("Tarefa adicionada!")
    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ").strip()
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida!")
        else:
            print("Tarefa não encontrada.")
    elif opcao == "3":
        if not tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            tarefas.sort()
            print("\nLista de tarefas (Ordem Alfabética):")
            for t in tarefas:
                print(f"- {t}")
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")


        agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Visualizar todos os contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        telefone = input("Digite o telefone: ").strip()
        agenda[nome] = telefone
        print(f"Contato '{nome}' salvo com sucesso!")
    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido!")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Digite o nome do contato a buscar: ").strip()
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("\nLista de Contatos:")
        if not agenda:
            print("(Agenda vazia)")
        else:
            for nome, telefone in agenda.items():
                print(f"- {nome}: {telefone}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")