'''

Ciclo de vida do projeto:
1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes, 
e criar um plano de desenvolvimento.
2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.
3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.
4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.
5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando 
corretamente.
6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir 
que o sistema continue atendendo às necessidades do negócio e dos clientes.

>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, 
sem interface gráfica.
>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica, 
para que os usuários possam interagir de forma mais intuitiva e agradável.

'''

# Isso é um comentário de linha única.
# print('Olá, Mundo!')
# print('\n-------------------------------------------------------------\n')


print('\n' + '-' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas - açaiteria!\n')
print('1 - Cadastrar produto')
print('2 - Listar produtos')
print('3 - Realizar venda')
print('0 - Sair do Sistema')
print('\n--------------------------------------\n')











opcao__definida = int(input('Digite a opção desejada: '))

if opcao__definida == 1:
    print('Cadastrando produto...')

elif opcao__definida == 2:
    print('Listando produtos...')

elif opcao__definida == 3:
    print('Realizando venda...')

elif opcao__definida == 0:
    print('Saindo do Sistema...')
    
else:
    print('Opção inválida, escolha novamente!')