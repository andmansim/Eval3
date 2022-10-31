mensaje_cifrar = input('Introduce el mensaje: ')

m1 = mensaje_cifrar.lower()

def cifrar(texto,clave):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    for i in range (0,longitud): #Bucle para recorrer el texto
        for j in range (0,26): #Bucle para recorrer el Abecedario
            if texto[i]==a[j]: #comparo las letras una por una
                nuev = 
                pos_abc=j+int(clave) #Me desplazo en el abecedario en función a la clave
                if pos_abc <26:
                    print(a[pos_abc])
                if pos_abc >25 : #En el caso de que me pase del abecedario, calculo el modulo
                    print(a[pos_abc%26])
            else:
                print('a')
    return
cifrar(m1, 8)


