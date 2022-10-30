
#funciones para las pilas.
class NodoPila:
    info, sig = None, None #Cuando definimos la clase, los valores iniciales siempre son none
    #Atributos: INFORMACION, SIGUIENTE

class Pila(object):
    def __init__(self):
        #Creamos una pila vacía
        self.cima = None #Puntero que apunta al nodo que está en la cima de la pila
        self.tamanio = 0 #Tamaño de la pila.
    
    def apilar(pila, dato):
        #apila un dato en la cima dela pila
        nodo = NodoPila() #Cuando queremos apilar un nuevo elemento, creamos una variable del tipo NodoPila.
        nodo.info = dato #Como su informacion metemos el valor del elemento ingresado como dato
        nodo.sig = pila.cima #Aqui se le guarda la dirección de referencia de la cima
        pila.cima = nodo #Se le asigna la direccion del nodo creado
        pila.tamanio += 1 #Aumentamos el tamaño

    def desapilar(pila):
        #Desapila el elemento que se situa en la cima y lo devuelve
        x = pila.cima.info #Almacenamos en una variable auxiliar la informacion del nodo en la cima
        pila.cima = pila.cima.sig #Ponemos en la cima de la pila el dato siguiente
        pila.tamanio -= 1 #Le quitamos uno al tamaño
        return x
    
    def pila_vacia(pila):
        #Devuelve true si la pila está vacía
        return pila.cima == None

    def en_cima(pila):
        #Devualve el valor almacenado en la cima de la pila
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
        
    def tamaño(pila):
        #Devuelve el numero de elementos en la pila
        return pila.tamanio


    def barrido(pila):
        #Muestra el contenido de una pila sin perder datos
        #creamos una pila adicional llamada paux, donde vamos a reapilar los datos de la pila principal. 
        #Vamos sacando uno por uno los datos de la pila y damos su valor, luego los metemos a paux
        #cuando terminamos, desapilamos paux y los volvemos a meter a la primera pila
        paux = Pila()
        while not pila.pila_vacia():
            dato = pila.desapilar()
            print(dato)
            paux.apilar(dato)
            return dato
        while not paux.pila_vacia():
            dato = paux.desapilar()
            print(dato)
            pila.apilar(dato)
            return dato
        


'''def comprobar(aguja, disco):
    if aguja.en_cima() == None:
        return True
    elif disco > aguja.en_cima():
        return True
    else:
        return False, aguja

def agujas(pila, dato):
    pila.apilar(dato)
    print(pila.en_cima())
    return pila

def cambio_aguja(resultado, agu1, agu2, agu3):
    if resultado == agu1:
        c, pila = comprobar(agu2, quito_d)
    elif resultado == agu2:
        c, pila = comprobar(agu3, quito_d)
    else:
        c, pila = comprobar(agu1, quito_d)
    return c, pila


def organizar(c, pila, quito_d):
    if c:
        pila = agujas(pila, quito_d)
    else:
        c, pila = cambio_aguja(pila, aguja1, aguja2, aguja3)

'''
aguja1 = Pila()
aguja2 = Pila()
aguja3 = Pila()

#El disco más pequeño esel 74 y el más grande el 1
for i in range(1, 75):
    aguja1.apilar(i)
print(aguja1.en_cima())

def quitar_agujas(aguja):
    quito_d = aguja.desapilar()
    print('Quito ' + str(quito_d) + ' de ' + str(aguja))
    return quito_d

def agujas(aguja, disco):
    c, pila = comprobar(aguja, disco) #Comprueba si puedo añadir ese elemento a la aguja
    if c :#Si puedo, entonces lo añade y nos devuelve True
        pila.apilar(disco)
        print('Añado ' + str(disco) + ' a ' +  str(pila))
        return True
    else:#no puedo pues nos devuelve False
        return False

def comprobar(aguja, disco):
    if aguja.en_cima() == None:
        return True, aguja
    elif disco > aguja.en_cima():
        return True, aguja
    else:
        return False, aguja

while aguja3.tamaño() != 74:
    quito = quitar_agujas(aguja1)
    a = agujas(aguja3, quito)
    if a == False:
        a = agujas(aguja2, quito)
        if a == False:
            if aguja2.en_cima() > aguja3.en_cima():
                quito = quitar_agujas(aguja2)
                a = agujas(aguja1, quito)
                
    



'''quito_d = quitar_agujas(aguja1)
c, pila = comprobar(aguja2, quito_d)
print(c)
organizar(c, pila, quito_d)

while aguja3.tamaño() != 74:
    #if aguja1.pila_vacia() is not None: #Mirar esta condicion 
        quito_d = quitar_agujas(aguja1)
        c, pila = cambio_aguja(pila, aguja1, aguja2, aguja3)
        print(c)
        print('Tamaño aguja 1 ' + str(aguja1.tamaño()) + '\n')
        print('Tamaño aguja 2 ' + str(aguja2.tamaño())+ '\n')
        print('Tamaño aguja 3 ' + str(aguja3.tamaño())+ '\n')
        organizar(c, pila, quito_d)
    #else:
        quito_d = quitar_agujas(aguja2)
'''
