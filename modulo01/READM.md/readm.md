# 💈 Sistema de Vendas - Barbearia

## 📌 Visão Geral
O **Sistema de Vendas da Barbearia** foi desenvolvido para auxiliar no gerenciamento de produtos comercializados em uma barbearia por meio de uma interface gráfica simples, moderna e intuitiva. 

A aplicação permite cadastrar produtos, controlar o estoque, registrar vendas, atualizar preços, aplicar descontos, buscar produtos e acompanhar o faturamento obtido em tempo real. Todas as operações são realizadas via botões e campos de entrada integrados com a biblioteca Tkinter, dispensando o uso do terminal.

---

## 🚀 Funcionalidades Principais

- ➕ **Cadastro de Novos Produtos:** Adicione novos itens informando nome, preço e quantidade inicial.
- 📋 **Exibição em Tempo Real:** Visualização dinâmica dos produtos cadastrados e seus respectivos status de estoque.
- 🛒 **Realização de Vendas:** Baixa e atualização automática do estoque a cada venda efetuada.
- 🗑️ **Remoção de Produtos:** Exclusão de itens do catálogo do sistema.
- 💲 **Atualização de Preços:** Modificação fácil e rápida do preço de venda de qualquer produto.
- 📦 **Reposição de Estoque:** Adição de novas unidades a produtos já cadastrados.
- 💰 **Consulta de Faturamento:** Visualização do faturamento total acumulado com as vendas.
- 🔍 **Busca por Nome:** Pesquisa rápida de produtos na lista.
- 🏷️ **Aplicação de Descontos:** Concessão de descontos percentuais ou diretos nos preços dos produtos.
- 💬 **Interface Intuitiva & Feedback:** Mensagens gráficas de confirmação, alertas de validação e tratamento de erros.

---

## 🛠️ Tecnologias e Estruturas Utilizadas

### Linguagem
- **Python 3**

### Biblioteca Principal
- **Tkinter** (Interface Gráfica Nativa do Python)

### Componentes de Interface (Tkinter / TTK)
- `Tk()`: Janela principal da aplicação.
- `Label`, `Entry`, `Button`, `Frame`, `LabelFrame`: Construção e estruturação do layout.
- `Text`: Exibição detalhada da lista de produtos e relatórios.
- `messagebox`: Diálogos pop-up para notificações de sucesso, erro e alertas.
- `ttk.Style`: Estilização e personalização visual dos componentes.

### Estruturas de Programação
- **Variáveis Globais e Estruturas de Dados:** Armazenamento dinâmico do catálogo e faturamento.
- **Funções Modularizadas:** Organização clara das operações (cadastrar, vender, atualizar, repor, etc.).
- **Estruturas Condicionais (`if`, `elif`, `else`):** Regras de negócio, validações de estoque e preços.
- **Tratamento de Exceções (`try` / `except`):** Prevenção de falhas na entrada de dados numéricos (ex: preços e quantidades).
- **Event-Driven Programming:** Manipulação de ações atreladas a botões e interação do usuário.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado em sua máquina.

### Passo a Passo

1. **Clonar ou baixar o repositório:**
   git clone [https://github.com/seu-usuario/sistema-vendas-barbearia.git](https://github.com/seu-usuario/sistema-vendas-barbearia.git)
   cd sistema-vendas-barbearia

2. **Executar a aplicação:**
   python main.py
   *(Substitua `main.py` pelo nome exato do seu arquivo Python).*

---

## 📝 Licença
Este projeto foi desenvolvido para fins educacionais e de gestão prática para barbearias.