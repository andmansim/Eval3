#Iterativa
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

def iterar(i,j,h, resta, suma, contador, matriz):
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



#Recursiva
def det_suma(matriz,i,j,h):
    t_suma = 0
    if j>2: j=0
    if h>2: h=0
    if i < 3:
        t_suma = matriz[0][i] * matriz[1][j] * matriz[2][h] + det_suma(matriz,i+1,j+1,h+1)
    return t_suma

def det_resta(matriz,i2,j2,h2):
    t_resta = 0
    if h2 <0: h2 = 2
    if j2 <0: j2 = 2
    if i2 >= 0:
        t_resta = matriz[0][i2] * matriz[1][j2] * matriz[2][h2] + det_resta(matriz,i2-1,j2-1,h2-1)
    return t_resta

def det_recursiva(matriz, i, j, h):
    s = det_suma(matriz,i,j,h) 
    r = det_resta(matriz,i+2,j,h-2)
    return s - r
    