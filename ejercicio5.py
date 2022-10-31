mensaje_cifrar = input('Introduce el mensaje: ')

m1 = mensaje_cifrar.lower()
a = 'abcdefghijklmnñopqrstuvwxyz'
def cifrar(texto,clave):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    for i in range (0,longitud): #Bucle para recorrer el texto
        for j in range (0,26): #Bucle para recorrer el Abecedario
            if texto[i]==a[j]: #comparo las letras una por una
                cod = []
                nuevo=j+int(clave) #Me desplazo en el abecedario en función a la clave
                if nuevo <26:
                    b = a[j + 1:nuevo + 1]
                    cod.append(b[::-1])
                    print( a[j + 1:nuevo + 1])
                    print(print(cod))
                    print(texto[i])
                if nuevo >25 : #En el caso de que me pase del abecedario, calculo el modulo
                    print(a[nuevo%26])
                    print(texto[i])
            else:
                print('NO')
    return
cifrar(m1, 8)


