mensaje_cifrar = input('Introduce el mensaje: ')

m1 = mensaje_cifrar.lower()#todo a minúscula
#m1 = m1.split()#quitamos espacios
a = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
mensaje = []
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
ns = cifrar(m1, 8, a)
print(ns)
def descifrar(texto, clave, a):
    for i  in range(len(texto)):
        for j in range(len(a)):
            des = []
            c = i[:9]
            des.append(c[::-1])
            texto.replace(c)
            
            if texto[i] == a[j]:
                nuevo =j-int(clave) 
                
