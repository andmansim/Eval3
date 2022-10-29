'''
Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], 
regla de Sarrus de forma recursiva y de forma iterativa.
'''
'''
matrz = [[1, 2, 3], 
         [2, 4, 5], 
         [6, 8, 6]]
'''


def det_iterativa(matriz):
    i = 0
    j = i+1
    h = j +1
    if i == 3:
        i = 1
    if j == 3:
        j = 1
    if  h== 3:
        h = 1
        
    else:
        pri = matriz[0][i] * matriz[1][i+1] * matriz[2][i+2]
    
    return pri

matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]
det_iterativa(matriz)