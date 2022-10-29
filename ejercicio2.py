'''
Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], 
regla de Sarrus de forma recursiva y de forma iterativa.
'''
'''
matrz = [[1, 2, 3], 
         [2, 4, 5], 
         [6, 8, 6]]
'''


def det_iterativa():
    for i in range(3):
        pri = i[0][] * i[1][] * i[2][]
        seg = i[0][] * i[1][] * i[2][]
        tri = i[0][] * i[1][] * i[2][]
    sum = pri + seg + tri
    return sum

matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]
det_iterativa(matriz)