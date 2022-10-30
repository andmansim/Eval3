import unittest
from ejercicio2 import *
from helpers import *


'''#FORMA ITERATIVA
i = 0
j = 1
h = 2
suma = 0
resta = 0
contador = 0'''


class TestDatabase(unittest.TestCase):
    def test_total(self):
        self.assertAlmostEqual(iterar(0, 1, 2, 0, 0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()