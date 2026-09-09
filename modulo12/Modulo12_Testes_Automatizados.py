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


import unittest


class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero!")
        return a / b


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(Calculadora().soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(Calculadora().subtracao(5, 3), 2)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora().multiplicacao(4, 3), 12)

    def test_divisao(self):
        self.assertEqual(Calculadora().divisao(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            Calculadora().divisao(10, 0)


if __name__ == "__main__":
    unittest.main()
