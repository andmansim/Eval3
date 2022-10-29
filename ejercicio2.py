'''
Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], 
regla de Sarrus de forma recursiva y de forma iterativa.
'''
'''
matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]
'''


def det_iterativa(matriz, i):
    if i >= 3:
        i = 0
    
    j = i+1
    if j >= 3:
        j = 0
        
    h = j +1
    if  h>= 3:
        h = 0
    pri = matriz[0][i] * matriz[1][j] * matriz[2][h]
    print(pri)
    return pri, i

matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]

numero = 0
suma = 0
while numero != 3:
    uno, numero = det_iterativa(matriz, numero)
    numero = numero + 1
    suma = suma + uno
    print(suma)