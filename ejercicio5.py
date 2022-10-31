mensaje_cifrar = input('Introduce el mensaje: ')

m1 = mensaje_cifrar.lower()#todo a minúscula
m1 = m1.split()#quitamos espacios
a = 'abcdefghijklmnñopqrstuvwxyz'
mensaje = []
def cifrar(texto,clave):
    mensaje = []
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    for i in range (0,longitud): #Bucle para recorrer el texto
        for j in range (0,26): #Bucle para recorrer el Abecedario
            if texto[i]==a[j]: #comparo las letras una por una
                cod = []
                nuevo=j+int(clave) #Me desplazo en el abecedario en función a la clave
                if nuevo <26:
                    b = a[j + 1:nuevo + 1]
                    
                    print( a[j + 1:nuevo + 1])
                    print(print(cod))
                    print(texto[i])
                if nuevo >25 : #En el caso de que me pase del abecedario, calculo el modulo
                    print(a[nuevo%26])
                    b = a[nuevo%26 : nuevo%26 + 8]
                    print(texto[i])
                cod.append(b[::-1])
                mensaje = mensaje + cod
                print(mensaje)
            else:
                print('NO')
    for h in mensaje:
        v = ''.join(h)
    return v 
cifrar(m1, 8)


