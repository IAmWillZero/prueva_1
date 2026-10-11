"""Pruebas unitarias de la lógica de los sorteos."""

import unittest

from app.games import dados, moneda, ruleta


class TestRuleta(unittest.TestCase):
    def test_color_de(self):
        self.assertEqual(ruleta.color_de(0), "verde")
        self.assertEqual(ruleta.color_de(1), "rojo")
        self.assertEqual(ruleta.color_de(2), "negro")

    def test_girar_siempre_en_rango(self):
        for _ in range(300):
            resultado = ruleta.girar()
            self.assertIn(resultado["numero"], range(0, 37))
            self.assertIn(resultado["color"], {"rojo", "negro", "verde"})


class TestDados(unittest.TestCase):
    def test_cantidad_y_total(self):
        resultado = dados.tirar(cantidad=3)
        self.assertEqual(len(resultado["dados"]), 3)
        self.assertEqual(resultado["total"], sum(resultado["dados"]))
        for valor in resultado["dados"]:
            self.assertIn(valor, range(1, 7))

    def test_limites_de_parametros(self):
        self.assertEqual(len(dados.tirar(cantidad=0)["dados"]), 1)
        self.assertEqual(len(dados.tirar(cantidad=999)["dados"]), 10)
        self.assertEqual(dados.tirar(caras=1)["caras"], 2)
        self.assertEqual(dados.tirar(caras=9999)["caras"], 100)


class TestMoneda(unittest.TestCase):
    def test_resultado_valido(self):
        for _ in range(200):
            self.assertIn(moneda.lanzar()["resultado"], {"cara", "cruz"})


if __name__ == "__main__":
    unittest.main()
