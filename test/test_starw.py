import unittest
from ejercicio3 import *
from helpers import *




class TestDatabase(unittest.TestCase):
    def setup(self):
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
    
    def test_nave_mayor_trip(self):
        self.assertEqual(naves(lista, [tripulacion[0]], 'tripulacion', 'nombre')  , ['Estrella de la Muerte'])
    
    def test_nave_mayor_pas(self):
        self.assertEqual(naves(lista, pasajeros1, 'pasajeros', 'nombre'), ['Sail barge', 'Multi-Troop Transport', 'C-9979 landing craft', 'Clone turbo tank', 'Estrella de la Muerte'])
    
    def test_anadir(self):
        self.assertEqual(lista[-1], {'nombre': 'Estrella de la Muerte', 'largo': 80000.0, 'pasajeros': 1200000.0, 'tripulacion': 825984.0})
        self.assertEqual(lista[-2], {'nombre': 'Halcón Milenario', 'largo': 34.37, 'pasajeros': 4.0, 'tripulacion': 4.0})
        
    
if __name__ == '__main__':
    unittest.main()