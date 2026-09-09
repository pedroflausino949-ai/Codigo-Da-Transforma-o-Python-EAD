import unittest
from modulo12.modelo12_frete_pedrohenrique import calcular_frete


class TestFrete(unittest.TestCase):

    def test_frete_calculado_corretamente(self):
        self.assertEqual(calcular_frete(5, 100), 25.00)

    def test_frete_com_peso_maior(self):
        self.assertEqual(calcular_frete(10, 100), 35.00)

    def test_peso_invalido(self):
        with self.assertRaises(ValueError):
            calcular_frete(0, 100)

    def test_distancia_invalida(self):
        with self.assertRaises(ValueError):
            calcular_frete(5, -10)


if __name__ == "__main__":
    unittest.main()
