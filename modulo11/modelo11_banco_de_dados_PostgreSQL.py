"""
=========================================================
MÓDULO 11 - BANCO DE DADOS COM POSTGRESQL
PROJETO: SISTEMA DE GERENCIAMENTO DE VENDAS
Autor: Pedro Henrique

Tecnologias:
- Python
- PostgreSQL

Funcionalidades:
- Criação das tabelas
- Cadastro de clientes
- Cadastro de produtos
- Registro de vendas
- Listagem de clientes, produtos e vendas
- Atualização de clientes
- Exclusão de clientes
- Filtro de clientes por nome
- Tratamento de erros
=========================================================
"""

import os
import psycopg2
from psycopg2 import Error


# =========================================================
# CONFIGURAÇÃO DO BANCO
# =========================================================

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "meu_banco"),
    "user": os.getenv("DB_USER", "meu_usuario"),
    "password": os.getenv("DB_PASSWORD", "minha_senha"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}


# =========================================================
# CONEXÃO COM O BANCO
# =========================================================

def conectar():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("\nConectado ao PostgreSQL com sucesso!")
        return conn

    except Error as erro:
        print("\nErro ao conectar ao PostgreSQL.")
        print("Verifique o banco, usuário, senha e se o PostgreSQL está ligado.")
        print(f"Detalhes: {erro}")
        return None


# =========================================================
# CRIAÇÃO DAS TABELAS
# =========================================================

def criar_tabelas(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                preco NUMERIC(10, 2) NOT NULL CHECK (preco >= 0),
                estoque INTEGER NOT NULL DEFAULT 0 CHECK (estoque >= 0)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id SERIAL PRIMARY KEY,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL CHECK (quantidade > 0),
                data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (cliente_id)
                    REFERENCES clientes(id),

                FOREIGN KEY (produto_id)
                    REFERENCES produtos(id)
            )
        """)

        conn.commit()
        print("Tabelas verificadas/criadas com sucesso!")

    except Error as erro:
        conn.rollback()
        print(f"Erro ao criar tabelas: {erro}")

    finally:
        cursor.close()


# =========================================================
# CLIENTES - INSERIR
# =========================================================

def inserir_cliente(conn):
    nome = input("Nome do cliente: ").strip()
    email = input("E-mail do cliente: ").strip()

    if not nome or not email:
        print("Nome e e-mail são obrigatórios.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO clientes (nome, email)
            VALUES (%s, %s)
        """, (nome, email))

        conn.commit()
        print("Cliente cadastrado com sucesso!")

    except Error as erro:
        conn.rollback()
        print(f"Erro ao cadastrar cliente: {erro}")

    finally:
        cursor.close()


# =========================================================
# CLIENTES - CONSULTAR
# =========================================================

def listar_clientes(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id, nome, email
            FROM clientes
            ORDER BY id
        """)

        clientes = cursor.fetchall()

        print("\n========== CLIENTES ==========")

        if not clientes:
            print("Nenhum cliente cadastrado.")

        else:
            for cliente in clientes:
                print(
                    f"ID: {cliente[0]} | "
                    f"Nome: {cliente[1]} | "
                    f"E-mail: {cliente[2]}"
                )

    except Error as erro:
        print(f"Erro ao consultar clientes: {erro}")

    finally:
        cursor.close()


# =========================================================
# CLIENTES - ATUALIZAR
# =========================================================

def atualizar_cliente(conn):
    try:
        cliente_id = int(
            input("ID do cliente que deseja atualizar: ")
        )

    except ValueError:
        print("Digite um ID válido.")
        return

    novo_nome = input("Novo nome: ").strip()
    novo_email = input("Novo e-mail: ").strip()

    if not novo_nome or not novo_email:
        print("Nome e e-mail são obrigatórios.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE clientes
            SET nome = %s,
                email = %s
            WHERE id = %s
        """, (novo_nome, novo_email, cliente_id))

        if cursor.rowcount == 0:
            print("Cliente não encontrado.")
            conn.rollback()

        else:
            conn.commit()
            print("Cliente atualizado com sucesso!")

    except Error as erro:
        conn.rollback()
        print(f"Erro ao atualizar cliente: {erro}")

    finally:
        cursor.close()


# =========================================================
# CLIENTES - DELETAR
# =========================================================

def deletar_cliente(conn):
    try:
        cliente_id = int(
            input("ID do cliente que deseja excluir: ")
        )

    except ValueError:
        print("Digite um ID válido.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM clientes
            WHERE id = %s
        """, (cliente_id,))

        if cursor.rowcount == 0:
            print("Cliente não encontrado.")
            conn.rollback()

        else:
            conn.commit()
            print("Cliente excluído com sucesso!")

    except Error as erro:
        conn.rollback()
        print("Não foi possível excluir o cliente.")
        print("Ele pode possuir vendas cadastradas.")
        print(f"Detalhes: {erro}")

    finally:
        cursor.close()


# =========================================================
# CLIENTES - FILTRAR
# =========================================================

def filtrar_clientes(conn):
    inicio = input(
        "Digite o começo do nome (ex.: A): "
    ).strip()

    if not inicio:
        print("Digite pelo menos uma letra.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id, nome, email
            FROM clientes
            WHERE nome ILIKE %s
            ORDER BY nome
        """, (inicio + "%",))

        clientes = cursor.fetchall()

        print("\n====== RESULTADO DA BUSCA ======")

        if not clientes:
            print("Nenhum cliente encontrado.")

        else:
            for cliente in clientes:
                print(
                    f"ID: {cliente[0]} | "
                    f"Nome: {cliente[1]} | "
                    f"E-mail: {cliente[2]}"
                )

    except Error as erro:
        print(f"Erro ao filtrar clientes: {erro}")

    finally:
        cursor.close()


# =========================================================
# PRODUTOS - INSERIR
# =========================================================

def inserir_produto(conn):
    nome = input("Nome do produto: ").strip()

    try:
        preco = float(
            input("Preço: ").replace(",", ".")
        )

        estoque = int(
            input("Quantidade em estoque: ")
        )

    except ValueError:
        print("Preço ou estoque inválido.")
        return

    if not nome or preco < 0 or estoque < 0:
        print("Informe valores válidos.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (%s, %s, %s)
        """, (nome, preco, estoque))

        conn.commit()
        print("Produto cadastrado com sucesso!")

    except Error as erro:
        conn.rollback()
        print(f"Erro ao cadastrar produto: {erro}")

    finally:
        cursor.close()


# =========================================================
# PRODUTOS - CONSULTAR
# =========================================================

def listar_produtos(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            ORDER BY id
        """)

        produtos = cursor.fetchall()

        print("\n========== PRODUTOS ==========")

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

    except Error as erro:
        print(f"Erro ao consultar produtos: {erro}")

    finally:
        cursor.close()


# =========================================================
# VENDAS - REGISTRAR
# =========================================================

def registrar_venda(conn):
    try:
        cliente_id = int(
            input("ID do cliente: ")
        )

        produto_id = int(
            input("ID do produto: ")
        )

        quantidade = int(
            input("Quantidade: ")
        )

    except ValueError:
        print("Digite valores numéricos válidos.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    cursor = conn.cursor()

    try:

        # Verificar cliente
        cursor.execute("""
            SELECT id
            FROM clientes
            WHERE id = %s
        """, (cliente_id,))

        cliente = cursor.fetchone()

        if cliente is None:
            print("Cliente não encontrado.")
            conn.rollback()
            return

        # Verificar produto
        cursor.execute("""
            SELECT id, nome, preco, estoque
            FROM produtos
            WHERE id = %s
        """, (produto_id,))

        produto = cursor.fetchone()

        if produto is None:
            print("Produto não encontrado.")
            conn.rollback()
            return

        # Verificar estoque
        if produto[3] < quantidade:
            print(
                f"Estoque insuficiente. "
                f"Disponível: {produto[3]}"
            )
            conn.rollback()
            return

        # Registrar venda
        cursor.execute("""
            INSERT INTO vendas
                (cliente_id, produto_id, quantidade)
            VALUES
                (%s, %s, %s)
        """, (cliente_id, produto_id, quantidade))

        # Atualizar estoque
        cursor.execute("""
            UPDATE produtos
            SET estoque = estoque - %s
            WHERE id = %s
        """, (quantidade, produto_id))

        conn.commit()

        total = produto[2] * quantidade

        print("\nVenda registrada com sucesso!")
        print(f"Produto: {produto[1]}")
        print(f"Quantidade: {quantidade}")
        print(f"Total: R$ {total:.2f}")

    except Error as erro:
        conn.rollback()
        print(f"Erro ao registrar venda: {erro}")

    finally:
        cursor.close()


# =========================================================
# VENDAS - CONSULTAR
# =========================================================

def listar_vendas(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                v.id,
                c.nome,
                p.nome,
                v.quantidade,
                p.preco,
                v.quantidade * p.preco AS total,
                v.data_venda
            FROM vendas v

            INNER JOIN clientes c
                ON c.id = v.cliente_id

            INNER JOIN produtos p
                ON p.id = v.produto_id

            ORDER BY v.id
        """)

        vendas = cursor.fetchall()

        print("\n========== VENDAS ==========")

        if not vendas:
            print("Nenhuma venda registrada.")

        else:
            for venda in vendas:
                print(
                    f"Venda: {venda[0]} | "
                    f"Cliente: {venda[1]} | "
                    f"Produto: {venda[2]} | "
                    f"Quantidade: {venda[3]} | "
                    f"Total: R$ {venda[5]:.2f} | "
                    f"Data: {venda[6]}"
                )

    except Error as erro:
        print(f"Erro ao consultar vendas: {erro}")

    finally:
        cursor.close()


# =========================================================
# MENU PRINCIPAL
# =========================================================

def menu():

    conn = conectar()

    if conn is None:
        return

    try:

        criar_tabelas(conn)

        while True:

            print("""
=========================================================
       SISTEMA DE GERENCIAMENTO DE VENDAS
=========================================================

CLIENTES
1 - Cadastrar cliente
2 - Listar clientes
3 - Atualizar cliente
4 - Excluir cliente
5 - Filtrar clientes por nome

PRODUTOS
6 - Cadastrar produto
7 - Listar produtos

VENDAS
8 - Registrar venda
9 - Listar vendas

0 - Sair
=========================================================
""")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                inserir_cliente(conn)

            elif opcao == "2":
                listar_clientes(conn)

            elif opcao == "3":
                atualizar_cliente(conn)

            elif opcao == "4":
                deletar_cliente(conn)

            elif opcao == "5":
                filtrar_clientes(conn)

            elif opcao == "6":
                inserir_produto(conn)

            elif opcao == "7":
                listar_produtos(conn)

            elif opcao == "8":
                registrar_venda(conn)

            elif opcao == "9":
                listar_vendas(conn)

            elif opcao == "0":
                print("\nPrograma encerrado. Até mais!")
                break

            else:
                print("\nOpção inválida. Tente novamente.")

    finally:
        conn.close()
        print("Conexão com o PostgreSQL encerrada.")


# =========================================================
# INÍCIO DO PROGRAMA
# =========================================================

if __name__ == "__main__":
    menu()