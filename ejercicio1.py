
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



def cambiar_disco(t, agu1, agu3, agu2):
    if t == 1:#Ficha 1 = el de la cima
        m = agu1.desapilar()
        agu3.apilar(m)
        return
    cambiar_disco(t-1, agu1, agu2, agu3) #Rotamos agujas para ir quitando y añadiendo
    m = agu1.desapilar()
    agu3.apilar(m)
    cambiar_disco(t-1, agu2, agu3, agu1)
 


