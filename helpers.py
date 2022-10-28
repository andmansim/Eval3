import os
import re #para comprobar si lo que nos dan está bien
import platform #detecta el sistema operativo que queremos y lo adapta para poder trabajar con él.
import csv

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

import csv
def leer(csv_leer):
    '''
    Leemos el csv y lo almacenamos en una lista de diccionarios
    '''
    lista = []
    with open(csv_leer, newline="\n") as fichero:
            reader = csv.DictReader(fichero, delimiter=",") #lo pasa a diccionario
            for linea in reader:
                lista.append(linea) 
    
    return lista

def limpiar(lista_dicc): # Le pasamos la lista de diccionarios
    '''
    leemos la listade diccionarios y cambiamos los blancos por None y las , por . 
    IMPORTANTE: Todos los valores del diccionario son str.
    '''
    for i in lista_dicc: #Recorremos la lista y accedemos a los diccionarios
        for j in i.keys(): #recogemos cada key de los diccionarios
            if i[j] == '':
                i[j] = None