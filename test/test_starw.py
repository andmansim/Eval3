import copy
import unittest
from ejercicio3 import *
from helpers import *


vehiculos = helpers.leer('vehicles.csv')
helpers.limpiar(vehiculos)
lista = filtrar(vehiculos)
halcon = añadir_datos('Halcón Milenario', 34.37, 4,4)
estrella = añadir_datos('Estrella de la Muerte', 80000, 1200000 , 825984)
lista.append(halcon)
lista.append(estrella)
nombre = ordenar(lista, 'nombre')
largo = ordenar(lista, 'largo')
tripulacion = ordenar(lista, 'tripulacion')

class TestDatabase(unittest.TestCase):
    def test_nave_mayor_trip(self):
        self.assertEqual(naves(lista, [tripulacion[0]], 'tripulacion', 'nombre')  , 'Estrella de la Muerte')
        
        

if __name__ == '__main__':
    unittest.main()