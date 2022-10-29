'''
Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3], 
regla de Sarrus de forma recursiva y de forma iterativa.
'''
'''
matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]
'''
def comprobacion(i, j, h):
    if i >= 3:
        i = 0
        
    if j >= 3:
        j = 0
        
    if  h >= 3:
        h = 0
        
    return i, j, h
def parametros(i, j, h):
    i = i +1
    i, j, h = comprobacion(i, j, h)
    j = j+1
    i, j, h = comprobacion(i, j, h)   
    h = h + 1
    i, j, h = comprobacion(i, j, h)
    
    return i, j, h

def det_iterativa(matriz, i, j, h):
    pri = matriz[0][i] * matriz[1][j] * matriz[2][h]
    print(pri)
    return pri, i

matriz = [[1, 2, 3], 
          [2, 3, 4], 
          [5, 6, 7]]

i = 2
j = 0
h = 1
suma = 0
resta = 0
contador = 0
while contador != 6:
    
    if contador < 3:
        i, j, h = parametros(i, j, h)
        uno, i = det_iterativa(matriz, i, j, h)
        suma = suma + uno
    else:
        print(i, j, h)
        h, j, i = parametros(i, j, h)
        print(i, j, h)
        dos, i = det_iterativa(matriz, i, j, h)
        resta = resta + dos
    contador = contador + 1
    

print(suma, resta)