import unittest
from ejercicio2 import *
from helpers import *

matriz = [[1, 2, 3], 
                    [2, 3, 4], 
                  [5, 6, 7]]
class TestDatabase(unittest.TestCase):
    def test_total(self):
        self.assertAlmostEqual(iterar(0, 1, 2, 0, 0, 0, matriz), 0)
        self.assertAlmostEqual(det_recursiva(matriz, 0, 1, 2), 0)
        
if __name__ == '__main__':
    unittest.main()