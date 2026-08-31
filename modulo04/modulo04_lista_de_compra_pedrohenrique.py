# 🚀 Projeto: Lista de Compras
# Este programa permite que você gerencie uma lista de compras.

# Começamos com uma lista vazia, onde os itens serão guardados.
lista_de_compras = []

# O programa vai rodar em um ciclo (loop) até você decidir sair.
while True:
    # Mostramos as opções disponíveis.
    print("\n--- Menu ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver a lista")
    print("4. Sair")
    
    # Pedimos ao usuário para escolher uma opção.
    escolha = input("Escolha uma opção (1-4): ")

    # Se a escolha for '1', vamos adicionar um item.
    if escolha == '1':
        item = input("Digite o nome do item: ")
        # Adicionamos o item no final da lista.
        lista_de_compras.append(item)
        print(f"✅ '{item}' adicionado!")
        
    # Se a escolha for '2', vamos remover um item.
    elif escolha == '2':
        item_a_remover = input("Digite o nome do item para remover: ")
        # Verificamos se o item existe na lista.
        if item_a_remover in lista_de_compras:
            # Se existir, removemos o item.
            lista_de_compras.remove(item_a_remover)
            print(f"🗑️ '{item_a_remover}' removido da lista.")
        else:
            # Se não existir, avisamos o usuário.
            print(f"❌ Erro: '{item_a_remover}' não está na lista.")
            
    # Se a escolha for '3', vamos ver a lista.
    elif escolha == '3':
        # Verificamos se a lista não está vazia.
        if lista_de_compras:
            print("\n🛒 Sua lista de compras:")
            # Percorremos a lista e mostramos cada item.
            for i, item in enumerate(lista_de_compras, start=1):
                print(f"{i}. {item}")
        else:
            # Se a lista estiver vazia, avisamos.
            print("📝 Sua lista está vazia.")
            
    # Se a escolha for '4', saímos do programa.
    elif escolha == '4':
        print("👋 Até mais!")
        break # Este comando encerra o ciclo (loop).
        
    # Se a opção for inválida, pedimos para tentar de novo