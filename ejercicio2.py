matriz = [[1, 2, 3], 
                    [2, 3, 4], 
                  [5, 6, 7]]

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
        i = i +1
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