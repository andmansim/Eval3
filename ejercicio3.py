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
        
        

print("Naves de Star Wars...\n")
            vehiculos = helpers.leer('vehicles.csv')
            helpers.limpiar(vehiculos)
            lista = e3.filtrar(vehiculos)
            nombre = e3.ordenar(lista, 'nombre')
            largo = e3.ordenar(lista, 'largo')
            
            print('Lista ordenada de nombres')
            print(nombre)
            print('Lista ordenada de largo')
            print(largo)
            pasajeros = e3.ordenar(lista, 'pasajeros')
            naves = e3.naves(lista, pasajeros, 'pasajeros', 'nombre')
            print('Naves con mayor número de pasajeros:')
            print(naves[0], naves[1], naves[2], naves[3], naves[4])
            tripulacion = e3.ordenar(lista, 'tripulacion')
            naves1 = e3.naves(lista, tripulacion, 'tripulacion', 'nombre')
            print('La nave con mayot tripulación es:')
            print(naves1[0])
            print('Naves que empiezan por AT')
            for i in nombre:
                if i.startswith('AT'):
                    print(i)
            print('Naves que pueden llevar 6 o más pasajeros:')
            pa = []
            for i in pasajeros:
                if i >= '6':
                    pa.append(i)
            
            naves2 = e3.naves(lista, pa, 'pasajeros', 'nombre')
            print(naves2)
            print('Nave más pequeña:')
            nave_p = e3.sacar_info(lista, largo[-1], 'largo')
            print(nave_p)
            print('La nave más grande:')
            nave_g =e3.sacar_info(lista, largo[0], 'largo')
            print(nave_g)