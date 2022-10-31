def cifrar(texto,clave, a):
    mensaje = []
    for i in range (0,len(texto)): 
        for j in range (0,len(a)): 
            if texto[i]==a[j]:
                cod = []
                nuevo=j+int(clave) 
                if nuevo <len(a):
                    b = a[j + 1:nuevo + 1]
                    
                if nuevo >len(a) -1 : 
                    b = a[nuevo%len(a) : nuevo%len(a) + 8]
                cod.append(b[::-1])
                mensaje = mensaje + cod
            else:
                pass
                        
    
    mensaje = ''.join(mensaje)
    return mensaje

def descifrar(texto, clave, a):
    des = []
    for i  in range(len(texto)):
        for j in range(len(a)):
            
            c = i[:9]
            des.append(c[::-1])
            texto.replace(c)
            
            if texto[i] == a[j]:
                nuevo =j-int(clave) 
                
