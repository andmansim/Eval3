def filtrar(lista, nombre, largo, tripulacion, pasajeros):
   
    lista1 = []
    for i in lista:
        dicc= {}
        dicc['nombre'] = i['name']
        dicc['largo'] = i ['lenght']
        dicc['pasajeros'] = i['passengers']
        dicc['tripulacion'] = i ['crew']
    lista1.append(dicc)
    return lista1

def ordenar(lista, nombre):
    l_o = []
    for i in lista:
        l_o.append(i[nombre])
    if nombre == 'name':
        l_o.sort()
    else:
        l_o.sort(reverse=True)
    return l_o

def informacion(lista, nombre):
    for i in lista:
        dict= {}
        dict['name'] = 'Halcon milenario'
        dict['length'] = '34.37'