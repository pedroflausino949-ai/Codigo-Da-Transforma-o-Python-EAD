"""
=========================================================
MÓDULO 11 - BANCO DE DADOS COM POSTGRESQL
PROJETO: SISTEMA DE GERENCIAMENTO DE VENDAS
Autor: Pedro Henrique

Tecnologias:
- Python
- PostgreSQL
- psycopg2
- SQL

Funcionalidades:
- Cadastro de clientes
- Cadastro de produtos
- Registro de vendas
- Listagem de dados
- Atualização de clientes
- Exclusão de clientes
- Controle de estoque
=========================================================
"""

import psycopg2
from decimal import Decimal, InvalidOperation


# =========================================================
# CONFIGURAÇÃO DO BANCO
# =========================================================

DB_CONFIG = {
    "host": "localhost",
    "database": "sistema_vendas",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}


# =========================================================
# CONEXÃO COM O BANCO
# =========================================================

def conectar():
    try:
        conexao = psycopg2.connect(
            host=DB_CONFIG["host"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"]
        )

        return conexao

    except psycopg2.Error as erro:
        print("\n❌ Erro ao conectar ao PostgreSQL!")
        print("Detalhes:", erro)
        return None


# =========================================================
# CRIAÇÃO DAS TABELAS
# =========================================================

def criar_tabelas():

    conexao = conectar()

    if conexao is None:
        return False

    cursor = None

    try:
        cursor = conexao.cursor()

        # -------------------------------------------------
        # TABELA DE CLIENTES
        # -------------------------------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL
            );
        """)

        # -------------------------------------------------
        # TABELA DE PRODUTOS
        # -------------------------------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                preco DECIMAL(10,2) NOT NULL,
                estoque INTEGER NOT NULL
            );
        """)

        # -------------------------------------------------
        # TABELA DE VENDAS
        # -------------------------------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id SERIAL PRIMARY KEY,
                cliente_id INTEGER REFERENCES clientes(id),
                produto_id INTEGER REFERENCES produtos(id),
                quantidade INTEGER NOT NULL,
                valor_total DECIMAL(10,2) NOT NULL,
                data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conexao.commit()

        print("✅ Tabelas verificadas/criadas com sucesso!")

        return True

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao criar tabelas:")
        print(erro)

        return False

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# CADASTRAR CLIENTE
# =========================================================

def cadastrar_cliente():

    print("\n" + "=" * 50)
    print("👤 CADASTRAR CLIENTE")
    print("=" * 50)

    nome = input("Digite o nome do cliente: ").strip()
    email = input("Digite o e-mail do cliente: ").strip()

    if nome == "":
        print("❌ O nome é obrigatório.")
        return

    if email == "":
        print("❌ O e-mail é obrigatório.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO clientes (nome, email)
            VALUES (%s, %s);
        """, (nome, email))

        conexao.commit()

        print("\n✅ Cliente cadastrado com sucesso!")

    except psycopg2.IntegrityError as erro:

        conexao.rollback()

        if "unique" in str(erro).lower():
            print("❌ Esse e-mail já está cadastrado.")
        else:
            print("❌ Erro de integridade:", erro)

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao cadastrar cliente:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# LISTAR CLIENTES
# =========================================================

def listar_clientes():

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, email
            FROM clientes
            ORDER BY id;
        """)

        clientes = cursor.fetchall()

        print("\n" + "=" * 70)
        print("👥 CLIENTES CADASTRADOS")
        print("=" * 70)

        if not clientes:

            print("Nenhum cliente cadastrado.")

        else:

            for cliente in clientes:

                print(
                    f"ID: {cliente[0]} | "
                    f"Nome: {cliente[1]} | "
                    f"E-mail: {cliente[2]}"
                )

    except psycopg2.Error as erro:

        print("❌ Erro ao listar clientes:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# ATUALIZAR CLIENTE
# =========================================================

def atualizar_cliente():

    print("\n" + "=" * 50)
    print("✏️ ATUALIZAR CLIENTE")
    print("=" * 50)

    try:

        id_cliente = int(
            input("Digite o ID do cliente: ")
        )

    except ValueError:

        print("❌ Digite um ID válido.")
        return

    novo_email = input(
        "Digite o novo e-mail: "
    ).strip()

    if novo_email == "":
        print("❌ O e-mail não pode ficar vazio.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE clientes
            SET email = %s
            WHERE id = %s;
        """, (novo_email, id_cliente))

        if cursor.rowcount == 0:

            print("❌ Cliente não encontrado.")

        else:

            conexao.commit()

            print("✅ E-mail atualizado com sucesso!")

    except psycopg2.IntegrityError as erro:

        conexao.rollback()

        if "unique" in str(erro).lower():

            print("❌ Esse e-mail já pertence a outro cliente.")

        else:

            print("❌ Erro de integridade:")
            print(erro)

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao atualizar cliente:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# EXCLUIR CLIENTE
# =========================================================

def excluir_cliente():

    print("\n" + "=" * 50)
    print("🗑️ EXCLUIR CLIENTE")
    print("=" * 50)

    try:

        id_cliente = int(
            input("Digite o ID do cliente que deseja excluir: ")
        )

    except ValueError:

        print("❌ Digite um ID válido.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT nome
            FROM clientes
            WHERE id = %s;
        """, (id_cliente,))

        cliente = cursor.fetchone()

        if cliente is None:

            print("❌ Cliente não encontrado.")
            return

        print(f"\nCliente encontrado: {cliente[0]}")

        confirmar = input(
            "Tem certeza que deseja excluir? (s/n): "
        ).strip().lower()

        if confirmar != "s":

            print("❌ Operação cancelada.")
            return

        cursor.execute("""
            DELETE FROM clientes
            WHERE id = %s;
        """, (id_cliente,))

        conexao.commit()

        print("✅ Cliente excluído com sucesso!")

    except psycopg2.IntegrityError:

        conexao.rollback()

        print(
            "\n⚠️ Esse cliente possui vendas cadastradas "
            "e não pode ser excluído."
        )

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao excluir cliente:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# CADASTRAR PRODUTO
# =========================================================

def cadastrar_produto():

    print("\n" + "=" * 50)
    print("📦 CADASTRAR PRODUTO")
    print("=" * 50)

    nome = input(
        "Digite o nome do produto: "
    ).strip()

    if nome == "":
        print("❌ O nome do produto é obrigatório.")
        return

    try:

        preco = Decimal(
            input("Digite o preço do produto: ")
            .replace(",", ".")
        )

        estoque = int(
            input("Digite a quantidade em estoque: ")
        )

    except (InvalidOperation, ValueError):

        print("❌ Preço ou estoque inválido.")
        return

    if preco < 0:

        print("❌ O preço não pode ser negativo.")
        return

    if estoque < 0:

        print("❌ O estoque não pode ser negativo.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (%s, %s, %s);
        """, (nome, preco, estoque))

        conexao.commit()

        print("✅ Produto cadastrado com sucesso!")

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao cadastrar produto:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# LISTAR PRODUTOS
# =========================================================

def listar_produtos():

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            ORDER BY id;
        """)

        produtos = cursor.fetchall()

        print("\n" + "=" * 75)
        print("📦 PRODUTOS CADASTRADOS")
        print("=" * 75)

        if not produtos:

            print("Nenhum produto cadastrado.")

        else:

            for produto in produtos:

                print(
                    f"ID: {produto[0]} | "
                    f"Produto: {produto[1]} | "
                    f"Preço: R$ {produto[2]:.2f} | "
                    f"Estoque: {produto[3]}"
                )

    except psycopg2.Error as erro:

        print("❌ Erro ao listar produtos:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# REALIZAR VENDA
# =========================================================

def realizar_venda():

    print("\n" + "=" * 50)
    print("🛒 REALIZAR VENDA")
    print("=" * 50)

    try:

        cliente_id = int(
            input("Digite o ID do cliente: ")
        )

        produto_id = int(
            input("Digite o ID do produto: ")
        )

        quantidade = int(
            input("Digite a quantidade: ")
        )

    except ValueError:

        print("❌ Digite apenas números válidos.")
        return

    if quantidade <= 0:

        print("❌ A quantidade deve ser maior que zero.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        # -------------------------------------------------
        # VERIFICAR CLIENTE
        # -------------------------------------------------

        cursor.execute("""
            SELECT id, nome
            FROM clientes
            WHERE id = %s;
        """, (cliente_id,))

        cliente = cursor.fetchone()

        if cliente is None:

            print("❌ Cliente não encontrado.")
            return

        # -------------------------------------------------
        # VERIFICAR PRODUTO
        # -------------------------------------------------

        cursor.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            WHERE id = %s;
        """, (produto_id,))

        produto = cursor.fetchone()

        if produto is None:

            print("❌ Produto não encontrado.")
            return

        preco = produto[2]
        estoque = produto[3]

        # -------------------------------------------------
        # VERIFICAR ESTOQUE
        # -------------------------------------------------

        if quantidade > estoque:

            print(
                f"❌ Estoque insuficiente.\n"
                f"Disponível: {estoque}"
            )

            return

        # -------------------------------------------------
        # CALCULAR TOTAL
        # -------------------------------------------------

        valor_total = preco * quantidade

        # -------------------------------------------------
        # REGISTRAR VENDA
        # -------------------------------------------------

        cursor.execute("""
            INSERT INTO vendas
            (
                cliente_id,
                produto_id,
                quantidade,
                valor_total
            )
            VALUES (%s, %s, %s, %s);
        """, (
            cliente_id,
            produto_id,
            quantidade,
            valor_total
        ))

        # -------------------------------------------------
        # ATUALIZAR ESTOQUE
        # -------------------------------------------------

        cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - %s
            WHERE id = %s;
        """, (
            quantidade,
            produto_id
        ))

        conexao.commit()

        print("\n" + "=" * 55)
        print("🛒 VENDA REALIZADA COM SUCESSO!")
        print("=" * 55)

        print(f"Cliente: {cliente[1]}")
        print(f"Produto: {produto[1]}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")

        print("=" * 55)

    except psycopg2.Error as erro:

        conexao.rollback()

        print("❌ Erro ao realizar venda:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# LISTAR VENDAS
# =========================================================

def listar_vendas():

    conexao = conectar()

    if conexao is None:
        return

    cursor = None

    try:

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                v.id,
                c.nome,
                p.nome,
                v.quantidade,
                v.valor_total,
                v.data_venda
            FROM vendas v
            JOIN clientes c
                ON v.cliente_id = c.id
            JOIN produtos p
                ON v.produto_id = p.id
            ORDER BY v.id;
        """)

        vendas = cursor.fetchall()

        print("\n" + "=" * 80)
        print("💰 VENDAS REALIZADAS")
        print("=" * 80)

        if not vendas:

            print("Nenhuma venda realizada.")

        else:

            for venda in vendas:

                print(f"ID da venda: {venda[0]}")
                print(f"Cliente: {venda[1]}")
                print(f"Produto: {venda[2]}")
                print(f"Quantidade: {venda[3]}")
                print(f"Valor total: R$ {venda[4]:.2f}")
                print(f"Data: {venda[5]}")
                print("-" * 80)

    except psycopg2.Error as erro:

        print("❌ Erro ao listar vendas:")
        print(erro)

    finally:

        if cursor:
            cursor.close()

        conexao.close()


# =========================================================
# MENU PRINCIPAL
# =========================================================

def menu():

    print("\n🔄 Inicializando sistema...")

    if not criar_tabelas():

        print("\n❌ Não foi possível iniciar o sistema.")
        print("Verifique se o PostgreSQL está funcionando.")
        return

    while True:

        print("\n")
        print("=" * 60)
        print("       🛒 SISTEMA DE GERENCIAMENTO DE VENDAS")
        print("=" * 60)

        print("\n👥 CLIENTES")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar e-mail")
        print("4 - Excluir cliente")

        print("\n📦 PRODUTOS")
        print("5 - Cadastrar produto")
        print("6 - Listar produtos")

        print("\n💰 VENDAS")
        print("7 - Realizar venda")
        print("8 - Listar vendas")

        print("\n0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":

            cadastrar_cliente()

        elif opcao == "2":

            listar_clientes()

        elif opcao == "3":

            atualizar_cliente()

        elif opcao == "4":

            excluir_cliente()

        elif opcao == "5":

            cadastrar_produto()

        elif opcao == "6":

            listar_produtos()

        elif opcao == "7":

            realizar_venda()

        elif opcao == "8":

            listar_vendas()

        elif opcao == "0":

            print("\n👋 Sistema encerrado. Até mais!")
            break

        else:

            print("\n❌ Opção inválida. Escolha uma opção do menu.")


# =========================================================
# INÍCIO DO PROGRAMA
# =========================================================

if __name__ == "__main__":
    menu() 

    DB_CONFIG = {
    "host": "localhost",
    "database": "sistema_vendas",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}