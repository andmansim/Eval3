def comprobacion(i, j, h):
    if i >= 3:
        i = 0
    elif j >= 3:
        j = 0
    elif  h >= 3:
        h = 0
    
    if i == -1:
        i = 2
    elif j == -1:
        j = 2
    elif h == -1:
        h =2
        
    return i, j, h

def parametros(i, j, h, contador):
    if contador < 3:
        i = i + 1
        j = j + 1
        h = h + 1
        i, j, h = comprobacion(i, j, h)
    else:
        i = i-1
        j = j-1
        h = h-1
        i, j, h = comprobacion(i, j, h) 
    
    return i, j, h

def det_iterativa(matriz, i, j, h):
    pri = matriz[0][i] * matriz[1][j] * matriz[2][h]
    return pri

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
while contador != 6:
    
    if contador < 3:
        
        uno = det_iterativa(matriz, i, j, h)
        suma = suma + uno
        i, j, h = parametros(i, j, h, contador)
    else:

        dos = det_iterativa(matriz, h, j, i)
        resta = resta + dos
        i, j, h = parametros(h, j, i, contador)
    contador = contador + 1
    
total = suma - resta

def recursivo(contador, i, j, h, suma, resta):
    if 0 < contador < 3:
        
        uno = det_iterativa(matriz, i, j, h)
        suma = suma + uno
        i, j, h = parametros(i, j, h, contador)
        
    else:

        dos = det_iterativa(matriz, h, j, i)
        resta = resta + dos
        i, j, h = parametros(h, j, i, contador)
    recursivo(contador-1, i, j, h, suma, resta)
    

recursivo(6, i, j, h, 0, 0)