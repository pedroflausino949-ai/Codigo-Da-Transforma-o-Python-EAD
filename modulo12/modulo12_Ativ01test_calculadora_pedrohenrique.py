import unittest
from modulo12.modulo12_calculadora_pedrohenrique import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calculadora.somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(self.calculadora.subtrair(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calculadora.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calculadora.dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()
