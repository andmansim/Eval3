def filtrar(lista):
   
    lista1 = []
    for i in lista:
        dicc= {}
        dicc['nombre'] = i['name']
        dicc['largo'] = i ['length']
        dicc['pasajeros'] = i['passengers']
        dicc['tripulacion'] = i ['crew']
        lista1.append(dicc)
    return lista1

def ordenar(lista, nombre):
    l_o = []
    for i in lista:
        l_o.append(i[nombre])
    if nombre == 'nombre':
        l_o.sort()
    else:
        l_o.sort(reverse=True)
    return l_o


def naves(lista, lista2, nombre, nombre1):
    naves = []
    for i in lista:
        if i[nombre] in lista2:
            naves.append(i[nombre1])
    return naves

def sacar_info(lista, dato, nombre):
    for i in lista:
        if i[nombre] == dato:
            return i