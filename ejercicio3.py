import helpers
def filtrar(lista):
   
    lista1 = []
    for i in lista:
        dicc= {}
        dicc['nombre'] = i['name']
        dicc['largo'] = float(i['length'])
        dicc['pasajeros'] = float(i['passengers'])
        dicc['tripulacion'] = float(i ['crew'])
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
lista = filtrar(vehiculos)
nombre = ordenar(lista, 'nombre')
largo = ordenar(lista, 'largo')

print('Lista ordenada de nombres ' + str(nombre) + '\n')
print('Lista ordenada de largo ' + str(largo) + '\n')

pasajeros = ordenar(lista, 'pasajeros')
pasajeros1 = pasajeros[0:5]
nave = naves(lista, pasajeros1, 'pasajeros', 'nombre')
print('Naves con mayor número de pasajeros: ' + str(nave) + '\n')
tripulacion = ordenar(lista, 'tripulacion')
naves1 = naves(lista, [tripulacion[0]], 'tripulacion', 'nombre')
print('La nave con mayor tripulación es: ' + str(naves1) + '\n')
print('Naves que empiezan por AT')
for i in nombre:
    if i.startswith('AT'):
        print(i)

pa = []
for i in pasajeros:
    if i >= 6.0:
        pa.append(i)

naves2 = naves(lista, pa, 'pasajeros', 'nombre')
print('Naves que pueden llevar 6 o más pasajeros: ' + str(naves2) + '\n')

nave_p = sacar_info(lista, largo[-1], 'largo')
print('Nave más pequeña: '+ str(nave_p)  + '\n')

nave_g =sacar_info(lista, largo[0], 'largo')
print('La nave más grande: ' + str(nave_g)  + '\n')
