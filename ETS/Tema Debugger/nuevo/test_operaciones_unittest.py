# Versión unittest: test_operaciones_unittest.py
# test_operaciones_unittest.py
# Para ejecutar: python -m unittest test_operaciones_unittest.py

import unittest
from operaciones import suma, resta, es_par, es_mayor_de_edad


class TestOperacionesBasicas(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta_positivos(self):
        self.assertEqual(resta(5, 2), 3)


class TestEsPar(unittest.TestCase):
    def test_es_par_para_numero_par(self):
        self.assertTrue(es_par(4))

    def test_es_par_para_numero_impar(self):
        self.assertFalse(es_par(5))


class TestEsMayorDeEdad(unittest.TestCase):
    def test_es_mayor_de_edad_para_20(self):
        self.assertTrue(es_mayor_de_edad(20))

    def test_es_mayor_de_edad_para_15(self):
        self.assertFalse(es_mayor_de_edad(15))


if __name__ == "__main__":
    unittest.main()
