import unittest
from ejercicio2 import *
from helpers import *

matriz = [[1, 2, 3], 
                    [2, 3, 4], 
                  [5, 6, 7]]
#FORMA ITERATIVA
i = 0
j = 1
h = 2
suma = 0
resta = 0
contador = 0
def iterar(i,j,h, resta, suma, contador):
    while contador != 6:

        if contador < 3:

            uno = det_iterativa(matriz, i, j, h)
            suma = suma + uno
            i, j, h = parametros(i, j, h, contador)

        else:
            if contador == 3:
                h, j, i = i, j, h

            dos = det_iterativa(matriz, i, j, h)
            resta = resta + dos
            i, j, h = parametros(i, j, h, contador)
        contador = contador + 1

    total = suma - resta
    return total

class TestDatabase(unittest.TestCase):
    def test_total(self):
        self.assertAlmostEqual(iterar(0, 1, 2, 0, 0), 0)