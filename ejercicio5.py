import hashlib
import lista_en as l
cadena_encrip = input('Introduce el texro a cifrar ')

#No he visto que cree ninguna clase hush, asi que he supuesto que solo son las funciones

def crear_tabla(tamanio):
    #Creamos una tabla vacia
    tabla = [None] * tamanio #La tabla tiene todos los elementos none
    return tabla


def cantidad_elementos(tabla):
    #Devuelve la cantidad de elementos que no son nulos
    return len(tabla) - tabla.count(None)


def funcion_hash(dato, tamanio_tabla):
    #Determina la posicion del dato en la tabla
    '''El objetivo de esta funcion es, que para cada dato, haya un codigo único (al menos, intentamos que lo sea)
    para que sea más fácil y rápido buscar el valor del dato en la tabla.
    Por ejemplo: si queremos buscar un nombre con apellidos, en vez de pasarle el nombre, que puede haber cientos, le pasas el código, que va a ser más exclusivo
    En este caso, el codigo es el resto de la longitud de la palabra (menos los espacios) entre el tamaño de la tabla.'''
    return len(str(dato).strip()) % tamanio_tabla

def agregar(tabla, dato):
    #agregamos un elemento a la tabla encadenada
    posicion = funcion_hash(dato, len(tabla)) #usamos la funcion anterior para determinar la posicion mediante el codigo
    if (tabla[posicion]) is None: 
        tabla[posicion] = l.Lista() #Si no ha habido anteriormente un elemento con ese dato, en vez de añadirlo a la lista que contiene el mismo codigo, la creamos 
    l.Lista.insertar(tabla[posicion], dato) #Si la lista ya existe, lo añade como un elemento mas


def buscar(tabla, buscado):
    #determina si un elemento exsiste en la tabla y devuelve la posicion
    pos = None
    posicion = funcion_hash(buscado, len(tabla)) #determinamos el codigo del dato buscado
    if tabla[posicion] is not None: #Para ver si existe ese dato en la tabla
        pos = l.Lista.buscar(tabla[posicion], buscado) #usamos una funcion extra para buscar el elemento en la lista
    return pos

def quitar(tabla, dato):
    #Quita un elemento de la tabla encadenada si existe
    dato = None
    posicion = funcion_hash(dato, len(tabla)) #determinamos la posicion del dato
    if tabla[posicion] is not None: #si la lista existe
        dato = l.Lista.eliminar(tabla[posicion], dato) #eliminamos el dato de la lista
        if l.Lista.lista_vacia(tabla[posicion]): #si no hay mas datos en la lista
            tabla[posicion] = None #igualamos la lista a None (borramos la lista)
    return dato


#EJEMPLO:
tabla = crear_tabla(9)
nombre = input('Ingrese nombre: ')
while nombre != '': #añadimos nombres hasta enter y los vamos añadiendo a la tabla
    agregar(tabla, nombre)
    nombre = input('Ingrese nombre: ')

buscado = input('Ingrese el nombre a buscar: ') 
posicion = buscar(tabla, buscado) #buscamos la posicion en la tabla del elemento
if posicion is not None:
    print('Elemento encontrado: ', posicion.info)
else:
    print('No se encontró el elemento buscado')
